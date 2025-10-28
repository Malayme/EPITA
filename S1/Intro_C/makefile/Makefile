CC=gcc
CFLAGS=-std=c99 -Wall -Wextra -Wvla -Werror -pedantic

exec: hello_world
	./hello_world

hello_world: hello_world.c
	$(CC) $(CFLAGS) -o hello_world hello_world.c

