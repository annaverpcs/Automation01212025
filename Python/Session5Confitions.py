#if-else statements. Conditions. Nested Conditions
iNumber = -110
if iNumber >0:
    print("it is positive number")
else:
    print("it is negative number")

is_positive = iNumber >0

if is_positive:
    print("it is positive number")
else:
    print("it is negative number")

if False:
    print("it is positive number")
else:
    print("it is negative number")

print(50*"-")
# verify that the number is in the range 0 to 100

is_less_than_100 = iNumber < 100

if is_positive and is_less_than_100:
    print("the number is in the range 0 to 100")
else:
    print("the number is not in the range 0 to 100")

print(50*"-")
if is_positive or is_less_than_100:
    print("the number match with all conditions or at least one condition")
else:
    print("the number is either negative or more than 100")

 # AND : each of the statements should be TRUE
 # OR : at least one of the statements should be TRUE

print(50 * "-")
#test results: A = 100%, B - 90-99%, C -80-89%, D 70-79%, F is the rest
print("Test results are based on this rules: A = 100%, B - 90-99%, C -80-89%, D 70-79%, F is the rest ")
iScore = int(input("Please enter your test score "))
print(f"Your score is {iScore}")
if iScore == 100:  # a==b  , a!=b
    print("Your grade is A")
elif iScore >=90 and iScore <=99:
    print("Your grade is B")
elif iScore >=80 and iScore <=89:
    print("Your grade is C")
elif iScore >=70 and iScore <=79:
    print("Your grade is D")
else:
    print("Your grade is F")

print(50 * "-")
# User enter the sentence. Need to print out that sentence is long if sentence more than 100 char.
#it is short if it is from 5 to 99 char
# it is too short if it is less then 5 char
sSentence = input("Please enter your sentence: ")
iLength_of_sSentence = len(sSentence)
print(f"the length of the sentence is {iLength_of_sSentence}")
if iLength_of_sSentence >= 100:
    print("the sentence is long")
elif iLength_of_sSentence > 5 and iLength_of_sSentence < 100:
    print("the sentence is short")
else:
    print("the sentence is too short")





