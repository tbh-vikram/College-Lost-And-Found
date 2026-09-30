# College Lost and Found System

A simple, terminal-based Python application designed to help students and staff track, search for, and report lost items across a college campus. The system uses a score-matching algorithm to assist users in identifying missing items and persists data locally using a plain text file.

---

## 📌 Features

* **Smart Matching Algorithm:** Evaluates potential matches using a 3-point scoring system based on Item Name, Colour, and Location.
* **Automatic Item Removal:** Automatically claims and deletes an item from the recorded list when a complete match ($3 / 3$) is confirmed.
* **Persistent Storage:** Reads and saves records into a local text file (`found_items.txt`), automatically initializing it if absent.
* **Inventory Overview:** Allows users to view all currently reported and unclaimed found items.
* **Case-Insensitive Input:** Converts inputs to lowercase to improve search accuracy and prevent matching errors.

---

## ⚙️ How It Works

### Matching & Scoring Logic
When searching for a lost item using **Option 1**, the application compares input criteria against every record in `found_items.txt`:

1. **Item Name Match** $\rightarrow +1$ point
2. **Colour Match** $\rightarrow +1$ point
3. **Location Match** $\rightarrow +1$ point

* **Score $\ge 2$:** Displayed to the user under **Possible Matches**.
* **Score $= 3$:** Identified as an **Exact Match**. The item is removed from `found_items.txt` automatically.

### File Storage Format
Items are saved in `found_items.txt` as pipe-delimited text records:

```text
item_name|colour|location
```

*Example:*
```text
water bottle|blue|library
keys|silver|canteen
backpack|black|auditorium
```

---

## 🚀 Getting Started

### Prerequisites
* [Python 3.x](https://www.python.org/downloads/) installed on your machine.

### Running the System

1. Save your Python script (e.g., `main.py`).
2. Open your terminal or command prompt and navigate to the project folder.
3. Run the application:

```bash
python main.py
```

---

## 💻 Menu Options

```text
     COLLEGE LOST AND FOUND     
1. I Lost Something
2. I Found Something
3. Show Found Items
4. Exit
```

| Option | Function |
| :--- | :--- |
| **1. I Lost Something** | Searches the database for matches. Removes exact matches ($3/3$) automatically. |
| **2. I Found Something** | Logs a newly found item and appends it to `found_items.txt`. |
| **3. Show Found Items** | Displays all currently unclaimed items in the system. |
| **4. Exit** | Exits the application. |

---

## 📁 Project Structure

```text
.
├── main.py             # Main application source code
└── found_items.txt     # Local database file (auto-created on first run)
```
