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

def isCommon(l1, l2):
    '''for i in range(len(l1)):
        for j in range(len(l2)):
            if i==j:
                return True
    return False'''
    hashmap= {}
    flag= False
    for i in range(len(l1)):
        hashmap[l1[i]]= i
    for i in l2:
        if i in hashmap:
            flag= True
    return flag

l1= [1, 2, 3]
l2= [4, 5, 6, 4]
print(isCommon(l1, l2))
