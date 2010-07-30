'''
Created on 29 Jul 2010

@author: ms705
'''

import json, gzip
import tempfile

from common import utils

# poster stuff
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

class ResultSubmitter(object):
    '''
    classdocs
    '''


    def __init__(self, resultsDict):
        '''
        Constructor
        '''
        self.res = resultsDict
    
    def submit(self):
        
        # generate a temporary file
        _, tmpfile = tempfile.mkstemp()
        tf = gzip.open(tmpfile, 'wb')
        tf.write(json.dumps(self.res, sort_keys=True, indent=4))
        tf.close()
        
        utils.debug_print("Results saved to:" + tmpfile, utils.SUCC)
        
        # submit them over the network
        
        # Register the streaming http handlers with urllib2
        register_openers()

        # Start the multipart/form-data encoding of the file "DSC0001.jpg"
        # "image1" is the name of the parameter, which is normally set
        # via the "name" parameter of the HTML <input> tag.
        
        # headers contains the necessary Content-Type and Content-Length
        # datagen is a generator object that yields the encoded parameters
        datagen, headers = multipart_encode({"submission1": open(tmpfile, "rb")})

        print headers
        print datagen

        # Create the Request object
        request = urllib2.Request("http://www-dyn.cl.cam.ac.uk/~ms705/survey/index.php", datagen, headers)
        # Actually do the request, and get the response
        print urllib2.urlopen(request).read()
