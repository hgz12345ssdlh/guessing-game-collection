CC=g++
CFLAGS=-std=c++11 -O2

all: game
	
game: main.cpp guessing_game.cpp
	${CC} ${CFLAGS} $^ -o $@

.PHONY: clean
clean:
	rm -f game
