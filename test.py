"""def takeinput(a, b):
    return a + b


def test_takeinput():
    result = takeinput(4, 5)
    assert result == 6 """


def trivia_quiz():
    print("Welcome to the Trivia Quiz!")


trivia_quiz()

score = 0

# Sample questions and answers
questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is 2 + 2?",
]
answers = ["Paris", "Mars", "4"]

for i in range(len(questions)):
    user_answer = input(questions[i] + " Your answer: ")
if user_answer.lower() == answers[i].lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is:", answers[i])
print("Your final score is:", score)

trivia_quiz()
