# functions

# map
def square(num):
    return num ** 2

mylist = [1,2,3,4,5,6,7,8,9]
mylist2 = map(square,mylist)
print(type(mylist2))
for num in mylist2:
    print(num)
