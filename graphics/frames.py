"""
This module defines classes of graphics objects that can be added to the TkInter GUI.
Each class subclasses the Frame class from TkInter, and has a .show() method that
displays this class on the TkInter main canvas. TkInter works in such a way that it 
can only run on the main thread, so there is no need to pass a canvas to the Frame - 
by calling the show method, it will be displayed on the main canvas.
Colors names are taken from TkInter. 

Classes:

    Label
        Template for displaying text on the GUI.
    DialClock
        Example of how to do animation.
    Map
        Class for drawing floor plans.

"""


import math
from cmath import sqrt

import sys, types, os
from time import localtime
from datetime import timedelta, datetime
from math import sin, cos, pi
from threading import Thread
from graphics.clock import clock, mapper
try:
    from tkinter import *  # python 3
except ImportError:
    try:
        from mtTkinter import *  # for thread safe
    except ImportError:
        from Tkinter import *  # python 2
hasPIL = True
# we need PIL for resizing the background image
# in Fedora do: yum install python-pillow-tk
# or yum install python3-pillow-tk
try:
    import PIL
    from PIL import Image, ImageTk
except ImportError:
    hasPIL = False


from utils import *


# API:


class Label(Frame):
    """Template of label that displays some text. Edit it to define custom text and format."""
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self)
        
        self.box = Text(self.canvas, background="green")
        
    def show(self, side=TOP):
        
        # Parameters that control the box where the box 
        # is displayed. 
        
        self.master.title("Some-title")
        self.pack(side=side, expand=0)
        self.canvas.configure(background=BACKGROUND_COLOR)
        self.canvas.pack(side=side, expand=0)
        self.canvas.create_text(50,50,text='hello', font="Times 20 italic bold")
    
    
    def change_color(self):
        current_color = self.box.cget("background")
        next_color = "green" if current_color == "red" else "red"
        self.box.config(background=next_color)
        

class DialClock(Frame):
    """Example on how to define an animated frame that can fit into the GUI."""

    def __init__(self):
        super().__init__()
        
        # Internal parameers, change to edit :
        deltahours = 3
        w = h = 400

        self.world = [-1, -1, 1, 1]
        self.showImage = False

        self.setColors()
        self.circlesize = 0.09
        self._ALL = 'handles'
        width, height = w, h
        self.pad = width / 16

        self.delta = timedelta(hours=deltahours)  
        self.canvas = Canvas(self)
        viewport = (self.pad, self.pad, width - self.pad, height - self.pad)
        self.T = mapper(self.world, viewport)
        self.canvas.bind("<Configure>", self.resize)
        self.canvas.pack(fill=BOTH, expand=YES)

        self.poll()
    
    def show(self, side=RIGHT):
        """When this method is called, this frame is added to the GUI."""
        
        # Parameters that control the box where the box 
        # is displayed. 
        
        self.master.title("Some-title")
        self.pack(side=side, expand=0)
        self.canvas.configure(background=BACKGROUND_COLOR)
        self.canvas.pack(side=side, expand=0)
        self.poll()
        
    # # Called when the window changes, by means of a user input.
    #
    def resize(self, event):
        sc = self.canvas
        sc.delete(ALL)  # erase the whole canvas
        width = sc.winfo_width()
        height = sc.winfo_height()

        imgSize = min(width, height)
        self.pad = imgSize / 16
        viewport = (self.pad, self.pad, width - self.pad, height - self.pad)
        self.T = mapper(self.world, viewport)

        if self.showImage:
            flu = self.fluImg.resize((int(0.8 * 0.8 * imgSize), int(0.8 * imgSize)), Image.ANTIALIAS) 
            self.flu = ImageTk.PhotoImage(flu)
            sc.create_image(width / 2, height / 2, image=self.flu)
        else:
            self.canvas.create_rectangle([[0, 0], [width, height]], fill=self.bgcolor)

        self.redraw()  # redraw the clock    

    # # Sets the clock colors.
    #
    def setColors(self):
        if self.showImage:
            self.bgcolor = 'antique white'
            self.timecolor = 'dark orange'
            self.circlecolor = 'dark green'
        else:
            self.bgcolor = '#000000'
            self.timecolor = '#ffffff'
            self.circlecolor = '#808080'

    # # Toggles the displaying of a background image.
    #
    def toggleImage(self, event):
        if hasPIL and os.path.exists (self.imgPath):
            self.showImage = not self.showImage
            self.setColors()
            self.resize(event)

    # # Redraws the whole clock.
    # 
    def redraw(self):
        start = pi / 2  # 12h is at pi/2
        step = pi / 6
        for i in range(12):  # draw the minute ticks as circles
            angle = start - i * step
            x, y = cos(angle), sin(angle)
            self.paintcircle(x, y)
        self.painthms()  # draw the handles
        if not self.showImage:
            self.paintcircle(0, 0)  # draw a circle at the centre of the clock
   
    # # Draws the handles.
    # 
    def painthms(self):
        self.canvas.delete(self._ALL)  # delete the handles
        T = datetime.timetuple(datetime.utcnow() - self.delta)
        x, x, x, h, m, s, x, x, x = T
        angle = pi / 2 - pi / 6 * (h + m / 60.0)
        x, y = cos(angle) * 0.70, sin(angle) * 0.70   
        scl = self.canvas.create_line
        # draw the hour handle
        scl(self.T.windowToViewport(0, 0, x, y), fill=self.timecolor, tag=self._ALL, width=self.pad / 3)
        angle = pi / 2 - pi / 30 * (m + s / 60.0)
        x, y = cos(angle) * 0.90, sin(angle) * 0.90
        # draw the minute handle
        scl(self.T.windowToViewport(0, 0, x, y), fill=self.timecolor, tag=self._ALL, width=self.pad / 5)
        angle = pi / 2 - pi / 30 * s
        x, y = cos(angle) * 0.95, sin(angle) * 0.95   
        # draw the second handle
        scl(self.T.windowToViewport(0, 0, x, y), fill=self.timecolor, tag=self._ALL, arrow='last')
   
    # # Draws a circle at a given point.
    # 
    #  @param x,y given point.
    # 
    def paintcircle(self, x, y):
        ss = self.circlesize / 2.0
        sco = self.canvas.create_oval
        sco(self.T.windowToViewport(-ss + x, -ss + y, ss + x, ss + y), fill=self.circlecolor)
  
    # # Animates the clock, by redrawing everything after a certain time interval. 
    #
    def poll(self):
        self.redraw()
#         self.root.after(200, self.poll)
        
class Map(Frame):
    """This class defines a canvas you can draw floorplans map on.
    It has methods that add walls, rooms and doors to the floorplans.
    To use, first define a Map object and then add items to it. When you want
    to display it, call the show() method and it will be displayed
    on the main GUI.
    After a map is displayed you can still interact with it. For example, you can change wall
    colors and you can open and close doors or add objects. 
    Rooms need names so you can refer to them when you perform actions on the map.
    
    
    For example:
    
    m = Map()
    m.draw_polygon_room("engine-room", [(50, 50), (50, 120), (80, 160), (120, 120), (120, 50)], "blue", "red",
                                    [
                                        [0, 10, "green"],
                                        [1, 10, "green"],
                                        [2, 10, "green"],
                                        [3, -40, "green"],
                                        [4, -40, "green"],
                                    ]) 
    
    m.show()
    m.open_door("engine-room", 0) # Open first door
    m.close_door("engine-room", 0) # Open first door
    """
    
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self)
        self.objs = {}

    def show(self, side=LEFT):
        
        # Parameters that control the box where the box 
        # is displayed. 
        
        self.master.title("Some-title")
        self.pack(side=side, expand=0)
        self.canvas.configure(background=BACKGROUND_COLOR)
        self.canvas.pack(side=side, expand=0)

    def draw_wall(self, x1, y1, x2, y2, color):
        """Draws a rectangle with given coordinates in given color."""
        wall = Wall((x1, y1), (x2, y2), color)
        wall.draw(self.canvas)

    def draw_polygon_room(self, name, points, wall_color, background_color, doors):
        """Draws a polygon with corners in @points. Each point in @points is a tuple
        (x,y) of 2d coordinates. Doors format: (wall_id, offset, door_color). Offset is the number of pixels
        that are between the door's start and the wall's start. So for example if 
        offset is 1/2 the wall's size, then the door will start at the middle of the wall.
        To refer to doors of a room, you will need to use their indices, which are defined 
        in the same order they were passed to the room.
        """
        room = PolygonRoom(points, wall_color, background_color, doors)
        room.draw(self.canvas)
        self.objs[name] = room

    def open_door(self, room_name, door_ind):
        """Marks door as open on the map."""
        
        room = self.objs[room_name]
        room.open_door(door_ind, self.canvas)

    def close_door(self, room_name, door_ind):
        """Returns open door to its default state."""
        room = self.objs[room_name]
        room.close_door(door_ind, self.canvas)

    def change_wall_color(self, room_name, wall_ind, new_color):
        room = self.objs[room_name]
        room.walls[wall_ind].change_color(new_color)
        for door in room.doors:
            door.draw(self.canvas)

    def add_image(self, path, x, y, basewidth):
        """Adds an image to the map in position @x and @y with width @basewidth
        to the map taken from @path."""
        # Example how to show image:
        image = Image.open(path, self.canvas)

        # Scale
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

        photo = ImageTk.PhotoImage(image)
        #root.one = photo
        self.canvas.create_image(x, y, image=photo)


def map_example():
    """Run this from main.py to show this map by itself:
        python main.py --map-ex
    """
    root = Tk()
    root.title("Some Title")
    root.geometry("%dx%d" % (HEIGHT, WIDTH))
    m = Map()
    m.draw_polygon_room("engine-room", [(50, 50), (50, 120), (80, 160), (120, 120), (120, 50)], "blue", "red",
                                    [
                                        [0, 10, "green"],
                                        [1, 10, "green"],
                                        [2, 10, "green"],
                                        [3, -40, "green"],
                                        [4, -40, "green"],
                                    ]) 
    
    m.show()
    m.open_door("engine-room", 0) # Open first door
    root.mainloop()
    
# internal:
    
##########################################################


def rotate(points, angle, pad):
    """Rotate a set of points in given angle relative to given
    pad."""
    angle = math.radians(angle)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    cx, cy = pad
    new_points = []
    for x_old, y_old in points:
        x_old -= cx
        y_old -= cy
        x_new = x_old * cos_val - y_old * sin_val
        y_new = x_old * sin_val + y_old * cos_val
        new_points.append([x_new + cx, y_new + cy])
    return new_points


def find_slope(p1, p2):
    """Find slope between two points"""
    if (p2[0] - p1[0]) == 0:
        return float('inf')
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def find_dx(magnitude, slope):
    """Find the new x value that results from moving with given magnitude and slope."""
    sign = magnitude / abs(magnitude)
    return sign * (sqrt(magnitude ** 2 / (slope ** 2 + 1)).real) if slope != float('inf') else 0


class MapObject:

    def draw(self, canvas):
        raise NotImplemented


class Wall(MapObject):

    def __init__(self, p1, p2, color):
        (self.x1, self.y1), (self.x2, self.y2), self.color = p1, p2, color

    def change_color(self, new_color, canvas):
        self.color = new_color
        self.draw(canvas)

    def draw(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.color, width=WALL_WIDTH)


class Door(MapObject):

    def __init__(self, point, slope, color, background_color):
        """
        
        @param point: starting point
        @param slope: slope in which to draw a DOOR_LENGTH line.
        @param color: color of the door itself.
        @param background_color: color of the floor on which the door stands (which is shown when the door is open).
        """
        self.slope, self.color, self.background_color = slope, color, background_color

        slope_sign = slope / abs(slope) if slope not in (0, float('inf')) else 1
        slope = abs(slope)

        # Find end point of door
        a = self.find_dx(DOOR_LENGTH)
        b = a * slope if slope != float('inf') else DOOR_LENGTH
        
        # Create door's coordinates (it's a line going from (x1,y1) to (x2,y2)
        self.x1, self.y1, self.x2, self.y2 = point[0], point[1], point[0] + a, point[1] + b * slope_sign

        self.is_open = False

    def draw(self, canvas):
        if self.is_open:
            self.open(canvas)
        else:
            self.close(canvas)

    def close(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2,
                           width=WALL_WIDTH,
                           fill=self.color)
        self.is_open = False

    def open(self, canvas):
        # First cover door in a line with color background_color
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.background_color, width=WALL_WIDTH)

        # Then create two lines, each 1/4 of the door's length, at the two sides of the door 
        magnitude = DOOR_LENGTH / 4  # magnitude of on open side of door
        dx = self.find_dx(magnitude)
        dy = dx * self.slope if self.slope != float('inf') else magnitude
        canvas.create_line(self.x1, self.y1, self.x1 + dx, self.y1 + dy, fill=self.color,
                           width=WALL_WIDTH)
        canvas.create_line(self.x1 + 3 * dx, self.y1 + 3 * dy, self.x2, self.y2, fill=self.color,
                           width=WALL_WIDTH)
        self.is_open = True

    def find_dx(self, magnitude):
        return find_dx(magnitude, self.slope)


class Room(MapObject):
    """Room interface."""
    doors, walls = [], []
    
    def __init__(self, *args):
        pass
    
    def draw(self, canvas):
        self.draw_walls(canvas)
        self.draw_doors(canvas)
    
    def open_door(self, ind, canvas):
        self.doors[ind].open(canvas)

    def close_door(self, ind, canvas):
        self.doors[ind].close(canvas)

    def change_wall_color(self, ind, new_color, canvas):
        self.walls[ind].change_color(new_color, canvas)


class PolygonRoom(Room):
    """Draws a polygon room with a list of points and doors.""" 
        

    def __init__(self, points, wall_color, background_color, doors):
        """Each point is a 2-tuple of x and y values. 
        Doors format: (wall_id, offset, door_color). Offset is the number of pixels
        that are between the door's start and the wall's start. So for example if 
        offset is 1/2 the wall's size, then the door will start at the middle of the wall."""
        
        self.points, self.wall_color, self.background_color, self.door_vars = points, wall_color, background_color, doors
        self.points.append(points[0])
        super().__init__(self)
        
    def draw_walls(self, canvas):
        # Draw walls:
        for i in range(len(self.points) - 1):
            p1, p2 = self.points[i], self.points[i + 1]
            wall = Wall(p1, p2, self.wall_color)
            wall.draw(canvas)
            self.walls.append(wall)

        # This makes the walls look smoother
        canvas.create_polygon(self.points, outline=self.wall_color, fill=self.background_color, width=WALL_WIDTH)

    def draw_doors(self, canvas):
        """Draws all the doors. Not the most elegant implementation maybe, 
        so feel free to change it if you have a better idea. But I think it works."""
        for ind, offset, color in self.door_vars:
            
            # Points and slope of the wall on which the door lies
            wall = self.walls[ind]
            x1, y1 = wall.x1, wall.y1
            x2, y2 = wall.x2, wall.y2
            p1, p2 = (x1, y1), (x2, y2)
            m = find_slope(p1, p2)  # slope of the door and wall
            
            # Find starting coords of the door
            dx = find_dx(offset, m)
            start_x = x1 + dx
            start_y = y1 + (m * dx if m < float('inf') else offset)
            
            # Create door and draw it 
            door = Door((start_x, start_y), m, color, self.background_color)
            self.doors.append(door)
            door.draw(canvas)


