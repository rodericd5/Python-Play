#bool flag used for prompting
flag = True

#while loop prompts and offers exception handling
while flag:
  try:
    choice = int(input("Enter a height of the pyramid:"))
    if not (0 <= choice <= 23):
      raise ValueError()
    else:
      flag = False

  except ValueError:
    print("That is not an integer between 0 and 23.")

#count is used for space and hash printing
count = choice

#for loop for entire mario pyramid
for i in range(choice):

  #left side of pyramid
  for j in range(count - 1):
    print(" ", end = "")
  for k in range(count - 2, choice):
    print("#", end = "")

  #two space divider
  print("  ", end = "")

  #right side of pyramid
  for j in range(count - 2, choice):
    print("#", end = "")
  for k in range(count - 1):
    print(" ", end = "")

  #decrement count and print a newline
  count -= 1
  print()

