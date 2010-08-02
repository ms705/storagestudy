'''
Created on 29 Jul 2010

@author: ms705
'''

from PyQt4 import QtCore

# poster stuff
from poster.encode import *
from poster.streaminghttp import *
import urllib2

class ResultSubmitter(QtCore.QObject):
    '''
    classdocs
    '''

    # configure the URL to POST gzip'ed files to here
    SUBMISSION_URL = "http://www-dyn.cl.cam.ac.uk/~ms705/survey/submissiontest.php"


    def __init__(self):
        '''
        Constructor
        '''
        #self.res = resultsDict
    
    def submit(self, tempfile):
        
        # submit the results over the network
        
        # Register the streaming http handlers with urllib2
        register_openers()

        # Start the multipart/form-data encoding of the file "DSC0001.jpg"
        # "image1" is the name of the parameter, which is normally set
        # via the "name" parameter of the HTML <input> tag.
        
        # headers contains the necessary Content-Type and Content-Length
        # datagen is a generator object that yields the encoded parameters
        file_param = MultipartParam.from_file("submission1", tempfile)
        datagen, headers = multipart_encode([file_param])


        # Create the Request object
        global SUBMISSION_URL
        request = urllib2.Request(self.SUBMISSION_URL, datagen, headers)
        # Actually do the request, and get the response
        size = int(headers['Content-Length'])
        #self.emit(QtCore.SIGNAL("makingHTTPRequest(int)"), size)

        resp = urllib2.urlopen(request)
        #i = 0
        #while i < size:
        #    resp.read(4096)
        #    i += 4096
        #    print str(i / 4096) + "%"
        resp.read()

        #self.emit(QtCore.SIGNAL("finishedHTTPRequest()"))

        resp.close()
