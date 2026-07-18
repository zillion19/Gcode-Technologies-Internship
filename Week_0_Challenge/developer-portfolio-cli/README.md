# Developer Portfolio CLI

A professional Python Command-Line Interface (CLI) application developed as part of the **AI Engineering Internship – Week 0 Challenge**. The application demonstrates fundamental Python programming, JSON data handling, REST API integration, and clean software development practices.

---

## Project Overview

The Developer Portfolio CLI is a console-based application that displays a developer's profile information from a JSON file and retrieves real-time GitHub profile information using the GitHub REST API.

This project demonstrates:

* Reading structured data from JSON files
* REST API consumption
* Error handling
* Modular programming
* Clean code organization
* Python best practices

---

## Features

* Read developer information from a JSON configuration file.
* Display a formatted developer portfolio.
* Retrieve live GitHub profile information using the GitHub REST API.
* Handle invalid usernames and network errors gracefully.
* Organize code into reusable modules.
* Follow clean coding standards.

---

## Technologies Used

* Python 3.12+
* JSON
* Requests Library
* Git
* GitHub
* REST API

---

## Project Structure

```text
developer-portfolio-cli/
│
├── main.py              # Main application
├── api.py               # GitHub API functions
├── utils.py             # JSON utility functions
├── profile.json         # Developer information
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── .gitignore
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/developer-portfolio-cli.git
```

### 2. Navigate to the Project Directory

```bash
cd developer-portfolio-cli
```

### 3. Create a Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate the environment

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Execute the following command:

```bash
python main.py
```

---

## Sample Output

```text
==================================================
        DEVELOPER PORTFOLIO
==================================================

Name       : Filimawit Birhane
Role       : AI Engineer & Data Science Student

Skills
 • Python
 • Machine Learning
 • Docker
 • PostgreSQL

GitHub
https://github.com/zillion19

Portfolio
https://filimawit-b-hailemariam-portfolio.netlify.app

Enter GitHub Username:
zillion19

GitHub Profile

Username           : zillion19
Followers          : 00
Following          : 00
Public Repositories: 8
Bio                : learn today lead tomorrow
```

---

## REST API

This project uses the **GitHub REST API** to retrieve public profile information.

Example endpoint:

```
https://api.github.com/users/{username}
```

Example data retrieved:

* Username
* Bio
* Followers
* Following
* Public Repositories
* Profile URL

---

## Error Handling

The application handles common errors, including:

* Missing JSON file
* Invalid JSON format
* Invalid GitHub username
* Internet connection problems
* API request failures

---

## Learning Outcomes

Through this project, I practiced:

* Python programming fundamentals
* JSON file processing
* REST API integration
* Exception handling
* Modular software design
* Git and GitHub workflow
* Technical documentation

---

## Future Improvements

Potential enhancements include:

* Interactive menu-driven interface
* Weather API integration
* Country information lookup
* Colored terminal output
* Export portfolio as PDF
* SQLite or PostgreSQL database support
* User authentication
* Logging and configuration management
* Unit testing

---

## Author

**Filimawit Birhane**

**Role:** AI Engineer & Data Science Student

**University:** Mekelle University

**Department:** Information Technology

**GitHub:** https://github.com/zillion19

**Portfolio:** https://filimawit-b-hailemariam-portfolio.netlify.app

---

## License

This project was developed for educational purposes as part of the **AI Engineering Internship – Week 0 Challenge**.
