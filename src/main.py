def ask_question(question: str, prompt: str) -> int:
	print(f"--- {question}? ---")

	try:
		return int(input(f"{prompt}: ").replace(" ", ""))
	except ValueError:
		print("Please only enter a whole number without any decimals....")
		raise SystemExit
	except KeyboardInterrupt:
		print("\nYou exited the program!")
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
