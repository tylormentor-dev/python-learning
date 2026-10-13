#Exercise

class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c


print(dir(A))
print("Instantiating A..")
a = A(1)
print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a

   print(a.alpha())
   d = 5
   print(d)
   print(a)

print("Instantiating B..")
b = B(a)
print(a)

# Python OOP Exercise: Classes, Objects, Methods and Execution Order

## 1. Learning Objectives

By the end of this exercise, I should understand:

- Classes and objects
- Object instantiation
- The `__init__()` constructor method
- The `self` parameter
- Class attributes versus instance attributes
- Class-body execution versus method execution
- Local variables and object attributes
- The `dir()` function
- Returning values from methods
- Passing one object into another class
- The `NameError` exception
- How Python executes code from top to bottom


## 2. Classes and Objects

### What is a class?

A class is a blueprint for creating objects. It defines the attributes and methods that objects can have.

Example:

```python
class A:
    pass
```

This defines a class called `A`. The `pass` keyword means that the class body is intentionally empty.

### What is an object?

An object is an instance of a class.

```python
a = A()
```

Here:
- `A` is the class.
- `a` is a variable referring to the object.
- `A()` creates an instance of class `A`.

**Remember:** Defining a class does not automatically create an instance of that class.

---

## 3. The `__init__()` Method

The `__init__()` method is a special method that Python calls automatically when an instance is initialized.

Example:

```python
class A:
    def __init__(self, c):
        self.c = c

a = A(1)
```

When `A(1)` is executed:

1. Python creates an instance of `A`.
2. The argument `1` is passed to the parameter `c`.
3. `self` refers to the new instance.
4. `self.c = c` stores the value `1` in the object's attribute `c`.

The object's attribute can be accessed with:

```python
print(a.c)
```

Output:

```text
1
```

### What is `self`?

`self` refers to the particular instance on which an instance method is operating.

For example:

```python
self.c = c
```

means that the value of the parameter `c` is stored in the current object's attribute `c`.

`self` is a conventional parameter name in Python instance methods.

---

## 4. Class Body Versus Method Body

Consider this example:

```python
class A:
    print("Print inside A.")

    def __init__(self, c):
        print("Inside the constructor")
        self.c = c

print("Before creating an object")
a = A(1)
```

Output:

```text
Print inside A.
Before creating an object
Inside the constructor
```

### Why does this happen?

Python executes the class body when it reaches the class definition.

Therefore:

```python
print("Print inside A.")
```

runs immediately while the class is being defined.

However:

```python
def __init__(self, c):
    print("Inside the constructor")
    self.c = c
```

defines a method. The method body runs when an instance is initialized.

### Important rule

- Statements directly inside a class body execute during class definition.
- Statements inside a method execute when that method is called.

Defining a method does not execute its body.

---

## 5. Understanding the `alpha()` Method

Consider the following code:

```python
class A:
    def __init__(self, c):
        self.c = c

    def alpha(self):
        c = self.c + 1
        return c

a = A(1)

print(a.alpha())
print(a.c)
```

Output:

```text
2
1
```

### Step-by-step explanation

When this line executes:

```python
a = A(1)
```

the object stores:

```python
a.c = 1
```

Next:

```python
print(a.alpha())
```

calls the `alpha()` method.

Inside the method:

```python
c = self.c + 1
```

Python calculates:

```text
1 + 1 = 2
```

The result is stored in a local variable called `c`.

Then:

```python
return c
```

returns `2` to the caller, and `print()` displays it.

However, the object's attribute remains `1`.

### Why doesn't `a.c` change?

Because the method uses:

```python
c = self.c + 1
```

instead of:

```python
self.c = self.c + 1
```

- The first statement assigns a value to a local variable. - The second statement updates the object's attribute.

### Modified version that changes the object

```python
def alpha(self):
    self.c = self.c + 1
    return self.c
```

Now each call increases the object's stored value by one.

Example:

```python
a = A(1)

print(a.alpha())
print(a.alpha())
print(a.c)
```

Output:

```text
2
3
3
```

---

## 6. Understanding `dir()`

The `dir()` function returns a list of names associated with an object.

Example:

```python
class A:
    def alpha(self):
        return 2

print(dir(A))
```

The output includes many built-in names, such as:

```text
__class__
__dict__
__init__
__module__
alpha
```

The precise list can vary by Python version and class configuration.

The name `alpha` appears because it is a method defined in class `A`.

Compare:

```python
dir(A)
```

with:

```python
dir(a)
```

The first inspects the class. The second inspects a particular instance.

---

## 7. Class Attributes Versus Instance Attributes

Example:

```python
class B:
    bravo = 5

b = B()
b.bravo = 3

print(B.bravo)
print(b.bravo)
```

Output:

```text
5
3
```

### Explanation

`bravo = 5` is a class attribute.

It belongs to the class and can be accessed using:

```python
B.bravo
```

When an instance is created, it can access that attribute if it does not have an instance attribute with the same name.

However:

```python
b.bravo = 3
```

creates an instance attribute that shadows the class attribute when accessed through `b`.

Therefore:

- `B.bravo` is `5`.
- `b.bravo` is `3`.

The class attribute has not been changed.

---

## 8. Understanding Class B in the Main Exercise

The main exercise contains:

```python
class B:
    def __init__(self, a):
        print("---------Inside class B----------")
        self.a = a

    print(a.alpha())
    d = 5
    print(d)
    print(a)
```

The statements below are directly inside the class body:

```python
print(a.alpha())
d = 5
print(d)
print(a)
```

They execute while Python defines class `B`, not when an instance of `B` is created.

### Why does `print(a.alpha())` work?

It works if a variable named `a` already refers to an object that has an `alpha()` method.

For example:

```python
a = A(1)

class B:
    print(a.alpha())
```

Since `a` already exists, Python can call its method.

If `a` has not been defined, Python raises:

```text
NameError: name 'a' is not defined
```

### Why does `print(d)` output 5?

Python first executes:

```python
d = 5
```

Then it executes:

```python
print(d)
```

Therefore, the output is:

```text
5
```

The instance of `B` does not need to exist for these class-body statements to execute.

---

## 9. Passing One Object into Another Class

Consider:

```python
class B:
    def __init__(self, a):
        self.a = a

b = B(a)
```

The existing object `a` is passed into the constructor of `B`.

Inside `__init__()`:

```python
self.a = a
```

stores a reference to that existing object on the new `B` instance.

You can then access it through:

```python
b.a
```

For example:

```python
print(b.a.c)
```

If `a.c` is `1`, the output is:

```text
1
```

**Important:** Passing an object into another class does not automatically create a new object of the original class. Both references can refer to the same object.

---

## 10. Understanding `print(a)`

When you write:

```python
print(a)
```

Python normally displays the object's default representation if the class has not defined a custom string representation.

Example:

```text
<__main__.A object at 0x...>
```

The exact text and memory address-like value can vary.

This representation identifies the object's class and provides implementation-specific information.

To print a particular attribute instead, use:

```python
print(a.c)
```

---

## 11. Understanding `NameError`

A `NameError` occurs when Python tries to use a name that cannot be resolved in the current scope.

Example:

```python
print(a)
```

If `a` has not been defined, Python raises:

```text
NameError: name 'a' is not defined
```

Compare this with:

```python
class B:
    def __init__(self, a):
        self.a = a
```

This class can be defined without a global variable named `a`.

Why? Because `a` is a parameter. It receives its value when the method is called.

Example:

```python
b = B(some_object)
```

Here, `some_object` must exist when the call executes, but the parameter name `a` does not need to exist globally.

---

## 12. Execution Order of the Main Exercise

The original program executes in this general order:

1. Python reaches the definition of class `A`.
2. Python executes the class-body statement `print("Print inside A.")`.
3. Python defines `__init__()` and `alpha()` without executing their method bodies.
4. `dir(A)` prints the names associated with class `A`.
5. The message `Instantiating A..` is printed.
6. `a = A(1)` creates and initializes object `a`.
7. The constructor prints its message and stores `a.c = 1`.
8. `a.alpha()` calculates and returns `2`.
9. Python reaches the definition of class `B`.
10. `print(a.alpha())` executes and prints `2`.
11. Python assigns `d = 5` and prints `5`.
12. `print(a)` displays the representation of object `a`.
13. The message `Instantiating B..` is printed.
14. `b = B(a)` creates object `b` and calls its constructor.
15. The constructor prints its message and stores a reference to object `a`.
16. The final `print(a)` displays the same object representation as before.

The exact execution order depends on which statements are commented out and whether the required variables have already been defined.

---

## 13. Common Mistakes and Corrections

| Mistake | Correction |
|---|---|
| Assuming a class-body `print()` waits for object creation | It runs during class definition |
| Assuming defining a method executes it | A method body runs when called |
| Assuming `c = self.c + 1` updates `self.c` | It assigns the result to a local variable |
| Assuming `b = B(a)` creates a new `A` object | It passes the existing `a` object to `B` |
| Assuming `print(a)` displays all attributes | Use `print(a.c)` to display a specific attribute |
| Using `a` before it exists | Define or receive the object before using it |
| Confusing class attributes and instance attributes | Use `ClassName.attribute` and `instance.attribute` to distinguish access |

---

## 14. Key Takeaways

1. A class is a blueprint; an object is an instance.
2. `__init__()` initializes an instance and receives arguments.
3. `self` refers to the current instance.
4. Class-body statements execute during class definition.
5. Method bodies execute when their methods are called.
6. `dir()` lists names associated with a class or object.
7. `return` sends a value back to the caller.
8. A local variable and an object attribute are not the same thing.
9. Passing an object to another class can create a reference to that same object.
10. `NameError` occurs when Python cannot resolve a name.
11. Python executes statements in order, and the placement of code matters.

---

## 15. Practice Questions

Try answering these without looking at the explanations above.

1. What is the difference between a class and an object?
2. When does Python execute a print statement directly inside a class?
3. When does Python execute the body of `__init__()`?
4. What does `self.c = c` do?
5. What is the difference between `c` and `self.c` inside `alpha()`?
6. Why does `a.alpha()` return `2` repeatedly in the original exercise?
7. What does `dir(A)` show?
8. Why can `print(a.alpha())` inside class `B` raise a `NameError`?
9. What does `self.a = a` do in class `B`?
10. How would you modify `alpha()` so that each call permanently increments the object's attribute?

**Revision goal:** Be able to explain the output of the original exercise line by line without running the code.


