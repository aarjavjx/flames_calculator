"""
FLAMES Calculator
-----------------
A fun console game that predicts the relationship between two people
based on their names, using the classic FLAMES algorithm.
 
F = Friends
L = Lovers
A = Affectionate
M = Marriage
E = Enemies
S = Siblings
"""
 
def clean_name(name):
    name = name.lower().replace(" ", "")
    if name.isalpha() and len(name) > 0:
        return name
    return None
 
def get_valid_name(prompt):
    while True:
        raw = input(prompt)
        cleaned = clean_name(raw)
        if cleaned:
            return cleaned
        print("That name isn't valid — please use letters only, with no numbers or symbols.")
 
def cancel_common_letters(name1, name2):

    list1 = list(name1)
    list2 = list(name2)

    for letter in list1[:]:  
        if letter in list2:
            list1.remove(letter)
            list2.remove(letter)
 
    remaining_count = len(list1) + len(list2)
    return remaining_count

def get_flames_result(count):
    letters = ["F", "L", "A", "M", "E", "S"]
    start_index = 0
 
    while len(letters) > 1:
        n = len(letters)
        remove_index = (start_index + count - 1) % n
        letters.pop(remove_index)

        if len(letters) > 0:
            start_index = remove_index % len(letters)
    return letters[0]
 
def get_meaning(letter):
    meanings = {
        "F": "Friends ",
        "L": "Lovers ",
        "A": "Affectionate ",
        "M": "Marriage ",
        "E": "Enemies ",
        "S": "Siblings "
    }
    return meanings.get(letter, "Unknown ")
 
 
def display_result(name1, name2, letter):
    meaning = get_meaning(letter)
    print("\n============================")
    print("FLAMES RESULT")
    print(f"{name1.capitalize()} {name2.capitalize()}")
    print(f"Result: {meaning}")
    print("============================\n")
 
def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Please enter 'yes' or 'no' only.")
 
def play_round():
    try:
        name1 = get_valid_name("Enter the first name: ")
        name2 = get_valid_name("Enter the second name: ")
 
        remaining_count = cancel_common_letters(name1, name2)
 
        if remaining_count == 0:
            remaining_count = len(["F", "L", "A", "M", "E", "S"])

        result_letter = get_flames_result(remaining_count)
        display_result(name1, name2, result_letter)
    except Exception as e:
        print(f"An error occurred: {e}")
 
def main():
    print("JOIN THE FLAMES CALCULATOR EXPERIENCE")
    if not ask_yes_no("Do you want to play the game? (yes/no): "):
        print("Okay, maybe next time!")
        return
    
    while True:
        play_round()
        if not ask_yes_no("Do you want to try another pair? (yes/no): "):
            print("Thanks for playing! See you next time!")
            break

if __name__ == "__main__":
    main()