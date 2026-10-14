# Method Resolution Order (MRO) in Python

## 1. What is Method Resolution Order?

**Method Resolution Order (MRO)** is the order Python follows when searching for a method or attribute in a class and its inheritance hierarchy.

MRO determines **which class Python checks first** when multiple classes could provide the same method or attribute.

### Why is MRO important?
- Helps Python resolve methods and attributes when classes use inheritance.
- Makes multiple inheritance predictable.
- Helps developers understand which implementation Python will use.

## 2. Types of Inheritance

There are five commonly discussed types of inheritance:

| Type | Description |
|---|---|
| **Simple inheritance** | A child class inherits from one parent class. |
| **Multiple inheritance** | A child class inherits from more than one parent class. |
| **Multilevel inheritance** | Inheritance occurs across several levels. |
| **Hierarchical inheritance** | Multiple child classes inherit from the same parent class. |
| **Hybrid inheritance** | A combination of two or more inheritance types. |

## 3. How MRO Works

Python generally searches:
1. The class of the object first.
2. Its parent classes according to the MRO.
3. Further ancestors in the calculated order.

This is especially important when several classes define a method or attribute with the same name.

### Example 1: Single inheritance

```python
class A:
    def greet(self):
        print("Hello from A")


class B(A):
    pass


obj = B()
obj.greet()
```

**Output:**
```text
Hello from A
```

Python checks `B` first. Since `B` does not define `greet()`, Python checks its parent, `A`.

The MRO is:

```python
print(B.mro())
```

Simplified output:

```text
[B, A, object]
```

`object` is the built-in base class at the top of most Python class hierarchies.

## 4. MRO and Multiple Inheritance

Multiple inheritance occurs when a class inherits from more than one parent.

```python
class X:
    def show(self):
        print("X")


class Y:
    def show(self):
        print("Y")


class Z(X, Y):
    pass


obj = Z()
obj.show()
```

**Output:**
```text
X
```

Python searches `Z` first, then `X`, then `Y`, then `object`.

```python
print(Z.mro())
```

Output:

```text
[Z, X, Y, object]
```

**Important:** Python normally follows the order of the parent classes as listed in the class definition, subject to its MRO rules. Therefore, `class Z(X, Y)` and `class Z(Y, X)` can produce different results.

## 5. Multilevel Inheritance and MRO

Multilevel inheritance occurs when a class inherits from a class that itself inherits from another class.

```python
class A:
    num = 5


class B(A):
    num = 9


class C(B):
    pass


print(C.num)
```

**Output:**
```text
9
```

Python checks `C` first, then `B`. It finds `num` in `B`, so it uses `9` rather than the value `5` defined in `A`.

The MRO is:

```python
print(C.mro())
```

Output:

```text
[C, B, A, object]
```

## 6. Linearization

**Linearization** is the process of arranging a class and its ancestors into a single, ordered sequence.

MRO is that sequence, which Python uses to decide where to find methods and attributes.

For example:

```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass
```

The linearized order for `C` is:

```text
C → B → A → object
```

## 7. The C3 Linearization Algorithm

Python 3 uses the **C3 linearization algorithm** to calculate MRO.

The algorithm helps ensure that:
- A class appears before its parent classes.
- The order of parent classes is respected.
- The inheritance order remains consistent across the hierarchy.
- Conflicting inheritance requirements are rejected rather than resolved arbitrarily.

If Python cannot construct a consistent MRO for a class, it raises a `TypeError` when the class is defined.

## 8. Useful Ways to Inspect MRO

### Method 1: `mro()`

Returns the MRO as a list.

```python
print(MyClass.mro())
```

### Method 2: `__mro__`

Returns the MRO as a tuple.

```python
print(MyClass.__mro__)
```

### Method 3: `help()`

Displays detailed information about a class, including its inheritance information and MRO.

```python
help(MyClass)
```

Use `mro()` or `__mro__` when you only need to inspect the resolution order. Use `help()` when you want broader class documentation.

## 9. Key Terms

- **MRO:** The order Python follows to search for methods and attributes.
- **Inheritance:** A mechanism that allows a class to reuse or extend another class's behavior.
- **Parent class:** The class being inherited from.
- **Child class:** The class that inherits from another class.
- **Multiple inheritance:** Inheriting from more than one parent class.
- **Linearization:** Arranging a class hierarchy into a single sequence.
- **C3 linearization:** The algorithm Python 3 uses to calculate the MRO.
- **Attribute:** Data or behavior associated with an object or class, such as a variable or method.

## 10. Quick Revision

- Python searches the current class before its ancestors.
- MRO determines which implementation is found first.
- Multiple inheritance makes MRO especially important.
- Parent classes are considered according to the calculated MRO, not simply by searching every class in an arbitrary order.
- `mro()` returns a list; `__mro__` returns a tuple.
- `help()` displays more detailed class information.
- Python 3 uses C3 linearization to calculate MRO.
