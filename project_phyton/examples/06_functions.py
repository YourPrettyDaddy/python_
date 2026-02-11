# Lesson 10 — Functions
# Run with: python examples/06_functions.py

def say_hello(name):
    print("Hello,", name, "!")

def add(a, b):
    return a + b

say_hello("Sam")
say_hello("Jamie")

result = add(2, 3)
print("2 + 3 =", result)
