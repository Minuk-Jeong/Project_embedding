# Optional: verify stub compiles (no Python, no OAI link)
CFLAGS ?= -Wall -Wextra -std=c11 -c

.PHONY: all clean

all: oai_sionna_bridge_stub.o

oai_sionna_bridge_stub.o: oai_sionna_bridge_stub.c oai_sionna_bridge.h
	$(CC) $(CFLAGS) -o $@ oai_sionna_bridge_stub.c

clean:
	rm -f oai_sionna_bridge_stub.o
