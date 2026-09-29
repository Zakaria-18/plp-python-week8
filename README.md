# Python- Personal Mini-Toolkit

## What this toolkit does
A menu-driven program that offers four tools: a Number Guessing Game, a
To-Do List, a Simple Calculator, and a Name Formatter. The menu keeps
appearing until the user chooses Quit, and an invalid menu choice gets a
polite message instead of a crash.

## Files
- `toolkit_plan.txt` - The plan: four tools, their descriptions, the exact menu text, and the concepts each tool uses.
- `toolkit.py` - The finished program with four tool functions and a main menu loop.
- `screenshots/` - Screenshots of the menu (including an invalid choice) and each tool running.

## How to run it
1. Make sure Python 3 is installed.
2. Open a terminal in this folder.
3. Run: `python toolkit.py`
4. Pick a number from 1 to 5 and follow the prompts. Type `back` inside
   the To-Do List to return to the main menu, and pick `5` to quit.

## Reflection
The hardest part was the To-Do List tool, because it has its own inner
loop and its own mini-menu, and I had to be careful to use `break` so it
returns to the main menu instead of quitting the whole program. The bug
that took me longest to fix was in the guessing game: when I typed a
letter instead of a number, `int()` raised a `ValueError` and the game
crashed - I added a `try` / `except` around the conversion and a `continue`
so the loop just asks again. I also had to remember to check `if task in
tasks:` before calling `.remove()` in the To-Do List, or it would crash
when the user typed something that wasn't there. If I had one more week,
I would save the tasks and the game's best score to a file so the toolkit
remembers them between runs. I would also add a fifth tool, maybe a
countdown timer, and a "clear all tasks" option to the To-Do List.
