# FLAMES Calculator

A fun console game that predicts the relationship between two people based on their names, using the classic FLAMES algorithm.

F = Friends, L = Lovers, A = Affectionate, M = Marriage, E = Enemies, S = Siblings

## How It Works

1. Enter two names.
2. Common letters between the two (cleaned, lowercase, no spaces) are cancelled out one-to-one.
3. The count of remaining letters is used to "count out" letters from F-L-A-M-E-S in a circular elimination, similar to the classic Josephus-style counting game.
4. The last remaining letter reveals your relationship result.

## Features

- Input validation (letters only, no numbers or symbols)
- Play multiple rounds without restarting the program
- Simple, friendly command-line interface
- Clean, well-documented, modular Python code

## Requirements

- Python 3.x (no external dependencies)

## Usage

```bash
python Flames.py
```

Follow the on-screen prompts to enter two names and see your FLAMES result. You'll be asked if you'd like to try another pair after each round.

## Example

```
JOIN THE FLAMES CALCULATOR EXPERIENCE
Do you want to play the game? (yes/no): yes
Enter the first name: John
Enter the second name: Jane

============================
FLAMES RESULT
John Jane
Result: Lovers
============================
```

## Project Structure

```
Flames.py   # Main script containing all game logic
```

## License

This project is free to use and modify for personal or educational purposes.
