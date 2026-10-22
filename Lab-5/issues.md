# Static Code Analysis Issues

## 1. Pylint Issues

**Initial score:** 5.14/10  
**Final score:** 10.00/10

The initial Pylint analysis identified the following code-quality and maintainability issues.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Long lines | Pylint C0301 | 5, 11, 18 | Several lines exceeded the configured maximum of 100 characters. | Split long statements across multiple lines. |
| Missing module docstring | Pylint C0114 | 1 | The module did not describe its purpose. | Added a module-level docstring. |
| Incorrect constant naming | Pylint C0103 | 7 | The module-level variable `service_count` did not follow the recommended UPPER_CASE naming convention for constants. | Removed the unnecessary global counter. |
| Missing function docstrings | Pylint C0116 | 10, 15, 25, 34, 42, 46 | Several functions lacked documentation explaining their purpose. | Added appropriate function docstrings. |
| Invalid function naming | Pylint C0103 | 10, 15, 34 | Functions such as `addTower`, `serviceTower`, and `riskLevel` did not follow snake_case naming conventions. | Renamed functions using snake_case. |
| Unnecessary string formatting | Pylint C0209 | 11 | A regular string was formatted using the `%` operator where an f-string was suggested. | Reviewed and improved string formatting as appropriate. |
| Global statement | Pylint W0603 | 16 | A function modified a global variable, making the program harder to maintain. | Removed the unnecessary global counter. |
| Broad exception handling | Pylint W0718 | 20 | Catching the general `Exception` class could hide unrelated errors. | Changed the handler to catch the appropriate exception type. |
| Unnecessary else | Pylint R1705 | 36 | An `else` followed a `return` statement unnecessarily. | Removed the `else` and de-indented the following code. |

**Final Pylint score:** 10.00/10.

## 2. Bandit Security Issues

The initial Bandit scan identified four potential security issues.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Possible SQL injection | Bandit B608 — Medium severity | 11 | SQL was constructed using string interpolation, potentially allowing unsafe query construction. | Replaced string interpolation with parameterized SQL queries. |
| Pickle deserialization | Bandit B301 — Medium severity | 43 | The code used pickle serialization and deserialization, which can be unsafe when handling untrusted data. | Removed unnecessary pickle serialization and deserialization. |
| Hardcoded password | Bandit B105 — Low severity | 6 | A password was stored directly in the source code. | Removed the hardcoded password. |
| Pickle import | Bandit B403 — Low severity | 1 | Importing pickle can introduce security risks when used to deserialize untrusted data. | Removed the unnecessary pickle import. |

**Final Bandit result:** No security issues identified in the final scan, as recorded in the final report.

## 3. Flake8 Issues

The initial Flake8 analysis identified the following style violations.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Excessive line length | Flake8 E501 | 5, 11, 18, 35, 43 | Several lines exceeded the configured maximum of 79 characters. | Wrapped long statements and improved formatting. |
| Excessive blank lines | Flake8 E303 | 25 | There were too many blank lines between definitions. | Removed unnecessary blank lines. |
| Missing operator whitespace | Flake8 E225 | 50 | An operator lacked the required surrounding whitespace. | Corrected the spacing. |

**Final Flake8 result:** No formatting errors reported, as recorded in the final report.

## 4. Summary

Static analysis was performed using Pylint, Bandit, and Flake8. The initial reports identified issues involving code documentation, naming conventions, formatting, exception handling, global variables, SQL query construction, and potentially unsafe pickle usage.

The applicable issues were addressed while preserving the program's intended functionality. The final Pylint score was 10.00/10, and the final Bandit and Flake8 reports recorded no remaining findings or formatting errors, respectively.
