src = $(wildcard *.py)
obj = $(src:.py=)

RPYFLAGS = -O0

all: $(obj)

%: %.py
	$(RPY) $(RPYFLAGS) $^

clean:
	@rm *-c
