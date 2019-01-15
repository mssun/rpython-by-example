from rpython.rlib.rsre import rsre_re as re

def rsre_example():
    # simulate scanf, %s - %d errors, %d warnings
    print re.search(r"(\S+) - (\d+) errors, (\d+) warnings",
                    "/usr/sbin/sendmail - 0 errors, 4 warnings").groups()

    # making a phone book
    text = """Ross McFluff: 834.345.1254 155 Elm Street
Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way
Heather Albrecht: 548.326.4584 919 Park Place"""
    entries = re.split("\n+", text)
    print [re.split(":? ", entry, 4) for entry in entries]

    # finding all adverbs
    text = "He was carefully disguised but captured quickly by police."
    print re.findall(r"\w+ly", text)

def entry_point(argv): rsre_example(); return 0
def target(*args): return entry_point
