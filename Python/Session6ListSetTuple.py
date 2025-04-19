#list

numbers = [1,5,9,55,789,4355]
prices = [2.5,5,7.8,6.23]
quantitys = [1,5,9,5,3]
fruits = ['apple','banana','orange','green apple','green banana','bloody orange']
print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[::-1]) #revert the list
print(50*"-")
print(fruits)
print(prices)
print(f"there are {len(fruits)} fruits in fruit list")
fruits.remove(fruits[len(fruits)-2])
print(fruits)
fruits.append("strawberry")
print(fruits)
print(50*"-")
# need to calculate the total price for the purchase
total_price = 0
for fruit, price in zip(fruits, prices):
    total_price += price
    print(f"{fruit} : {price} and is added to basket total_price: {total_price}")
print(f"Total price: {total_price}")
print(50*"-")
# need to calculate the total price for the purchase
# prices = [2.5,5,7.8,6.23]
# quantitys = [1,5,9,5,3]
# fruits = ['apple','banana','orange','green apple','green banana','bloody orange']
total_price = 0
for fruit, price, quanity in zip(fruits, prices, quantitys):
    total_price = total_price + price * quanity
    print(f"{fruit} : {quanity}*{price} and is added to basket total_price: {total_price}")
print(f"Total price: {total_price}")

print(50*"-")
mixedLists = ["apple",12,"strawberry", 4.5, True, False, "banana"]
print(mixedLists)

