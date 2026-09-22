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
    """
    Cleans the input name: converts to lowercase and removes spaces.
    Returns the cleaned name, or None if invalid.
    """
    name = name.lower().replace(" ", "")
    if name.isalpha() and len(name) > 0:
        return name
    return None
 
 
def get_valid_name(prompt):
    """
    Keeps asking the user for a name until a valid one is entered.
    """
    while True:
        raw = input(prompt)
        cleaned = clean_name(raw)
        if cleaned:
            return cleaned
        print("❌ Invalid name! Please enter letters only (no numbers/symbols).")
 
 
def cancel_common_letters(name1, name2):
    """
    Cancels out common letters between the two names, one-to-one.
    If a letter appears multiple times, only as many matching
    occurrences as exist in both names are cancelled.
 
    Returns the total count of remaining (uncancelled) letters.
    """
    list1 = list(name1)
    list2 = list(name2)
 
    # Go through each letter in name1 and try to remove one matching
    # occurrence from name2 (this naturally handles repeated letters
    # correctly, since list.remove() only removes the first match).
    for letter in list1[:]:  # iterate over a copy since we're modifying list1
        if letter in list2:
            list1.remove(letter)
            list2.remove(letter)
 
    remaining_count = len(list1) + len(list2)
    return remaining_count
 
 
def get_flames_result(count):
    """
    Uses the circular counting-out method to eliminate letters from
    FLAMES based on the given count, until only one letter remains.
 
    Logic:
    - Arrange F, L, A, M, E, S as if in a circle.
    - Starting from the current position, count forward 'count' steps
      (wrapping around when reaching the end of the list).
    - Remove the letter landed on.
    - Continue counting from the very next letter after the removed one
      (never restart from the beginning).
    - Repeat until one letter remains.
    """
    letters = ["F", "L", "A", "M", "E", "S"]
    start_index = 0
 
    while len(letters) > 1:
        n = len(letters)
        # Calculate index to remove: move (count - 1) steps forward
        # from start_index, wrapping around using modulo.
        remove_index = (start_index + count - 1) % n
        letters.pop(remove_index)
 
        # Next round starts from the same index position (since the
        # list shrank, this naturally points to the next letter).
        # If we removed the last element, wrap back to 0.
        if len(letters) > 0:
            start_index = remove_index % len(letters)
 
    return letters[0]
 
 
def get_meaning(letter):
    """
    Maps the final FLAMES letter to its meaning and emoji.
    """
    meanings = {
        "F": "Friends 🤝",
        "L": "Lovers 💕",
        "A": "Affectionate 😍",
        "M": "Marriage 💍",
        "E": "Enemies 😡",
        "S": "Siblings 👫"
    }
    return meanings.get(letter, "Unknown 🤔")
 
 
def display_result(name1, name2, letter):
    """
    Displays the final FLAMES result in a nicely formatted way.
    """
    meaning = get_meaning(letter)
    print("\n============================")
    print("🔥 FLAMES RESULT 🔥")
    print(f"{name1.capitalize()} ❤️ {name2.capitalize()}")
    print(f"Result: {meaning}")
    print("============================\n")
 
 
def ask_yes_no(prompt):
    """
    Keeps asking until the user enters 'y' or 'n'.
    Returns True for yes, False for no.
    """
    while True:
        answer = input(prompt).strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("❌ Please enter 'y' or 'n' only.")
 
 
def play_round():
    """
    Handles one full round of the game: taking names, calculating
    the result, and displaying it.
    """
    try:
        name1 = get_valid_name("Enter the first name: ")
        name2 = get_valid_name("Enter the second name: ")
 
        remaining_count = cancel_common_letters(name1, name2)
 
        # Edge case: if somehow all letters cancel out (remaining_count = 0),
        # treat it as a full circle pass equal to the FLAMES length.
        if remaining_count == 0:
            remaining_count = len(["F", "L", "A", "M", "E", "S"])
 
        result_letter = get_flames_result(remaining_count)
        display_result(name1, name2, result_letter)
 
    except Exception as e:
        print(f"❌ Something went wrong: {e}")
 
 
def main():
    """
    Main entry point of the program. Shows the welcome banner,
    asks if the user wants to play, and loops through rounds.
    """
    print("🔥🔥🔥 WELCOME TO THE FLAMES CALCULATOR 🔥🔥🔥")
 
    if not ask_yes_no("Do you want to play the game? (y/n) 🎮: "):
        print("👋 Okay, maybe next time!")
        return
 
    while True:
        play_round()
        if not ask_yes_no("Do you want to try another pair? (y/n) 🔁: "):
            print("👋 Thanks for playing! See you next time!")
            break
 
 
if __name__ == "__main__":
    main()