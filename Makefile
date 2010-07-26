.PHONY: all run scan clean

PYTHON=/usr/bin/python

# configure: compile resource files etc.
configure:
	./configure.sh

# build everything
all: 
	./build.sh

# run server
run:
	cd src $(PYTHON) main.py

# clean
clean:
	rm -f *.pyc

