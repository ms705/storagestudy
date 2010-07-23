#!/bin/bash 
# build eggs used by the tool

PLATFORM=`uname`
WGET="wget -c"
PYTHON=/usr/bin/python

CDIR=$(pwd)
#V=2.0.9
set -ex
LIBDIR=$CDIR/libs
mkdir -p $LIBDIR

# Python version to use
PV=26

#-----------
# On the Mac, we need to install an alternative 
# python version from MacPorts first
if [[ $PLATFORM == 'Darwin' ]]; then 
  port install python$PV
  python_select pythong$PV
fi

#-----------
# Install SIP
SIPV='4.10.5'
if [[ $PLATFORM == 'Darwin' ]]; then 
  port install py$PV-sip
elif [[ $PLATFORM == "Linux" ]]; then
  cd $LIBDIR
  if [ ! -f "$LIBDIR/sip-$SIPV.tar.gz" ]; then
    $WGET http://www.riverbankcomputing.co.uk/static/Downloads/sip4/sip-$SIPV.tar.gz
  fi
  tar -zxvf sip-$SIPV.tar.gz
  cd sip-$SIPV
  $PYTHON configure.py
  make
  make install
fi

#-----------
# Install PyQt
PYQTV='4.7.4'
if [[ $PLATFORM == 'Darwin' ]]; then 
  port install py$PV-pyqt4
elif [[ $PLATFORM == "Linux" ]]; then
  cd $LIBDIR
  $WGET http://www.riverbankcomputing.co.uk/static/Downloads/PyQt4/PyQt-x11-gpl-$PYQTV.tar.gz
  tar -zxvf PyQt-x11-gpl-$PYQTV.tar.gz
  cd PyQt-x11-gpl-$SIPV
  $PYTHON configure.py
  make
  make install
fi


