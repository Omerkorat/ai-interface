import time
from click.termui import progressbar


from constants import *

def exit_thread(quit_list):
    """Call this method to start an exit box.
    Whenever this box is an active window and the user presses the 'q' key, 
    quit_list will be set to [True]. This can be used to handle quitting 
    gracefully without a KeyBoardInterrupt. Whichever method should support
    quitting should have an 'if quit_list: quit()' statement wherever quitting
    is to be enabled. This is also useful because you might want to make sure that the
    system closes any open files before quitting is made possible. In such a case
    just make sure that 'if quit_list: quit()' is not inside the scope of an open
    file."""
    
    print("To quit, type 'q' when the pygame box is active.")
    print("Quitting might take a while because the exit thread waits for open files.")
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((1, 1))
    
    while not quit_list:
        key_state = pygame.key.get_pressed()
        if key_state[getattr(pygame, "K_"+QUIT_KEY)]:
            quit_list.append(True)
        pygame.event.pump()  # process event queue  

def pad(string, length, pad_char= ' '):
    """Put @string in the middle of a @lenght-long sequence of @pad_char,
    truncating it if necessary."""
    return string[:length].center(length,pad_char)


def progbar(n=2**10, sleep_time = .009):
    """This is a graphics tool for coolness that display a progress bar that iterates does @n iterations, each of which
    taking @sleep_time seconds."""
    i=0
    with progressbar(range(n), fill_char="=", empty_char=".") as bar:
        for item in bar:
            i+=item
            time.sleep(sleep_time)
    print("Result:", i)