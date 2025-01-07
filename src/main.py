def exit_with_message(message: str) -> None:
	print(message)
	raise SystemExit


def ask_question(question: str, prompt: str) -> int:
	print(f"--- {question}? ---")

	try:
		return int(input(f"{prompt}: ").replace(" ", ""))
	except ValueError:
		exit_with_message("Please enter a whole number without any decimals....")
	except KeyboardInterrupt:
		exit_with_message("\nYou exited the program!")


def print_multiple_times(message: str, iterations: int) -> None:
	for _ in range(iterations):
		print(message)


floors: int = ask_question(
	"How many floors do you want in your skyscraper", "Floors")

rod_dots: int = ask_question(
	"How tall do you want your lightning rod to be", "# of dots for the rod")

print_multiple_times("   .", rod_dots)
print_multiple_times(".......", floors)
