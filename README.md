# 🏥 Smart Hospital Patient Management System

A Python-based **Smart Hospital Patient Management System** designed to collect patient information, validate health data, classify patients according to risk conditions, and provide basic health analysis.

The system is a **menu-driven console application** developed using Python. It demonstrates fundamental programming concepts such as functions, loops, dictionaries, lists, conditional statements, input validation, exception handling, and basic data analysis.

## ✨ Features

* 👤 Add and store patient information
* 🔢 Validate and convert patient age into an integer
* 🌡️ Validate body temperature in Fahrenheit
* 🫁 Validate oxygen level percentage
* 🚨 Automatically classify patients into:

  * **Normal**
  * **Critical**
  * **Emergency**
* 📊 Calculate average body temperature
* 📈 Calculate average oxygen level
* 📋 Display all patient records
* 🚨 Display the highest-risk patient
* 📊 Display a risk-category summary
* ❌ Handle invalid user input
* 🖥️ Simple menu-driven console interface

## 🧠 Patient Risk Classification

The system uses body temperature and oxygen level to determine a patient's risk category.

| Risk Category | Condition                                                                            |
| ------------- | ------------------------------------------------------------------------------------ |
| 🟢 Normal     | Patient does not meet Critical or Emergency conditions                               |
| 🟡 Critical   | Oxygen level is between 85% and 92%, or temperature is between 100°F and below 103°F |
| 🔴 Emergency  | Oxygen level is below 85%, or temperature is 103°F or higher                         |

Emergency conditions have the highest priority in the classification process.

## 🛠️ Technologies Used

* **Python 3**
* Python Standard Library
* `math` module

The project currently uses the built-in `math` module and does not require external Python packages.

## 📂 Project Structure

```text
Smart-Hospital-Patient-Management-System/
│
├── smart_hospital.py
├── README.md
└── .gitignore
```

> You can rename your Python file from `Pasted code.py` to `smart_hospital.py` before uploading it to GitHub.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Smart-Hospital-Patient-Management-System.git
```

### 2. Open the Project Folder

```bash
cd Smart-Hospital-Patient-Management-System
```

### 3. Run the Program

```bash
python smart_hospital.py
```

If your system uses `python3`, run:

```bash
python3 smart_hospital.py
```

## ▶️ How to Use

After starting the program, the main menu appears:

```text
========================================
 SMART HOSPITAL PATIENT MANAGEMENT SYSTEM
========================================
1. Add Patient
2. Display Patient Records
3. Calculate Average Temperature and Oxygen
4. Display Risk Summary
5. Display Highest-Risk Patient
6. Exit
```

The application provides six options through the main menu.

### 1. Add Patient

Enter:

* Patient name
* Patient age
* Body temperature in °F
* Oxygen level in %

The program validates the entered information before storing the patient record.

Example:

```text
Enter patient name: Ali
Enter patient age: 25
Enter body temperature (°F): 98.6
Enter oxygen level (%): 97

Patient record added successfully.
Risk Category: Normal
```

### 2. Display Patient Records

Displays all stored patient information, including:

* Name
* Age
* Temperature
* Oxygen level
* Risk category

The records are stored in a Python list, while each patient is represented using a dictionary.

### 3. Calculate Average Health Values

The program calculates:

* Average body temperature
* Average oxygen level

and displays the results rounded to two decimal places.

Example:

```text
Average Temperature: 99.25 °F
Average Oxygen Level: 96.5 %
```

### 4. Display Risk Summary

The system counts the number of:

* Normal patients
* Critical patients
* Emergency patients

Example:

```text
Total Critical Patients: 2
Total Emergency Patients: 1
Normal Patients Count: 5
```

### 5. Display Highest-Risk Patient

The program compares patient risk categories using a priority system:

```text
Normal    → 1
Critical  → 2
Emergency → 3
```

The patient with the highest risk priority is displayed.

### 6. Exit

Selecting option `6` exits the application.

## 🧩 Python Concepts Demonstrated

This project demonstrates several important Python programming concepts:

* Variables
* Data types
* Type conversion
* `if / elif / else`
* `while` loops
* `for` loops
* Functions
* Lists
* Dictionaries
* Exception handling
* `try / except`
* Input validation
* Dictionary-based priority management
* Basic statistical calculations
* Menu-driven programming

## 📊 Data Validation

The project performs validation before accepting patient information.

### Patient Name

The name cannot be empty.

### Age

Age must be a whole number between:

```text
0 - 120
```

### Body Temperature

Temperature must be a valid finite number between:

```text
80°F - 115°F
```

### Oxygen Level

Oxygen level must be a valid finite number between:

```text
0% - 100%
```

## ⚠️ Important Note

This project is an **educational Python application** and should not be used as a real medical diagnosis or clinical decision-making system. The risk thresholds are implemented according to the project's programming requirements and are not a substitute for professional medical assessment.

## 🚀 Future Improvements

Possible future versions could include:

* 💾 Save patient records to a JSON/CSV/database
* 🔍 Search patients by name or ID
* ✏️ Update patient records
* 🗑️ Delete patient records
* 📅 Add patient admission dates
* 🆔 Generate unique patient IDs
* 📊 Add graphical health statistics
* 🤖 Integrate a machine-learning model
* 🖥️ Develop a GUI using Tkinter or PyQt
* 🌐 Convert the system into a web application
* 🔐 Add authentication and user roles
* 🗄️ Connect the system with MySQL or PostgreSQL

## 👨‍💻 Author

**Your Name**

BS Computer Science (BSCS)

University of Sialkot

---

## 📄 License

This project is created for **educational and academic purposes**.

You may modify and improve the project for learning and development purposes.
