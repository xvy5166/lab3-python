# Author: Yanling Wang yuw17@psu.edu
# Collaborator: Aravind Hariprased azh5899@psu.edu
# Collaborator:Krish Choudhary ksc5496@psu.edu
# Collaborator: Peter Schulman pks5481@psu.edu
# Section: 4
# Breakout: 6


def sum_n(n):
  if n == 0:
    return 0
  else :
    return n+sum_n(n-1)

def print_n(s,n):
  if n>0:
    print(s)
    print_n(s,n-1)
  

    

def run():
  i = int(input("Enter an int: "))
  number = sum_n(i)
  print(f"sum is {number}.")
  string = input("Enter a string: ")
  print_n(string, i)


if __name__ == "__main__":
  run()
  

