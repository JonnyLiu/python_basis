# coding:utf-8

def binarySearch(list1,destValue):
    low = 0
    high = len(list1) - 1
    mid = (low + high) / 2
    while low < high  :
        if list1[mid] == destValue:
            return mid
        elif list1[mid] > destValue:
            high = mid - 1
        else:
            low = mid + 1
        mid = (low + high) / 2
    return -mid-1
list1=[1,3,8,12,23,34,37,42,48,58]
print  list(enumerate(list1))
print  binarySearch(list1,8),8
print  binarySearch(list1,9),8