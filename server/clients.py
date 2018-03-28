#! /usr/bin/python3


# Example on how to use a dynamic loading bar:
# from click.termui import progressbar
# import time
#
#
# i=0


import cmd
import argparse
import sys
import socket
import select
import threading
import time
import winsound
from sys import stdout

try:
    from utils import *
    print("Running clients.py in administrator mode")
    print("Variables are imported from utils.py")
except ImportError:
    print("Running clients.py in client mode")
    print("Variables are defined locally.")
    print("Please make sure these definitions match those of the server you are trying to conect to.")
    
    # This is the address the client is trying to connect to and the server is built at by default
    DEFAULT_HOST = "localhost" 
    # The port through which connections are made
    DEFAULT_PORT = 5006 
    # Maximum size of messages that can be sent or received
    RECV_BUFFER = 4096  
    # Can type and read messages to the chat room and actiavte system commands
    CHAT_CLIENT = "chat-client"         
    # This is a window where the full output of system commands is displayed
    DISP_CLIENT = "disp-client"         
    # Max username length
    USERNAME_LENGTH = 12
    # disconnects from terminal as a chat client
    QUIT_CMD = ":q"         

    def pad(string, length, pad_char= ' '):
        """Put @string in the middle of a @lenght-long sequence of @pad_char,
        truncating it if necessary."""
        return string[:length].center(length,pad_char)

class Client:

    run_loop=[1]
    quit_list = []
    identity = ""
    prompt = ""

    # Standard pythonic way to implement abstract methods
    def run(self, host=DEFAULT_HOST, port=DEFAULT_PORT):
        raise NotImplementedError

    def connect(self, host, port):
        """Connect to a server and start sharing data."""
        self.socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)  # Creates a socket through which we talk with host
        self.socket.settimeout(2)  # If host does not respond after this many seconds, disconnect
        # connect to remote host
        self.socket.connect_ex((host, port))  # Try to connect to host.

        try:
            self.send(self.identity)
        except socket.timeout:
            print("Failed to connect.")
            sys.exit()
        
        
    def recv_messages(self):
        """Recieves messages from the server."""
        while self.run_loop:  # Run until sent_t stops, in which case self.run_loop will be popped
            try:
                sock = select.select([self.socket], [], [])[0][0]
                data = sock.recv(RECV_BUFFER).decode()
                if data:
                    stdout.write(data+"\n" + self.prompt)

                    #winsound.Beep(BEEP_FREQ, BEEP_DURATION) # send beeps 

                else:
                    self.run_loop.pop()  # will cause disconnection
            except socket.error:
                pass
            except ValueError as e:
                # Sometimes when disconnecting, value error is raised, I don't know why. 
                # We probably just have to ignore those cases.
                if str(e)!="file descriptor cannot be a negative integer (-1)":
                    print(e)
        print("\rDisconnected from terminal")
    
    def send(self, msg):
        self.socket.send(msg.encode())
    
    def receive(self):
        return self.socket.recv(RECV_BUFFER).decode()
    
class ChatClient(Client):
    """A client for sending and receiving text messages and commands to a server."""
    identity = CHAT_CLIENT
    
    def run(self, host=DEFAULT_HOST, port=DEFAULT_PORT):
        print("Connectiong to host %s:%s..." %(host, port))
        self.connect(host,port)

        # Login:
        username_prompt = self.receive()
        self.username = pad(input(username_prompt),USERNAME_LENGTH)
        self.send(self.username)
        print ("Welcome, %s." % self.username.strip())
        print("type %s to quit. Type 'help' to print available commands to display clients." % QUIT_CMD)
        self.prompt = "[%s] " % self.username

        # Invoke a thread with the send_messages function, allowing messages to now be sent
        send_t = threading.Thread(name="send_t", target=self.send_messages, args=[])
        send_t.daemon = True
        send_t.start()

        self.recv_messages()


    def send_messages(self):
        """Should run on a thread of its own. Sends messages from sys.stdin.readline() through socket"""
        msg = ""
        # There is a delay between the two threads. We wait until the delay is broken and then
        # start modifying the self.waiting variable
        in_delay = True

        while msg != QUIT_CMD:

            stdout.write("\r"); stdout.write(self.prompt); stdout.flush()
            msg = sys.stdin.readline().strip()  # reads message
            # Prompt: (but it creates problems)
            self.send(msg)  # Sends data

            time.sleep(.1) # Delay to give system time to print feedback

        self.socket.close()
        self.run_loop.pop()  # self.run_loop is now empty, which will cause the main loop to stop

class DispClient(Client):
    """A client that only displays detailed system information."""
    identity = DISP_CLIENT
    
    def run(self, host=DEFAULT_HOST, port=DEFAULT_PORT):
        self.connect(host, port)
        print ("Connected in display mode. Full system output will be printed here.")
        print("This client will stay connected to the server until it shuts down.")
        self.recv_messages()

if __name__ == '__main__':
    # Parse runtime options from command line
    parser = argparse.ArgumentParser()

    # Options:
    parser.add_argument("-cclient", action="store_true", default=False, help="Start chat client.")
    parser.add_argument("-dclient", action="store_true", default=False, help="Start display client.")
    parser.add_argument("-host", type=str, default=DEFAULT_HOST, help="Host IP address string to connect/start a server in. To connect locally use localhost.")
    parser.add_argument("-port",type=int, default=DEFAULT_PORT, help="Port to connect/start a server in. Default: 5006.")
    
    # Now get a list of options and all their arguments
    args = parser.parse_args()
    
    if args.cclient:
        ChatClient().run(args.host, args.port)
    elif args.dclient:
        DispClient().run(args.host, args.port)
    