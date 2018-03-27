"""Here system constants will be defined that are used throughout the entire program."""

from collections import defaultdict

   
###########################
# Paths
###########################

INPUT_DIR = "input"

    
###########################
# Server constants
###########################

DEFAULT_PORT = 5006  # The port through which connections are made

# This is the address the client is trying to connect to and the server is built at by default
DEFAULT_HOST = "localhost"  

# Specific IP addresses you might want to save for custom uses:
SERVER_IP = "localhost"  

#IP1 =  "141.226.243.200"
#IP2 = "141.226.246.6"
#IP3 = "141.226.246.6"
# Etc'

RECV_BUFFER = 4096  # Maximum size of messages that can be sent or received


# Identities of clients (types of clients)

CHAT_CLIENT = "chat-client"         # Can type and read messages to the chat room and actiavte system commands
DISP_CLIENT = "disp-client"         # This is a window where the full output of system commands is displayed

  
###########################
# Permission levels
###########################

# These are classes of permission level by client username
# When a client executes a command, the AiInterface receives his permission level
# and it can use it to decide if the command can be performed or not.

# Change each of these to change the username of each of these clients
# If you want, you can map each IP to its username automatically
SERVER_USERNAME = "SERVER_USERNAME"
SYSTEM_USERNAME = "System"
AI_USERNAME = "System"
BASIC = "BASIC"

# Permission levels
MASTER_PERMISSION = 0
AI_PERMISSION = 1
ENGINE_ROOM_PERMISSION = 5 # example
DEFAULT_PREMISSION = 3

# Maps username to its permission level
# when a chat client connects, it is prompted for a username, which is then used as the key to this dictionary 
USERNAME_TO_PERMISSION_LEVEL = defaultdict(lambda: DEFAULT_PREMISSION) # 3 is the default permission status
USERNAME_TO_PERMISSION_LEVEL[SERVER_USERNAME] = MASTER_PERMISSION
USERNAME_TO_PERMISSION_LEVEL[SYSTEM_USERNAME] = MASTER_PERMISSION
USERNAME_TO_PERMISSION_LEVEL[AI_USERNAME] = AI_PERMISSION

  
###########################
# System commands
###########################

# These are commands the AiInterface recognizes

# There are different quit commands for chat clients and for the server host/display clients.
# The reason is that we do not want to enable keyboard input for the latter two, and if there is no input,
# then quitting has to happen in a separate window on a different thread using the exit_thread function. 
QUIT_KEY = "q"          # Press this key to shit down AiInterface or a display client
QUIT_CMD = ":q"         # disconnects from terminal as a chat client

BEEP_FREQ = 1000
BEEP_DURATION = 500     # Set Duration To 500 ms == .5 seconds

USERNAME_LENGTH = 12

# Commands that the system recognizes
CMD_TO_HELP = {
    "open" : "Open a door on the map. Args: room name (string), door index (int)",  
    "close" : "Close a door on the map. Args: room name (string), door index (int)",
    "show" : "Show a gui item. Args: AiInterface graphics object name. Currently defined: map, clock.",
    "help" : "Show this message",
}
SYSTEM_COMMANDS = sorted(list(CMD_TO_HELP.keys()))





   
###########################
# Graphics
###########################

# Graph constants
COLORS = ('b', 'g', 'r', 'c', 'm', 'y', 'k')
LINE_STYLES = ['_', '-', '--', ':']


# GUI constants
HEIGHT, WIDTH = 1500, 800       # Canvas dimensions
CANVAS_MID_X = WIDTH / 2        
CANVAS_MID_Y = HEIGHT / 2
BACKGROUND_COLOR = "white"
WALL_WIDTH = 5                  # Default width of walls and doors
DOOR_LENGTH = 20                # Default length of doors

