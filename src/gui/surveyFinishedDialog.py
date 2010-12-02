'''
Created on 23 Jul 2010

@author: ms705
'''
import sys
import json, gzip
import tempfile

import ui_finished

from PyQt4 import QtGui
from PyQt4.QtCore import *

from common import utils
from results import submit

# Windows distributable versions of Python don't have a quit()
# primitive, so we need to define it in every file!
def quit():
    sys.exit(0)
    pass


class surveyFinishedDialog(QtGui.QDialog):
    
    def __init__(self, owner, results, token):        
        QtGui.QMainWindow.__init__(self)
        self.ui = ui_finished.Ui_finishedDialog()
        self.ui.setupUi(self)
        self.ui.progressBar.hide()
        
        self.done = False
        self.submitter = submit.ResultSubmitter()
        self.token = token;
        

        # generate a temporary file and store the results there
        _, tmpfile = tempfile.mkstemp(suffix='.gz')
        tf = gzip.open(tmpfile, 'wb')
        tf.write(json.dumps(results, sort_keys=True, indent=4))
        tf.close()

        # store the tempfile path
        self.tmpfile = tmpfile
        
        utils.debug_print("Results saved to:" + tmpfile, utils.SUCC)
        
        self.ui.reviewPathLabel.setText('<b>' + tmpfile + '</b>')
        
        # signal/slot connections
        self.connect(self.ui.btnCancel, SIGNAL('clicked()'), self.cancel)
        self.connect(self.ui.btnNext, SIGNAL('clicked()'), self.next)
        #self.connect(self.submitter, SIGNAL('makingHTTPRequest(int)'), self, SLOT('updateProgress(int)'))
        #self.connect(self.submitter, SIGNAL('finishedHTTPRequest()'), self.updateProgress(100))
        

    def next(self):
        self.done =  True
        
        self.ui.progressBar.show()
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(100)
        # actually submit the data
        self.submitter.submit(self.tmpfile, self.token)
        
        #for i in range(1,5):
        #    print self.results[i]
        
        # This is broken - just set the progress bar from 0 to 100 once done
        self.ui.progressBar.setValue(100)
        
        # done
        QtGui.QMessageBox.information(self, 'Data submitted',
            "The data has been submitted. Thank you for participating!", QtGui.QMessageBox.Ok)
        quit()
        
        
    def cancel(self):
        if self.confirmClose():
            utils.debug_print("Cancelled before submission!", utils.ERR)
            quit()
        else:
            pass
    
    
    def closeEvent(self, event):
        if not self.done: 
            if self.confirmClose():
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
        
        
    def confirmClose(self):
        reply = QtGui.QMessageBox.question(self, 'Confirm cancellation',
            "Are you sure you want to cancel? This will mean that all data entered " +  
            "is lost and no results are submitted to the researchers.", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        return (reply == QtGui.QMessageBox.Yes)
    
    
    def updateProgress(self, percent):
        self.ui.progressBar.setValue(percent)
        
    
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
