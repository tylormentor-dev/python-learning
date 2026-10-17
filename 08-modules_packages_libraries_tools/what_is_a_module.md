# What Is a Module in Python?

## 1. Definition of a Module

A **module** in Python is a file containing Python statements and definitions, such as variables and functions, that can be imported and reused in other Python programs.

Modules allow developers to add functionality to their code without having to write everything from scratch.

For example, a file named `sample.py` can be imported as a module named `sample`.

### Example

Suppose you have a Python file named `greetings.py`:

```python
def say_hello():
    print("Hello, world!")
```

You can import and use this function in another Python file:

```python
import greetings

greetings.say_hello()
```

**Output:**

```text
Hello, world!
```

The `greetings` module allows you to reuse the `say_hello()` function in another file.

## 2. What Is Modular Programming?

**Modular programming** is the practice of dividing a program into smaller, separate parts, with each part responsible for a particular purpose.

Instead of writing an entire program in one large file, you can organize its functionality into modules.

For example, a project could have separate modules for:

- Authentication
- Data processing
- File management
- Calculations

This makes code easier to organize, understand, maintain, and reuse.

## 3. Advantages of Modules

### 3.1 Scope and Namespaces

A **namespace** is a mapping between names and the objects they refer to.

Modules provide separate namespaces, which help prevent naming conflicts between variables and functions in different modules.

For example, two modules can each contain a function named `calculate()`.

```python
# math_tools.py
def calculate():
    print("Mathematical calculation")
```

```python
# finance_tools.py
def calculate():
    print("Financial calculation")
```

You can access each function through its module:

```python
import math_tools
import finance_tools

math_tools.calculate()
finance_tools.calculate()
```

Each function can be accessed without needing to rename it.

### 3.2 Reusability

Modules allow you to reuse existing code instead of rewriting the same functionality.

For example, Python provides the built-in `math` module, which includes functions for mathematical operations.

```python
import math

print(math.factorial(5))
print(math.gcd(12, 18))
```

**Output:**

```text
120
6
```

- `math.factorial(5)` calculates the factorial of 5.
- `math.gcd(12, 18)` calculates the greatest common divisor of 12 and 18.

### 3.3 Simplicity

Modules help keep programs organized by separating functionality into smaller, focused components.

When modules have clearly defined responsibilities and limited dependencies on one another, the overall program becomes easier to understand and maintain.

For example, the `re` module provides tools for working with regular expressions, while `matplotlib` provides tools for data visualization.

## 4. Types of Python Modules

The lesson introduces built-in modules and discusses how modules provide different functionality.

### 4.1 Built-in and Standard Library Modules

Python includes a standard library containing modules that provide commonly needed functionality.

Examples include:

| Module | Purpose |
|---|---|
| `math` | Mathematical operations. |
| `re` | Working with regular expressions. |
| `os` | Interacting with operating-system functionality. |

Example:

```python
import math

print(math.sqrt(25))
```

**Output:**

```text
5.0
```

The `import` statement makes the module available for use in your program.

### 4.2 Third-Party Modules

Python developers can install additional modules created by other developers and organizations.

For example, `matplotlib` is commonly used for creating charts and visualizations.

```python
import matplotlib
```

Third-party packages may need to be installed before they can be imported.

### 4.3 User-Defined Modules

You can create your own modules by writing Python code in a `.py` file.

For example:

```text
project/
├── main.py
└── calculations.py
```

In `calculations.py`:

```python
def add(a, b):
    return a + b
```

In `main.py`:

```python
import calculations

result = calculations.add(5, 3)

print(result)
```

**Output:**

```text
8
```

The `calculations.py` file is your own module, which can be imported into `main.py`.

## 5. Importing Modules

The `import` statement allows you to use functionality defined in another module.

### Import an Entire Module

```python
import math

print(math.sqrt(16))
```

**Output:**

```text
4.0
```

### Import a Specific Function

You can import a particular function from a module.

```python
from math import factorial

print(factorial(5))
```

**Output:**

```text
120
```

In this example, you can call `factorial()` directly without writing `math.factorial()`.

### Import a Module Using an Alias

You can assign a shorter name to a module using `as`.

```python
import math as m

print(m.sqrt(36))
```

**Output:**

```text
6.0
```

The alias `m` is used to access the module.

## 6. How Module Execution Works

When Python imports a module, it executes the module's top-level statements the first time that module is loaded during a normal interpreter session.

For example, consider a file named `example.py`:

```python
print("Module loaded")

def greet():
    print("Hello!")
```

When another file imports it:

```python
import example

example.greet()
```

**Output:**

```text
Module loaded
Hello!
```

The `print("Module loaded")` statement runs during import. The `greet()` function is defined during import but its body runs only when the function is called.

Python normally caches imported modules in `sys.modules`, so importing the same module again in the same interpreter session does not ordinarily execute its top-level code again.

## 7. Where Should Import Statements Go?

Import statements are conventionally placed at the beginning of a Python file.

Example:

```python
import math

def calculate_area(radius):
    return math.pi * radius ** 2

print(calculate_area(5))
```

This makes dependencies clear and easy to find.

Python also allows imports inside functions when there is a specific reason to do so. In that case, the import statement executes when the function reaches it, although an already loaded module is normally retrieved from the import cache.

## 8. Key Takeaways

- A module is a Python file containing statements and definitions.
- Modules allow code to be organized into smaller, reusable components.
- Namespaces help distinguish functions and variables belonging to different modules.
- Python provides standard library modules such as `math` and `re`.
- Third-party modules can add functionality beyond the standard library.
- You can create your own modules using `.py` files.
- Use `import` to make modules available to your program.
- Top-level statements execute during the module's initial import, while function bodies execute when called.
- Imports are conventionally placed at the beginning of a file.

## 9. Practice Exercise

Create a small project with two Python files.

**File structure:**

```text
python-modules/
├── main.py
└── calculator.py
```

**Tasks:**

- [ ] Create a function called `add(a, b)` inside `calculator.py`.
- [ ] Create a function called `multiply(a, b)` inside `calculator.py`.
- [ ] Import `calculator` into `main.py`.
- [ ] Call both functions from `main.py`.
- [ ] Print their results.
- [ ] Experiment with importing a specific function using `from calculator import add`.

**Goal:** Understand how modules allow you to organize Python code and reuse functions across different files.