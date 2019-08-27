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

runpy: julianshared.so
	@./client-py.py

run: build
	@./client-cpp

all: build shared

build: client-cpp

client-cpp: client-cpp.o julian.o
	$(COMPILER) -o client-cpp client-cpp.o julian.o

client-cpp.o: client-cpp.cpp julian.h
	$(COMPILER) -c client-cpp.cpp

julian.o: julian.cpp julian.h
	$(COMPILER) -fpermissive -c julian.cpp

shared: julianshared.so

julianshared.so: julian.cpp
	$(COMPILER) -fpermissive -std=c++11 -Wall -fPIC -c julian.cpp
	$(COMPILER) -std=c++11 -shared -Wl,-soname,julianshared.so.1 -o julianshared.so julian.o

format:
	$(FORMATTER) client-cpp.cpp
	$(FORMATTER) julian.cpp
	$(FORMATTER) julian.h

clean:
	$(DELETER) *.o *.so
	$(DELETER) *.orig
	$(DELETER) client-cpp
