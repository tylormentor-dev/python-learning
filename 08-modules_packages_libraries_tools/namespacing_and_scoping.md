# Namespacing and Scoping

## 1. What Is a Namespace?

A **namespace** is a mapping between names and objects in Python. It keeps track of the names used in a program and the objects they refer to.

- A variable name refers to an object.
- A dictionary-like structure is used to represent a namespace.
- Every Python module has its own namespace containing its attributes, functions, classes, and variables.
- Namespaces help prevent naming conflicts.

## 2. What Is a Scope?

A **scope** is the region of a program where a name can be accessed directly.

Python has four main scopes, which follow the **LEGB rule** when resolving variable names.

| Scope | Description |
|---|---|
| **L — Local** | Names defined inside the current function. |
| **E — Enclosed** | Names defined in an enclosing function, usually when functions are nested. |
| **G — Global** | Names defined at the module level, outside functions and classes. |
| **B — Built-in** | Names provided by Python, such as `print()`, `len()`, and `id()`. |

Python searches for a name in this order: **Local → Enclosed → Global → Built-in**.

This process is called **scope resolution**.

## 3. Local and Global Variables

### Local Variables

A local variable is defined inside a function and is normally accessible only within that function.

```python
def greet():
    message = "Hello"
    print(message)

greet()
```

**Output:**

```text
Hello
```

The variable `message` is local to `greet()`.

### Global Variables

A global variable is defined at the module level, outside functions.

```python
country = "South Africa"

def show_country():
    print(country)

show_country()
print(country)
```

**Output:**

```text
South Africa
South Africa
```

The function can read the global variable because no local variable named `country` overrides it.

> A variable defined at the module level is global to that module, but it is not automatically global across every module in a project.

## 4. Variables With the Same Name

Different scopes can contain variables with the same name. These names can refer to different objects.

```python
animal = "camel"

def show_animal():
    animal = "elephant"
    print("Local:", animal)

show_animal()
print("Global:", animal)
```

**Output:**

```text
Local: elephant
Global: camel
```

The local variable `animal` does not change the global variable with the same name.

Python variables are created through assignment rather than explicit type declarations. Their scope depends on where they are bound and how the name is used.

## 5. The `locals()` and `globals()` Functions

Python provides two built-in functions for inspecting namespaces.

- `locals()` returns a mapping of the current local namespace.
- `globals()` returns a dictionary representing the current module's global namespace.

```python
country = "South Africa"

def show_variables():
    city = "Cape Town"

    print(locals())
    print(globals())

show_variables()
```

The local namespace contains `city`, while the global namespace contains `country` and other module-level names.

The output of `globals()` can be large because it also includes names Python creates for the module.

## 6. The `global` Keyword

The `global` keyword allows a function to reassign a variable defined at the module level.

```python
animal = "camel"

def change_animal():
    global animal
    animal = "giraffe"

change_animal()
print(animal)
```

**Output:**

```text
giraffe
```

Without `global`, assigning to `animal` inside the function would normally create a local binding instead.

Use `global` sparingly. Excessive reliance on global variables can make programs harder to understand, test, debug, and maintain.

## 7. The `nonlocal` Keyword

The `nonlocal` keyword allows a nested function to reassign a variable in its nearest enclosing function scope.

The variable must already be bound in an enclosing function scope. It cannot refer to a global variable.

```python
def outer():
    animal = "elephant"

    def inner():
        nonlocal animal
        animal = "giraffe"
        print("Inside inner:", animal)

    inner()
    print("Inside outer:", animal)

outer()
```

**Output:**

```text
Inside inner: giraffe
Inside outer: giraffe
```

The nested function changes the variable belonging to `outer()`, so the updated value remains available after `inner()` finishes.

### Global vs. Nonlocal

| Keyword | Purpose |
|---|---|
| `global` | Reassigns a variable in the module-level namespace. |
| `nonlocal` | Reassigns a variable in an enclosing function's scope. |

## 8. Practical Example: Animal Farm

This example demonstrates global, local, and enclosed variables working together.

```python
animal = "camel"

def d():
    animal = "elephant"

    def e():
        nonlocal animal
        animal = "giraffe"
        print("Inside nested function:", animal)

    print("Before nested function:", animal)
    e()
    print("After nested function:", animal)

d()
print("Global animal:", animal)
```

**Output:**

```text
Before nested function: elephant
Inside nested function: giraffe
After nested function: giraffe
Global animal: camel
```

### Explanation

1. The global variable `animal` is assigned `"camel"`.
2. Function `d()` creates a local variable `animal` with the value `"elephant"`.
3. Nested function `e()` uses `nonlocal` to refer to the variable inside `d()`.
4. The nested function changes that value to `"giraffe"`.
5. The updated value remains `"giraffe"` inside `d()`.
6. The global variable remains `"camel"` because the local and enclosed assignments do not modify it.

If the assignment `animal = "elephant"` is removed from `d()`, the `nonlocal animal` statement will raise a `SyntaxError` because there is no binding for `animal` in an enclosing function scope.

## 9. Best Practices

- Prefer local variables when possible.
- Use descriptive variable names to improve readability.
- Avoid unnecessary global variables because they introduce shared state.
- Use `nonlocal` when a nested function genuinely needs to update an enclosing variable.
- Remember that a module has its own namespace.
- Practise tracing variable assignments using the LEGB rule.

## Key Takeaways

- **Namespace:** A mapping between names and objects.
- **Scope:** The region where a name can be accessed directly.
- **LEGB:** Local, Enclosed, Global, Built-in.
- **`locals()`:** Inspects the current local namespace.
- **`globals()`:** Inspects the module-level namespace.
- **`global`:** Allows reassignment of a module-level variable.
- **`nonlocal`:** Allows reassignment of a variable in an enclosing function scope.
- **Scope resolution:** Python's process of searching for a name using the LEGB rule.