
# Intelligent Number Guessing Agent
low = 1
high = 100
attempt = 0
print("Think of a number between 1 and 100.")

while low <= high:

    guess = (low + high) // 2

    print("My guess is:", guess)
    attempt += 1
    feedback = input("Higher, Lower or Correct :").lower()

    if feedback == "higher":
        low = guess + 1

    elif feedback == "lower":
        high = guess - 1

    elif feedback == "correct":
        print("Number guessed successfully!")
        print("Attempts Required:", attempt)
        break

    else:
        print("Invalid feedback!")
        attempt -= 1

else:
    print("Invalid or inconsistent feedback!")
