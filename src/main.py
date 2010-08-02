'''
Created on 19 Jul 2010

@author: ms705
'''

import sys

#import gtk
from PyQt4 import QtGui, QtCore

from gui import surveyWelcomeDialog

# configure the URL to POST gzip'ed files to here
SUBMISSION_URL = "http://www-dyn.cl.cam.ac.uk/~ms705/survey/submissiontest.php"

if __name__ == '__main__':
    
    # set up Qt application
    app = QtGui.QApplication(sys.argv)
    m = surveyWelcomeDialog.surveyWelcomeDialog(app)
    m.show()
    
    sys.exit(app.exec_())

    pass