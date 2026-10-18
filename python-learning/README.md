# Python Learning Portfolio

A growing collection of small, readable Python examples and practice exercises. This repository documents my progress with core Python concepts as I work towards more advanced software development and AI projects.

**Background:** MSc Artificial Intelligence student at the University of Kent, with a BSc in Cloud Computing.

> **Getting started:** The initial examples are a starter set. I'll keep adding my own exercises, explanations, and improvements as I learn.

## Topics covered

| File | Concept | What it demonstrates |
| --- | --- | --- |
| `exercises/lists_and_functions.py` | Lists and functions | `append()`, `sum()`, `len()`, parameters and `return` |
| `exercises/dictionaries.py` | Dictionaries | Keys, values, `.values()`, `.items()`, insertion order |
| `exercises/hashing.py` | Hashing | `hash()` and how hashing differs from ordering |
| `exercises/oop.py` | Object-oriented programming | Classes, objects, `self`, instance attributes, methods |

Each example can run on its own.

## Run the examples

Install **Python 3.10 or newer**. In a terminal opened in this repository's folder, run:

```bash
python exercises/lists_and_functions.py
python exercises/dictionaries.py
python exercises/hashing.py
python exercises/oop.py
```

On some Windows installations, use `py` instead of `python`.

## Run the tests

No third-party packages are required.

```bash
python -m unittest discover -s tests -v
```

## What I'm learning

- **Parameters and arguments:** A function receives values from the caller.
- **`return`:** A function sends a result back to its caller; it does not automatically create a global variable.
- **Dictionary views:** `.values()` gives a view of values, while `.items()` produces key-value pairs.
- **Dictionary order vs hashing:** Dictionaries preserve insertion order, but hashing is used for fast key lookup. The position is not chosen by a hash value.
- **Instance attributes:** Data saved as `self.name` belongs to that object and can be used by its methods.

## Roadmap

- [ ] Add and explain my own university practice exercises
- [ ] Add more examples of slicing and comprehensions
- [ ] Build a small command-line application
- [ ] Add more test cases and improve documentation
- [ ] Start a separate project for applied data analysis / machine learning

## Repository organisation

```text
python-learning/
├── README.md
├── .gitignore
├── exercises/
│   ├── __init__.py
│   ├── lists_and_functions.py
│   ├── dictionaries.py
│   ├── hashing.py
│   └── oop.py
└── tests/
    └── test_exercises.py
```

The examples are for learning and can be improved over time. Sensitive files, credentials, and personal data should never be committed to a public repository.
