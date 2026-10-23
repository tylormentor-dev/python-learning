# Test-Driven Development (TDD)

## 1. What Is Test-Driven Development?

Test-Driven Development (TDD) is a software development approach in which developers write tests **before writing the code**.

The code is then written to satisfy those tests. This helps developers focus on the expected behavior of a feature from the beginning instead of leaving testing until the end.

In traditional development, developers often write the code first and test it after-wards. TDD takes a different approach by making testing part of the development process from the start.

## 2. The TDD Process

TDD follows a repeating process commonly known as the **Red-Green-Refactor cycle**.

### Step 1: Red — Write a Failing Test

Write a test that describes the expected behavior of a feature.

The test should initially fail because the required code has not yet been implemented.

### Step 2: Green — Write the Code

Write just enough code to make the failing test pass.

The goal is to satisfy the test without adding unnecessary complexity.

### Step 3: Refactor — Improve the Code

Once the test passes, improve the structure and readability of the code without changing its intended behavior.

Run the tests again to confirm that the changes have not broken anything.

Repeat the cycle for each new feature or behavior.

**The main idea:** Write a test, make it pass, improve the code, and repeat.

## 3. Using pytest with TDD

`pytest` is a Python testing framework that can be used to implement TDD.

It allows developers to write test functions using the `test_` naming convention and the `assert` statement to check expected results.

For example, suppose we want to create a function that adds two numbers.

First, write a test:

```python
def test_add():
    assert add(4, 5) == 9
```

Initially, this test may fail because the `add()` function has not been implemented.

Next, write the function:

```python
def add(a, b):
    return a + b
```

Run the test again. If the function returns `9`, the test passes.

You can then refactor the code if necessary and rerun the test to confirm that it still works.

## 4. Benefits of TDD

### Clear Requirements

Writing tests first forces developers to think about what a feature should do and what results are expected before implementing it.

### Early Bug Detection

Tests can reveal problems as code is being developed, making defects easier to investigate before they spread to other parts of the application.

### Better Code Structure

The process encourages developers to write smaller, focused functions that are easier to understand, test, and maintain.

### Easier Refactoring

Because tests can be rerun after code changes, developers can check whether improvements have accidentally broken existing behavior.

### Improved Integration

Clearly defined expected behavior helps developers understand how new features should work with existing components and interfaces.

### Easier Maintenance

A collection of automated tests can be rerun whenever the code changes, helping developers identify regressions and maintain software over time.

## 5. TDD vs Traditional Testing

| Test-Driven Development | Traditional Testing |
|---|---|
| Tests are written before the implementation code. | Tests are commonly written after the implementation code. |
| Testing guides the development process. | Testing checks the code after or during implementation. |
| Requirements and expected behavior are considered early. | Expected behavior may be tested after the code has been written. |
| Tests are run repeatedly throughout development. | Testing may occur at later stages, depending on the team's process. |

Both approaches can be used within the same software development project. The appropriate approach depends on the project's requirements, workflow, and development practices.

## 6. Important Things to Remember

- TDD stands for Test-Driven Development.
- Tests are written before the code they are intended to verify.
- The Red-Green-Refactor cycle is the central process of TDD.
- Red means the test fails, green means the test passes, and refactor means improving the code while preserving its behavior.
- `pytest` can be used to write and execute tests during TDD.
- TDD encourages early feedback, clear requirements, and maintainable code.
- Tests should be rerun after refactoring to check that existing behavior still works.

## Key Takeaway

**TDD uses tests to guide development rather than treating testing as a final step.** Developers write a failing test, implement the required code, make the test pass, and improve the code before repeating the process.