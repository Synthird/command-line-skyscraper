def print_multiple_times(message, iterations):
    for _ in range(iterations):
        print(message)


print("How many floors do you want in your skyscraper?")

floors = int(input("Floors (Please enter only an Integer): "))

print_multiple_times("   .", 3)

print_multiple_times(".......", floors)
