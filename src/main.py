'''
Created on 19 Jul 2010

@author: ms705
'''

import os
import sys

from common import utils
from walker import walker

#import gtk
from PyQt4 import QtGui

from gui import surveyMainWindow


if __name__ == '__main__':
    
    # show GUI for preliminary stuff
#    builder = gtk.Builder()
#    builder.add_from_file("res/gladeTest.glade")
#    builder.get_object("surveyDialog").show()
#    builder.connect_signals({"on_surveyDialog_destroy": gtk.main_quit})
#    gtk.main()
    app = QtGui.QApplication(sys.argv)
    m = surveyMainWindow.surveyMainWindow(app)
    m.show()
    
    sys.exit(app.exec_())

    # launch directory walker
    homeDirPath = os.getenv("HOME","")
    utils.debug_print("Your home directory is: " + homeDirPath)
    
    w = walker.Walker()
    #w.walk("/local/scratch/ms705/survey/HomeDirSurvey")
    w.walk(homeDirPath)
    
    
    pass