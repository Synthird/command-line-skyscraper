def ask_question(question: str, prompt: str) -> int:
    print(f"--- {question}? ---")
    try:
        number: int = int(input(f"{prompt}: "))
        if number > -1:
            return number
        else:
            raise ValueError
    except:
        print("!!! Cannot print a skyscraper! !!!")
        print("Probably because you entered:")
        print("a) Decimals")
        print("b) Letters")
        print("c) Symbols")
        print("d) Spaces between numbers")
        print("e) Negative numbers")
        print("f) You exited the program")
        raise SystemExit


def print_multiple_times(message: str, iterations: int) -> None:
    for _ in range(iterations):
        print(message)


floors: int = ask_question(
    "How many floors do you want in your skyscraper", "Floors")

rod_dots: int = ask_question(
    "How tall do you want your lightning rod to be", "# of dots for the rod")

print_multiple_times("   .", rod_dots)
print_multiple_times(".......", floors)
