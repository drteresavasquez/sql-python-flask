while True:
  try:
    X = int(input('Enter a number: '))
    break
  except ValueError:
    print("That's not a valid number")
  finally:
    print("Attempt input")

  
