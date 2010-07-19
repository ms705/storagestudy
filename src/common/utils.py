'''
Created on 20 Jan 2010

@author: ms705
'''

YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
GRAY = '\033[90m'
ENDCOLOUR = '\033[0m'
    
DEBUG_LEVEL = 4
    
WARN = 0
ERR = 1
MSG = 2
SUCC = 3
    
def debug_print(message, type=MSG, newline=0):
    """ test """
    # Prints debug message

    if DEBUG_LEVEL != 0:
        if type == WARN: 
            if DEBUG_LEVEL >= 2:
                print YELLOW + "[WARN]: " + ENDCOLOUR + message + ("\n" if newline else "")
        elif type == ERR:
            if DEBUG_LEVEL >= 1:
                print RED + "[ERR]: " + ENDCOLOUR + message + ("\n" if newline else "")
        elif type == MSG:
            if  DEBUG_LEVEL >= 3:
                print GRAY + "[DBG]: " + ENDCOLOUR + message + ("\n" if newline else "")
        elif type == SUCC: 
            if DEBUG_LEVEL >= 1:
                print GREEN + "[OK]: " + ENDCOLOUR + message + ("\n" if newline else "")
        else:
            raise Exception("Unknown message type encountered.")
    else:
        pass
    