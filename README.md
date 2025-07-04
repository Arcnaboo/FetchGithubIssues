# FetchGitHubIssues

A minimal Java proof-of-concept app that connects to the GitHub API, fetches all issues from a repository, and prints trainable data such as titles, bodies, authors, timestamps, and more.

---

## 🚀 What does it do?

✅ Authenticates to GitHub using a personal access token (PAT).  
✅ Fetches up to 100 issues in a single API request.  
✅ Extracts key information from each issue (title, body, author, created date, etc.).  
✅ Prints each issue’s details in a readable format — ideal for building a knowledge base for LLM training or semantic search.

---

## 📂 Files

- **FetchGitHubIssues.java**  
  The main Java file containing the entire application logic.

---

## 🔧 Requirements

- Java 17 or newer
- [OkHttp](https://square.github.io/okhttp/) 4.x
- [Jackson Databind](https://github.com/FasterXML/jackson-databind) 2.x

---

## 🛠️ Setup

1. **Clone this repo or copy the file** to your project folder.

2. **Add dependencies** (e.g., with Maven):
   ```xml
   <dependency>
     <groupId>com.squareup.okhttp3</groupId>
     <artifactId>okhttp</artifactId>
     <version>4.11.0</version>
   </dependency>
   <dependency>
     <groupId>com.fasterxml.jackson.core</groupId>
     <artifactId>jackson-databind</artifactId>
     <version>2.17.0</version>
   </dependency>
