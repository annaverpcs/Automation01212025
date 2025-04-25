#Tuple
# Salary of employees. Print out the whole tuple, min, max of salary
from selenium import common

salaries = (1000,2500,400,3,750,456,7899,1521,132455.4564564,454.23)
print(f"Salaries ", salaries)
print(f"Maximum salary ", max(salaries))
print(f"Minimum salary ", min(salaries))
employee_john = ('John', 123456)
name, salary = employee_john
print(f"Employee {name} earns {salary}")

#set
# there are 2 sets : all test sets , executed test sets.
# Need to find out what is left and missed and need to be executed later on.
allTests = {"regression", "boundary", "compatibility", "smoke", "sanity", "functional", "stress", "API testing"}
executedTests ={"smoke", "functional",  "API testing","stress", "UI testing"}
print( allTests )
print( executedTests )
missingTests = allTests - executedTests
print(f"Missing Tests ", missingTests )
commonTest = allTests.intersection(executedTests)
print(f"intersection ", commonTest )
differenceTests = allTests.difference(executedTests)
print(f"difference ", differenceTests )







