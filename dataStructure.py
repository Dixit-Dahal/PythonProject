# # list

# cart = ['apple', 'orange', 'grapes']

# # cart.append([10,20]) # can only insert at a single index number
# # cart.append('milk')

# # cart.extend('milk')     # can only pass iterable object; loop concept

# cart.insert(0, 'milk')  # can pass value to a certain index number

# cart.remove(cart[0])    # can delete values using both index and the value itself, can't be empty

# cart.pop(1)         # can delete values using index only, can be empty LIFO

# # cart.clear()        # Deletes all values

# cart[0] = 'grapes'

# print(cart)


# # Tuple

# cart = ('apple', 'orange', 'grapes')

# newCart = list(cart)

# newCart[0] = 'milk'

# cart = tuple(newCart)
# print(cart)

# # Set

# # You can't change a value that's already assigned in a set
# # You can't use indexing and slicing in a set because it is unordered

cart1 = {'apple', 'orange', 'grapes'}
cart2 = {'apple', 'orange'}

# cart1.add('milk') # Can assign single value
# # cart.update('milk') # Iterable object, can assign multiple values
# cart1.update({10,20})

# cart1.remove('apple')        # Does not avoid error if the argument doesn't exist
# cart1.discard('apple')       # Aoids errors, Safer version of removing items
# cart1.pop()                  # Removes any item that is on the first index after the set gets shuffled
# print(cart1)

# Set operations
# cart = cart1.union(cart2)
# cart = cart1.intersection(cart2)
# cart = cart1.isdisjoint(cart2)
# cart = cart1.issubset(cart2)     # Compares cart2 to cart1
# cart = cart1.issuperset(cart2)   # Compares cart1 to cart2

# cart = cart2.symmetric_difference(cart1)

# print(cart)


