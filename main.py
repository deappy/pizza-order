print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

if size=='S':
  result=15
  if ((add_pepperoni == 'N')):
    result=15
  elif add_pepperoni == 'Y':
    result=result+2

  if extra_cheese == 'Y':
    result=result+1
  elif extra_cheese == 'N':
    result=result+0

if size=='M':
  result=20
  if ((add_pepperoni == 'N')):
    result=20
  elif add_pepperoni == 'Y':
    result=result+3
  if extra_cheese == 'Y':
    result=result+1
  elif extra_cheese == 'N':
    result=result+0

if size=='L':
  result=25
  if ((add_pepperoni == 'N')):
    result=25
  elif add_pepperoni == 'Y':
    result=result+3
  if extra_cheese == 'Y':
    result=result+1
  elif extra_cheese == 'N':
    result=result+0

print(f"Your final bill is: ${result}.")