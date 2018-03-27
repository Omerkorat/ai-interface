"""This file is used to test Omer's code. It is part of the omer branch and should only be used to
test Omer's code. The reason we need this is because Omer's code will ultimately be run from this directory, and not from
the omer directory, in order to integrate it with the rest of the code."""

import sys, argparse
from constants import *


def main(args):
    if args.map_ex:
        from graphics.frames import map_example
        map_example()
    elif args.server:
        from server.chat_server import ChatServer
        ChatServer(args.host, args.port).start()
    elif args.cclient:
        from server.clients import ChatClient
        ChatClient().run(args.host, args.port)
    elif args.dclient:
        from server.clients import DispClient
        DispClient().run(args.host, args.port)
    else:
        from AiInterface import AiInterface
        AiInterface(server_host=args.host, server_port=args.port).run()

if __name__ == '__main__':
    # Parse runtime options from command line
    parser = argparse.ArgumentParser()

    # Options:
    parser.add_argument("-server", action="store_true", default=False, help="Start chat server.")
    parser.add_argument("-cclient", action="store_true", default=False, help="Start chat client.")
    parser.add_argument("-dclient", action="store_true", default=False, help="Start display client.")
    parser.add_argument("-host", type=str, default=DEFAULT_HOST, help="Host IP address string to connect/start a server in. To connect locally use localhost.")
    parser.add_argument("-port",type=int, default=DEFAULT_PORT, help="Port to connect/start a server in. Default: 5006.")
    parser.add_argument("-me","--map-ex",action="store_true", default=False, help="Show map example.")
    
    # Now get a list of options and all their arguments
    args = parser.parse_args()

    main(args)