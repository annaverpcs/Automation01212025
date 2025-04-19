# Severity for bugs
#
# CrItical
# major
# medium
# minor
# cosmetic

bugSeverity = input("Please enter the severity of the bug: ").lower()

match bugSeverity:
    case "critical":
        print("This bug need immediate attention from dev")
    case "major":
        print("This bug is serious, functionality is impacted.")
    case "medium":
        print("Moderate issie. It is not blocking bug, but need attention.")
    case "minor":
        print("This is not the urgent issue, however better to fix")
    case "cosmetic":
        print("When you'll have time, please take a look at the code.")
    case _:
        print("there is no such severity. Please try again.")

print(50*"-")
#HTTP Status code: 100,200,300,400,500
# 1xx informational response – the request was received, continuing process
# 2xx successful – the request was successfully received, understood, and accepted
# 3xx redirection – further action needs to be taken in order to complete the request
# 4xx client error – the request contains bad syntax or cannot be fulfilled
# 5xx server error – the server failed to fulfil an apparently valid request

status_code = int(input("Please enter the HTTP status  group: "))

match status_code:
    case 100:
        print("1xx informational response – the request was received, continuing process")
    case 200:
        print("2xx successful – the request was successfully received, understood, and accepted")
    case 300:
        print("3xx redirection – further action needs to be taken in order to complete the request")
    case 400:
        print("4xx client error – the request contains bad syntax or cannot be fulfilled")
    case 500:
        print("5xx server error – the server failed to fulfil an apparently valid request")
    case _:
        print("there is no such HTTP error code. Please try again.")