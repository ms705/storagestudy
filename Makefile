.PHONY: all run scan clean

PYTHON=/usr/bin/python

# build everything
all: 
	./build.sh

# run server
run:
	cd src $(PYTHON) main.py

# clean
clean:
	rm -f *.pyc

