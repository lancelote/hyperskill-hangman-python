def main() -> None:
    print("H A N G M A N")
    secret = "python"
    guess = input("Guess the word: ")

    if guess == secret:
        print("You survived!")
    else:
        print("You lost!")


if __name__ == "__main__":
    main()
