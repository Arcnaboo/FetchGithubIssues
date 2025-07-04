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
   ```

---

## 🛠️ Python setup

1. Edit `concurrent_github_fetcher.py`:
   - Replace `GITHUB_TOKEN`, `OWNER`, `REPO`, and `BRANCH` as needed.

2. Install dependencies:
   ```bash
   pip install httpx
   ```

3. Run the script:
   ```bash
   python concurrent_github_fetcher.py
   ```

---

## 📝 Output examples

**Java:**
```
====================================
Title: Issue title
Author: authorUsername
Created: 2023-01-01T12:34:56Z
State: open
Comments: 2
Body:
Full issue description here...
====================================
```

**Python:**
```
Found 5 files at repo root.
[+] README.md: 1234 bytes
[+] app.py: 5678 bytes
...
```

---

## ➕ Next steps

✅ Extend Java PoC to store issues in a database.  
✅ Enhance Python fetcher to recurse into subdirectories.  
✅ Add embedding generation for semantic search.  
✅ Build a unified knowledge base combining issues + files.

---

## ⚠️ Notes

- GitHub API imposes rate limits (5,000 requests/hour for authenticated users).  
- Keep your personal access token private — never commit it to public repos.

---

## 📄 License

MIT License (or your preferred license).
