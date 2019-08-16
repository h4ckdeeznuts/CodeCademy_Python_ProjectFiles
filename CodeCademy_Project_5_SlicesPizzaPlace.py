toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)
print("We sell "+str(num_pizzas)+" different kinds of pizza!")
pizzas = list(zip(prices, toppings))
pizzas.sort()
print(list(pizzas))
cheapest_pizza = pizzas[1]
print("Our cheapest pizza is "+str(cheapest_pizza))
priciest_pizza = pizzas[-1]
print("Our priciest pizza is "+str(priciest_pizza))
three_cheapest = pizzas[:3]
print("3 cheapest pizzas- "+str(three_cheapest))

num_two_dollar_slices = pizzas.count('2')
print(str(num_two_dollar_slices))
