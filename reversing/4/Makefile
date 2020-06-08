all: main

main: main.c
	gcc -o 4pre main.c -static
	upx -o 4 ./4pre
	rm 4pre

clean:
	rm 4 4pre
