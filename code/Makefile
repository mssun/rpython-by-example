src = $(filter-out $(wildcard *_unsupported.py) $(wildcard *_error.py), $(wildcard *.py))
obj = $(src:.py=)

RPYFLAGS = -O0
RPY ?= rpython

all: $(obj)

%: %.py
	$(RPY) $(RPYFLAGS) $^

clean:
	@rm -f *-c
	@rm -rf __pycache__
