"""This file is used to test Omer's code. It is part of the omer branch and should only be used to
test Omer's code. The reason we need this is because Omer's code will ultimately be run from this directory, and not from
the omer directory, in order to integrate it with the rest of the code."""

import sys, argparse

def main(args):
    if args.server:
        from server.chat_server import ChatServer
        ChatServer().start()
    elif args.cclient:
        from server.clients import ChatClient
        ChatClient().run()
    elif args.disp:
        from server.clients import DispClient
        DispClient().run()
    else:
        from AiInterface import AiInterface
        AiInterface().run()

if __name__ == '__main__':
    # Parse runtime options from command line
    parser = argparse.ArgumentParser()

    # Options:
    parser.add_argument("-server", action="store_true", default=False, help="Start chat server.")
    parser.add_argument("-cclient", action="store_true", default=False, help="Start chat client.")
    parser.add_argument("-disp", action="store_true", default=False, help="Start display client.")
    # Now get a list of options and all their arguments
    args = parser.parse_args()

    main(args)