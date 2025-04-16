# comment for Session 5

print("Hello World!")

sName = "Anna"
s_Name = "John"
iAge = 22
fPi = 3.14
print("Hello",{sName})
print(f"Hello,{s_Name}")
print(f"Hello, {s_Name}")
print("Hello, {s_Name}")
print(f"{sName}, who is age {iAge} like to solve math problem about {fPi} with {s_Name}")
print(sName, s_Name,iAge,fPi)
print(type(sName), type(s_Name),type(iAge),type(fPi))

print(50*"-") #separator for the output
# index 0,1,2,3,4

iIndex = 0
print("Index currently is equal to",iIndex, type(iIndex))
iIndex +=1
print("Index currently is equal to",iIndex, type(iIndex))
iIndex = iIndex +1
print("Index currently is equal to",iIndex, type(iIndex))
iIndex += 1.2
print("Index currently is equal to",iIndex, type(iIndex))
iIndex += 1
print("Index currently is equal to",iIndex, type(iIndex))
iIndex -= 1.2
print("Index currently is equal to",iIndex, type(iIndex))

print(50*"-")
# apples 50 items per $1.59
# oranges 20 items per $2.45
# calculate the total price for the purchase and print it out

fApplePrice = 1.59
fOrangePrice = 2.45
iApplePoundQuantity = 50
iOrangePoundQuantity = 20
fTotalPrice = fApplePrice * iApplePoundQuantity + fOrangePrice *iOrangePoundQuantity
print(fTotalPrice)
print(f"The total price is {fTotalPrice}")
print(sName + " paid " + str(fTotalPrice) + " for the whole purchase")
