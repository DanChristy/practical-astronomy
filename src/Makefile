COMPILER = g++
OBJ_ARGS = -fpermissive -std=c++11 -Wall -fPIC -c
BINARY_ARGS = -std=c++11 -shared -Wl,-soname,practicalastro.so.1 -o
OBJ_FILES = convert.o doe.o julian.o
FORMATTER = astyle -t --style=stroustrup
DELETER = -rm -f

default:
	@echo 'Targets:'
	@echo ' build       Build shared library'
	@echo ' format      Beautify C++ code.'
	@echo ' clean       Remove binaries, object files, and other temporary files.'

build: $(OBJ_FILES)
	$(COMPILER) $(BINARY_ARGS) practicalastro.so $(OBJ_FILES)

convert.o: convert.cpp include/convert.h
	$(COMPILER) $(OBJ_ARGS) convert.cpp

doe.o: doe.cpp include/doe.h
	$(COMPILER) $(OBJ_ARGS) doe.cpp

julian.o: julian.cpp include/julian.h
	$(COMPILER) $(OBJ_ARGS) julian.cpp

format:
	$(FORMATTER) include/shared.h
	$(FORMATTER) convert.cpp
	$(FORMATTER) include/convert.h
	$(FORMATTER) doe.cpp
	$(FORMATTER) include/doe.h
	$(FORMATTER) julian.cpp
	$(FORMATTER) include/julian.h
	
clean:
	$(DELETER) *.o *.so
	$(DELETER) *.orig
	$(DELETER) include/*.orig
