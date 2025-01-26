try:
   num =int(input("Enter a number"))
   print(num)
except ValueError as ex:
  print("exeption:",ex)
print("i am a outside try block")
