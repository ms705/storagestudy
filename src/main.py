'''
Created on 19 Jul 2010

@author: ms705
'''

import os

from common import utils
from walker import walker

if __name__ == '__main__':
    
    # show GUI for preliminary stuff
    
    
    # launch directory walker
    homeDirPath = os.getenv("HOME","")
    utils.debug_print("Your home directory is: " + homeDirPath)
    
    w = walker.Walker()
    w.walk(homeDirPath)
    
    
    pass