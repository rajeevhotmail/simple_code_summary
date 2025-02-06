# Project Analysis Report

![Python](https://img.shields.io/badge/python-3.6%2B-blue)

## Contents
1. [Overview](#overview)
2. [Function Relationships](#function-relationships)
3. [Code Analysis](#code-analysis)

## Overview
Total files analyzed: 10

## Function Relationships

### `test_is_limited`
**Location**: `test_utils.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `sms_is_limited`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_is_limited Performs sequence sorting and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `test_sms_length`
**Location**: `test_utils.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `len`
- `sms_length`

#### Called By:
- `temp_repo/tests/test_utils.py:test_sms_rest`
- `temp_repo/tests/test_utils.py:test_sms_length`
- `temp_repo/smsc/utils.py:sms_rest`
- `temp_repo/smsc/utils.py:sms_parse`
- `temp_repo/tests/test_utils.py:test_sms_parse`
- `temp_repo/smsc/utils.py:sms_length`
</details>

#### Analysis
```python
Function test_sms_length Performs sequence sorting and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `test_sms_rest`
**Location**: `test_utils.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `sms_rest`
- `len`

#### Called By:
- `temp_repo/tests/test_utils.py:test_sms_rest`
</details>

#### Analysis
```python
Function test_sms_rest Performs sequence sorting and Handles mathematical calculations and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `test_sms_parse`
**Location**: `test_utils.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `sms_parse`
- `len`

#### Called By:
- `temp_repo/tests/test_utils.py:test_sms_parse`
</details>

#### Analysis
```python
Function test_sms_parse Performs sequence sorting and Handles mathematical calculations and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `test_send_mobile_number`
**Location**: `test_functional.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `SMSC`
- `MagicMock`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_send_mobile_number Performs sequence sorting and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `test_validate_code_area`
**Location**: `test_validations.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `validate_area_code`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_validate_code_area Performs sequence sorting and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `test_validate_local_number`
**Location**: `test_validations.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `validate_local_number`

#### Called By:
- `temp_repo/tests/test_validations.py:test_validate_local_number`
</details>

#### Analysis
```python
Function test_validate_local_number Performs sequence sorting and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `test_validate_length_phone_number`
**Location**: `test_validations.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `validate_length_phone_number`

#### Called By:
- `temp_repo/tests/test_utils.py:test_sms_rest`
- `temp_repo/tests/test_utils.py:test_sms_length`
- `temp_repo/smsc/utils.py:sms_rest`
- `temp_repo/tests/test_validations.py:test_validate_length_phone_number`
- `temp_repo/smsc/utils.py:sms_parse`
- `temp_repo/tests/test_utils.py:test_sms_parse`
- `temp_repo/smsc/utils.py:sms_length`
</details>

#### Analysis
```python
Function test_validate_length_phone_number Performs sequence sorting and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `test_validate_phones`
**Location**: `test_validations.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `validate_phone_numbers`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_validate_phones Performs sequence sorting and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `test_validate_priority`
**Location**: `test_validations.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `validate_priority`

#### Called By:
- `temp_repo/tests/test_validations.py:test_validate_priority`
- `temp_repo/smsc/smsc.py:send`
- `temp_repo/smsc/smsc.py:send_many`
</details>

#### Analysis
```python
Function test_validate_priority Performs sequence sorting and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `validate_phone_number`
**Location**: `validations.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `AreaCodeSMSCError`
- `LocalNumberSMSCError`
- `PhoneNumberLongSMSCError`

#### Called By:
- `temp_repo/smsc/validations.py:validate_phone_numbers`
- `temp_repo/smsc/smsc.py:send`
</details>

#### Analysis
```python
Function validate_phone_number Performs sequence sorting and Handles mathematical calculations and Processes API responses and JSON data and Manages list operations and Handles text processing and Implements error handling and Manages URL operations and Validates input parameters
```

---

### `validate_phone_numbers`
**Location**: `validations.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `validate_phone_number`

#### Called By:
- `temp_repo/smsc/smsc.py:send_many`
- `temp_repo/smsc/validations.py:validate_phone_numbers`
- `temp_repo/smsc/smsc.py:send`
- `temp_repo/tests/test_validations.py:test_validate_phones`
</details>

#### Analysis
```python
Function validate_phone_numbers Performs sequence sorting and Manages list operations and Handles text processing and Validates input parameters
```

---

### `validate_area_code`
**Location**: `validations.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `bool`

#### Called By:
- `temp_repo/tests/test_validations.py:test_validate_code_area`
</details>

#### Analysis
```python
Function validate_area_code Performs sequence sorting and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `validate_local_number`
**Location**: `validations.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `bool`

#### Called By:
- `temp_repo/tests/test_validations.py:test_validate_local_number`
</details>

#### Analysis
```python
Function validate_local_number Performs sequence sorting and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `validate_length_phone_number`
**Location**: `validations.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `bool`

#### Called By:
- `temp_repo/tests/test_utils.py:test_sms_rest`
- `temp_repo/tests/test_utils.py:test_sms_length`
- `temp_repo/smsc/utils.py:sms_rest`
- `temp_repo/tests/test_validations.py:test_validate_length_phone_number`
- `temp_repo/smsc/utils.py:sms_parse`
- `temp_repo/tests/test_utils.py:test_sms_parse`
- `temp_repo/smsc/utils.py:sms_length`
</details>

#### Analysis
```python
Function validate_length_phone_number Performs sequence sorting and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `validate_priority`
**Location**: `validations.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `PriorityOutOfRangeError`

#### Called By:
- `temp_repo/tests/test_validations.py:test_validate_priority`
- `temp_repo/smsc/smsc.py:send`
- `temp_repo/smsc/smsc.py:send_many`
</details>

#### Analysis
```python
Function validate_priority Performs sequence sorting and Manages list operations and Handles text processing and Implements error handling and Validates input parameters
```

---

### `__init__`
**Location**: `smsc.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function __init__ Basic function operations
```

---

### `_url`
**Location**: `smsc.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `dict`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _url Performs sequence sorting and Handles mathematical calculations and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `send`
**Location**: `smsc.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `validate_phone_number`
- `validate_priority`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function send Performs sequence sorting and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `send_many`
**Location**: `smsc.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `validate_phone_numbers`
- `validate_priority`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function send_many Performs sequence sorting and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

### `sent`
**Location**: `smsc.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function sent Processes API responses and JSON data and Manages URL operations
```

---

### `received`
**Location**: `smsc.py`

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
#### Calls:
- No incoming calls
</details>

#### Analysis
```python
Function received Processes API responses and JSON data and Manages URL operations
```

---

### `status`
**Location**: `smsc.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function status Processes API responses and JSON data and Manages URL operations
```

---

### `balance`
**Location**: `smsc.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function balance Processes API responses and JSON data and Manages URL operations
```

---

### `cancel_queue`
**Location**: `smsc.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function cancel_queue Processes API responses and JSON data and Manages URL operations
```

---

### `__init__`
**Location**: `exceptions.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function __init__ Basic function operations
```

---

### `sms_is_limited`
**Location**: `utils.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `ord`

#### Called By:
- `temp_repo/tests/test_utils.py:test_is_limited`
- `temp_repo/smsc/utils.py:sms_parse`
- `temp_repo/smsc/utils.py:sms_length`
- `temp_repo/smsc/utils.py:sms_rest`
</details>

#### Analysis
```python
Function sms_is_limited Performs sequence sorting and Manages list operations and Handles text processing and Validates input parameters
```

---

### `sms_length`
**Location**: `utils.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `len`
- `sms_is_limited`

#### Called By:
- `temp_repo/tests/test_utils.py:test_sms_rest`
- `temp_repo/tests/test_utils.py:test_sms_length`
- `temp_repo/smsc/utils.py:sms_rest`
- `temp_repo/smsc/utils.py:sms_parse`
- `temp_repo/tests/test_utils.py:test_sms_parse`
- `temp_repo/smsc/utils.py:sms_length`
</details>

#### Analysis
```python
Function sms_length Performs sequence sorting and Manages list operations and Handles text processing and Validates input parameters
```

---

### `sms_rest`
**Location**: `utils.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `len`
- `sms_is_limited`

#### Called By:
- `temp_repo/tests/test_utils.py:test_sms_rest`
</details>

#### Analysis
```python
Function sms_rest Performs sequence sorting and Handles mathematical calculations and Manages list operations and Handles text processing and Validates input parameters
```

---

### `sms_parse`
**Location**: `utils.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `len`
- `range`
- `sms_is_limited`

#### Called By:
- `temp_repo/tests/test_utils.py:test_sms_parse`
</details>

#### Analysis
```python
Function sms_parse Performs sequence sorting and Handles mathematical calculations and Processes API responses and JSON data and Manages list operations and Handles text processing and Manages URL operations and Validates input parameters
```

---

## Code Analysis

### setup.py
```python
# File: temp_repo/setup.py
Python module for setup
```

### test_utils.py
```python
# File: temp_repo/tests/test_utils.py
Python module for test_utils
```

### test_functional.py
```python
# File: temp_repo/tests/test_functional.py
Python module for test_functional
```

### test_validations.py
```python
# File: temp_repo/tests/test_validations.py
Python module for test_validations
```

### __init__.py
```python
# File: temp_repo/tests/__init__.py
Python module for __init__
```

### validations.py
```python
# File: temp_repo/smsc/validations.py
Python module for validations
```

### smsc.py
```python
# File: temp_repo/smsc/smsc.py
Python module for smsc
```

### exceptions.py
```python
# File: temp_repo/smsc/exceptions.py
Python module for exceptions
```

### utils.py
```python
# File: temp_repo/smsc/utils.py
Python module for utils
```

### __init__.py
```python
# File: temp_repo/smsc/__init__.py
Python module for __init__
```

