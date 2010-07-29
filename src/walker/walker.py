'''
Created on 19 Jul 2010

@author: ms705
'''

import os, mimetypes
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
        self.results = self.walk(self.dir)
    
    
    def walk(self, dir):
        totalSize = 0
        numFiles = 0
        numDirs = 0
        id = 0
        
        # set up main result data structure: a list of dicts
        results = []
        
        for root, dirs, files in os.walk(dir, onerror=self.walkError):
            try:
                if self.exiting:
                    return
                #utils.debug_print("DIR: " + root)
                
                numFiles += len(files)
                numDirs += 1
                #self.emit(SIGNAL("scanned(int, int)"), numFiles, numDirs)

                # ignore filer snapshot dirs at the CL
                if '.snapshot' in dirs:
                    dirs.remove('.snapshot')
                    
                #print sum(getsize(join(root, name)) for name in files),
                totalSize += sum(getsize(join(root, name)) for name in files)
                #print "bytes in", len(files), "non-directory files"
                
                for f in files:
                    #utils.debug_print("FILE: " + f)
                    # create a dict for this file
                    fp = join(root, f)
                    mime = mimetypes.guess_type(fp, False)
                    fileDict = {'elementID': id, 'size': getsize(fp), 'isDir': False, 'type': mime, 'path': fp}
                    results.append(fileDict)
                    id += 1

                for d in dirs:
                    #utils.debug_print("SUBDIR: " + d)
                    # create a dict for this subdirectory
                    dp = join(root, d)
                    mime = mimetypes.guess_type(dp, False)
                    dirDict = {'elementID': id, 'size': getsize(join(root, d)), 'isDir': True, 'type': mime, 'path': dp}
                    results.append(dirDict)
                    id += 1
                
            except OSError as e:
                self.walkError(e)
            else:
                pass
        utils.debug_print("walked " + str(numFiles) + " files and " + str(numDirs) + 
                          " directories, totalling " + str(totalSize) + " bytes", utils.SUCC)

        # return the list of dicts (this will be MASSIVE)
        #print json.dumps(results, sort_keys=True, indent=4)
        
        return results


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
        
        