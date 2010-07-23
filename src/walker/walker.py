'''
Created on 19 Jul 2010

@author: ms705
'''

import os
from os.path import join, getsize

class Walker(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def walk(self, dir):
        size = 0
        numFiles = 0
        numDirs = 0
        for root, dirs, files in os.walk(dir, onerror=self.walkError):
            try:
                #print root, "consumes",
                
                # ignore filer snapshot dirs at the CL
                if '.snapshot' in dirs:
                    dirs.remove('.snapshot')
                    
                #print sum(getsize(join(root, name)) for name in files),
                size += sum(getsize(join(root, name)) for name in files)
                numFiles += len(files)
                numDirs += 1
                #print "bytes in", len(files), "non-directory files"
            except OSError as e:
                self.walkError(e)
            else:
                pass
        print "walked ", numFiles, " files and ", numDirs, " directories, totalling ", size, " bytes"

    def walkError(self, err):
        print "ERROR! ", err.strerror, " on ", err.filename
        pass
        