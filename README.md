### Overview

This program defines a user interface with GUI, a chat server, and system commands. Once a host starts the interface starts, clients can connect to a server and chat with each other, and type 
system commands. System commands are passed to the host and can interact with the GUI or instruct the host to perform any other computation. They are evaluated by the host process/machine, not by the process/machine that runs the client. 

The GUI currently runs only on the host process, so if you are connected from a different machine you cannot see the GUI. This will be changed in future versions.

## Usage

To start the interface, run:

	python main.py
	
This will start an instance of the AiInterface class. This class in turn starts a server and a GUI which can communicate with each other and with clients connected to the server. The GUI runs on the main thread, and the server runs on a separate thread. The server and GUI are fields of the AiInterface. 
To connect to the server as a chat client:

	python main.py -cclien

A chat client can type messages to the chat room. AiInterface has a 'while True' loop (the method 'command_loop') which runs on its own thread and constantly checks the server's todo queue. If a message written by a client starts with a word which appears in the list of known system commands, it will be added to the server's todo queue, and the command loop will pop it out of the queue. 
After a command was popped out of the server it is evaluated by the AiInterface's eval_cmd method,
which displays the output to all connected display clients. Display clients are there simply to
show the full output of system commands, which enables the server to stay clean for chatting. A
short feedback message will be displayed to the chat clients when a command is executed. System output is global, so all display clients are the same. 
To connect for display:

	python main.py -dclient
	
	
## Customization

The parts of this program were written with the intention of being customized for many different purposes. Many parts of this program are templates, and they were accompanied by examples and explanations how to modify them for other purposes. To add system commands, add them to the CMD_TO_HELP constant, which maps command names to their help documentation strings. The server
will now recognize these commands as valid system commands. To define what a command does, go to
AiInterface.cmd_loop and create an if-clause that recognizes this commands and decides what it does.
Commands can print any output to display clients, and they can interact with the AiInterface's internal variables. For example, it can change permission levels, do computations in the background and save them to the internal dictionary (AiInterface.vars), and interact with the GUI. For examples see AiInterface.
To create new GUI items, use the existing templates. A GUI item is a subclass of Tk.Frame with a show() method. You can define a GUI item as a class with any graphics you wish, and then to display it call its show() method, which will put it on the GUI. It needs to be saved as a variable of AiInterface in order to be available for usage and interaction.


## Remote conection
 
 
To connect remotely to a server, you should pass its public IP address as the host parameter. If you are connected via a public network or a router, your public IP is the address of that network/router, and you have to make sure that the server starts on a port which is routed to your machine upon incoming connections to your network/router. 