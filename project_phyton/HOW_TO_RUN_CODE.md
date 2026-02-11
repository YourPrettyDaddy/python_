# How to run your code — pick one way

You have **3 ways** to run Python. Use whichever feels easiest.

---

## 1. Run button in Cursor (easiest — no typing commands)

Best for: running a whole file and seeing the result quickly.

1. Open the Python file (e.g. `hello.py`).
2. Click the **▶ Run** button at the top right of the editor.
3. Or right‑click in the file → **Run Python File in Terminal**.

The output appears in the **Terminal** panel at the bottom. No need to type anything.

---

## 2. Terminal (run a file)

Good for: when you’re comfortable with the editor and want to run from the terminal.

1. Open the **Terminal** in Cursor: **Terminal → New Terminal** (or `` Ctrl+` `` / `` Cmd+` ``).
2. Make sure you’re in the project folder (you should see `project_phyton` in the path).
3. Run one of these:

**On Mac (if `python` doesn’t work, use `python3`):**
```bash
python3 hello.py
```

**Or after activating the venv (you’ll see `(venv)` in the line):**
```bash
source venv/bin/activate
python hello.py
```

**On Windows:**
```bash
python hello.py
```

You’ll see the program’s output in the same terminal.

---

## 3. Interactive mode (try one line at a time)

Good for: testing a single line or a small idea without saving a file.

1. Open Terminal.
2. Type:
   ```bash
   python3
   ```
   (or `python` if that works on your computer)
3. You’ll see something like `>>>`. That means Python is waiting for your code.
4. Type a line and press Enter. For example:
   ```python
   >>> print("Hi!")
   Hi!
   >>> 2 + 3
   5
   ```
5. To exit, type `exit()` and press Enter.

---

## Quick reference

| What you want to do              | Use this                          |
|----------------------------------|-----------------------------------|
| Run the file I have open         | **▶ Run** button (or right‑click → Run Python File) |
| Run a file from terminal         | `python3 hello.py` (Mac) or `python hello.py` (Windows) |
| Try one line without a file      | Terminal: `python3` then type code |

If **`python`** says "command not found", use **`python3`** instead (common on Mac).
