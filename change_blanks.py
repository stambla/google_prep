#! usr/bin/env python
"""
    1.5 Write method to replace all spaces in a string with '%20'.
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
def check_anagram(str_1):
    return str_1.replace(" ", "%20")

print (check_anagram(str_1))
