import re

# Assorted helper functions

def printgreeting():
  print("My name is Mad Libs Max, and welcome to another edition of THUNDERDOOOOOME \n\nWhen the prompt pops up enter a word that corresponds.  For example when asked for 'adjective' you might return 'smelly' or 'purple'\n\nAt the end, you'll be treated to a crazy story of your own creation.")

def read_file(filepath):
  with open(filepath) as f:
    return f.read()

def parse_string_and_inputs(string):
  results = ''
  string_list = re.split("{|}",string)
  # String list should look like this:
  # ['text','Q','text','Q','text','Q',etc]
  for i in range (1,len(string_list),2):
    string_list[i] = input(f"{string_list[i]}:  ")
    # Asks users questions and save answers
  for string in string_list:
    results += string
  return results

def write_file(string):
  f=open("CompletedMadlib.txt","w+")
  f.write(string)

# Executable
def do_madlib(filepath):
  printgreeting()
  mad_lib_string=''
  try:
    mad_lib_string = read_file(filepath)
  except FileNotFoundError as e:
    print ('file not found')
    print (str(e))
  finished_lib = parse_string(mad_lib_string)
  write_file(finished_lib)