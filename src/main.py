def ask_question(question, prompt) -> str:
    print(f"--- {question} ---")
    print("(Please don't enter decimals or units)")
    answer: int = int(input(f"{prompt}: "))
    return answer


def print_multiple_times(message, iterations) -> None:
    for _ in range(iterations):
        print(message)


# Floors
floors: int = ask_question(
    "How many floors do you want in your skyscraper?", "Floors")

# Lightning rod
rod_dots: int = ask_question(
    "How tall do you want your lightning rod to be?", "Number of dots for the rod")

print_multiple_times("   .", rod_dots)

print_multiple_times(".......", floors)
