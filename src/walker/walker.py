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
        for root, dirs, files in os.walk(dir, onerror=self.walkError):
            try:
                print root, "consumes",
                print sum(getsize(join(root, name)) for name in files),
                print "bytes in", len(files), "non-directory files"
                if 'CVS' in dirs:
                    dirs.remove('CVS')  # don't visit CVS directories
            except OSError as e:
                self.walkError(e)
            else:
                pass

    def walkError(self, err):
        print "ERROR!"
        pass
        