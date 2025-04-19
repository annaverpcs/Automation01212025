#1+2+3+4+5+...20
summary = 0
for i in range(1, 21):
    #summary += i
    summary = summary +i
    print(f"summary for each {i} step is {summary}")
print(f"Total summary is : {summary}")

# i =20
print(50*"-")
i=1
summary = 0
while i<=20:
    summary +=i
    print(f"summary for each {i} step is {summary}")
    i+=1
print(f"Total summary is : {summary}")

#1+3+5+7+9+....21
print(50*"-")
summary = 0
for j in range(1, 20, 2):
    #summary += j
    summary = summary +j
    print(f"summary for each {j} step is {summary}")
print(f"Total summary is : {summary}")

print(50*"-")
i=1
summary = 0
while i<=20:
    summary +=i
    print(f"summary for each {i} step is {summary}")
    i+=2
print(f"Total summary is : {summary}")

# 10+8+6+4+2
print(50*"-")
i=10
summary = 0
while i>0:
    summary +=i
    print(f"summary for each additional{i} number is {summary}")
    i-=2
print(f"Total summary is : {summary}")

print(50*"-")

#nested loops: print out multiplication table
# i * j = {i*j}
#range 1-6
for i in range(1, 6):
    for j in range(1, 6):
        p = i*j
        print(f"{i} * {j} = {p}")
    print(10 * "*")
print(50*"-")

#break and continue
for i in range(1, 6):
    print(f"before the if statement {i}")
    if i==4:
        print(f"before the break {i}")
        print("exit the loop when i=4")
        break
    print(f"after the break {i}")

for i in range(1, 6):
    print(f"before the if statement {i}")
    if i==4:
        print(f"before the break {i}")
        continue
    print(f"after the break {i}")