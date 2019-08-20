COMPILER = g++
DELETER = -rm -f
FORMATTER = astyle -t --style=stroustrup

default:
	@echo 'Targets:'
	@echo ' run'
	@echo ' client-cpp  (application)'
	@echo ' format'
	@echo ' clean'

run: client-cpp
	@./client-cpp

client-cpp: client-cpp.o doe.o
	$(COMPILER) -o client-cpp client-cpp.o doe.o

client-cpp.o: client-cpp.cpp doe.h
	$(COMPILER) -c client-cpp.cpp

doe.o: doe.cpp doe.h
	$(COMPILER) -c doe.cpp

format:
	$(FORMATTER) client-cpp.cpp
	$(FORMATTER) doe.cpp
	$(FORMATTER) doe.h

clean:
	$(DELETER) *.o
	$(DELETER) *.orig
	$(DELETER) client-cpp
