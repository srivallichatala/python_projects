def quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
        "What is the largest planet in our solar system?": "Jupiter"
    }

    score = 0
    name = input("Enter your name: ")

    print(f"Welcome, {name}! Let's start the quiz.\n")

    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")

    print(f"\n{name}, you scored {score} out of {len(questions)}.")
    if score == len(questions):
        print("Congratulations! You got all the questions right!")
    elif score >= len(questions) / 2:
        print("Well done!")
    else:
        print("You can do better next time.")

quiz()