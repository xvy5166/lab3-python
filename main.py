# Author: Yanling Wang yuw17@psu.edu
# Collaborator: Aravind Hariprased azh5899@psu.edu
# Collaborator:Krish Choudhary ksc5496@psu.edu
# Collaborator: Peter Schulman pks5481@psu.edu
# Section: 4
# Breakout: 6


def sum_n(n):
  count = 0
  if n<= 1:
    return 1
  else :
    return n+sum_n(n-1)

def print_n(s,n):
  if n>0:
    print(s)
    print_n(s,n-1)
  

    

def run():
  number = sum_n(int(input("Enter an int: ")))
  print(f"sum is {number}")
  string = input("Enter a string: ")
  print_n(string, number)


if __name__ == "__main__":
  run()
  

