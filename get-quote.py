import os
import random

def main():
  f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "quotes.txt"), encoding="utf-8")
  quotes = f.read().splitlines()
  f.close()

  print(random.choice(quotes))

if __name__== "__main__":
  main()
