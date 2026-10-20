# Module Use-Cases

## 1. Modules, Packages, and Libraries

Modules, packages, and libraries help organise Python code and make it easier to reuse functionality across projects.

### Modules

A **module** is a Python file that can contain functions, classes, variables, and executable statements.

Example:

```text
math_operations.py
```

You can import and use a module in another Python file.

```python
import math_operations
```

### Packages

A **package** is a module that provides a way to organise related modules and sub-packages.

Packages are commonly organised as directories containing Python files and other packages. Traditional packages often contain an `__init__.py` file, although Python also supports namespace packages without one.

Example:

```text
my_package/
├── __init__.py
├── calculations.py
└── helpers.py
```

### Libraries

A **library** is a collection of reusable code that provides functionality for specific tasks. A library may contain multiple modules and packages.

Examples include libraries for working with HTTP requests, data analysis, and visualisation.

### Comparison

| Term | Description | Example |
|---|---|---|
| Module | A unit of Python code, commonly a `.py` file | `math_operations.py` |
| Package | A module that organises related modules and sub-packages | `my_package/` |
| Library | A collection of reusable functionality | Requests, Matplotlib |

Modules and packages can be imported using Python's import system.

## 2. Installing Third-Party Packages With `pip`

Python includes a **standard library** containing built-in modules and packages. Additional functionality can be installed from external sources.

**`pip`** is Python's package installer. It is commonly used to install third-party packages from the Python Package Index (PyPI).

Website: https://pypi.org/

You can install packages using:
- Your operating system's terminal or command line.
- The integrated terminal in an IDE, such as VS Code.

Make sure you install packages into the same Python environment or interpreter that you use to run your code.

### Checking or Installing `pip`

**Windows:**

```bash
py -m ensurepip --upgrade
```

**macOS/Linux:**

```bash
python3 -m ensurepip --upgrade
```

These commands ensure that `pip` is available when supported by your Python installation.

## 3. Installing a Third-Party Package

For example, to install the `requests` package:

**Windows:**

```bash
py -m pip install requests
```

**macOS/Linux:**

```bash
python3 -m pip install requests
```

Once installed, you can import the package into your Python code.

```python
import requests

response = requests.get("https://example.com")
print(response.status_code)
```

This example sends an HTTP GET request and prints the response status code.

### Important Notes

- Package names and commands must be entered correctly. Package names on PyPI are generally case-insensitive, although Python import names can be case-sensitive.
- Packages are installed into a particular Python environment, not automatically into every interpreter on your machine.
- You normally only need to install a package once per environment, unless you uninstall it or create another environment.
- Read the package documentation to understand its functions, classes, parameters, and usage.
- Check PyPI, the project's official website, and its GitHub repository for documentation and examples.

## 4. Sub-Packages

A **sub-package** is a package contained within another package.

Packages can contain sub-packages, just as directories can contain other directories.

Python uses **dot notation** to refer to modules and sub-packages within a package.

For example, Matplotlib provides a submodule named `pyplot`.

### Importing a Submodule

```python
import matplotlib.pyplot
```

You can then access its functions using the full module name.

```python
matplotlib.pyplot.plot([1, 2, 3], [4, 5, 6])
```

### Importing With an Alias

An alias gives an imported module a shorter name.

```python
import matplotlib.pyplot as plt
```

You can now use the shorter alias:

```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
```

**`plt`** is the conventional alias for `matplotlib.pyplot`. Using familiar aliases makes code easier for other Python developers to understand.

## 5. Exploring Package Structure

To understand how a package works, you can:

1. Read its official documentation.
2. Explore its modules and sub-packages.
3. Look at code examples and tutorials.
4. Inspect its source code on GitHub.
5. Review its module index or API reference.

Documentation explains how to use the package's available functions, classes, and attributes.

## Key Takeaways

- A **module** is a unit of Python code, commonly stored in a `.py` file.
- A **package** organizes related modules and sub-packages.
- A **library** is a collection of reusable functionality.
- `pip` installs third-party packages into a Python environment.
- **PyPI** is the Python Package Index, where many third-party packages are published.
- Use `importlib` and Python's import system to work with modules.
- **Sub-packages** are packages contained within other packages.
- **Dot notation** accesses modules and sub-packages, while **aliases** provide shorter names.
- Always consult official documentation when learning a new package.