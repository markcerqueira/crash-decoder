SHELL := /bin/bash

all: hex2binary plcrashutil

hex2binary: 
	g++ HexToBinary.cpp -o HexToBinary

plcrashutil:
	build-plcrashutil.bash

clean:
	rm -f HexToBinary
	rm -f plcrashutil
