import sys

def main():
# nothing happens yet, but someday there will be code

if __name__ == '__main__':
  exitcode = 0
  try:
    exitcode = main()
  except:
    sys.stderr.write('An exception occurred while running your program.\n')
    exitcode = 1
  sys.exit(exitcode)