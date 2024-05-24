"""
functions:
built in function   print()     len()       type()      range()
user defined function
"""

"""
default parameters:
aasigning a default value to parameter which is used when no argument is passed"""
def cal_prod(a = 4, b= 3):  # a= 4 and b = 3 is default parameters
    print(a *b)
    return a * b
cal_prod()
cal_prod()