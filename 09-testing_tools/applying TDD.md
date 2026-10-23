# Applying Test-Driven Development (TDD)

## 1. Overview

Test-Driven Development (TDD) is a development approach in which you write test cases before writing the code.

The tests describe what the program should do. You then write code to satisfy those tests and improve the code while ensuring that the tests continue to pass.

For example, when checking student enrollments, you might want to verify that:

- The student's name exists in the approved list.
- The name follows the required format.
- The name does not contain numeric characters.

Each requirement can be turned into a test case.

## 2. Example: Validating Student Names

Imagine you are checking student enrollments against a list of approved names.

In a real application, the names might be stored in a database. For this example, a Python list will be used instead.

The program needs to check two things:

1. Whether a name exists in the approved list.
2. Whether a name contains numeric characters.

We will use `pytest` to test these requirements.

## 3. Create the Project Files

Create two Python files:

| File | Purpose |

| `test_findstring.py` | Contains the test cases |
| `findstring.py` | Contains the functions being tested |

In TDD, we begin by writing the tests in `test_findstring.py` before implementing the functions in `findstring.py`.

## 4. Write the First Test

Start by writing a test to check whether a name exists in the approved list.

In `test_findstring.py`:

```python
from findstring import ispresent

def test_ispresent():
    assert ispresent("Al") == True
```

The test expects `ispresent("Al")` to return `True`.

At this stage, the function has not been implemented, so the test cannot pass yet.

## 5. Write the Code

Next, create the `ispresent()` function in `findstring.py`.

```python
def ispresent(person):
    names = ["Al", "John", "Mary"]

    if person in names:
        return True
    else:
        return False
```

The function checks whether the supplied name exists in the list.

If the name is present, it returns `True`. Otherwise, it returns `False`.

Run the test using:

```bash
python -m pytest test_findstring.py
```

The test should pass because `"Al"` is in the list.

## 6. Add Another Test

The first test checks whether a name exists in the list. However, it does not check whether the name follows the required format.

Suppose names must not contain numeric characters.

Add another test to `test_findstring.py`:

```python
from findstring import ispresent, nodigit

def test_ispresent():
    assert ispresent("Al") == True

def test_nodigit():
    assert nodigit("Al") == True
    assert nodigit("N7") == False
```

This test checks two cases:

- `"Al"` should be accepted because it contains no digits.
- `"N7"` should be rejected because it contains a digit.

## 7. Implement the New Function

Now add the `nodigit()` function to `findstring.py`.

```python
def nodigit(person):
    if person.isalpha():
        return True
    else:
        return False
```

The `isalpha()` method returns `True` when a non-empty string contains only alphabetic characters.

This means `"Al"` passes, while `"N7"` fails the name-format check.

Run the tests again:

```bash
python -m pytest test_findstring.py
```

If the implementation behaves as expected, both test functions should pass.

## 8. Repeat the TDD Cycle

As you add requirements, continue repeating the process.

1. Write a test for the new requirement.
2. Run the test and confirm that it fails when the behavior has not been implemented.
3. Write or update the code to satisfy the test.
4. Run the tests again.
5. Refactor the code if necessary and confirm that the tests still pass.

Continue until the required behavior is implemented, and the relevant tests pass.

## Key Takeaways

- TDD starts with test cases rather than implementation code.
- Each test should check a specific expected behavior.
- `pytest` can run the tests and report failures.
- New requirements can be introduced by adding new test cases.
- A test failure helps identify behavior that does not meet expectations.
- Re-running tests helps confirm that new changes have not broken existing functionality.

**The main idea:** Write the test first, implement the behavior, and repeat the cycle as the requirements grow.