pi = input()
chars = set('0123456789')
if Pi == "LG" or Pi == "XL":
  Toppings = input()
  if all((c in chars) for c in Toppings):
    if Toppings > 0:
      Price = (Toppings-1)*0.75 + 1
    else:
      Price = 0
    if Pi == "LG":
      Price = Price + 6
  elif Pi == "XL":
    Price = Price + 10
  Price = Price*1.13
  print("The total is: $" + str(Price))
  else:
    print("Invalid Toppings")
else:
  print("Invalid Size")