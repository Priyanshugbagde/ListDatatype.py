#Task - to check the pop()and remove() operations/functions
l = [10,20,30,40,50]

print(l.pop(2))           # Removes element at index 2 → 30
# print(l.remove(2))      # Error: 2 is not a value in list

l = [10,20,30,40, 50]
l.remove(40)              # Removes value 40
print(l)

# l.remove(1, 20)          # Error: remove() takes 1 argument
# l.pop(1, 20)             # Error: pop() takes at most 1 argument

l = [10,20,30,40]  
print(l.pop())            # Removes last element → 30

# l.remove()              # Error: missing argument for value

l = [10,20,30,40,50]
# print(l.pop(10))        # Error: index 10 out of range

l = [10,20,30]
# l.remove(100)           # Error: 100 not in list
