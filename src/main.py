'''
Created on 19 Jul 2010

@author: ms705
'''

import os

from common import utils
from walker import walker

import gtk

if __name__ == '__main__':
    
    # show GUI for preliminary stuff
    builder = gtk.Builder()
    builder.add_from_file("res/gladeTest.glade")
    builder.get_object("surveyDialog").show()
    builder.connect_signals({"on_surveyDialog_destroy": gtk.main_quit})
    gtk.main()    
    
    # launch directory walker
    homeDirPath = os.getenv("HOME","")
    utils.debug_print("Your home directory is: " + homeDirPath)
    
    w = walker.Walker()
    #w.walk("/local/scratch/ms705/survey/HomeDirSurvey")
    w.walk(homeDirPath)
    
    
    pass