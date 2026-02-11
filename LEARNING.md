# Python from zero — beginner guide

You don’t need any coding experience. We’ll go step by step.

---

## How to use this guide

- Read one section at a time.
- Type the examples yourself (don’t just copy-paste at first).
- Run the code and see what happens.
- Change something small and run again.

**To run a file:** Click the **▶ Run** button with the file open, or in the terminal: `python3 filename.py` (Mac) or `python filename.py` (Windows).  
**To try code line by line:** In the terminal run `python3` (or `python`), then type code and press Enter.  
**More details:** See **HOW_TO_RUN_CODE.md**.

---

## Lesson 1: Your first program

Python runs the instructions you write, one after another.

Create a file named `hello.py` with this single line:

```python
print("Hello, world!")
```

Run it: open `hello.py` and click **▶ Run**, or in the terminal run `python3 hello.py` (Mac) or `python hello.py` (Windows).

You should see: `Hello, world!`

- `print(...)` means “show this on the screen”.
- The quotes `"..."` mean it’s text (a **string**).

**Try:** Change the text inside the quotes and run again.

---

## Lesson 2: Variables — giving names to values

A **variable** is a name that holds a value. You can reuse it.

```python
name = "Alex"
print("Hi,", name)

age = 10
print("You are", age, "years old")
```

- `name` and `age` are variable names.
- `=` means “store this value in this name” (assignment).

**Try:** Create variables for your favorite color and number, then print them.

---

## Lesson 3: Getting input from the user

You can ask the user to type something:

```python
your_name = input("What is your name? ")
print("Nice to meet you,", your_name)
```

- `input("...")` shows a message and waits for the user to type and press Enter.
- What they type is stored in `your_name`.

**Try:** Ask for their favorite food and print a sentence using it.

---

## Lesson 4: Numbers and simple math

Python can do math. You don’t use quotes for numbers.

```python
a = 5
b = 3
print("Sum:", a + b)      # 8
print("Difference:", a - b)  # 2
print("Product:", a * b)   # 15
print("Division:", a / b)  # 1.666...
```

- `+` add, `-` subtract, `*` multiply, `/` divide.
- `#` starts a comment — Python ignores it; it’s for you.

**Try:** Use variables for two numbers and print their sum and product.

---

## Lesson 5: Types of data

Values have **types**:

- **String** — text in quotes: `"hello"`
- **Integer** — whole number: `42`
- **Float** — decimal number: `3.14`

`input()` always gives you a string. To do math with it, convert:

```python
age_text = input("How old are you? ")
age = int(age_text)   # convert to integer
next_year = age + 1
print("Next year you'll be", next_year)
```

- `int(...)` converts to a whole number.
- `float(...)` converts to a decimal number.

**Try:** Ask for a number, convert it, and print its double.

---

## Lesson 6: Making decisions with `if`

Programs can choose what to do based on conditions:

```python
age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")
```

- `if condition:` — if the condition is true, run the block below.
- The block is everything **indented** (usually 4 spaces). Indentation matters in Python.
- `else:` — run this block when the condition is false.

Comparison operators: `==` equal, `!=` not equal, `>`, `<`, `>=`, `<=`.

**Try:** Ask for a number; if it’s positive, print “Positive”, else print “Negative or zero”.

---

## Lesson 7: Repeating with `for` loops

A **loop** runs the same code several times.

```python
for i in range(5):
    print("Step", i)
```

- `range(5)` gives 0, 1, 2, 3, 4.
- The indented line runs once for each value.

Loop over a list of items:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)
```

**Try:** Use a loop to print “Hello” three times. Then loop over a list of your favorite things.

---

## Lesson 8: Lists — storing many values

A **list** holds multiple values in order:

```python
colors = ["red", "green", "blue"]
print(colors[0])   # first item: "red"
print(colors[1])   # second: "green"
print(len(colors)) # length: 3

colors.append("yellow")  # add at the end
print(colors)
```

- Indexes start at 0: first item is `[0]`, second is `[1]`.
- `len(list)` is the number of items.
- `list.append(x)` adds `x` to the end.

**Try:** Make a list of 3 names, print the second one, then append a fourth name.

---

## Lesson 9: Repeating with `while`

`while` repeats as long as a condition is true:

```python
count = 0
while count < 3:
    print("Count is", count)
    count = count + 1
print("Done!")
```

**Try:** Ask the user for a number; use a `while` loop to count from 0 up to that number.

---

## Lesson 10: Functions — reusable blocks of code

A **function** is a named block you can run whenever you need it:

```python
def say_hello(name):
    print("Hello,", name, "!")

say_hello("Sam")
say_hello("Jamie")
```

Functions can **return** a value:

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # 5
```

- `def function_name(parameters):` defines the function.
- `return` sends a value back to whoever called the function.

**Try:** Write a function that takes a name and returns a greeting string, then print it.

---

## Mini project ideas

After you finish the lessons, try:

1. **Guessing game:** Pick a secret number; user guesses until they get it (use `if` and `while`).
2. **Shopping list:** Ask for items in a loop, store in a list, then print the list.
3. **Simple quiz:** Ask 2–3 questions, check answers with `if`, and print a score.

---

## Cheat sheet

| Concept      | Example |
|-------------|---------|
| Print       | `print("text")` or `print(x)` |
| Variable    | `name = "Alex"` |
| Input       | `x = input("Prompt: ")` |
| Convert     | `int("42")`, `float("3.14")` |
| If/else     | `if x > 0:` ... `else:` ... |
| For loop    | `for i in range(5):` or `for x in my_list:` |
| While loop  | `while condition:` |
| List        | `items = [1, 2, 3]`, `items[0]`, `items.append(4)` |
| Function    | `def name(a, b):` ... `return result` |

---

## What’s next?

- Practice by changing the examples in the **examples/** folder.
- Search for “Python tutorial for beginners” for more exercises.
- When you’re comfortable, try a small project (e.g. a to-do list in the terminal).

Good luck and have fun.
