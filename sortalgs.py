#binary search algorithm

def binary_search(item_list, item):
  first = 0 # for the first item
  last = len(item_list)-1 #for the last item. has -1 bc the  list starts w 0 
  found = False #variable to be manipulated. so far nothing has been found so until the  list has been searched, it will continue to say false
  while (first <= last and not found): #while loop to begin the binary search
    mid = (first + last) //2 #variable for the middle number
    if item_list[mid] == item : #if the index of the item we land on is equal to the item we are searching....
      found = True #found would be changed to true
    else: #else if the index of the item landed on is not equal to desried item...
      if item < item_list[mid] : #if the desired item is before the mid point of the list...
        last = mid - 1 #the variable for the last number is changed to the number right before the mid point
      else: #if the desired item is after the mid point
        first = mid + 1 #new first number is the number right after the mid point
  return found #return whether the number was found or not

print(binary_search([1, 2, 3, 5, 8], 6))
print(binary_search([1, 2, 3, 5, 8], 5))

#selection sort

def selectionsort(list):
  n = len(list) #get the length of the list
  for i in range(n): #for loop to go through all of the elements through n
    minelement = i #set the minimum element to the first element
    print("pass " + str(i)) #print pass number
    for j in range(i+1, n): #for loop to iterate through the elements from i+1 to n
      if list[minelement] > list[j]: #checking for the minimum number
        minelement = j #set the new minimum number
      list[i], list[minelement] = list[minelement], list[i] #swap values for the minimum number
      slicedlist = list[:] 
      print(slicedlist)
      print()
  return list #return the sorted list
randlist = [64, 25, 3, 22, 11]
selectionsort(randlist)
print(randlist)
# better algorithm than bubblesort because we are decreasing the iterations 
# and you swap less. also saving more run time and space because 

# main answer: not making multiple comparisons with selection sort and only swapping once

#bubble sort
def bubblesort(list):
  n = len(list)
  for i in range(n):
    print("pass " + str(i))
    for j in range(0, n-i-1):
      if list[j] > list[j+1]:
        list[j], list[j+1] = list[j+1], list[j]
        slicedlist = list[:]
        print(slicedlist)

        
mylist = [9, 24, 8, 10, 293, 5, 1]

bubblesort(mylist)
print(mylist)
