
<body>

<h1>📘 Advanced Git Workflow & Version Control</h1>

<h2>🎯 Objective</h2>
<p>
This assignment demonstrates how Git is used in real-world development,
including branching, merging, rebasing, and history management.
</p>

<h2>📁 Repository Link</h2>
<p>
<a href="https://github.com/zenuncrack/ETL-project.git" target="_blank">
https://github.com/zenuncrack/ETL-project.git
</a>
</p>

<h2>🔹 Task 1: Repository Initialization</h2>

<pre>
mkdir advanced-git-workflow
cd advanced-git-workflow
git init

echo "# Advanced Git Workflow" > README.md
git add .
git commit -m "Initial commit"

git branch -M main
git checkout -b develop
git checkout -b feature/login
</pre>

<p>
Explanation: A repository was created and initialized with main, develop, and feature branches.
</p>

---

<h2>🔹 Task 2: Branching Workflow</h2>

<pre>
git checkout develop
git checkout -b feature/payment

git checkout develop
git checkout -b feature/profile

git checkout develop
git checkout -b bugfix/login-error
</pre>

<p>
Multiple branches were created for features and bug fixes to simulate real-world workflow.
</p>

---

<h2>🔀 Merge Strategy</h2>

<pre>
git checkout develop
git merge feature/payment
</pre>

<p>
Merge combines branches and keeps full history with a merge commit.
</p>

---

<h2>🔁 Rebase Strategy</h2>

<pre>
git checkout feature/profile
git rebase develop

git checkout develop
git merge feature/profile
</pre>

<p>
Rebase creates a clean and linear commit history.
</p>

---

<h2>🔹 Task 3: Commit History Management</h2>

<pre>
git checkout -b feature/history-demo

echo "1" >> demo.txt
git add . && git commit -m "commit 1"

echo "2" >> demo.txt
git add . && git commit -m "commit 2"

echo "3" >> demo.txt
git add . && git commit -m "commit 3"

echo "4" >> demo.txt
git add . && git commit -m "commit 4"

echo "5" >> demo.txt
git add . && git commit -m "commit 5"
</pre>

---

<h2>🔁 Interactive Rebase</h2>

<pre>
git rebase -i HEAD~5
</pre>

<p>
Used to squash commits and modify commit messages.
</p>

---

<h2>✏️ Squash & Reword</h2>

<p><b>Squash:</b> Combines multiple commits into one.</p>
<p><b>Reword:</b> Changes commit messages.</p>

---

<h2>📊 Merge vs Rebase</h2>

<table border="1">
<tr>
<th>Feature</th>
<th>Merge</th>
<th>Rebase</th>
</tr>
<tr>
<td>History</td>
<td>Keeps full history</td>
<td>Linear history</td>
</tr>
<tr>
<td>Commit</td>
<td>Creates merge commit</td>
<td>No extra commit</td>
</tr>
<tr>
<td>Usage</td>
<td>Safe for teams</td>
<td>Cleaner history</td>
</tr>
</table>

---

<h2>📤 Push to GitHub</h2>

<pre>
git remote add origin https://github.com/zenuncrack/ETL-project.git

git push -u origin main
git push origin develop
git push origin feature/login
git push origin feature/payment
git push origin feature/profile
git push origin bugfix/login-error
git push origin feature/history-demo
</pre>

---

<h2>⭐ Bonus: Git Hook</h2>

<pre>
#!/bin/sh
if ! grep -q "^[A-Z]" "$1"; then
  echo "Commit message must start with a capital letter"
  exit 1
fi
</pre>

---

<h2>✅ Conclusion</h2>

<p>
This assignment demonstrates real-world Git workflows including branching,
merging, rebasing, and history cleanup techniques.
</p>

</body>
</html>
