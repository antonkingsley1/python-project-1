confirm = input("Do you want to add questions? ").strip().lower()

while confirm == "yes":
    new_question = input("Question: ")
    choices = []
    for i in range(1, 5):
        choice = input(f"Choice {i}: ")
        choices.append(choice)
    answer = input("Correct answer: ")
    new_dict = {"question": new_question, "choices": choices, "answer": answer}
    question_bank.append(new_dict)
    with open("question_bank.json", "w", encoding="utf-8") as file:
        json.dump(question_bank, file, indent=4)
    print("Question saved!")
    confirm = input("Add another question? ").strip().lower()
