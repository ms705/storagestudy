#!/bin/bash

PLATFORM=`uname`

if [[ $PLATFORM == 'Darwin' ]]; then
  echo "Building Mac OS X App using py2app..."
  python src/setup/setup_mac.py py2app
elif [[ $PLATFORM == "Linux" ]]; then
  echo "Binary support on linux requires pyinstaller-1.4, which has not been scripted yet. Please use 'make run' to run the tool."
else
  echo "Unrecongnised platform: cannot build package."
fi

