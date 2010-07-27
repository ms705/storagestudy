'''
Created on 23 Jul 2010

@author: ms705
'''

import os, sys
import ui_scanning

from PyQt4 import QtGui
from PyQt4.QtCore import *

from common import utils
from walker import walker


class surveyScanningDialog(QtGui.QDialog):
    
    def __init__(self, owner):        
        QtGui.QMainWindow.__init__(self)
        self.ui = ui_scanning.Ui_scanDialog()
        self.ui.setupUi(self)
        
        # set up worker thread
        self.scanThread = walker.Walker()
        self.callbacks = 0

        # signal/slot connections
        self.connect(self.scanThread, SIGNAL("finished()"), self.finishedScanning)
        self.connect(self.scanThread, SIGNAL("terminated()"), self.error)
        #self.connect(self.scanThread, SIGNAL(""))
        self.connect(self.ui.btnCancel, SIGNAL('clicked()'), self.cancel)
        self.connect(self.scanThread, SIGNAL("scanned(int, int)"), self.iterate)

        #vpos = d.height() / 2 - (self.height() / 2);
        #if (d.width() > 2*d.height()):
        #    hpos = d.width() / 4 - (self.width() / 2);
        #else:
        #    hpos = d.width() / 2 - (self.width() / 2);
        #self.move(hpos, vpos);
        self.center()
        
        homeDirPath = os.getenv("HOME","")
        utils.debug_print("Your home directory is: " + homeDirPath)
        self.scanThread.scan(homeDirPath)


    def cancel(self):
        if self.confirmClose():
            utils.debug_print("Cancelled scanning!", utils.ERR)
            self.scanThread.exit()
            quit()
        else:
            pass
    
    def iterate(self, files, dirs):
        self.callbacks += 1
        #utils.debug_print("iterated: added " + str(files) + " files and " + str(dirs) + " directories.", utils.MSG)
        
        #if self.callbacks > 100:
        #    avgfiles = files / dirs
        #    self.ui.progressBar.setMaximum(files + dirs)
        #    self.ui.progressBar.setMinimum(0)
        #    self.ui.progressBar.reset()
        #    self.ui.progressBar.setValue(files)
    
    def finishedScanning(self):
        utils.debug_print("Finished scanning", utils.SUCC)
        
        # TODO show results screen here
        quit()
    
    
    def error(self):
        utils.debug_print("Scan thread terminated unexpectedly!", utils.ERR)
    
    
    def closeEvent(self, event):
        if self.confirmClose():
            event.accept()
        else:
            event.ignore()    
        
        
    def confirmClose(self):
        reply = QtGui.QMessageBox.question(self, 'Confirm cancellation',
            "Are you sure you want to cancel? This will mean that all data entered" +  
            "is lost and no results are submitted to the researchers.", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        return (reply == QtGui.QMessageBox.Yes)
    
    
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

        # launch directory walker
        #homeDirPath = os.getenv("HOME","")
        #utils.debug_print("Your home directory is: " + homeDirPath)
        
        #w = walker.Walker()
        #w.walk("/local/scratch/ms705/survey/HomeDirSurvey")
        #w.walk(homeDirPath)
        