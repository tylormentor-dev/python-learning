# Types of Software Testing

## 1. Overview

Software testing can be categorized in different ways depending on what is being tested, how the tests are performed, and what the tester knows about the internal implementation.

The four main levels of testing are:

1. Unit testing
2. Integration testing
3. System testing
4. Acceptance testing

Other classifications include black box and white box testing, functional and non-functional testing, and manual and automated testing.

## 2. Black Box and White Box Testing

### Black Box Testing

Black box testing checks the functionality of software without requiring knowledge of its internal code or implementation.

The tester provides inputs and checks whether the actual results match the expected results.

**Example:** Entering an incorrect password and checking whether the application displays an appropriate error message.

### White Box Testing

White box testing examines software with knowledge of its internal code, structure, or logic.

It can be used to verify code paths, conditions, and internal operations.

**Example:** Checking whether a Python function correctly handles different conditions in its code.

## 3. Functional, Non-Functional, and Maintenance Testing

### Functional Testing

Functional testing checks whether the software behaves according to its specified requirements.

It focuses on what the system does.

**Examples:**

- Checking whether a user can log in.
- Verifying that a form rejects invalid input.
- Confirming that a search function returns relevant results.

### Non-Functional Testing

Non-functional testing evaluates how well the software operates rather than only checking its features.

**Examples:**

- Performance testing
- Load testing
- Security testing
- Compatibility testing
- Usability testing

### Maintenance Testing

Maintenance testing is performed when software or its operating environment changes.

It helps determine whether changes have introduced new problems and whether the system continues to work correctly.

**Example:** Testing an application after a software update or a database migration.

## 4. Manual and Automated Testing

### Manual Testing

A tester executes test steps themselves and checks the results without relying on a test automation script to perform the test.

Manual testing is useful for exploratory testing and evaluating aspects of usability.

### Automated Testing

Automated testing uses scripts or tools to execute tests and check results.

It is useful for repetitive tests, regression testing, and running tests frequently during development.

Both approaches can be used together, depending on the requirements of the project.

## 5. The Four Main Levels of Testing

### Unit Testing

Unit testing checks individual components or small units of code in isolation.

It is often performed by developers while writing code.

**Example:** Testing a Python function that calculates the total price of an order.

A Python testing framework such as `pytest` can be used to write and run unit tests.

### Integration Testing

Integration testing checks whether different components work correctly together.

It focuses on the interactions and interfaces between components.

**Example:** Checking whether an application correctly retrieves information from a database and displays it on a webpage.

Common integration approaches include top-down, bottom-up, and sandwich testing.

### System Testing

System testing evaluates the complete, integrated application against its specified requirements.

It can include checks for functionality, performance, security, reliability, and compatibility with the intended operating environment.

**Example:** Testing an entire online shopping application, from signing in to completing a purchase.

### Acceptance Testing

Acceptance testing determines whether the software meets the acceptance criteria and is suitable for its intended use.

It often involves customers, stakeholders, or representative end users.

**Example:** Asking users to complete typical business tasks in an application and confirming that the results meet their needs.

Alpha and beta testing are examples of acceptance-related testing approaches.

## 6. Comparison of the Four Testing Levels

| Testing level | Main focus | Example |

| Unit | Individual components | Testing a calculation function 
| Integration | Interactions between components | Testing database communication 
| System | The complete application | Testing the entire checkout process 
| Acceptance | User and business requirements | Confirming the application meets customer needs 

## 7. Testing Throughout Development

The four testing levels are often introduced in a sequence, but they do not have to happen only once or in a strict order.

In iterative development, such as Agile, teams test repeatedly as the software changes.

Testing early and frequently helps identify defects before they become more difficult and expensive to fix.

## Key Takeaways

- Unit testing checks individual components.
- Integration testing checks interactions between components.
- System testing checks the complete application.
- Acceptance testing checks whether the software meets user and business needs.
- Black box and white box describe approaches based on the tester's knowledge of the internal implementation.
- Functional testing checks specified behavior, while non-functional testing evaluates qualities such as performance and usability.
- Manual and automated testing are complementary approaches.
- Testing should be performed throughout development, not only before release.
