#! usr/bin/env python
"""
    1.4 Write method which to decide if two strings are anagram or not.
    The method takes to input strings
    
    written by stambla
"""
import time

def speed_test(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        #for x in xrange(5000):
        results = func(*args, **kwargs)
        t2 = time.time()
        print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
        return results
    return wrapper

str_1 = input("Please input first word:")
str_2 = input("Please input second word:")

@speed_test
def check_anagram(str_1, str_2):
    temp =  str_1[::-1]
    if temp == str_2:
	print "%s is angaram of  %s" % (str_1, str_2)
    else:
	print "Hard luck!!! %s is not angaram of  %s" % (str_1, str_2)

check_anagram(str_1, str_2)
