import threading
from tkinter import *

from graphics.frames import Map, DialClock, Label
from server.chat_server import ChatServer
from sys import stdout
from os import mkdir
from os.path import exists

from constants import *

HEIGHT, WIDTH = 1500, 800  # Canvas dimensions
CANVAS_MID_X = WIDTH / 2
CANVAS_MID_Y = HEIGHT / 2


class AiInterface(object):

    # A dictionary mapping natural language words into 
    # the corresponding attribute in this class
    name_to_field = {"map" : "_map"}
    
    # Function to permission level necessary to use it
    permissions = {
                    '<some-function>' : '<permission-level>'
                }
    
        
    def __init__(self):
        
        self.root = Tk()
        self.root.title("Some Title")
        self.root.geometry("%dx%d" % (HEIGHT, WIDTH))
        self.vars = {}
        self.server = ChatServer()
        
        
        # Add graphics:
        
        self._map = Map()
        self.prep__map()
        
        # Example. To change specific things, go to the Animation class and edit them
        # In order to control where frames appear, we should parametrize them
        self.clock = DialClock() 
        
        # Example label
        self.label = Label()
        self.label.show()
        
        # Create input directory if doesn't exist
        if not exists(INPUT_DIR):
            mkdir(INPUT_DIR)
        
    def run(self):
        """Start the system."""
        
        threading.Thread(name="server_t", target=self.server.start).start() # thread for running the server
        threading.Thread(name="vars_t", target=self.update_loop).start() # thread for evaluating commands
        self.root.mainloop() # run gui 
    
    def update_loop(self):
        """Main user loop of the program. It update animiation and internal variables
        in every time step, and also handles user commands. It repeatedly read the server's 
        command queue, and if it contains a command, pops it and evaluates it."""
        while True:
            
            # Do something with animation on every time step (example):
            self.root.after(200, self.clock.redraw())
            
            # Do something with label
            self.root.after(1000, self.label.change_color())
            
            if self.server.cmd_queue:
                cmd, permission = self.server.cmd_queue.pop(0)
                self.eval_cmd(cmd, permission)
                
    def eval_cmd(self, cmd, permission):
        """Evaluates a command relative to this object's environment. A command 
        is a string with a function and its arguments."""
        # split command into function and arguments
        spl = re.split("\s+", cmd.strip()) 
        func, args = spl[0], spl[1:]
        try:
            # Check if permision allows
            if func in self.permissions and self.permissions[func]>permission:
                self.server.display("Permission denied: %s." % func)
            
            # Exectue command
            elif func=="show": 
                obj = args[0]
                name = self.field_from_name(obj)
                getattr(self, name).show()
                self.server.display("Showing " + obj)
            elif func == "open":
                room, door_id = args[0], eval(args[1])
                self._map.open_door(room, door_id)
                self.server.display("Opening door %d in %s" % (door_id, room))
            elif func == "close":
                room, door_id = args[0], eval(args[1])
                self._map.close_door(room, door_id)
                self.server.display("Closing door %d in %s" % (door_id, room))
                
            else:
                self.server.display("Command not recognized: " + func)
            
        except Exception as e:
            print(type(e).__name__+ " occurred: " + str(e))
            
            self.server.display("Failed to execute command: " + cmd)
    
    def field_from_name(self, name):
        """Get an instance field from its corresponding name."""
        return self.name_to_field.get(name, None) or name
        
            
    # # # Graphics # # #
    # These functions define specific details about the Frame classes used 
    # by the interface        
    
    def prep__map(self):
        """This defines the map used by this ."""
        
        self._map.draw_polygon_room("engine-room", [(50, 50), (50, 120), (80, 160), (120, 120), (120, 50)], "blue", "red",
                                    [
                                        [0, 10, "green"],
                                        [1, 10, "green"],
                                        [2, 10, "green"],
                                        [3, -40, "green"],
                                        [4, -40, "green"],
                                    ])
        
        
if __name__ == '__main__':
    AiInterface().run()