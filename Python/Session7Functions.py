#library of functions

def greeting():
    print("Hello Team")

def greeting2():
    print("What is the weather today?")

def greeting3(name):
    return f"Hello {name}!"

#use the same tuple from Session7TupleSet.py
def analyse_salaries (salaries, employee):
    print(f"Salaries  {salaries}")
    print(f"Maximum salary  {max(salaries)}")
    print(f"Minimum salary {min(salaries)}")
    name, salary = employee
    print(f"Employee {name} earns {salary}")

#use the same set from Session7TupleSet.py
def analyse_testsets(all_tests, executed_tests):
        print(f"all tests: {all_tests}")
        print(f"executed tests: {executed_tests}")
        missing_tests = all_tests - executed_tests
        print(f"Missing Tests : {missing_tests}")
        common_test = all_tests.intersection(executed_tests)
        print(f"intersection {common_test}")
        difference_tests = all_tests.difference(executed_tests)
        print(f"difference  {difference_tests}")


#calculate test results rate
# rate = passed testcases / total number of testcases *100
def calculate_test_result_rate (results):
    passed  = results.count("passed")
    return round((passed / len(results)) * 100,2)

#calculate duplicated entities in the list

def calculate_duplicates (results, word):
    passed  = results.count(word)
    return round((passed / len(results)) * 100,0)
