COMPILER = g++
OBJ_ARGS = -fPIC -fpermissive -c
SHARED_ARGS = -std=c++11 -shared -Wl,-soname,
DELETER = -rm -f
FORMATTER = astyle -t --style=stroustrup

default:
	@echo 'Targets:'
	@echo ' convert-runpy    Run convert test app (Python)'
	@echo ' convert-run      Run convert test app (C++)'
	@echo ' convert          Build convert test app and shared library (C++)'
	@echo ' doe-runpy        Run doe test app (Python)'
	@echo ' doe-run          Run doe test app (C++)'
	@echo ' doe              Build doe test app and shared library (C++)'
	@echo ' julian-runpy     Run julian test app (Python)'
	@echo ' julian-run       Run julian test app (C++)'
	@echo ' julian           Build julian test app and shared library (C++)'
	@echo ' format           Beautify C++ code.'
	@echo ' clean            Remove binaries, object files, and other temporary files.'

convert-runpy: convert
	@./convert.py

convert-run: convert
	@./convert

convert:
	$(COMPILER) $(OBJ_ARGS) ../src/convert.cpp -o convert-lib.o
	$(COMPILER) -c convert.cpp
	$(COMPILER) -o convert convert.o convert-lib.o
	$(COMPILER) $(SHARED_ARGS)convertshared.so.1 -o convertshared.so convert-lib.o

doe-runpy: doe
	@./doe.py

doe-run: doe
	@./doe

doe:
	$(COMPILER) $(OBJ_ARGS) ../src/doe.cpp -o doe-lib.o
	$(COMPILER) -c doe.cpp
	$(COMPILER) -o doe doe.o doe-lib.o
	$(COMPILER) $(SHARED_ARGS)doeshared.so.1 -o doeshared.so doe-lib.o

julian-runpy: julian
	@./julian.py

julian-run: julian
	@./julian

julian:
	$(COMPILER) $(OBJ_ARGS) ../src/julian.cpp -o julian-lib.o
	$(COMPILER) -c julian.cpp
	$(COMPILER) -o julian julian.o julian-lib.o
	$(COMPILER) $(SHARED_ARGS)julianshared.so.1 -o julianshared.so julian-lib.o

format:
	$(FORMATTER) convert.cpp
	$(FORMATTER) doe.cpp
	$(FORMATTER) julian.cpp

clean:
	$(DELETER) convert
	$(DELETER) doe
	$(DELETER) julian
	$(DELETER) *.o *.so
	$(DELETER) *.orig
