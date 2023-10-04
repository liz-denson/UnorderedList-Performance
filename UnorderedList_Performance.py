######################################
# UnorderedList Performance
# Liz Denson & Connor Loudermilk
# 2023-10-06
######################################

"""Import Libraries"""
from CSC201UT import UnorderedList
import random
import time
import timeit

###########
# FUNCTIONS
###########

"""Create UnorderedList"""
def create_ul():
  ul = UnorderedList() # Initialize UnorderedList object
  for _ in range(25000): # Loop 25,000 times
    ul.append(random.randint(0, 999)) # Append a random number between 0 and 999
  return ul # Return UnorderedList

"""Create Python List"""
def create_pl():
  pl = [] # Initialize empty Python List
  for _ in range(25000): # Loop 25,000 times
      pl.append(random.randint(0, 999)) # Append a random number between 0 and 999
  return pl # Return Python List

"""Delete UnorderedList"""
def delete_ul(ul): # Delete all the items in UnorderedList
  while not ul.is_empty(): # Loop until UnorderedList is empty
    ul.pop() # Remove last item from UnorderedList

"""Delete Python List"""
def delete_pl(pl): # Delete all the items in Python List
  while pl: # Loop until Python List is empty
    pl.pop() # Remove last item from Python List

######
# MAIN
######

def main():
    """Create Timing"""
    # Time how long it takes to create an UnorderedList of 25,000 values 100 times
    ul_create_time = timeit.timeit("create_ul()", "from __main__ import create_ul", number=100)
    # Time how long it takes to create a Python List of 25,000 values 100 times
    pl_create_time = timeit.timeit("create_pl()", "from __main__ import create_pl", number=100)
  
    # Print the time it took creating both lists
    print(f"Creating:")
    print(f"UnorderedList: {ul_create_time:.3f}s")
    print(f"Python List: {pl_create_time:.3f}s")

    """Delete Timing"""
    ul = create_ul() # Create UnorderedList for deletion timing
    pl = create_pl() # Create Python List for deletion timing
  
    # Time how long it takes to delete UnorderedList
    start_time = time.time() # Begin timer for start time
    delete_ul(ul) # Call delete_ul function
    ul_delete_time = time.time() - start_time # Calculate deletion time
  
    # Time how long it takes to delete Python List
    start_time = time.time() # Begin timer for start time
    delete_pl(pl) # Call delete_pl function
    pl_delete_time = time.time() - start_time # Calculate deletion time

    # Print the time it took deleting every value from both lists
    print(f"\nDeleting:")
    print(f"UnorderedList: {ul_delete_time:.3f}s")
    print(f"Python List: {pl_delete_time:.3f}s")

if __name__ == "__main__":
    main()
