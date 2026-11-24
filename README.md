<div align="center">

# 🐍 Cisco Networking Academy · Python

Exercises and projects from the **Python Essentials** courses by Cisco Networking Academy.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Cisco](https://img.shields.io/badge/Cisco-Networking%20Academy-1BA0D7?logo=cisco&logoColor=white)
![Status](https://img.shields.io/badge/status-in%20progress-yellow)

</div>

---

## 📚 Contents

| Course | Project | Description |
|---|---|---|
| **Python Essentials 1** | [Tic-Tac-Toe](Python%20Essentials%201/) | Console tic-tac-toe against the computer: the final project of the course. |
| **Python Essentials 2** | [Module exploration](Python%20Essentials%202/) | Practice scripts for working with modules (`math`). |

---

## 🎮 Python Essentials 1: Tic-Tac-Toe

A console game where you play `O` against the computer (`X`). The computer opens in the center and then picks random free squares.

```
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
```

There are two versions:

| File | What it offers |
|---|---|
| `tictactoe.py` | The base solution, written to the course specification. |
| `tictactoePro.py` | An improved version with ANSI colors, turn headers and a notice of the computer's move. Colors can be turned off with `USE_COLORS = False`. |

📄 The full problem statement and the technical requirements are in the [project README](Python%20Essentials%201/README.md).

---

## 🧪 Python Essentials 2

| File | What it does |
|---|---|
| `tester.py` | Lists everything the `math` module exposes, using `dir()`. |

---

## ▶️ How to run

The only requirement is **Python 3**. No external libraries are needed.

```bash
git clone https://github.com/VictoriaRodriguezDenis/CISCO-Academy-Python.git
cd CISCO-Academy-Python

# Tic-Tac-Toe
python "Python Essentials 1/tictactoe.py"
python "Python Essentials 1/tictactoePro.py"

# Python Essentials 2
python "Python Essentials 2/tester.py"
```

> 💡 If the colors in `tictactoePro.py` show up as strange characters, your console doesn't support ANSI codes. Set `USE_COLORS = False` at the top of the file.

---

## 🗂️ Repository structure

```
CISCO-Academy-Python/
├── Python Essentials 1/
│   ├── README.md
│   ├── tictactoe.py
│   └── tictactoePro.py
├── Python Essentials 2/
│   └── tester.py
└── README.md
```

---

## 🌿 Workflow

This repository follows **GitFlow**:

- `main`: final versions only.
- `develop`: integration branch.
- `feature/*`: one branch per course or topic. Each one is merged into `develop` through a Pull Request.

Commits follow [Conventional Commits](https://www.conventionalcommits.org/).

---

<div align="center">

Made by **Victoria Rodríguez Denis** while studying with Cisco Networking Academy.

</div>
