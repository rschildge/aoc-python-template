def part1(data):
  __import__('time').sleep(1)
  # Data is automatically read from 08.txt
  data = data.split("\n")
  values = [""]*len(data) 
  accu = 0
  index = 0
  while values[index] == '':
    values[index] = accu
    #print(data[index][0:5])
    if data[index][0:5] == "acc +":
      accu += int(data[index][5:])
    elif data[index][0:5] == "acc -":
      accu -= int(data[index][5:])
    elif data[index][0:5] == "jmp +":
      index += int(data[index][5:])
      continue
    elif data[index][0:5] == "jmp -":
      index -= int(data[index][5:])
      continue
    index += 1
  return accu
    

def testFix(data):
  values = [""]*len(data) 
  accu = 0
  index = 0
  while values[index] == '':
    values[index] = accu
    #print(data[index][0:5])
    if data[index][0:5] == "acc +":
      accu += int(data[index][5:])
      index += 1
    elif data[index][0:5] == "acc -":
      accu -= int(data[index][5:])
      index += 1
    elif data[index][0:3] == "nop":
      index += 1
    elif data[index][0:5] == "jmp +":
      index += int(data[index][5:])
    elif data[index][0:5] == "jmp -":
      index -= int(data[index][5:])
    if (index == len(data)):
      return accu
  return -1

def removeNextJmp(data,start):
  while data[start][0:3]!="jmp":
    start+=1
  data[start]="nop" + data[start][3:]
  return data

def part2(dataInitial):
  __import__('time').sleep(1)
  # Data is automatically read from 08.txt
  data = dataInitial.split("\n")
  values = [""]*len(data) 
  accu = 0
  index = 0
  #print(len(data))
  while testFix(data) == -1:
    index+=1
    data = dataInitial.split("\n")
    data = removeNextJmp(data,index)
  return testFix(data)

  # while index < len(values):
  #   values[index] = accu
  #   #print(data[index][0:5])
  #   if data[index][0:5] == "acc +":
  #     accu += int(data[index][5:])
  #     index += 1
  #   elif data[index][0:5] == "acc -":
  #     accu -= int(data[index][5:])
  #     index += 1
  #   elif data[index][0:3] == "nop":
  #     index += 1
  #   elif data[index][0:5] == "jmp +":
  #     if values[index + int(data[index][5:])] == "":
  #       index+=int(data[index][5:])
  #     else:
  #       print(str(index) + " " + data[index] + " " + str(values[index + int(data[index][5:])]))
  #       index += 1
  #   elif data[index][0:5] == "jmp -":
  #     if values[index - int(data[index][5:])] == "":
  #       index-=int(data[index][5:])
  #     else:
  #       print(str(index) + " " + data[index]+ " " + str(values[index + int(data[index][5:])]))
  #       index += 1
  # return accu
