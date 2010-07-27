'''
Created on 27 Jul 2010

@author: ms705
'''

from PyQt4 import QtGui
from PyQt4.QtCore import *


class CheckableFSModel(QtGui.QDirModel):
    checked = []
        
    def data(self, index, role = Qt.DisplayRole):

        if index.isValid() and (index.column() == 0) and (role == Qt.CheckStateRole):
            # the item is checked only if we have stored its path
            #print CheckableFSModel.checked, unicode(self.filePath(index))
            if unicode(self.filePath(index)) in CheckableFSModel.checked:
                return Qt.Checked
            else:
                return Qt.Unchecked
                
        return QtGui.QDirModel.data(self, index, role)        
        
    def flags(self, index):
        if (index.column() == 0): # make the first column checkable
            return QtGui.QDirModel.flags(self, index) | Qt.ItemIsUserCheckable
        else:
            return QtGui.QDirModel.flags(self, index)            
        
    def setData(self, index, value, role = Qt.EditRole):
        if index.isValid() and (index.column() == 0) and role == Qt.CheckStateRole:
            # store checked paths, remove unchecked paths
            if (value == Qt.Checked):
                CheckableFSModel.checked.append(unicode(self.filePath(index)))
                return False
            else:
                CheckableFSModel.checked.remove(unicode(self.filePath(index)))
                return False
                
        else:
            return QtGui.QDirModel.setData(self, index, value, role); 
