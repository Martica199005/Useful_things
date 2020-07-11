
import os
import pathlib
import sys
import math


from os import listdir
from os.path import isfile, join


def bool_search(path):
  list=[]
  with open(path,'r') as f:
    tag = input("Enter attribute to search\n ")
    list.append(tag)
    if tag in f.read():
      founded=True
    else:
      founded=False
      print('Not present')
    list.append(founded)
  return list


#Search for a tag/attribute
def search_attribute(path,result):
  if result[1]==True:
    with open(path,'r') as f:
      tag=result[0]
      #tag = input("Enter attribute to search\n ")
      for line in f:
        if tag in line:
          b="{} is in {}".format(tag,line)
          print(b)
          return b


def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles 

def print_list(list):
  if list:
    listOfFiles=list
    for elem in listOfFiles:
      if not ".git" in elem:
        count=elem.count('/')
        if count>1:
          space=count*"\t"
          identation=space+str(elem)
          print(identation)
        if elem.endswith(".txt") or elem.endswith(".xaml"):
          print("")
          result=bool_search(elem)
          b=search_attribute(elem,result)
        print ("*"*len(str(elem)))
        return b 




def greetings():
  name=input('Say your name: ')
  hi='Hello '+name+"!"
  return hi



##filename = input ("filename: ");
#with open (filename, "w") as f:
#  b=greetings()
#  f.write (b);


#Gives current directory
basepath=os.getcwd()
print("Path: "+basepath)


dirName =basepath
# Get the list of all files in directory tree at given path
listOfFiles = getListOfFiles(dirName)

# Get the list of all files in directory tree at given path
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(dirName):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    
#Number of relevant elements in listOfFiles
count=0
for elem in listOfFiles:
    if not ".git" in elem:
      count=count+1
print("Number of elements: "+str(count)) 


##filename = input ("filename: ");
#with open (filename, "w") as f:
#  b=greetings()
#  f.write (b);