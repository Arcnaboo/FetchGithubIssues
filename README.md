# FetchGitHubIssues

A minimal Java and Python proof-of-concept demonstrating how to extract trainable data from GitHub repositories. Now includes an example script for **real concurrent file fetching** with Python.

---

## 🚀 What does it do?

✅ Authenticates to GitHub using a personal access token (PAT).  
✅ Fetches issues in Java (proof of concept).  
✅ Fetches file contents concurrently in Python (new example).  
✅ Extracts key metadata: titles, bodies, authors, timestamps, file sizes, etc.  
✅ Designed to build a knowledge base or power AI retrieval-augmented generation (RAG) systems.

---

## 📂 Files

- **FetchGitHubIssues.java**  
  Java proof of concept: fetches all issues from a repo and prints their details.

- **concurrent_github_fetcher.py**  
  Python script: fetches file metadata concurrently with bounded parallelism using `asyncio` and `httpx`.

---

## 🔧 Requirements

- Java 17+
- Python 3.8+
- [OkHttp](https://square.github.io/okhttp/) 4.x (for Java)
- [Jackson Databind](https://github.com/FasterXML/jackson-databind) 2.x (for Java)
- [httpx](https://www.python-httpx.org/) (for Python)

---

## 🛠️ Java setup

1. Edit `FetchGitHubIssues.java`:
   - Replace `YOUR_PERSONAL_ACCESS_TOKEN` with your GitHub PAT.
   - Set `OWNER` and `REPO` appropriately.

2. Build and run:
   ```bash
   javac -cp ".:path/to/okhttp.jar:path/to/jackson-databind.jar" FetchGitHubIssues.java
   java -cp ".:path/to/okhttp.jar:path/to/jackson-databind.jar" FetchGitHubIssues
