# Abstract Classes and Methods

## 1. Learning Objectives

By the end of this lesson, I should understand:

- What abstraction means in Object-Oriented Programming (OOP)
- What an abstract class is
- What an abstract method is
- The difference between abstract classes and concrete classes
- How to use Python's `abc` module
- How to use `ABC` and `@abstractmethod`
- How inheritance and method overriding work with abstract classes
- Why abstract classes are useful
- How to implement an abstract class in a practical example

---

## 2. What Is Abstraction?

**Abstraction** is an OOP principle that hides unnecessary implementation details and exposes the essential functionality.

For example, when driving a car, I use the steering wheel, accelerator and brakes without needing to understand every detail of the engine's internal operation.

In programming, abstraction allows me to define what an object must be able to do without specifying every detail of how it does it.

### Why is abstraction useful?

- **Consistency:** Different classes follow the same required structure.
- **Interoperability:** Different objects can be used through a common interface.
- **Maintainability:** Changes to internal implementation can be made without changing how other code interacts with the object.
- **Code organization:** It separates required functionality from implementation details.

---

## 3. What Is an Abstract Class?

An **abstract class** is a class designed to act as a blueprint for other classes.

It cannot be instantiated directly when it contains unimplemented abstract methods.

For example, `Vehicle` could be an abstract class, with `Car`, `Boat` and `Tractor` as concrete subclasses.

Each subclass must implement the required abstract methods before its instances can be created.

Conceptually:

```text
Vehicle (abstract class)
    |
    |-- Car
    |-- Boat
    |-- Tractor
```

The abstract class defines the required interface. Each concrete subclass supplies its implementation.

### Example

A vehicle may need a method called `start_engine()`.

A car and a tractor could implement that method differently, but both must provide it if the abstract class requires it.

---

## 4. What Is an Abstract Method?

An **abstract method** is a method declared in an abstract class that requires concrete subclasses to provide an implementation.

In Python, abstract methods are commonly defined using the `@abstractmethod` decorator from the `abc` module.

Example:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass
```

### Explanation

- `from abc import ABC, abstractmethod` imports the necessary tools.
- `class Vehicle(ABC):` defines a class that uses Python's Abstract Base Class mechanism.
- `@abstractmethod` marks the method as abstract.
- `def start_engine(self):` declares the required method.
- `pass` means the method body contains no implementation.

The abstract method establishes a requirement: concrete subclasses must implement `start_engine()`.

**Important:** `pass` does not implement the engine-starting behavior. It simply allows the method declaration to have an empty body.

---

## 5. Understanding the `abc` Module

Python provides the built-in `abc` module for creating Abstract Base Classes.

Two important components are:

### `ABC`

`ABC` is a base class used to define abstract classes.

```python
class Vehicle(ABC):
    pass
```

### `@abstractmethod`

The `@abstractmethod` decorator marks a method as abstract.

```python
@abstractmethod
def start_engine(self):
    pass
```

The `@` symbol indicates that a decorator is being applied to the method.

For now, I can think of a decorator as a mechanism that modifies or adds behavior to a function or method.

---

## 6. Abstract Classes Cannot Be Instantiated Directly

Consider this example:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

car = Vehicle()
```

This raises a `TypeError` because `Vehicle` contains an abstract method that has not been implemented.

The error is similar to:

```text
TypeError: Can't instantiate abstract class Vehicle
with abstract method start_engine
```

### Why does this happen?

Python prevents me from creating an instance of `Vehicle` because its required abstract method has no concrete implementation.

However, I can create a concrete subclass that implements the method.

---

## 7. Inheritance and Method Overriding

A subclass inherits from a parent class.

When the parent is an abstract class, a concrete subclass must implement all inherited abstract methods before it can be instantiated.

Example:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):

    def start_engine(self):
        print("Car engine started")


my_car = Car()
my_car.start_engine()
```

Output:

```text
Car engine started
```

### Step-by-step explanation

1. `Vehicle` defines the abstract method `start_engine()`.
2. `Car` inherits from `Vehicle`.
3. `Car` overrides `start_engine()` with a concrete implementation.
4. `my_car = Car()` creates an instance because the abstract method has been implemented.
5. `my_car.start_engine()` calls the implementation defined in `Car`.

**Key concept:** Method overriding allows a subclass to provide its own implementation of a method inherited from its parent class.

---

## 8. What Happens If a Subclass Does Not Implement Every Abstract Method?

Example:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):

    def start_engine(self):
        print("Car engine started")


my_car = Car()
```

This raises a `TypeError` because `Car` implements `start_engine()` but does not implement `stop_engine()`.

The subclass is still abstract because one required method remains unimplemented.

To fix it, implement both methods:

```python
class Car(Vehicle):

    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")
```

Now instances of `Car` can be created.

**Rule:** A concrete subclass must implement every inherited abstract method before it can be instantiated.

---

## 9. Practical Example: Employee Donations

Imagine that a company wants employees to donate money to a charitable cause.

Every employee must have a `donate()` method, but the abstract class does not specify the implementation.

A concrete subclass provides the implementation.

```python
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def donate(self):
        pass


class Donation(Employee):

    def donate(self):
        amount = int(input("Enter donation amount: "))
        return amount


john = Donation()
peter = Donation()

amounts = []

amounts.append(john.donate())
amounts.append(peter.donate())

print(amounts)
print(sum(amounts))
```

### Example input

```text
Enter donation amount: 100
Enter donation amount: 200
```

### Output

```text
[100, 200]
300
```

### Step-by-step logic

**Step 1: Import the tools**

```python
from abc import ABC, abstractmethod
```

This imports the functionality required to define an abstract class and abstract methods.

**Step 2: Define the abstract class**

```python
class Employee(ABC):

    @abstractmethod
    def donate(self):
        pass
```

The `Employee` class establishes that concrete employee classes must provide a `donate()` method.

**Step 3: Define the concrete subclass**

```python
class Donation(Employee):

    def donate(self):
        amount = int(input("Enter donation amount: "))
        return amount
```

`Donation` inherits from `Employee` and overrides `donate()`.

The method:
1. Asks the user to enter an amount.
2. Converts the input from a string to an integer using `int()`.
3. Returns the integer.

**Step 4: Create instances**

```python
john = Donation()
peter = Donation()
```

Both instances can be created because `Donation` implements the required abstract method.

**Step 5: Store the returned values**

```python
amounts = []

amounts.append(john.donate())
amounts.append(peter.donate())
```

Each call returns a donation amount, which is added to the list.

**Step 6: Display the donations and total**

```python
print(amounts)
print(sum(amounts))
```

The first statement prints the list of donations. The second calculates and prints the total.

Note: This example uses `Donation` as the concrete class name to match the exercise scenario. In a real application, a class named `Employee` could itself be subclassed into separate classes for different employee types.

---

## 10. Abstract Classes Versus Concrete Classes

| Feature | Abstract class | Concrete class |
|---|---|---|
| Main purpose | Define a common interface or blueprint | Provide usable implementations |
| Can be instantiated? | Not while abstract methods remain unimplemented | Yes, if otherwise valid |
| Can contain abstract methods? | Yes | It must implement inherited abstract methods |
| Can contain implemented methods? | Yes | Yes |
| Can be inherited? | Yes | Yes |

An abstract class can contain both abstract methods and ordinary methods with implementations.

It is not necessary for every method in an abstract class to be abstract.

---

## 11. Important Concepts to Remember

### `ABC`

The base class used to define an Abstract Base Class.

### `@abstractmethod`

A decorator that marks a method as abstract.

### `pass`

A placeholder statement that does nothing.

### Inheritance

Allows a subclass to inherit from a parent class.

### Method overriding

Allows a subclass to provide its own implementation of a parent method.

### Instantiation

The process of creating an object from a class.

### `TypeError`

Python raises this error when you try to instantiate an abstract class that still has unimplemented abstract methods.

---

## 12. Common Mistakes

| Mistake | Why it is incorrect |
|---|---|
| Trying to instantiate an abstract class with unimplemented abstract methods | Python prevents this |
| Forgetting `@abstractmethod` | The method will not be marked as abstract |
| Forgetting to inherit from `ABC` when using this pattern | The class will not use `ABC`'s abstract-class enforcement as intended |
| Leaving an inherited abstract method unimplemented | The subclass cannot be instantiated |
| Confusing `pass` with a real implementation | `pass` does not perform the required behavior |
| Forgetting to return the donation amount | The caller will receive `None` if the method has no return value |
| Forgetting to convert `input()` to a number | `input()` returns a string by default |

---

## 13. Practice Questions

Try answering these questions without looking at the earlier sections.

1. What is abstraction in Object-Oriented Programming?
2. What is an abstract class?
3. What is an abstract method?
4. What is the purpose of Python's `abc` module?
5. What does `ABC` do?
6. What does the `@abstractmethod` decorator do?
7. Why can't an abstract class with unimplemented abstract methods be instantiated?
8. What is method overriding?
9. Why must a concrete subclass implement all inherited abstract methods?
10. In the donation example, what does `amounts.append(john.donate())` do?
11. What does `sum(amounts)` return?
12. What error occurs when you attempt to instantiate a class with unimplemented abstract methods?





