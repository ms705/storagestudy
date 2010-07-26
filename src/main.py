'''
Created on 19 Jul 2010

@author: ms705
'''

import sys

#import gtk
from PyQt4 import QtGui, QtCore

from gui import surveyWelcomeDialog

if __name__ == '__main__':
    
    # set up Qt application
    app = QtGui.QApplication(sys.argv)
    m = surveyWelcomeDialog.surveyWelcomeDialog(app)
    m.show()
    
    sys.exit(app.exec_())

    pass