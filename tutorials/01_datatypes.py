# Datatypes
myint = 100
print("Integer     : {}, {}".format(myint, type(myint)))


myfloat = 99.999
print("Float point : {}, {}".format(myfloat, type(myfloat)))


mystring = 'Hello World'
print("String      : {}, {}".format(mystring, type(mystring)))


mylist = [0,1,2,3,4,5,6,7,8,9, 'Hello', 99.9999, [1,2,3], {1:'One',2:'Two'}, (1,2,3), {1,2,3},True]
print("List        : {}, {}".format(mylist, type(mylist)))


mydict = {'one':1, 2:'two', 3:[1,2], (1,2):(1,2), 5:{1,2}, 6:{'one':1}, True:'Hello', False:"Wang Bo"}
print("Dictionary  : {}, {}".format(mydict, type(mydict)))


mytuple = (1, 2.121, 'Hello', mylist, mydict, {1,2,3}, True, (1,2,3))
print('Tuple       : {}, {}'.format(mytuple, type(mytuple)))

myset = {1, 2.11, 'Hello', True, (1,2,3)}
print('Set         : {}, {}'.format(myset, type(myset)))

isTrue = True
print('Boolean     : {}/{}, {}'.format(isTrue,not isTrue, type(isTrue)))

####################################################################
# TypeError: unhashable type: 'list'
# TypeError:unhashable type: 'set'
# TypeError: unhashable type: 'dict'
#
# List, Set and Dictionary are unhashable, so can not bein the key of dictionary or in the value of set.
# Set need the elements are hashable.
# Dictionary need the key are hashable.
#