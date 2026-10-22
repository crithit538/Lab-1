# Static Code Analysis Issues

## 1. Pylint Issues

**Initial score:** 5.14/10

The initial Pylint analysis identified these issues:

| Issue | Description | Fix Applied |
|---|---|---|
| Missing module docstring | The Python file did not describe its purpose. | Added a module docstring. |
| Missing function docstrings | Functions did not explain their purpose. | Added docstrings to functions. |
| Invalid naming conventions | Function names used camelCase instead of snake_case. | Renamed functions using snake_case. |
| Incorrect constant naming | `service_count` did not follow the recommended constant naming style. | Removed the unnecessary global counter. |
| Long lines | Several lines exceeded the recommended length. | Split long statements across multiple lines. |
| SQL string formatting | SQL statements were constructed using string interpolation. | Used parameterized SQL queries. |
| Global statement | A function modified a global variable. | Removed the global counter. |
| Broad exception handling | The program caught the general `Exception` class. | Changed the handler to catch `sqlite3.Error`. |
| Unnecessary else | An `else` followed a return statement. | Removed the unnecessary `else`. |
| Trailing newlines | Extra blank lines existed at the end of the file. | Removed trailing blank lines. |

**Final score:** 10.00/10

## 2. Bandit Issues

The initial Bandit scan identified four security findings:

| Finding | Risk | Fix Applied |
|---|---|---|
| B403: Pickle import | Pickle can be unsafe when handling untrusted data. | Removed the pickle import. |
| B105: Hardcoded password | A password was stored directly in the source code. | Removed the hardcoded password. |
| B608: Possible SQL injection | SQL was constructed using string interpolation. | Used parameterized SQL queries. |
| B301: Pickle deserialization | Deserializing untrusted pickle data can execute unsafe operations. | Removed pickle serialization and deserialization. |

**Final result:** No security issues identified.

## 3. Flake8 Issues

The initial Flake8 scan identified:

| Issue | Description | Fix Applied |
|---|---|---|
| E501 | Lines exceeded the maximum allowed length. | Wrapped long lines. |
| E303 | Too many blank lines between functions. | Removed unnecessary blank lines. |
| E225 | Missing whitespace around an operator. | Corrected spacing. |

**Final result:** No formatting errors reported.
