'''
Created on 19 Jul 2010

@author: ms705
'''

import os
from os.path import join, getsize
from common import utils

from PyQt4.QtCore import *

class Walker(QThread):
    '''
    classdocs
    '''

    def __init__(self, parent = None):
        '''
        Constructor
        '''
        QThread.__init__(self, parent)
        self.exiting = False
        
    def scan(self, scanRoot):
        self.dir = scanRoot
        self.start()
        
    def run(self):
        utils.debug_print("Starting scan thread...", utils.MSG)
        self.walk(self.dir)
    
    def walk(self, dir):
        size = 0
        numFiles = 0
        numDirs = 0
        for root, dirs, files in os.walk(dir, onerror=self.walkError):
            try:
                if self.exiting:
                    return
                #print root, "consumes",
                
                numFiles += len(files)
                numDirs += 1
                self.emit(SIGNAL("scanned(int, int)"), numFiles, numDirs)

                # ignore filer snapshot dirs at the CL
                if '.snapshot' in dirs:
                    dirs.remove('.snapshot')
                    
                #print sum(getsize(join(root, name)) for name in files),
                size += sum(getsize(join(root, name)) for name in files)
                #print "bytes in", len(files), "non-directory files"
            except OSError as e:
                self.walkError(e)
            else:
                pass
        print "walked ", numFiles, " files and ", numDirs, " directories, totalling ", size, " bytes"
        #self.emit

    def walkError(self, err):
        utils.debug_print(err.strerror + " on " + err.filename, utils.ERR)
        pass
        
    def exit(self):
        utils.debug_print("Scan thread exiting...", utils.MSG)
        self.exiting = True
        
    def __del__(self):
        self.exiting = True
        utils.debug_print("Scan thread waiting to terminate...", utils.MSG, False)
        self.wait()
        
        