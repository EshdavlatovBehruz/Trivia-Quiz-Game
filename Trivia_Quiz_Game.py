import requests
import html
import random

def get_categories():
    r = requests.get("https://opentdb.com/api_category.php")
    categories = r.json()["trivia_categories"]
    new_dict = {}
    for i in categories:
        category_id = str(i['id'])
        category_name = i['name']
        print(f"{category_id}: {category_name}")
        new_dict[category_id] = category_name
    return new_dict


def get_question(amount, category, difficulty):
    url = (
        f"https://opentdb.com/api.php?amount={amount}"
        f"&category={category}&difficulty={difficulty}&type=multiple"
    )

    response = requests.get(url)
    return response.json()["results"]

def run_quiz():
    print("Welcome to thr Trivia Quzi Game!\n")
    categories = get_categories()

    category = input("\nChoose a category by typing the category number: \n").strip()
    while category not in categories:
        category = input("\nInvalid category. Try again: \n").strip()

    difficulty = input("\nChoose difficulty (easy / medium / hard): \n").strip().lower()
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = input("\nInvalid difficulty. Try again: \n").strip().lower()

    print("\nFetching questions...\n")
    questions = get_question(5,category, difficulty)

    score = 0

    for i , q in enumerate(questions, 1):
        question = html.unescape(q["question"])
        correct_answer = html.unescape(q["correct_answer"])
        options = [html.unescape(x) for x in q["incorrect_answers"]]
        options.append(correct_answer)
        random.shuffle(options)

        print(f"Question {i}: {question}")
        for y, z in enumerate(options,1):
            print(f"{y}.{z}")
        
        
        choice = input("\nYour answer (1-4): \n").strip()
        while choice not in ["1", "2", "3", "4"]:
            choice = input("\nPlease enter 1, 2, 3, or 4: \n").strip()

        if options[int(choice) - 1] == correct_answer:
            print("\nCorrect :)\n")
            score += 1
        else:
            print(f"\nWrong answer :( The correct: {correct_answer}\n")

    print("\n--- Quiz Finished ---\n")
    print(f"\nYou scored {score} out of {len(questions)}.\n")
if __name__ == "__main__":
    run_quiz()