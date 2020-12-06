
from collections import Counter
def part1(data):
  __import__('time').sleep(1)
  # Data is automatically read from 06.txt
  data = data.split("\n")
  group = getNextGroup(data)
  total=0
  while group != -1:
    #find sum and add it to total
    #print("StartLoop")
    total += findSum(group)
    data = removeNextGroup(data)
    group = getNextGroup(data)
  return total

def getNextGroup(data):
  #print(len(data))
  if len(data)==0:
    return -1
  index = 0
  group = []
  #print(len(data))
  while index != len(data) and data[index]!="":
    group.append(data[index])
    index += 1
  #print("end getNextGroup")
  return group

def removeNextGroup(data):
  #print("start removeNextGroup")
  index = 0
  while index !=len(data) and data[index]!="":
    index += 1
    #print(data[index])
  #print("End RemoveNextGroup")
  return data[index+1:]


def findSum(group):
  group="".join(group)
  Counter(group).keys() # equals to list(set(words))
  #print(len(Counter(group).keys()))
  return len(Counter(group).keys()) # counts the elements' frequency

def part2(data):
  __import__('time').sleep(1)
  # Data is automatically read from 06.txt
  data = data.split("\n")
  group = getNextGroup(data)
  total=0
  while group != -1:
    #find sum and add it to total
    #print("StartLoop")
    total += findSum2(group)
    data = removeNextGroup(data)
    group = getNextGroup(data)
  return total

def findSum2(group):
  #group="".join(group)
  #Counter(group).keys() # equals to list(set(words))
  #print(len(Counter(group).keys()))
  a = group[0]
  for b in group:
    a = [x for x in a if x in b]
  return len(a) # counts the elements' frequency
