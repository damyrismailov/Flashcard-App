
# Flash Card Language App

Flash card app built with Python and Tkinter to help memorise vocabulary.

## Main features

- Displays a random French word on the front of a card.
- After a short delay the card flips to show the English translation.
- ✅ **Know** button: marks the word as learned, removes it from the pool and saves the remaining words.
- ❌ **Don’t know** button: keeps the word in the pool and moves on to a new card.
- Progress is saved in `data/words_to_learn.csv`, so next time the app only shows words that are still unknown.
- If `words_to_learn.csv` does not exist yet, the app starts from the full list in `data/french_words.csv`.

## What I learned

- Building graphical interfaces with Tkinter (window, canvas, images, buttons, layout).
- Using timers (`after`) to flip the card after a few seconds and cancelling them when needed.
- Loading and saving CSV files with `pandas`.
- Managing application state so user progress is stored between runs.

## How to run

1. Make sure you have Python 3 installed.
2. Install the `pandas` package with `pip install pandas`.
3. From the project folder, run `python flashcard-python/main.py`.

A window will open. Use the ✅ and ❌ buttons to mark words as known or unknown and keep practising until the list is empty.
```
