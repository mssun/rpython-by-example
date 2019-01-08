from rpython.rlib import rsha

def rsha_example():
    print "digest_size:", rsha.digest_size
    print "blocksize:", rsha.blocksize

    d1 = rsha.RSHA()    # or rsha.new()
    d1.update("123")

    # Terminate and return digest in HEX form.
    print d1.hexdigest()

    # Terminate the message-digest computation and return digest.
    print d1.digest()

    d2 = rsha.RSHA("123")    # or rsha.new("123")

    #  Return a copy ('clone') of the md5 object. This can be used to
    #  efficiently compute the digests of strings that rshared a common initial
    #  substring.
    d3 = d2.copy()

    print d3.hexdigest()
    print d3.digest()

def entry_point(argv): rsha_example(); return 0
def target(*args): return entry_point

