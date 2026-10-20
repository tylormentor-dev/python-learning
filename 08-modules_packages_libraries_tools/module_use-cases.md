# Module Use-Cases

## Modules, Packages, and Libraries

Modules, packages, and libraries help organise Python code and make it easier to reuse functionality across projects.

### Modules

A module is a Python file that can contain functions, classes, variables, and executable statements.

Example: `math_operations.py`

Import a module using the `import` statement.

```python
import math_operations
```

### Packages

A package organises related modules and sub-packages. Packages are commonly structured as directories containing Python files and other packages.

Example:

```text
my_package/
├── __init__.py
├── calculations.py
└── helpers.py
```

Traditional packages usually contain an `__init__.py` file. Python also supports namespace packages without one.

### Libraries

A library is a collection of reusable code that provides functionality for specific tasks. A library can contain multiple modules and packages.

Examples include Requests for HTTP requests and Matplotlib for data visualization.

### Quick Comparison

| Term | Meaning 

| Module | A unit of Python code, commonly a `.py` file |
| Package | Organizes related modules and sub-packages |
| Library | A collection of reusable functionality |

## Installing Packages With pip

Python includes a standard library containing modules and packages that come with Python. You can install additional functionality using `pip`, Python's package installer.

Third-party packages are commonly published on the Python Package Index (PyPI).

Website: https://pypi.org/

You can install packages through your operating system's terminal, command line, or the integrated terminal in an IDE such as VS Code.

### Checking pip

On Windows, run:

```bash
py -m ensurepip --upgrade
```

On macOS or Linux, run:

```bash
python3 -m ensurepip --upgrade
```

These commands help ensure that pip is available for your Python installation.

### Installing a Package

For example, to install the `requests` package:

Windows:

```bash
py -m pip install requests
```

macOS or Linux:

```bash
python3 -m pip install requests
```

Once installed, you can import and use the package in your Python code.

```python
import requests

response = requests.get("https://example.com")
print(response.status_code)
```

This example sends an HTTP GET request and prints the response status code.

### Important Notes

- Install packages into the same Python environment used to run your code.
- Packages are installed per environment, so you may need to install them again in a different virtual environment.
- Package names on PyPI are generally case-insensitive, but Python import names can be case-sensitive.
- Read the package documentation to understand its functions, classes, and usage.

## Sub-Packages

A sub-package is a package contained within another package. Packages can contain other packages, similar to how directories contain subdirectories.

Python uses dot notation to access modules and sub-packages.

For example, Matplotlib includes a submodule called `pyplot`.

### Importing a Submodule

```python
import matplotlib.pyplot
```

You can access its functions using the full module name.

```python
matplotlib.pyplot.plot([1, 2, 3], [4, 5, 6])
```

### Importing With an Alias

An alias gives an imported module a shorter name.

```python
import matplotlib.pyplot as plt
```

You can then use `plt` to access its functions.

```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
```

`plt` is the conventional alias for `matplotlib.pyplot`. Using familiar aliases makes code easier to read.

## Exploring Packages

When learning a new package, you can:

1. Read the official documentation.
2. Explore its modules and sub-packages.
3. Review examples and tutorials.
4. Examine its source code on GitHub.
5. Refer to its API documentation or module index.

Documentation explains how to use the package's functions, classes, and attributes.

## Key Takeaways

- A module is a unit of Python code, commonly stored in a `.py` file.
- A package organizes related modules and sub-packages.
- A library is a collection of reusable functionality.
- `pip` installs third-party packages into a Python environment.
- PyPI hosts many Python packages.
- Dot notation accesses modules and sub-packages.
- Aliases provide shorter names for imported modules.
- Official documentation is a useful resource when learning a new package.