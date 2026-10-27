# %%
quiz = {
    "What is 1 + 1?": "2",
    "What color is an apple best known for?": "red"
}

score = 0
for question, answer in quiz.items():
    guess = input(f"{question} ")
    if guess.strip().lower() == answer:
        score += 1
        print("Correct!")
    else:
        print("Nope, it was", answer)
print(f"You got {score}/{len(quiz)} ({score / len(quiz) * 100:.0f}%)")


