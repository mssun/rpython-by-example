from rpython.rlib import rmd5

def rmd5_example():
    print "digest_size:", rmd5.digest_size

    d1 = rmd5.RMD5()    # or rmd5.new()
    d1.update("123")

    # Terminate and return digest in HEX form.
    print d1.hexdigest()

    # Terminate the message-digest computation and return digest.
    print d1.digest()

    d2 = rmd5.RMD5("123")    # or rmd5.new("123")

    #  Return a copy ('clone') of the md5 object. This can be used to
    #  efficiently compute the digests of strings that shared a common initial
    #  substring.
    d3 = d2.copy()

    print d3.hexdigest()
    print d3.digest()

def entry_point(argv): rmd5_example(); return 0
def target(*args): return entry_point

