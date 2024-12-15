# Propmts the user for the size of pizza, then returns a cost based off the size of the pizza.
def chooseSize():
  vaildInput = False
  sizeCost = 0
  while vaildInput == False:
    size = input("Please input size of pizza: ")
    size = size.upper()
    if size == "L":
      sizeCost = 6.00 
      vaildInput = True
    elif size == "XL": 
      sizeCost = 10.00
      vaildInput = True
    else:
      print("Please input either L or XL")
      vaildInput = False
  return sizeCost

# Propmts the user for the number of toppings, then returns cost based off the number of toppings.
def chooseToppings():
  # Asks for the number of toppings and loops till we get a vaild input.
  vaildInput = False
  while vaildInput == False:
    toppings = input("Please input number of toppings: ")
    try:
      toppings = int(toppings)
    except:
      print("Please input a number from 0 to 4")
      continue
    
    if toppings < 0 or toppings > 4:
      print("Please input a number from 0 to 4")
    else:
      vaildInput = True

  # Now that we have a vaild input it determines the cost and returns it.
  toppingsCost = 0
  if toppings == 1:
    toppingsCost = 1.00
  elif toppings == 2:
    toppingsCost = 1.75
  elif toppings == 3:
    toppingsCost = 2.50
  elif toppings == 4:
    toppingsCost = 3.25
  return toppingsCost

# Takes sizeCost and toppingsCost and prints them out and also prints subtotal, tax, and total based off the sizeCost and toppingsCost
def printOrder(sizeCost, toppingsCost):
  print(f"Size cost:     ${sizeCost:5.2f}")
  print(f"Toppings cost: ${toppingsCost:5.2f}")
  subtotal = sizeCost + toppingsCost
  tax = subtotal * 0.13
  total = tax +  subtotal
  print(f"Subtotal:      ${subtotal:5.2f}")
  print(f"Tax:           ${tax:5.2f}")
  print(f"Total:         ${total:5.2f}")

# Main program starts here
sizeCost = chooseSize()
toppingsCost = chooseToppings()
printOrder(sizeCost, toppingsCost)