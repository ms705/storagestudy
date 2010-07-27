'''
Created on 23 Jul 2010

@author: ms705
'''
from gui.surveyScanningDialog import surveyScanningDialog
from gui.checkableDirModel import CheckableFSModel

import ui_folderselection
from PyQt4 import QtGui
from PyQt4.QtCore import *

from common import utils

class surveyFolderSelectionDialog(QtGui.QDialog):
    
    def next(self):
        utils.debug_print("Folders selected:", utils.SUCC)
        self.close()
        d = surveyScanningDialog(self.app)
        d.setAttribute(Qt.WA_DeleteOnClose)    
        d.exec_()

    def __init__(self, owner):        
        QtGui.QMainWindow.__init__(self)
        self.ui = ui_folderselection.Ui_surveyDialog()
        self.ui.setupUi(self)
        self.app = owner;

        # signal/slot connections
        self.connect(self.ui.btnCancel, SIGNAL('clicked()'), QtGui.qApp, SLOT('quit()'))
        self.connect(self.ui.btnNext, SIGNAL('clicked()'), self.next)
    
        # set up the directory tree
        #self.model = QtGui.QFileSystemModel()
        index = QModelIndex()
        dir_model = CheckableFSModel()
        filters = QDir.AllDirs|QDir.Readable|QDir.NoDotAndDotDot
        dir_model.setData(index, Qt.Checked, Qt.CheckStateRole)
        dir_model.setFilter(filters)
        dir_model.setReadOnly(True)
        self.ui.directoryTree.setModel(dir_model)
        self.ui.directoryTree.setColumnHidden(1, True)
        self.ui.directoryTree.setColumnHidden(2, True)
        self.ui.directoryTree.setColumnHidden(3, True)
        self.ui.directoryTree.expandToDepth(0) 
        #self.tree = QtGui.QTreeView()
        #self.ui.directoryTree.setModel(self.model)
        #self.tree.setModel(self.model)
    
        #d = QtGui.QApplication.desktop()
        #print d.width(), " by ", d.height() 

        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

        #vpos = d.height() / 2 - (self.height() / 2);
        #if (d.width() > 2*d.height()):
        #    hpos = d.width() / 4 - (self.width() / 2);
        #else:
        #    hpos = d.width() / 2 - (self.width() / 2);
        #self.move(hpos, vpos);

