build: # Change this block if you have more files or another file .cpp
	g++ main.cpp -o main

start: # Change this block if you have more files or another file .cpp
	clear && ./main

clear-builds: # Change this block if you have more files or another file .cpp
	rm main

buildAndStart: # Change this block if you have more files or another file .cpp
	g++ main.cpp -o main ; clear && ./main
