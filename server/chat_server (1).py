#! /usr/bin/python3

"""
@TODO:
    - Process system commands
    - Save permission level files
    - Self-prompt
    - Known bug: two users can't login at the same time
    - Quit options display client and server (use pygame?)


"""
import sys
import socket
import select
import re
import time

import ipgetter  # pip install ipgetter. This allows the server to fetch it'socket own external ip address

from constants import *


class Client:
    def __init__(self, identity, username=None):
        self.identity = identity
        self.username = username
        if username:
            self.permission_level = USERNAME_TO_PERMISSION_LEVEL[username]
        else:
            self.permission_level = -1  # No permission level, because no username; this is for non-chat clients


class ChatServer:
    def __init__(self, host=HOST, port=PORT):
        print("Your socket:", socket.gethostbyname(socket.gethostname()))
        self.host = host
        self.port = port
        self.socket_to_client = {}
        self.disp_sockets = []
        self.chat_sockets = []
        self.cmd_queue = []
        
    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(10)
        
        # add server socket object to the list of readable connections
        self.socket_to_client[self.socket] = SERVER_USERNAME

        # external_ip=ipgetter.myip()

        print ("Chat server started on port " + str(self.port))
        # print('External IP: '+external_ip)
        # print ('Host: '+host)

        while True:

            # get the list sockets which are ready to be read through select
            # 4th arg, time_out  = 0 : poll and never block
            ready_to_read, ready_to_write, in_error = select.select(self.socket_to_client, [], [], 0)

            for sock in ready_to_read:
                # a new connection request recieved
                if sock == self.socket:
                    new_socket, addr = self.socket.accept()

                    # Handle socket identity
                    identity = self.receive(new_socket)

                    # Handle login and permission level
                    recognized = True
                    if identity == CHAT_CLIENT:
                        self.send(new_socket, "Enter username: ")
                        username = self.receive(new_socket)
                        self.socket_to_client[new_socket] = Client(identity, username)
                        self.chat_sockets.append(new_socket)
                    elif identity == DISP_CLIENT:
                        self.socket_to_client[new_socket] = Client(identity)
                        self.disp_sockets.append(new_socket)
                    else:
                        # Not recognized client identity
                        print ("Connection attempted from (%s, %s), identity unrecognized" % addr)
                        recognized = False

                    # If this chat client was recognized, add it
                    if recognized:
                        print ("Client (%s, %s) connected with permission level %d" % (
                            addr[0], addr[1], self.socket_to_client[new_socket].permission_level))

                        if self.socket_to_client[new_socket].username and self.socket_to_client[new_socket].username!=AI_USERNAME:
                            self.broadcast("[%s] entered the terminal" % self.socket_to_client[new_socket].username,
                                           filter(lambda s:s!=new_socket,self.chat_sockets))

                # a message from a client, not a new connection
                else:
                    # process data received from client,
                    try:
                        # receiving data from the socket.
                        data = self.receive(sock)
                        if not data:
                            raise Exception  # Disconnect

                        data = data.strip()

                        # Return system feedback
                        feedback = ""
                        if re.split("\s+", data)[0] in SYSTEM_COMMANDS:
                            feedback = self.eval_cmd(data, sock)
                            
                            self.send(sock, "\r"+feedback)
                            feedback = "\n" + feedback

                        # Broadcast message and feedback (if exists) to everyone
                        self.broadcast('\r[' + self.socket_to_client[sock].username + '] '
                                       + data + feedback, 
                                       filter(lambda s:s!=sock, self.chat_sockets))
                        
                    # No connection
                    except Exception as e:

                        # Remove socket from server and tell everyone
                        if self.socket_to_client[sock].username:
                            self.broadcast("%s disconnected from terminal" % self.socket_to_client[sock].username,
                                           filter(lambda s:s!=sock, self.chat_sockets))
                        if sock in self.socket_to_client:
                            del self.socket_to_client[sock]

        self.socket.close()

    def eval_cmd(self, line, sock):
        """Evaluate a line entered into the server by some ip address, and output
        system feedback. The socket argument determines permission level."""
        # Do stuff, in a new thread or add to some execution queue
        elems = re.split("\s+", line)
        cmd, args = elems[0], elems[1:]
        
        feedback = "[System] executing %s(%s)\r" % (cmd, ", ".join(args))
        
        self.cmd_queue.append((line))
        
        # Output system feedback about what's happening
        return feedback

    def broadcast(self, message, sockets):
        """Send a message to all sockets except for the ones on the blacklist."""
        for socket in sockets:
            try:
                self.send(socket, message)
            except:
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in self.socket_to_client:
                    del self.socket_to_client[socket]

    def display(self, message):
        self.broadcast("[System] " + message, self.disp_sockets)
        
    def send(self, sock, msg):
        sock.send(msg.encode())
    
    def receive(self, sock):
        return sock.recv(RECV_BUFFER).decode()
if __name__ == "__main__":
    sys.exit(ChatServer().start())
