from rpython.rlib import rpath

def rpath_example():
    # normalize a pathname by collapsing redundant separators and up-level
    # references so that A//B, A/B/, A/./B and A/foo/../B all become A/B
    print rpath.rnormpath("///..//./foo/.//bar")    # "/foo/bar"

    # return a normalized absolutized version of the pathname path
    print rpath.rabspath('foo')                            # $(pwd)/foo

    # join two pathname components, inserting '/' as needed
    print rpath.rjoin("/foo", "bar" + rpath.sep + "foo")

    # return True if path is an absolute pathname
    print rpath.risabs('C:\\foo\\bar')              # 0

    # return True if path is an existing directory
    print rpath.risdir('_some_non_existant_file_')         # 0

def entry_point(argv): rpath_example(); return 0
def target(*args): return entry_point
