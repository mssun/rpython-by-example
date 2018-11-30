def entrypoint(args):
    print "Hello, World!"
    return 0

def target(*args):
    return entrypoint, None
