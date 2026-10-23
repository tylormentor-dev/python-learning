# Unit Testing with pytest

## 1. What Is pytest?

`pytest` is a popular Python testing framework used to write and run automated tests.

It is beginner-friendly because it allows you to create tests with simple, readable code.

In unit testing, we test individual functions or small parts of a program to check whether they behave as expected.

## 2. Creating a Simple Python Program

First, create a file called `addition.py`. This file contains the functions we want to test.

```python
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
```

The `add()` function returns the sum of two values, while `sub()` returns their difference.

## 3. Creating Test Cases

Next, create a file called `test_addition.py`. This file contains the tests for the functions in `addition.py`.

```python
from addition import add, sub

def test_add():
    assert add(4, 5) == 9

def test_sub():
    assert sub(4, 5) == -1
```

The test file imports the functions that need to be tested.

Each test function begins with the prefix `test_`. This naming convention allows pytest to discover the tests automatically.

### Understanding assert

The `assert` statement checks whether a condition is true.

```python
assert add(4, 5) == 9
```

This checks whether adding 4 and 5 produces 9.

- If the condition is true, the test passes.
- If the condition is false, the test fails.

You can use different comparison operators and expressions with `assert`, depending on what you want to check.

## 4. Running the Tests

Open a terminal in your project directory and run:

```bash
python -m pytest test_addition.py
```

This command runs the tests inside `test_addition.py`.

If both tests pass, pytest displays two dots (`..`) in its short test progress output. Each dot represents a passing test.

The final summary also reports how many tests passed or failed.

## 5. Understanding a Failed Test

Suppose you accidentally change the subtraction test:

```python
def test_sub():
    assert sub(4, 5) == -2
```

The actual result is `-1`, not `-2`, so the test fails.

When a test fails, pytest provides information about the failed assertion and the values involved. This helps you understand why the expected result did not match the actual result.

A failure does not automatically mean the function is incorrect. The function, the expected result, or the test itself could be wrong.

## 6. Using Multiple Assertions

You can include multiple `assert` statements in one test function.

```python
def test_add():
    assert add(4, 5) == 9
    assert add(2, 3) == 5
    assert add(0, 0) == 0
```

Each assertion checks a different condition.

For the test to pass, every assertion that gets executed must succeed. If an assertion fails, pytest marks the test as failed and stops executing the remaining statements in that test function.

This allows one test function to check several expected behavior of the same function.

## 7. Why `pass` Is Not a Real Test

You can write an empty test function using `pass`:

```python
def test_add():
    pass
```

This test will pass because no assertion or other failing operation occurs.

However, it does not verify that the addition function works correctly.

**Important:** A passing test is only useful when it actually checks the expected behavior of the software.

## 8. Running a Specific Test

You do not always need to run every test in a file. You can run one specific test by using `::` followed by its function name.

For example:

```bash
python -m pytest test_addition.py::test_add
```

This runs only `test_add()` from `test_addition.py`.

To run all tests in the file, use:

```bash
python -m pytest test_addition.py
```

## 9. Key Takeaways

- `pytest` is a Python framework for writing and running tests.
- Unit tests check individual functions or small components of a program.
- Test files and test functions should follow pytest's naming conventions, so tests can be discovered.
- The `assert` statement checks whether the actual result matches the expected condition.
- Pytest reports passing and failing tests and provides useful failure details.
- A test function can contain multiple assertions.
- A test that contains only `pass` does not verify program behavior.
- You can run all tests in a file or select a specific test using `::`.