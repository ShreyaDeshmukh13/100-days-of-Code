# 🧠 Quizzler - Python Quiz App

Quizzler is a simple and interactive quiz application built using **Python** and **Tkinter**.
It fetches real-time True/False questions from the **Open Trivia Database API** and presents them in a clean graphical interface.

---

## 🚀 Features

* 🎯 Dynamic quiz questions from an online API
* 🖥️ User-friendly GUI built with Tkinter
* ✅ Instant feedback (correct/incorrect answers)
* 📊 Live score tracking
* 🎨 Clean and responsive interface

---

## 📂 Project Structure

```
project/
│
├── main.py              # Entry point
├── data.py              # Fetches questions from API
├── question_model.py    # Question class
├── quiz_brain.py        # Quiz logic
├── ui.py                # Tkinter user interface
│
└── images/
    ├── true.png
    └── false.png
```

---

## ⚙️ Requirements

* Python 3.x
* `requests` library

Install dependencies:

```
pip install requests
```

---

## ▶️ How to Run

1. Clone the repository or download the files
2. Navigate to the project folder
3. Run:

```
python main.py
```

---

## 🌐 API Used

* Open Trivia Database
  https://opentdb.com/

---

## 🧩 How It Works

1. Questions are fetched from the API (`data.py`)
2. Converted into `Question` objects
3. `QuizBrain` handles quiz logic and scoring
4. `QuizInterface` displays questions and manages user interaction

---

## 🎨 Future Improvements

* Difficulty selection
* Category selection
* Timer for each question
* Dark mode
* Save high scores

---

## 👨‍💻 Author

Shreya Deshmukh

---

## 📜 License

This project is open-source and free to use.
