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
def create_ul():
  ul = UnorderedList()
  for _ in range(25000):
    ul.append(random.randint(0, 999))

def create_pl():
  pl = []
  for _ in range(25000):
      pl.append(random.randint(0, 999))

def delete_ul(ul):
  while not ul.is_empty():
    ul.pop()

def delete_pl(pl):
  while pl:
    pl.pop()

######
# MAIN
######
def main():
    """Create Timing"""
    ul_create_time = timeit.timeit("create_ul()", "from __main__ import create_ul", number=100)
    pl_create_time = timeit.timeit("create_pl()", "from __main__ import create_pl", number=100)

    print(f"Creating:")
    print(f"UnorderedList: {ul_create_time:.3f}s")
    print(f"Python List: {pl_create_time:.3f}s")

    """Delete Timing"""
    ul = create_ul()
    pl = create_pl()

    start_time = time.time()
    delete_ul(ul)
    ul_delete_time = time.time() - start_time

    start_time = time.time()
    delete_pl(pl)
    pl_delete_time = time.time() - start_time

    print(f"\nDeleting:")
    print(f"UnorderedList: {ul_delete_time:.3f}s")
    print(f"Python List: {pl_delete_time:.3f}s")

if __name__ == "__main__":
    main()

#########
# SOURCES
#########
