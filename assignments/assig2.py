'''sum = 0
list = [12,24,12,24]
for element in range(0,len(list)):
    sum = sum+list[element]
print("Sum of all elements in given list: ",sum)'''


'''list = [12,24,12,24]
def count(sum):
    soup = 0
    for i in sum:
        soup+=i
    return soup

print(count(list))'''

'''list = [12,24,12,24]
i= 0
result = 0
while i <len(list):
    result = result+list[i]
    i+=1
print(result) '''

'''class List:
    def __init__(self,list):
        self.list = list
    def count(self):
            soup = 0
            for i in self.list:
                soup += i
            print(soup)
add = List([12,12,12,12])
add.count()'''                      # sum of elements in a list
'''-------------------------------------------------------------------------------------------------------------------'''
'''mult= 1
list = [2,3,4]
for element in range(0,len(list)):
    mult = mult*list[element]
print("product of all elements in given list: ",mult)'''

'''list = [2,3,4,5]
def product(mult):
    soup = 1
    for i in mult:
        soup*=i
    return soup
print(product(list))'''

'''import numpy
list1 = [1, 2, 3]
list2 = [3, 2, 4]
result1 = numpy.prod(list1)
result2 = numpy.prod(list2)
print('list1 result :',result1)
print('result of list2 :',result2)'''

'''class Product:
    def __init__(self, list):
        self.list = list
    def multiply(self):
        i = 0
        result = 1
        while i < len(self.list):
            result = result * self.list[i]
            i += 1
        print(result)
final = Product([2,2,3])
final.multiply()'''         # product of elements in list
'''--------------------------------------------------------------------------------------------------------------'''

'''list = [2,10,3,5]
list.sort()
print("Largest element is:", list[-1])'''

'''class Max:
    def __init__(self,list):
        self.list = list
    def maximum(self):
        print("Largest element is:", max(self.list))

find = Max([10, 20, 4, 45, 99])
find.maximum()'''

'''list = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
    element = int(input("Enter elements: "))
    list.append(element)
print("Largest element is:", max(list))'''

'''x = 0
list =[1,2,3,4]
lar = list[x]
while x<len(list):
    if list[x]>lar:
        lar = list[x]
    x = x+1
print("Largest number of the list by using while loop:",lar)'''

'''--------------------------------------------------------------------------------------------------------------'''


'''list1 = [2,5,4,1]
list1.sort()
print("Smallest element is:",list1[:1])'''

'''class Min:
    def __init__(self,list):
        self.list = list
    def minimum(self):
        print("smallest element is:", min(self.list))

find = Min([10, 20, 4, 45, 99])
find.minimum()'''

'''list = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list.append(ele)
print("Smallest element is:", min(list))'''

'''x = 0
list =[2,3,4]
small = list[x]
while x<len(list):
    if list[x]<small:
        small = list[x]
    x = x+1
print("small number of the list by using while loop:",small)''' #smallest number fro the list
'''------------------------------------------------------------------------------------------------------------'''
'''list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(list))
res = []
for i in list:
    if i not in res:
        res.append(i)
print("The list after removing duplicates : " + str(res))'''

'''test_list = [1,2,3,4,4,3,2,1]
print ("The original list is : " +  str(test_list))
test_list = list(set(test_list))
print ("The list after removing duplicates : " + str(test_list))'''

'''def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate = [2,4,6,4,2,1,6,7,8]
print(Remove(duplicate))'''

'''class Duplicate:
    def __init__(self):
        print('the elements after removing duplication from the list')
    def Remove(self,duplicate):
        final_list = []
        for num in duplicate:
            if num not in final_list:
                final_list.append(num)
        print('the final list :',final_list)

double =  Duplicate()
double.Remove([1,2,4,2,4,6,7,9])      #removing duplicates from the list'''
