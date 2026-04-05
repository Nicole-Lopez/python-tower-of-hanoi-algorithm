# Tower of Hanoi Algorithm

This project is part of the [freeCodeCamp Python Certification](https://www.freecodecamp.org/learn/python-v9/lab-tower-of-hanoi/implement-the-tower-of-hanoi-algorithm).

It implements a recursive solution to the classic Tower of Hanoi problem. The program simulates the movement of disks between three towers, following the game rules, and outputs each step of the process as a text-based visualization.

---

## 📌 Features

- Solve the Tower of Hanoi problem for any number of disks
- Use recursion to break the problem into smaller subproblems
- Simulate three towers (source, auxiliary, target) using lists
- Move disks following the rules:
  - Only one disk can be moved at a time
  - A larger disk can never be placed on top of a smaller one
- Track and display every intermediate state of the towers
- Generate a step-by-step text output of the solution
- Demonstrate how recursive algorithms evolve state over time

---

## 🛠️ Technologies

- Python 3

---
## 📖 User Stories
1.  You should have a function named `hanoi_solver` that takes an integer representing the total number of disks of the puzzle as the argument.
2.  The `hanoi_solver` function should solve the puzzle following the given rules in $2^n - 1$ moves, where `n` is the total number of disks.
3.  The `hanoi_solver` function should return a string with all the moves taken to solve the puzzle, including the starting arrangement, with each move on a new line. Rods should be represented as lists of integers, (the smallest disk is represented by the number `1`) with each rod separated by a space. For example, `hanoi_solver(3)` should return the following:

```python
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]
```

---

## 🧪 Example Usage

Example test cases are included as commented lines at the bottom of `main.py`.

Uncomment them to run and see the output.

---
## 📚 Notes

- This project was developed to meet the certification requirements.
- The implementation focuses on correctness and clarity rather than extended functionality.    
