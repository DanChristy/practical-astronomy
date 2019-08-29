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

runpy: convertshared.so
	@./client-py.py

run: build
	@./client-cpp

all: build shared

build: client-cpp

client-cpp: client-cpp.o convert.o
	$(COMPILER) -o client-cpp client-cpp.o convert.o

client-cpp.o: client-cpp.cpp convert.h
	$(COMPILER) -c client-cpp.cpp

convert.o: convert.cpp convert.h
	$(COMPILER) -fpermissive -c convert.cpp

shared: convertshared.so

convertshared.so: convert.cpp
	$(COMPILER) -fpermissive -std=c++11 -Wall -fPIC -c convert.cpp
	$(COMPILER) -std=c++11 -shared -Wl,-soname,convertshared.so.1 -o convertshared.so convert.o

format:
	$(FORMATTER) client-cpp.cpp
	$(FORMATTER) convert.cpp
	$(FORMATTER) convert.h

clean:
	$(DELETER) *.o *.so
	$(DELETER) *.orig
	$(DELETER) client-cpp
