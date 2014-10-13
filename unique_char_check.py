#! usr/bin/env python
"""
    1.1 Implement the algorithm to determine if a string has all unique characters.
    What if you can't use additional data structure?
    The method takes one input strings
    
    written by stambla
"""
import time

def speed_test(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        results = func(*args, **kwargs)
        t2 = time.time()
        print '\n[+]%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
        return results
    return wrapper

str_1 = input("Please input string:")

@speed_test
def check_unique_char(str_1):
    len_str = len(str_1)
    len_unique = len(set("".join(sorted(str_1))))
    if len_str == len_unique:
	print "[+]%s has got unique characters" % str_1
    else:
	print "[+]%s has not got unique characters" % str_1

print (check_unique_char(str_1))
