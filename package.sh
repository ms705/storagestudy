#!/bin/bash

PLATFORM=`uname`

if [[ $PLATFORM == 'Darwin' ]]; then
  echo "Building Mac OS X App using py2app..."
  python src/setup/setup_mac.py py2app
elif [[ $PLATFORM == "Linux" ]]; then
  echo "No binary support on linux yet."
else
  echo "Unrecongnised platform: cannot build package."
fi

