"""One Sentence for a Traveler from 1800 — entry for make.fun.

Writes one sentence to /output/entry.txt.
The sentence is one explanation, under 200 characters, built from things a person from 1800 already knows.
"""
import os

LINE = "Imagine a road where every letter, book, and newspaper in the world arrives at your door in the blink of an eye, and you can answer back at once."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
