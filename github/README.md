# Personal Website – Git & Jekyll Workflow

This guide explains how to run your site locally and push updates to GitHub.

---

## 0. Run the Site Locally (Jekyll)

Before committing, preview your site locally:

```bash
bundle install
bundle exec jekyll s
```

Then open:

```
http://localhost:4000
```

The site will automatically rebuild when you edit files.

Stop the server with:

```
Ctrl + C
```

---

## 1. Configure Git Identity (First Time Only)

Set your name and email:

```bash
# Set globally (recommended)
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"

# OR set only for this repository
git config user.name "Your Name"
git config user.email "your_email@example.com"
```

Check your configuration:

```bash
git config --list
```

---

## 2. Check Repository Status

See what files have changed:

```bash
git status
```

---

## 3. Stage Changes

Add all modified files:

```bash
git add .
```

---

## 4. Commit Changes

Write a clear commit message:

```bash
git commit -m "feat: update website content"
```

---

## 5. Pull Remote Changes (Avoid Push Rejection)

Always pull before pushing:

```bash
git pull origin main --rebase
```

If prompted about unrelated histories:

```bash
git pull origin main --rebase --allow-unrelated-histories
```

---

## 6. Push to GitHub

```bash
git push origin main
```

Your GitHub Pages site will automatically update after a successful push to `main`.

---

## Quick Daily Workflow

```bash
bundle exec jekyll s
git status
git add .
git commit -m "update"
git push
```
