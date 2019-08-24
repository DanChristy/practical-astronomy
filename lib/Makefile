COMPILER = g++
OBJ_ARGS = -fpermissive -std=c++11 -Wall -fPIC -c
BINARY_ARGS = -std=c++11 -shared -Wl,-soname,practicalastro.so.1 -o
DELETER = -rm -f
SRC_DOE = ../modules/doe/doe.cpp
SRC_JULIAN = ../modules/julian/julian.cpp

default:
	@echo 'Targets:'
	@echo ' build       Build shared library'
	@echo ' clean       Remove binaries, object files, and other temporary files.'

build: julian.o doe.o
	$(COMPILER) $(BINARY_ARGS) practicalastro.so julian.o doe.o

doe.o: $(SRC_DOE)
	$(COMPILER) $(OBJ_ARGS) $(SRC_DOE)

julian.o: $(SRC_JULIAN)
	$(COMPILER) $(OBJ_ARGS) $(SRC_JULIAN)

clean:
	$(DELETER) *.o *.so
	$(DELETER) *.orig
