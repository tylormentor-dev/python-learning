# Reloading Modules in Python

## 1. What Is `reload()`?

The `reload()` function allows you to re-execute a module that has already been imported in Python.

Python normally imports a module once per interpreter session and reuses the cached module when the same module is imported again. If the module's source code changes, importing it again does not automatically execute the updated code.

The `reload()` function is available from the `importlib` module.

```python
import importlib

importlib.reload(module_name)
```

**Important:** The module must already have been successfully imported before it can be reloaded.

## 2. Importing a Module Multiple Times

Suppose you create a file named `sample.py`:

```python
print("Hello world")
```

You then create another file named `reloads.py`:

```python
import sample
import sample
import sample
```

**Output:**

```text
Hello world
```

Although `sample` is imported three times, its top-level code normally executes only once during that interpreter session.

## 3. Reloading a Module With `importlib.reload()`

To execute the module's code again, use `importlib.reload()`.

```python
import importlib
import sample

importlib.reload(sample)
importlib.reload(sample)
```

**Output:**

```text
Hello world
Hello world
Hello world
```

The message appears three times: once during the initial import and twice during the reloads.

## 4. Using `reload()` to Detect File Changes

The `reload()` function can be useful when a program needs to re-execute a module after its source code has changed.

For example, suppose you have two files:

```text
project/
├── reloads.py
└── filechanges.py
```

### Step 1: Create `filechanges.py`

Use the `os` module to list the files in a directory.

```python
import os

contents = os.listdir(r"C:\path\to\your\directory")

def show_contents():
    print("Directory contents:")
    print(contents)
```

Replace the example path with the directory you want to inspect. The `r` prefix creates a raw string, which is useful for Windows paths.

### Step 2: Create `reloads.py`

```python
import importlib
import filechanges

def changes():
    try:
        importlib.reload(filechanges)
        filechanges.show_contents()
    except Exception as error:
        print("Error:", error)

for _ in range(5):
    input("Press Enter to refresh...")
    changes()
```

Each time you press Enter, the program reloads `filechanges` and calls `show_contents()`.

### Step 3: Observe the Changes

While the program is running, try the following:

1. Add a text file to the directory.
2. Press Enter to refresh the module.
3. Delete a text file.
4. Press Enter again.
5. Change the print statement inside `filechanges.py` and reload it.

The reloaded module's code will execute again, allowing changes to its source code to take effect.

**Note:** This example captures the directory listing when `filechanges.py` is executed. Reloading it refreshes the `contents` variable. If the directory changes without reloading the module, the variable will not automatically update.

## 5. Important Considerations

- `importlib.reload()` requires an already imported module object.
- Reloading re-executes the module's code, including its top-level statements.
- Reloading does not automatically update every reference to objects imported using `from module import name`.
- Existing instances of classes are not automatically recreated when their class definitions are reloaded.
- Reloading a module does not restart the Python interpreter.
- Use `importlib.reload()` carefully in production code because re-executing module-level code can have side effects.

## Key Takeaways

- Python normally executes a module's code only on its initial import within an interpreter session.
- Repeating an `import` statement does not normally execute the module again.
- `importlib.reload(module)` re-executes an already imported module.
- Reloading can help during development when testing changes to module code.
- The `os.listdir()` function returns the names of files and directories in a specified directory.
- Reloading a module refreshes its code and module-level variables, but does not automatically refresh every existing reference to its objects.