# 📈 Stock Portfolio Tracker

📌 **Domain**: Python Programming Internship  
👨‍💻 **Intern:** Devansh Patel  
🏢 **Organization:** CodeAlpha

---

## 📜 Project Overview
This is a simple **text-based Stock Portfolio Tracker** developed as part of the **CodeAlpha Python Programming Internship**. The user picks a stock from a predefined list, enters how many shares to track, and the program calculates **total investment** (price × quantity) and saves a snapshot to a text file. It demonstrates **dictionaries**, **loops**, **conditions**, **file handling**, and **user input/output** in Python.

---

## 🧠 Key Python Concepts Used
- Dictionaries (stock names → prices)  
- Loops (`for` over dictionary keys)  
- `if` / `else` conditions  
- User input / output (`input`, `print`)  
- String methods (`.upper()`)  
- Type conversion (`int`)  
- File writing (`with open(..., "w")`)

---

## ⚙️ How It Works
1. The program keeps a **dictionary** of sample stocks and their prices (for learning—not live market data).  
2. It **lists all available stocks** and their prices in the terminal.  
3. The user enters a **stock name** (matched case-insensitively after converting input to uppercase).  
4. The user enters **quantity** (number of shares).  
5. If the stock exists, the program computes **total investment** = price × quantity.  
6. Results are **printed** and **written** to `portfolio.txt`.  
7. If the stock name is not in the dictionary, the program shows **“Stock not found!”** ❌  

---

## ▶️ To run the program
From the `codealpha_Stock Portfolio Tracker` folder:
```bash
python "Stock Portfolio Tracker.py"
```
On some systems use `python3` instead of `python`.  
Use quotes around the filename because it contains spaces.

---

## 📂 Folder Structure
```
codealpha_Stock Portfolio Tracker/
│
├── Stock Portfolio Tracker.py    # Main program
├── portfolio.txt                 # Saved snapshot (created/updated when you run the script)
└── README.md                     # Project documentation
```

---

## 🧾 Internship Details
This project is one of the assigned tasks under the **CodeAlpha Python Programming Internship**, focusing on practical use of Python fundamentals.

---

## 🔗 Connect
**GitHub (repository):** [github.com/Devanshpatel27/codealpha_tasks](https://github.com/Devanshpatel27/codealpha_tasks)  
**LinkedIn:** [linkedin.com/in/devansh-patel-a8b159329](https://www.linkedin.com/in/devansh-patel-a8b159329/)