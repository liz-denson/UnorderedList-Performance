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
  # Part I: Creation
  
  # Part II: Deletion
  
  
if __name__ == "__main__":
    main()

#########
# SOURCES
#########