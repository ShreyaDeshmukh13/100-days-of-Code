## 📘 Flashy – French to English Flashcard App

Flashy is a simple desktop flashcard application built using Python and Tkinter to help users learn French vocabulary. The app displays French words on flashcards and automatically flips them to show their English meanings after a short delay.

## ✨ Features

- Displays random French words using flashcards

- Automatically flips the card after 3 seconds

- Allows users to mark words as known or unknown

- Saves progress so learned words are not repeated

- Clean and user-friendly graphical interface

## 🛠️ Technologies Used

- Python

- Tkinter (GUI)

- Pandas (CSV data handling)

- Random module

## 📂 Project Structure

```text
project-folder/
│
├── data/
│   ├── french_words.csv
│   └── words_to_learn.csv
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
│
├── main.py
└── README.md
```


## 📄 Dataset

- french_words.csv – Original dataset containing French–English word pairs

- words_to_learn.csv – Stores words the user has not yet learned (created automatically)

## ▶️ How It Works

1. A French word is displayed on the flashcard.

2. After 3 seconds, the card flips to show the English translation.

3. Clicking ❌ marks the word as not known and keeps it in the learning list.

4. Clicking ✅ marks the word as known and removes it from future cards.

5. Progress is saved automatically in words_to_learn.csv

## 🚀 How to Run the Application

1. Make sure Python is installed.

2. Install the required library:
pip install pandas
3. Run the program: python main.py

## 🧠 Learning Outcome

- Understanding of GUI development using Tkinter

- Working with CSV files using Pandas

- Event-driven programming in Python

- File handling and state persistence

## 📌 Future Improvements

-  Add pronunciation audio

- Support for multiple languages

- Progress statistics dashboard

- Mobile version of the app

## 👩‍💻 Author

Shreya Deshmukh