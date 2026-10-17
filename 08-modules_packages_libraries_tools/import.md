# Import Statements in Python

## 1. What Is an Import Statement?

An `import` statement allows you to access code from another Python module. This lets you reuse functions, variables, and other code instead of rewriting them.

Every Python file with a `.py` extension can act as a module.

For example, if you have a file named `sample.py`, you can import it using:

```python
import sample
```

You do not include the `.py` extension when importing a module.

The main module is the file that serves as the starting point for your program.

## 2. Importing Files from the Current Directory

Python can import modules located in directories it searches for modules, including the current project directory in common setups.

Example project structure:

```text
project/
├── main.py
└── sample.py
```

Inside `main.py`, you can write:

```python
import sample
```

Python can then access code defined in `sample.py`.

A file that is not a Python module, such as `sample.txt`, cannot be imported using the normal Python module import statement.

## 3. Standard Library Modules

Python includes a standard library containing modules that provide built-in functionality. These modules generally do not need to be installed separately.

For example:

```python
import json

data = '{"name": "Adrian"}'
result = json.loads(data)

print(result["name"])
```

Output:

```text
Adrian
```

The `json` module provides functions for working with JSON data.

You can explore available modules in the [Python Standard Library documentation](https://docs.python.org/3/library/).

## 4. What Are Python Packages?

A package organizes related Python modules into a directory structure.

For example:

```text
project/
├── main.py
└── workplace/
    ├── __init__.py
    └── trial.py
```

The `__init__.py` file is commonly used to mark a directory as a regular Python package. Modern Python also supports namespace packages that do not require this file.

Packages help organize larger projects and make code easier to maintain.

## 5. Installing Third-Party Packages with pip

Python has a large collection of community-developed packages available through the Python Package Index (PyPI).

`pip` is a package installer that can install packages from PyPI.

For example, to install NumPy:

```bash
python -m pip install numpy
```

After installation, you can import it:

```python
import numpy
```

Another example is Seaborn, a library for statistical data visualization.

Install it using:

```bash
python -m pip install seaborn
```

Then import it:

```python
import seaborn
```

If a package is not installed in the Python environment you are using, the import may fail with a `ModuleNotFoundError`.

**Important:** Install packages in the same Python environment that runs your program.

## 6. Importing Modules from Another Directory

Python searches for modules using a list of locations stored in `sys.path`.

You can inspect these locations with:

```python
import sys

for location in sys.path:
    print(location)
```

The list can include locations such as the current working directory, standard library directories, and installed package directories. The exact contents depend on your Python environment and how you run the program.

### Adding a Directory to `sys.path`

Suppose your project has this structure:

```text
project/
├── main.py
└── workplace/
    └── trial.py
```

Inside `trial.py`, you have:

```python
names = ["Adrian", "Maria"]
```

If Python cannot find `trial.py` automatically, you can temporarily add its directory to the module search path:

```python
import sys

sys.path.insert(0, r"/path/to/project/workplace")

import trial

print(trial.names)
```

Output:

```text
['Adrian', 'Maria']
```

Replace `/path/to/project/workplace` with the actual path to your `workplace` directory.

### Understanding the Code

- `import sys` imports Python's system-specific functionality.
- `sys.path` contains the locations Python searches when importing modules.
- `sys.path.insert(0, ...)` adds a directory at the beginning of that list.
- The `r` before the path string creates a raw string, which is useful for Windows paths containing backslashes.
- `import trial` imports the module named `trial`.
- `trial.names` accesses the `names` variable defined inside `trial.py`.

**Note:** Changing `sys.path` affects the current Python process. It does not permanently configure your Python installation.

An IDE such as VS Code may still display an import warning even when Python can execute the import successfully, because the IDE's language analysis may not recognize the modified search path.

## 7. Best Practices for Imports

- Place import statements near the beginning of your Python file.
- Prefer importing modules from your current project structure when practical.
- Use packages to organize related modules as your project grows.
- Avoid modifying `sys.path` unnecessarily; it can make projects harder to maintain.
- Use a virtual environment for third-party dependencies in individual projects.
- Use clear, descriptive module and package names.

## Key Takeaways

- The `import` statement lets you reuse code from other modules.
- Python files ending in `.py` can act as modules.
- Python includes a standard library of modules.
- Third-party packages can be installed with `pip`.
- PyPI is a repository of Python packages.
- Packages help organize related modules.
- `sys.path` controls the locations Python searches for imports.
- Keeping your project organized makes importing modules easier.

## Practice Exercise

1. Create a file named `greetings.py`.
2. Inside it, define a variable called `message` with the value `"Hello, Python!"`.
3. Create another file named `main.py` in the same directory.
4. Import `greetings` into `main.py`.
5. Print `greetings.message`.
6. Install a third-party package, such as NumPy, and import it into a Python file.
7. Print the locations listed in `sys.path`.

**Expected output for step 5:**

```text
Hello, Python!
```
