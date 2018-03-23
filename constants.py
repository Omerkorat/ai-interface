"""Here system constants will be defined that are used throughout the entire program."""

from collections import defaultdict


# Paths

INPUT_DIR = "input"

    

# Server constants

PORT = 5006  # The port through which connections are made
AI_IP = ""  # Address of the machine whose user plays the AI 

# This is the IP that sets up the server
SERVER_IP = "localhost"  

# This is the address the client is trying to connect to automatically
HOST = "localhost"  

#SERVER_IP =  "141.226.243.200"  # Address of the server host
# SERVER_IP = "141.226.246.6"
# HOST = "141.226.246.6"

RECV_BUFFER = 4096  # Maximum size of messages that can be sent or received

N_TERMINALS = 5  # Example


# Identities

CHAT_CLIENT = "chat-client"
DISP_CLIENT = "disp-client"

# Permission levels:

# Change each of these to change the username of each of these clients
SERVER_USERNAME = "SERVER_USERNAME"
SYSTEM_USERNAME = "System"
AI_USERNAME = "System"
BASIC = "BASIC"

MASTER_PERMISSION = 0
AI_PERMISSION = 1
ENGINE_ROOM_PERMISSION = 5 # example
DEFAULT_PREMISSION = 3


USERNAME_TO_PERMISSION_LEVEL = defaultdict(lambda: DEFAULT_PREMISSION) # 3 is the default permission status
USERNAME_TO_PERMISSION_LEVEL[SERVER_USERNAME] = MASTER_PERMISSION
USERNAME_TO_PERMISSION_LEVEL[SYSTEM_USERNAME] = MASTER_PERMISSION
USERNAME_TO_PERMISSION_LEVEL[AI_USERNAME] = AI_PERMISSION

# Graph constants

COLORS = ('b', 'g', 'r', 'c', 'm', 'y', 'k')
LINE_STYLES = ['_', '-', '--', ':']

# Command prompt constants

BEEP_FREQ = 1000
BEEP_DURATION = 500 # Set Duration To 500 ms == .5 seconds

USERNAME_LENGTH = 12

# Commands that the system recognizes
SYSTEM_COMMANDS = [
    "mkdir",
    "open",
    "close",
    "show"
]
QUIT_CMD = ":q"  # disconnects from terminal
