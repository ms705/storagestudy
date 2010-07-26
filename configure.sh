#!/bin/bash

PYUIC4='pyuic4-2.6'
PYRCC4='pyrcc4-2.6'

# UI files
$PYUIC4 src/gui/welcome.ui > src/gui/ui_welcome.py
$PYUIC4 src/gui/scanning.ui > src/gui/ui_scanning.py

# resources
$PYRCC4 res/qtresources.qrc > src/gui/qtresources_rc.py
