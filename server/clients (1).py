#! /usr/bin/python3


# Example on how to use a dynamic loading bar:
# from click.termui import progressbar
# import time
#
#
# i=0
# with progressbar(range(2**10), fill_char="=", empty_char=".") as bar:
#     for item in bar:
#         i+=item
#         time.sleep(.009)
# print("Result:", i)

import cmd
import argparse
import sys
import socket
import select
import threading
import time
import winsound
from constants import *
from sys import stdout

class Client:

    run_loop=[1]
    identity = ""
    prompt = ""
    # Standard pythonic way to implement abstract methods
    def run(self, host=HOST, port=PORT):
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
                sock = select.select([self.socket], [], [])[0][0]  # This should be discarded and  only socket used
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
    "79.181.140.220"
    
    def run(self, host=HOST, port=PORT):
        print("Connectiong to host %s:%s..." %(HOST, PORT))
        self.connect(host,port)

        # Login:
        username_prompt = self.receive()
        self.username = input(username_prompt)
        self.send(self.username)
        print ("Welcome, %s." % self.username)
        print("type %s to quit." % QUIT_CMD)
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

    def run(self, host="localhost", port=PORT):
        self.connect(host, port)
        self.recv_messages()

