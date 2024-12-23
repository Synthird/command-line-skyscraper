def exit_with_possible_reasons() -> None:
	print("!!! Cannot print dots! !!!")
	print("Probably because you entered:")
	print("a) Decimals")
	print("b) Letters")
	print("c) Symbols")
	print("d) A negative number")
	print("e) You exited the program")
	raise SystemExit


def ask_question(question: str, prompt: str) -> int:
	number: int = 0

	print(f"--- {question}? ---")

	try:
		number = int(input(f"{prompt}: ").replace(" ", ""))
	except:
		exit_with_possible_reasons()

	if number > -1:
		return number
	else:
		exit_with_possible_reasons()


def print_multiple_times(message: str, iterations: int) -> None:
	for _ in range(iterations):
		print(message)


floors: int = ask_question(
	"How many floors do you want in your skyscraper", "Floors")

rod_dots: int = ask_question(
	"How tall do you want your lightning rod to be", "# of dots for the rod")

print_multiple_times("   .", rod_dots)
print_multiple_times(".......", floors)
