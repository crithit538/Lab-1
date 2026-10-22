# Reflection on Static Code Analysis

## 1. What did you learn from static code analysis?

I learned that static code analysis tools identify potential problems in a program without executing it. Pylint checks code quality, Bandit identifies potential security vulnerabilities, and Flake8 checks coding style and formatting.

## 2. Why is it important to fix security vulnerabilities?

Security vulnerabilities can expose applications to attacks and unexpected behavior. Removing hardcoded passwords, avoiding unsafe deserialization, and using parameterized SQL queries help improve program security.

## 3. How did the tools improve the program?

Pylint helped improve naming conventions, documentation, exception handling, and readability. Bandit identified unsafe pickle usage, a hardcoded password, and a possible SQL injection issue. Flake8 identified long lines, unnecessary blank lines, and spacing errors.

## 4. What did you learn about maintaining code quality?

I learned that code should be readable, consistently formatted, and secure. Running the tools again after fixing the reported issues helps verify the improvements. The final program achieved a Pylint score of 10.00/10, while Bandit and Flake8 reported no issues.
