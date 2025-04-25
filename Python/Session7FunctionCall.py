#from Python.Session7Functions import greeting
from Python.Session7Functions import *
greeting()
greeting2()
print(greeting3("Anna") + greeting3("John")+ " Sometext ")

salaries = (1000,2500,400,3,750,456,7899,1521,132455.4564564,454.23)
employee_john = ('John', 123456)
analyse_salaries(salaries, employee_john)

allTests = {"regression", "boundary", "compatibility", "smoke", "sanity", "functional", "stress", "API testing"}
executedTests ={"smoke", "functional",  "API testing","stress", "UI testing"}
release_test_plan_coverage = {"boundary", "compatibility", "smoke", "sanity", "functional", "stress", "API testing"}
release_executed_test ={"smoke", "API testing","stress", "UI testing"}
analyse_testsets(allTests,executedTests)
print(50*"#")
analyse_testsets(release_test_plan_coverage, release_executed_test)
print(50*"#")
analyse_testsets(release_executed_test,allTests)

#calculate test results rate
# rate = passed testcases / total number of testcases *100
test_results =["passed","failed","passed","failed", "passed","passed","skipped","failed", "passed" ]
print(f"The test results rate is  ", calculate_test_result_rate(test_results))

allTest = ["regression", "boundary", "compatibility", "smoke", "sanity", "functional", "stress", "API testing","regression", "boundary", "compatibility", "smoke", "sanity", "functional", "stress","regression", "boundary",  "stress","stress","stress","stress","stress","stress"]
print(f"the duplicated of word SANITY in the list of data is ", calculate_duplicates(allTest,"sanity"))


