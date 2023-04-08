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

# W3Resources 21st for tomorrow

# learn this..
    # Write a Python program to generate all permutations of a list in Python.
    # learn List Comprehensions 
    # Lambda functions

###################################################
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