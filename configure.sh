#!/bin/bash


if [[ $PLATFORM == 'Darwin' ]]; then 
  PYUIC4='pyuic4-2.6'
  PYRCC4='pyrcc4-2.6'
elif [[ $PLATFORM == "Linux" ]]; then
  PYUIC4='pyuic4'
  PYRCC4='pyrcc4'
else
  PYUIC4='pyuic4'
  PYRCC4='pyrcc4'
fi


# UI files
$PYUIC4 src/gui/welcome.ui > src/gui/ui_welcome.py
$PYUIC4 src/gui/scanning.ui > src/gui/ui_scanning.py

# resources
$PYRCC4 res/qtresources.qrc > src/gui/qtresources_rc.py
