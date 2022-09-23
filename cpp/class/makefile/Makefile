# The main structure of a makefile is this:
# target: dependencies
#	action
# dependencies are the files which, if changed, the action is perform so that the target is generated
# In the following, when no dependency exists, then the target is a command came after `make` in terminal

output: main.o SampleClass.o
	g++ main.o SampleClass.o -o exec

main.o: main.cpp
	g++ -c main.cpp 
# -c forces the compiler to create object file (`.o` file) from the script

SampleClass.o: SampleClass.cpp SampleClass.h
	g++ -c SampleClass.cpp

clean:
	rm *.o exec

