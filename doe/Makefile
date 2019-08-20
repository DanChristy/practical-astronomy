COMPILER = g++
DELETER = -rm -f
FORMATTER = astyle -t --style=stroustrup

default:
	@echo 'Targets:'
	@echo ' run'
	@echo ' cppclient  (application)'
	@echo ' format'
	@echo ' clean'

run: cppclient
	@./cppclient

cppclient: cppclient.o doe.o
	$(COMPILER) -o cppclient cppclient.o doe.o

cppclient.o: cppclient.cpp doe.h
	$(COMPILER) -c cppclient.cpp

doe.o: doe.cpp doe.h
	$(COMPILER) -c doe.cpp

format:
	$(FORMATTER) cppclient.cpp
	$(FORMATTER) doe.cpp
	$(FORMATTER) doe.h

clean:
	$(DELETER) *.o
	$(DELETER) *.orig
	$(DELETER) cppclient
