'''
#Finds sum of all elements from a list:
def Q1_sum_list(items):
    sum= 0
    for x in items:
        sum+= x
    return sum
print("Q1:", Q1_sum_list([1,2,3,4,5]))
'''

'''
#Bubble sort:
def Q8_sorting(arr):
    n= len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[i+j+1]< arr[i]:
                arr[i], arr[i+j+1]= arr[i+j+1], arr[i]
    return arr
print("Q8:", Q8_sorting([6,5, -2,4,3,2,1]))
'''

'''
#Removes all duplicated values from a list
def Q7_removeDuplicate(list):
    arr= [list[0]]
    for i in list[1:]:
        doAdd= True
        for j in arr:
            if i== j:
                doAdd= False
        if(doAdd==True):
            arr.append(i)
    return arr
print(Q7_removeDuplicate([1,1,1,12,3,4,12]))
'''

'''
#find list of string where individual strings length is greater than n
def Q10(list, x):
    arr=[]
    for i in list:
        if len(str(i))> x:
            arr.append(i)
    return arr
print(Q10([1,10,100,1000,10000]),3)
'''

'''
def Q11_isCommon(l1, l2):
    hashmap= {}
    for i in l1:
        hashmap[l1[i]]= false
    for i in l2:
        if i in hashmap:
            return True
    return False

l1= [1, 2, 3]
l2= [4, 5, 6, 4]
print(Q11_isCommon(l1, l2))
'''

'''
l= [7,8, 120, 25, 44, 20, 27]
print([x for x in l if x%2!= 0])
'''

'''
print([x*x for x in range(1, 31) if x< 6 or x >25])
print([x*x for x in range(1, 31) if x> 5])
'''

#Implementation of Linked List:
'''
class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Createe an empty list
        self.head = None
        self.tail = None
        self.count = 0
    def iterate_item(self):
        # Iterate the list.
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val
    def append_item(self, data):
        #Append items on the list
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1
'''
'''
#list: 31
def minmax(list, min, max):
    count= 0
    for i in list:
        if min <= i <= max:
            count+=1
    return count

print(minmax([1,23,4,4,5,6], 2, 5))
'''

'''
# list-32 
# to check whether a list contains a sublist.
def isSublist(main, check):
    lenMain= len(main)
    lenCheck= len(check)
    if lenMain< lenCheck:
        return False
    for i in range(lenMain- lenCheck+ 1):
        if main[i: i+ lenCheck] == check:
            return True
    return False
    

print(isSublist([1,2,3,4,5,6], [1,2,3]))
'''

'''
# list-34
# sieve of enstosthenes
def sieveOfEnstosthenes(n):
    prime= [True]* (n+1)
    prime[0]= prime[1]= False
    i= 2
    while i*i<= n:
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j]= False
        i+=1
    return [num for num, prime in enumerate(prime) if prime]
        
print(sieveOfEnstosthenes(80))
'''

'''
# create a list by concatenating a given list with a range from 1 to n
def findList(list, n):
    new= []
    for i in range(1,n+1):
        for j in list:
            new.append(str(j)+str(i))
    return new

def findList2(list, n):
    return ['{}{}'.format(x, y) for x in list for y in range(1 , n+1)]

print(findList2(['p','q'],5))
'''

#########################################################################################  IMP:-
'''
# Sieve of Enthosis
def sieve(max):
    prime= [True]* (max+1)
    prime[0]= prime[1]= False
    i= 2
    while i*i<=max:
        if prime[i]:
            for k in range(i*i, max+1, i):
                prime[k]= False
        i+=1
    return [num for num, value in enumerate(prime) if value]

print(sieve(8))
'''

'''
# convert list of dict to dict of list.
def list_of_dicts(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print("Original dictionary of lists:")
print(marks)
print("\nSplit said dictionary of lists into list of dictionaries:")
print(list_of_dicts(marks))
'''

'''
# get this array
# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
l = [[j for j in range((i-1)*5+1,i*5+1)] for i in range(1,5)]
'''

'''
# convert 2D array into unique sorted array.
L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),(7, 8), (9, 10)]
arr = list(j for i in L for j in i)
print(list(set(arr)))
'''

'''
# split a list every nth element. 
#    ex.,
#       l= [1, 2, 3, 4, 5, 6]
#       --> l1= [1, 3, 5]
#           l2= [2, 4, 6]
C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
def list_slice(S, step):
    return [S[i::step] for i in range(step)]
print(list_slice(C,3))
'''

'''
# find different element between two list
l= ['1', '2', '3', '4', '5', '6']
m= ['5', '6']

# convert into set and find subtract of set
l1= set(l)
m1= set(m)
print(l1-m1)

# comparing both list --> high time complexity
l2= [i for i in l if i not in m ]
print(l2)
'''

'''
# replace last element of a list with another list's elements
num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2
print(num1)
'''


#76
def find_count(x):
    x+='1'
    prev= x[0]
    count= 1
    l=[]
    for i in range(1, len(x)):
        if i== prev:
            count+=1
        else:
            l.append([count, prev])
    return l
        
#x= [1, 1, 2, 3, 4, 4, 5, 1]
x= "aabcddddadnss"
print(x)
print(find_count(x))

###################################################

### W3Resources
    # learn itertools:
        # do list-33, list-40, list-53
    # learn Dict:
        # do list-50, list-55
    # learn format method 
    # learn from operator import eq
    # Write a Python program to generate all permutations of a list in Python.
    # learn List Comprehensions 
    # zip method
    # join method
    # learn collections
        # counter:
            # do list-52
    # learn ast
        # do list-56

# learn this method:
'''
            import itertools
            n = 10
            def fibonacci_nums(x=0, y=1):
                yield x
                while True:
                    yield y
                    x, y = y, x + y
            print("First 10 Fibonacci numbers:")
            result = list(itertools.islice(fibonacci_nums(), n))
'''
###################################################