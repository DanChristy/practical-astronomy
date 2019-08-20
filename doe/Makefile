COMPILER = g++
DELETER = -rm -f
FORMATTER = astyle -t --style=stroustrup

default:
	@echo 'Targets:'
	@echo ' runpy       Run client-py script.'
	@echo ' run         Run client-cpp application.'
	@echo ' all         Build all.'
	@echo ' build       Build client-cpp application.'
	@echo ' shared      Create shared library - cpp.'
	@echo ' format      Beautify C++ code.'
	@echo ' clean       Remove binaries, object files, and other temporary files.'

runpy: doeshared.so
	@./client-py.py

run: build
	@./client-cpp

all: build shared

build: client-cpp

client-cpp: client-cpp.o doe.o
	$(COMPILER) -o client-cpp client-cpp.o doe.o

client-cpp.o: client-cpp.cpp doe.h
	$(COMPILER) -c client-cpp.cpp

doe.o: doe.cpp doe.h
	$(COMPILER) -fpermissive -c doe.cpp

shared: doeshared.so

doeshared.so: doe.cpp
	$(COMPILER) -fpermissive -std=c++11 -Wall -fPIC -c doe.cpp
	$(COMPILER) -std=c++11 -shared -Wl,-soname,doeshared.so.1 -o doeshared.so doe.o

format:
	$(FORMATTER) client-cpp.cpp
	$(FORMATTER) doe.cpp
	$(FORMATTER) doe.h

clean:
	$(DELETER) *.o *.so
	$(DELETER) *.orig
	$(DELETER) client-cpp
