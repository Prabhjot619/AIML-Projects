# Quiz Game

def quiz_game():
    score = 0
    lifeline = 1

    questions = [
        {"q": "What is the capital of India?", "a": "delhi"},
        {"q": "Which language is used for AI?", "a": "python"},
        {"q": "What is 5 * 6?", "a": "30"},
        {"q": "Who developed Python?", "a": "guido van rossum"},
        {"q": "Which planet is known as Red Planet?", "a": "mars"},
        {"q": "What is the square root of 64?", "a": "8"},
        {"q": "Which data structure uses FIFO?", "a": "queue"},
        {"q": "HTML stands for?", "a": "hypertext markup language"},
        {"q": "Which company created Windows?", "a": "microsoft"},
        {"q": "Binary of 5?", "a": "101"},
        {"q": "CPU stands for?", "a": "central processing unit"},
        {"q": "Fastest land animal?", "a": "cheetah"}
    ]

    print("\n Welcome to Advanced Quiz Game!")

    for i, q in enumerate(questions):
        print(f"Level {i+1}: {q['q']}")
        print("Type 'skip' to use lifeline")

        ans = input("Your answer: ").lower()

        if ans == "skip" and lifeline > 0:
            print("⏭ Lifeline used! Skipping question.")
            lifeline -= 1
            continue

        if ans == q["a"]:
            print("✅ Correct!")
            score += 1
        else:
            print(" Wrong! Game Over.")
            break

    print(f"\n Final Score: {score}/{len(questions)}")

quiz_game()`1