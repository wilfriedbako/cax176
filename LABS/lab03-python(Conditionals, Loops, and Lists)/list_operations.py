numbers = [64, 25, 12, 22, 11]

print("Original list:", numbers)
print("Sorted list:", sorted(numbers))
print("Original list after sorted():", numbers)  # show that sorted did not modify the original list 

numbers.sort()                  # put in order permanently 

print("List after .sort():", numbers)

numbers.append(100)   # add the number 100 in the current list called numbers

print("After append:", numbers)   

numbers.insert(2,"learning")        # add item at a specif place, not at the end like 
print("add in middle :", numbers)

numbers.remove(22)

print("After removing 22:", numbers)

numbers.reverse()      # make it backwards

print("Reversed list:", numbers)