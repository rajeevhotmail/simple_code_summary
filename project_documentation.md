# Project Analysis Report

![Python](https://img.shields.io/badge/python-3.6%2B-blue)

## Contents
1. [Overview](#overview)
2. [Function Relationships](#function-relationships)
3. [Code Analysis](#code-analysis)

## Overview
Total files analyzed: 5

## Function Relationships

### File: `setup.py`

#### Function: `read`
**Signature:** `def read()`

**Operations:**
```python
Function read Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `join`, `dirname`
- Called by: None

---

### File: `conf.py`

### File: `test_asn1.py`

#### Function: `test_boolean`
**Signature:** `def test_boolean(self)`

**Operations:**
```python
Function test_boolean Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_integer`
**Signature:** `def test_integer(self)`

**Operations:**
```python
Function test_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `isinstance`
- Called by: `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_long_integer`
**Signature:** `def test_long_integer(self)`

**Operations:**
```python
Function test_long_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_negative_integer`
**Signature:** `def test_negative_integer(self)`

**Operations:**
```python
Function test_negative_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_long_negative_integer`
**Signature:** `def test_long_negative_integer(self)`

**Operations:**
```python
Function test_long_negative_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_twos_complement_boundaries`
**Signature:** `def test_twos_complement_boundaries(self)`

**Operations:**
```python
Function test_twos_complement_boundaries Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_octet_string`
**Signature:** `def test_octet_string(self)`

**Operations:**
```python
Function test_octet_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `test_bitstring`
**Signature:** `def test_bitstring(self)`

**Operations:**
```python
Function test_bitstring Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `test_printable_string`
**Signature:** `def test_printable_string(self)`

**Operations:**
```python
Function test_printable_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_unicode_octet_string`
**Signature:** `def test_unicode_octet_string(self)`

**Operations:**
```python
Function test_unicode_octet_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `test_unicode_printable_string`
**Signature:** `def test_unicode_printable_string(self)`

**Operations:**
```python
Function test_unicode_printable_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_null`
**Signature:** `def test_null(self)`

**Operations:**
```python
Function test_null Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_object_identifier`
**Signature:** `def test_object_identifier(self)`

**Operations:**
```python
Function test_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_long_object_identifier`
**Signature:** `def test_long_object_identifier(self)`

**Operations:**
```python
Function test_long_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_real_object_identifier`
**Signature:** `def test_real_object_identifier(self)`

**Operations:**
```python
Function test_real_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_enumerated`
**Signature:** `def test_enumerated(self)`

**Operations:**
```python
Function test_enumerated Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_sequence`
**Signature:** `def test_sequence(self)`

**Operations:**
```python
Function test_sequence Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_sequence_of`
**Signature:** `def test_sequence_of(self)`

**Operations:**
```python
Function test_sequence_of Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_set`
**Signature:** `def test_set(self)`

**Operations:**
```python
Function test_set Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_set_of`
**Signature:** `def test_set_of(self)`

**Operations:**
```python
Function test_set_of Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_context`
**Signature:** `def test_context(self)`

**Operations:**
```python
Function test_context Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_application`
**Signature:** `def test_application(self)`

**Operations:**
```python
Function test_application Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_private`
**Signature:** `def test_private(self)`

**Operations:**
```python
Function test_private Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_long_tag_id`
**Signature:** `def test_long_tag_id(self)`

**Operations:**
```python
Function test_long_tag_id Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_contextmanager_construct`
**Signature:** `def test_contextmanager_construct(self)`

**Operations:**
```python
Function test_contextmanager_construct Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `test_contextmanager_calls_enter`
**Signature:** `def test_contextmanager_calls_enter(self)`

**Operations:**
```python
Function test_contextmanager_calls_enter Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `TestEncoder`, `RuntimeError`
- Called by: None

---

#### Function: `enter`
**Signature:** `def enter(self, nr)`

**Operations:**
```python
Function enter Performs unit testing and Validates input data
```

**Dependencies:**
- Calls: `RuntimeError`
- Called by: None

---

#### Function: `test_contextmanager_calls_leave`
**Signature:** `def test_contextmanager_calls_leave(self)`

**Operations:**
```python
Function test_contextmanager_calls_leave Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `TestEncoder`, `RuntimeError`
- Called by: None

---

#### Function: `leave`
**Signature:** `def leave(self)`

**Operations:**
```python
Function leave Performs unit testing and Validates input data
```

**Dependencies:**
- Calls: `RuntimeError`
- Called by: None

---

#### Function: `test_long_tag_length`
**Signature:** `def test_long_tag_length(self)`

**Operations:**
```python
Function test_long_tag_length Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_emit_length_long`, `temp_repo/src/asn1.py:leave`, `temp_repo/src/asn1.py:_decode_boolean`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:write`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_encode_integer`, `temp_repo/src/asn1.py:_decode_null`, `temp_repo/src/asn1.py:_read_bytes`, `temp_repo/src/asn1.py:_end_of_input`, `temp_repo/src/asn1.py:output`

---

#### Function: `test_error_init`
**Signature:** `def test_error_init(self)`

**Operations:**
```python
Function test_error_init Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_error_stack`
**Signature:** `def test_error_stack(self)`

**Operations:**
```python
Function test_error_stack Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_error_object_identifier`
**Signature:** `def test_error_object_identifier(self)`

**Operations:**
```python
Function test_error_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_default_encoding`
**Signature:** `def test_default_encoding(self)`

**Operations:**
```python
Function test_default_encoding Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `check_defaults`, `type`
- Called by: None

---

#### Function: `check_defaults`
**Signature:** `def check_defaults(value, number)`

**Operations:**
```python
Function check_defaults Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `type`
- Called by: `temp_repo/tests/test_asn1.py:test_default_encoding`

---

#### Function: `test_context_no_tag_number`
**Signature:** `def test_context_no_tag_number(self)`

**Operations:**
```python
Function test_context_no_tag_number Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_context_with_tag_number_10`
**Signature:** `def test_context_with_tag_number_10(self)`

**Operations:**
```python
Function test_context_with_tag_number_10 Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_boolean`
**Signature:** `def test_boolean(self)`

**Operations:**
```python
Function test_boolean Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_integer`
**Signature:** `def test_integer(self)`

**Operations:**
```python
Function test_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `isinstance`
- Called by: `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_long_integer`
**Signature:** `def test_long_integer(self)`

**Operations:**
```python
Function test_long_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_negative_integer`
**Signature:** `def test_negative_integer(self)`

**Operations:**
```python
Function test_negative_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_long_negative_integer`
**Signature:** `def test_long_negative_integer(self)`

**Operations:**
```python
Function test_long_negative_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_twos_complement_boundaries`
**Signature:** `def test_twos_complement_boundaries(self)`

**Operations:**
```python
Function test_twos_complement_boundaries Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_octet_string`
**Signature:** `def test_octet_string(self)`

**Operations:**
```python
Function test_octet_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `test_printable_string`
**Signature:** `def test_printable_string(self)`

**Operations:**
```python
Function test_printable_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_bitstring`
**Signature:** `def test_bitstring(self)`

**Operations:**
```python
Function test_bitstring Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `test_bitstring_unused_bits`
**Signature:** `def test_bitstring_unused_bits(self)`

**Operations:**
```python
Function test_bitstring_unused_bits Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `test_unicode_printable_string`
**Signature:** `def test_unicode_printable_string(self)`

**Operations:**
```python
Function test_unicode_printable_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_null`
**Signature:** `def test_null(self)`

**Operations:**
```python
Function test_null Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_object_identifier`
**Signature:** `def test_object_identifier(self)`

**Operations:**
```python
Function test_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_long_object_identifier`
**Signature:** `def test_long_object_identifier(self)`

**Operations:**
```python
Function test_long_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_real_object_identifier`
**Signature:** `def test_real_object_identifier(self)`

**Operations:**
```python
Function test_real_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_enumerated`
**Signature:** `def test_enumerated(self)`

**Operations:**
```python
Function test_enumerated Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_sequence`
**Signature:** `def test_sequence(self)`

**Operations:**
```python
Function test_sequence Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_sequence_of`
**Signature:** `def test_sequence_of(self)`

**Operations:**
```python
Function test_sequence_of Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_set`
**Signature:** `def test_set(self)`

**Operations:**
```python
Function test_set Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_set_of`
**Signature:** `def test_set_of(self)`

**Operations:**
```python
Function test_set_of Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_context`
**Signature:** `def test_context(self)`

**Operations:**
```python
Function test_context Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_application`
**Signature:** `def test_application(self)`

**Operations:**
```python
Function test_application Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_private`
**Signature:** `def test_private(self)`

**Operations:**
```python
Function test_private Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_long_tag_id`
**Signature:** `def test_long_tag_id(self)`

**Operations:**
```python
Function test_long_tag_id Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_long_tag_length`
**Signature:** `def test_long_tag_length(self)`

**Operations:**
```python
Function test_long_tag_length Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_emit_length_long`, `temp_repo/src/asn1.py:leave`, `temp_repo/src/asn1.py:_decode_boolean`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:write`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_encode_integer`, `temp_repo/src/asn1.py:_decode_null`, `temp_repo/src/asn1.py:_read_bytes`, `temp_repo/src/asn1.py:_end_of_input`, `temp_repo/src/asn1.py:output`

---

#### Function: `test_read_multiple`
**Signature:** `def test_read_multiple(self)`

**Operations:**
```python
Function test_read_multiple Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_skip_primitive`
**Signature:** `def test_skip_primitive(self)`

**Operations:**
```python
Function test_skip_primitive Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_skip_constructed`
**Signature:** `def test_skip_constructed(self)`

**Operations:**
```python
Function test_skip_constructed Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `test_error_init`
**Signature:** `def test_error_init(self)`

**Operations:**
```python
Function test_error_init Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_error_stack`
**Signature:** `def test_error_stack(self)`

**Operations:**
```python
Function test_error_stack Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_no_input`
**Signature:** `def test_no_input(self)`

**Operations:**
```python
Function test_no_input Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_error_missing_tag_bytes`
**Signature:** `def test_error_missing_tag_bytes(self)`

**Operations:**
```python
Function test_error_missing_tag_bytes Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:start`, `temp_repo/src/asn1.py:_emit_length_long`, `temp_repo/src/asn1.py:_emit_length_short`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_encode_integer`, `temp_repo/src/asn1.py:_emit_tag_long`, `temp_repo/src/asn1.py:_encode_object_identifier`, `temp_repo/src/asn1.py:_emit_tag_short`, `temp_repo/src/asn1.py:_encode_boolean`, `temp_repo/src/asn1.py:_encode_null`

---

#### Function: `test_error_no_length_bytes`
**Signature:** `def test_error_no_length_bytes(self)`

**Operations:**
```python
Function test_error_no_length_bytes Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:leave`, `temp_repo/src/asn1.py:_emit_length_short`, `temp_repo/src/asn1.py:_decode_null`, `temp_repo/src/asn1.py:_emit_length_long`, `temp_repo/src/asn1.py:_decode_boolean`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:write`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_emit_tag_short`, `temp_repo/src/asn1.py:start`, `temp_repo/src/asn1.py:_encode_integer`, `temp_repo/src/asn1.py:_encode_object_identifier`, `temp_repo/src/asn1.py:_read_bytes`, `temp_repo/src/asn1.py:_end_of_input`, `temp_repo/src/asn1.py:_encode_boolean`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_emit_tag_long`, `temp_repo/src/asn1.py:_encode_null`, `temp_repo/src/asn1.py:output`

---

#### Function: `test_error_missing_length_bytes`
**Signature:** `def test_error_missing_length_bytes(self)`

**Operations:**
```python
Function test_error_missing_length_bytes Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:leave`, `temp_repo/src/asn1.py:_emit_length_short`, `temp_repo/src/asn1.py:_decode_null`, `temp_repo/src/asn1.py:_emit_length_long`, `temp_repo/src/asn1.py:_decode_boolean`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:write`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_emit_tag_short`, `temp_repo/src/asn1.py:start`, `temp_repo/src/asn1.py:_encode_integer`, `temp_repo/src/asn1.py:_encode_object_identifier`, `temp_repo/src/asn1.py:_read_bytes`, `temp_repo/src/asn1.py:_end_of_input`, `temp_repo/src/asn1.py:_encode_boolean`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_emit_tag_long`, `temp_repo/src/asn1.py:_encode_null`, `temp_repo/src/asn1.py:output`

---

#### Function: `test_error_too_many_length_bytes`
**Signature:** `def test_error_too_many_length_bytes(self)`

**Operations:**
```python
Function test_error_too_many_length_bytes Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:leave`, `temp_repo/src/asn1.py:_emit_length_short`, `temp_repo/src/asn1.py:_decode_null`, `temp_repo/src/asn1.py:_emit_length_long`, `temp_repo/src/asn1.py:_decode_boolean`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:write`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_emit_tag_short`, `temp_repo/src/asn1.py:start`, `temp_repo/src/asn1.py:_encode_integer`, `temp_repo/src/asn1.py:_encode_object_identifier`, `temp_repo/src/asn1.py:_read_bytes`, `temp_repo/src/asn1.py:_end_of_input`, `temp_repo/src/asn1.py:_encode_boolean`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_emit_tag_long`, `temp_repo/src/asn1.py:_encode_null`, `temp_repo/src/asn1.py:output`

---

#### Function: `test_error_no_value_bytes`
**Signature:** `def test_error_no_value_bytes(self)`

**Operations:**
```python
Function test_error_no_value_bytes Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:start`, `temp_repo/src/asn1.py:_emit_length_long`, `temp_repo/src/asn1.py:_emit_length_short`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_encode_integer`, `temp_repo/src/asn1.py:_emit_tag_long`, `temp_repo/src/asn1.py:_encode_object_identifier`, `temp_repo/src/asn1.py:_emit_tag_short`, `temp_repo/src/asn1.py:_encode_boolean`, `temp_repo/src/asn1.py:_encode_null`

---

#### Function: `test_error_missing_value_bytes`
**Signature:** `def test_error_missing_value_bytes(self)`

**Operations:**
```python
Function test_error_missing_value_bytes Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:start`, `temp_repo/src/asn1.py:_emit_length_long`, `temp_repo/src/asn1.py:_emit_length_short`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_encode_integer`, `temp_repo/src/asn1.py:_emit_tag_long`, `temp_repo/src/asn1.py:_encode_object_identifier`, `temp_repo/src/asn1.py:_emit_tag_short`, `temp_repo/src/asn1.py:_encode_boolean`, `temp_repo/src/asn1.py:_encode_null`

---

#### Function: `test_error_non_normalized_positive_integer`
**Signature:** `def test_error_non_normalized_positive_integer(self)`

**Operations:**
```python
Function test_error_non_normalized_positive_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_error_non_normalized_negative_integer`
**Signature:** `def test_error_non_normalized_negative_integer(self)`

**Operations:**
```python
Function test_error_non_normalized_negative_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_error_non_normalised_object_identifier`
**Signature:** `def test_error_non_normalised_object_identifier(self)`

**Operations:**
```python
Function test_error_non_normalised_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_error_bitstring_with_too_many_unused_bits`
**Signature:** `def test_error_bitstring_with_too_many_unused_bits(self)`

**Operations:**
```python
Function test_error_bitstring_with_too_many_unused_bits Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `test_big_negative_integer`
**Signature:** `def test_big_negative_integer(self)`

**Operations:**
```python
Function test_big_negative_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_mix_context_universal`
**Signature:** `def test_mix_context_universal(self)`

**Operations:**
```python
Function test_mix_context_universal Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `assert_encode_decode`
**Signature:** `def assert_encode_decode(v, t)`

**Operations:**
```python
Function assert_encode_decode Validates expected behavior and Makes API requests and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_boolean`
**Signature:** `def test_boolean(self)`

**Operations:**
```python
Function test_boolean Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_big_numbers`
**Signature:** `def test_big_numbers(self)`

**Operations:**
```python
Function test_big_numbers Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_big_negative_numbers`
**Signature:** `def test_big_negative_numbers(self)`

**Operations:**
```python
Function test_big_negative_numbers Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_bitstring`
**Signature:** `def test_bitstring(self)`

**Operations:**
```python
Function test_bitstring Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `test_octet_string`
**Signature:** `def test_octet_string(self)`

**Operations:**
```python
Function test_octet_string Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `test_null`
**Signature:** `def test_null(self)`

**Operations:**
```python
Function test_null Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_real_object_identifier`
**Signature:** `def test_real_object_identifier(self)`

**Operations:**
```python
Function test_real_object_identifier Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_long_object_identifier`
**Signature:** `def test_long_object_identifier(self)`

**Operations:**
```python
Function test_long_object_identifier Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_enumerated`
**Signature:** `def test_enumerated(self)`

**Operations:**
```python
Function test_enumerated Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_utf8_string`
**Signature:** `def test_utf8_string(self)`

**Operations:**
```python
Function test_utf8_string Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `test_printable_string`
**Signature:** `def test_printable_string(self)`

**Operations:**
```python
Function test_printable_string Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `test_ia5_string`
**Signature:** `def test_ia5_string(self)`

**Operations:**
```python
Function test_ia5_string Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `test_utc_time`
**Signature:** `def test_utc_time(self)`

**Operations:**
```python
Function test_utc_time Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_generalized_time`
**Signature:** `def test_generalized_time(self)`

**Operations:**
```python
Function test_generalized_time Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `test_unicode_string`
**Signature:** `def test_unicode_string(self)`

**Operations:**
```python
Function test_unicode_string Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

### File: `asn1.py`

#### Function: `__init__`
**Signature:** `def __init__(self)`

**Operations:**
```python
Function __init__ Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `start`
**Signature:** `def start(self)`

**Operations:**
```python
Function start Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `bytes`, `isinstance`, `Error`
- Called by: None

---

#### Function: `enter`
**Signature:** `def enter(self, nr)`

**Operations:**
```python
Function enter Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `Error`
- Called by: None

---

#### Function: `leave`
**Signature:** `def leave(self)`

**Operations:**
```python
Function leave Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `len`, `Error`
- Called by: None

---

#### Function: `construct`
**Signature:** `def construct(self, nr)`

**Operations:**
```python
Function construct Makes API requests and Handles string operations
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `write`
**Signature:** `def write(self, value)`

**Operations:**
```python
Function write Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `isinstance`, `len`, `Error`
- Called by: None

---

#### Function: `output`
**Signature:** `def output(self)`

**Operations:**
```python
Function output Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `len`, `Error`
- Called by: None

---

#### Function: `_emit_tag`
**Signature:** `def _emit_tag(self, nr, typ, cls)`

**Operations:**
```python
Function _emit_tag Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `_emit_tag_short`
**Signature:** `def _emit_tag_short(self, nr, typ, cls)`

**Operations:**
```python
Function _emit_tag_short Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `bytes`
- Called by: None

---

#### Function: `_emit_tag_long`
**Signature:** `def _emit_tag_long(self, nr, typ, cls)`

**Operations:**
```python
Function _emit_tag_long Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `bytes`
- Called by: None

---

#### Function: `_emit_length`
**Signature:** `def _emit_length(self, length)`

**Operations:**
```python
Function _emit_length Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_emit_length_long`, `temp_repo/src/asn1.py:leave`, `temp_repo/src/asn1.py:_decode_boolean`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:write`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_encode_integer`, `temp_repo/src/asn1.py:_decode_null`, `temp_repo/src/asn1.py:_read_bytes`, `temp_repo/src/asn1.py:_end_of_input`, `temp_repo/src/asn1.py:output`

---

#### Function: `_emit_length_short`
**Signature:** `def _emit_length_short(self, length)`

**Operations:**
```python
Function _emit_length_short Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `bytes`
- Called by: `temp_repo/src/asn1.py:_emit_length_long`, `temp_repo/src/asn1.py:leave`, `temp_repo/src/asn1.py:_decode_boolean`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:write`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_encode_integer`, `temp_repo/src/asn1.py:_decode_null`, `temp_repo/src/asn1.py:_read_bytes`, `temp_repo/src/asn1.py:_end_of_input`, `temp_repo/src/asn1.py:output`

---

#### Function: `_emit_length_long`
**Signature:** `def _emit_length_long(self, length)`

**Operations:**
```python
Function _emit_length_long Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `bytes`, `len`
- Called by: `temp_repo/src/asn1.py:_emit_length_long`, `temp_repo/src/asn1.py:leave`, `temp_repo/src/asn1.py:_decode_boolean`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:write`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_encode_integer`, `temp_repo/src/asn1.py:_decode_null`, `temp_repo/src/asn1.py:_read_bytes`, `temp_repo/src/asn1.py:_end_of_input`, `temp_repo/src/asn1.py:output`

---

#### Function: `_emit`
**Signature:** `def _emit(self, s)`

**Operations:**
```python
Function _emit Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `isinstance`
- Called by: None

---

#### Function: `_encode_value`
**Signature:** `def _encode_value(self, cls, nr, value)`

**Operations:**
```python
Function _encode_value Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `_encode_boolean`
**Signature:** `def _encode_boolean(value)`

**Operations:**
```python
Function _encode_boolean Performs unit testing and Validates input data and Handles string operations
```

**Dependencies:**
- Calls: `bytes`
- Called by: None

---

#### Function: `_encode_integer`
**Signature:** `def _encode_integer(value)`

**Operations:**
```python
Function _encode_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `bytes`, `len`, `range`
- Called by: `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `_encode_octet_string`
**Signature:** `def _encode_octet_string(value)`

**Operations:**
```python
Function _encode_octet_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations
```

**Dependencies:**
- Calls: `isinstance`
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `_encode_bit_string`
**Signature:** `def _encode_bit_string(value)`

**Operations:**
```python
Function _encode_bit_string Performs unit testing and Validates expected behavior and Validates input data and Handles string operations
```

**Dependencies:**
- Calls: `isinstance`
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `_encode_null`
**Signature:** `def _encode_null()`

**Operations:**
```python
Function _encode_null Performs unit testing and Validates input data and Handles string operations
```

**Dependencies:**
- Calls: `bytes`
- Called by: None

---

#### Function: `_encode_object_identifier`
**Signature:** `def _encode_object_identifier(self, oid)`

**Operations:**
```python
Function _encode_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `bytes`, `list`, `map`, `Error`
- Called by: None

---

#### Function: `__init__`
**Signature:** `def __init__(self)`

**Operations:**
```python
Function __init__ Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `start`
**Signature:** `def start(self, data)`

**Operations:**
```python
Function start Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `bytes`, `isinstance`, `Error`
- Called by: None

---

#### Function: `peek`
**Signature:** `def peek(self)`

**Operations:**
```python
Function peek Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `Error`
- Called by: None

---

#### Function: `read`
**Signature:** `def read(self)`

**Operations:**
```python
Function read Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `Error`
- Called by: None

---

#### Function: `eof`
**Signature:** `def eof(self)`

**Operations:**
```python
Function eof Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `enter`
**Signature:** `def enter(self)`

**Operations:**
```python
Function enter Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `Error`
- Called by: None

---

#### Function: `leave`
**Signature:** `def leave(self)`

**Operations:**
```python
Function leave Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `len`, `Error`
- Called by: None

---

#### Function: `_read_tag`
**Signature:** `def _read_tag(self)`

**Operations:**
```python
Function _read_tag Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `Tag`
- Called by: None

---

#### Function: `_read_length`
**Signature:** `def _read_length(self)`

**Operations:**
```python
Function _read_length Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `Error`, `int`
- Called by: `temp_repo/src/asn1.py:_emit_length_long`, `temp_repo/src/asn1.py:leave`, `temp_repo/src/asn1.py:_decode_boolean`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:write`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_encode_integer`, `temp_repo/src/asn1.py:_decode_null`, `temp_repo/src/asn1.py:_read_bytes`, `temp_repo/src/asn1.py:_end_of_input`, `temp_repo/src/asn1.py:output`

---

#### Function: `_read_value`
**Signature:** `def _read_value(self, cls, nr, length)`

**Operations:**
```python
Function _read_value Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: None

---

#### Function: `_read_byte`
**Signature:** `def _read_byte(self)`

**Operations:**
```python
Function _read_byte Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `Error`
- Called by: None

---

#### Function: `_read_bytes`
**Signature:** `def _read_bytes(self, count)`

**Operations:**
```python
Function _read_bytes Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `len`, `Error`
- Called by: `temp_repo/src/asn1.py:start`, `temp_repo/src/asn1.py:_emit_length_long`, `temp_repo/src/asn1.py:_emit_length_short`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_encode_integer`, `temp_repo/src/asn1.py:_emit_tag_long`, `temp_repo/src/asn1.py:_encode_object_identifier`, `temp_repo/src/asn1.py:_emit_tag_short`, `temp_repo/src/asn1.py:_encode_boolean`, `temp_repo/src/asn1.py:_encode_null`

---

#### Function: `_end_of_input`
**Signature:** `def _end_of_input(self)`

**Operations:**
```python
Function _end_of_input Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `len`
- Called by: None

---

#### Function: `_decode_boolean`
**Signature:** `def _decode_boolean(bytes_data)`

**Operations:**
```python
Function _decode_boolean Performs unit testing and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `len`, `Error`
- Called by: None

---

#### Function: `_decode_integer`
**Signature:** `def _decode_integer(bytes_data)`

**Operations:**
```python
Function _decode_integer Performs unit testing and Validates expected behavior and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `range`, `len`, `Error`, `int`
- Called by: `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `_decode_octet_string`
**Signature:** `def _decode_octet_string(bytes_data)`

**Operations:**
```python
Function _decode_octet_string Handles string operations
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `_decode_null`
**Signature:** `def _decode_null(bytes_data)`

**Operations:**
```python
Function _decode_null Performs unit testing and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `len`, `Error`
- Called by: None

---

#### Function: `_decode_object_identifier`
**Signature:** `def _decode_object_identifier(bytes_data)`

**Operations:**
```python
Function _decode_object_identifier Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `list`, `map`, `range`, `str`, `len`, `Error`, `int`
- Called by: None

---

#### Function: `_decode_printable_string`
**Signature:** `def _decode_printable_string(bytes_data)`

**Operations:**
```python
Function _decode_printable_string Makes API requests and Handles string operations
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_read_length`

---

#### Function: `_decode_bitstring`
**Signature:** `def _decode_bitstring(bytes_data)`

**Operations:**
```python
Function _decode_bitstring Performs unit testing and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `len`, `range`, `bytes`, `bytearray`, `Error`, `int`
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

### File: `dump.py`

#### Function: `read_pem`
**Signature:** `def read_pem(input_file)`

**Operations:**
```python
Function read_pem Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `ValueError`
- Called by: None

---

#### Function: `tag_id_to_string`
**Signature:** `def tag_id_to_string(identifier)`

**Operations:**
```python
Function tag_id_to_string Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:pretty_print`, `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `class_id_to_string`
**Signature:** `def class_id_to_string(identifier)`

**Operations:**
```python
Function class_id_to_string Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `ValueError`
- Called by: `temp_repo/examples/dump.py:pretty_print`, `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `object_identifier_to_string`
**Signature:** `def object_identifier_to_string(identifier)`

**Operations:**
```python
Function object_identifier_to_string Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: None
- Called by: `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `value_to_string`
**Signature:** `def value_to_string(tag_number, value)`

**Operations:**
```python
Function value_to_string Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `str`, `isinstance`, `repr`, `object_identifier_to_string`
- Called by: `temp_repo/examples/dump.py:pretty_print`, `temp_repo/examples/dump.py:value_to_string`, `temp_repo/src/asn1.py:_decode_object_identifier`

---

#### Function: `pretty_print`
**Signature:** `def pretty_print(input_stream, output_stream)`

**Operations:**
```python
Function pretty_print Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

**Dependencies:**
- Calls: `tag_id_to_string`, `value_to_string`, `pretty_print`, `class_id_to_string`
- Called by: `temp_repo/src/asn1.py:_decode_object_identifier`, `temp_repo/src/asn1.py:_decode_integer`, `temp_repo/src/asn1.py:_decode_bitstring`, `temp_repo/examples/dump.py:pretty_print`, `temp_repo/src/asn1.py:_read_length`

---


## Call Stack Visualization

```mermaid
flowchart TD
```

### `read`
**Location**: `setup.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `join`
- `dirname`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function read Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_boolean`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_boolean Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_integer`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `isinstance`

#### Called By:
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_long_integer`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_long_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_negative_integer`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_negative_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_long_negative_integer`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_long_negative_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_twos_complement_boundaries`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_twos_complement_boundaries Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_octet_string`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function test_octet_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_bitstring`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function test_bitstring Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_printable_string`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_printable_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_unicode_octet_string`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function test_unicode_octet_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_unicode_printable_string`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_unicode_printable_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_null`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_null Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_object_identifier`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_long_object_identifier`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_long_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_real_object_identifier`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_real_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_enumerated`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_enumerated Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_sequence`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_sequence Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_sequence_of`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_sequence_of Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_set`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_set Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_set_of`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_set_of Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_context`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_context Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_application`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_application Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_private`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_private Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_long_tag_id`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_long_tag_id Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_contextmanager_construct`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function test_contextmanager_construct Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_contextmanager_calls_enter`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `TestEncoder`
- `RuntimeError`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_contextmanager_calls_enter Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `enter`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `RuntimeError`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function enter Performs unit testing and Validates input data
```

---

### `test_contextmanager_calls_leave`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `TestEncoder`
- `RuntimeError`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_contextmanager_calls_leave Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `leave`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `RuntimeError`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function leave Performs unit testing and Validates input data
```

---

### `test_long_tag_length`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_emit_length_long`
- `temp_repo/src/asn1.py:leave`
- `temp_repo/src/asn1.py:_decode_boolean`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:write`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_encode_integer`
- `temp_repo/src/asn1.py:_decode_null`
- `temp_repo/src/asn1.py:_read_bytes`
- `temp_repo/src/asn1.py:_end_of_input`
- `temp_repo/src/asn1.py:output`
</details>

#### Analysis
```python
Function test_long_tag_length Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_init`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_error_init Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_stack`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_error_stack Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_object_identifier`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_error_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_default_encoding`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `check_defaults`
- `type`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_default_encoding Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `check_defaults`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `type`

#### Called By:
- `temp_repo/tests/test_asn1.py:test_default_encoding`
</details>

#### Analysis
```python
Function check_defaults Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_context_no_tag_number`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_context_no_tag_number Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_context_with_tag_number_10`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_context_with_tag_number_10 Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_boolean`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_boolean Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_integer`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `isinstance`

#### Called By:
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_long_integer`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_long_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_negative_integer`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_negative_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_long_negative_integer`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_long_negative_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_twos_complement_boundaries`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_twos_complement_boundaries Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_octet_string`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function test_octet_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_printable_string`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_printable_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_bitstring`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function test_bitstring Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_bitstring_unused_bits`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function test_bitstring_unused_bits Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_unicode_printable_string`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_unicode_printable_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_null`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_null Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_object_identifier`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_long_object_identifier`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_long_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_real_object_identifier`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_real_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_enumerated`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_enumerated Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_sequence`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_sequence Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_sequence_of`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_sequence_of Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_set`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_set Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_set_of`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_set_of Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_context`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_context Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_application`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_application Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_private`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_private Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_long_tag_id`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_long_tag_id Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_long_tag_length`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_emit_length_long`
- `temp_repo/src/asn1.py:leave`
- `temp_repo/src/asn1.py:_decode_boolean`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:write`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_encode_integer`
- `temp_repo/src/asn1.py:_decode_null`
- `temp_repo/src/asn1.py:_read_bytes`
- `temp_repo/src/asn1.py:_end_of_input`
- `temp_repo/src/asn1.py:output`
</details>

#### Analysis
```python
Function test_long_tag_length Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_read_multiple`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_read_multiple Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_skip_primitive`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_skip_primitive Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_skip_constructed`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function test_skip_constructed Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_init`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_error_init Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_stack`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_error_stack Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_no_input`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_no_input Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_missing_tag_bytes`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:start`
- `temp_repo/src/asn1.py:_emit_length_long`
- `temp_repo/src/asn1.py:_emit_length_short`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_encode_integer`
- `temp_repo/src/asn1.py:_emit_tag_long`
- `temp_repo/src/asn1.py:_encode_object_identifier`
- `temp_repo/src/asn1.py:_emit_tag_short`
- `temp_repo/src/asn1.py:_encode_boolean`
- `temp_repo/src/asn1.py:_encode_null`
</details>

#### Analysis
```python
Function test_error_missing_tag_bytes Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_no_length_bytes`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:leave`
- `temp_repo/src/asn1.py:_emit_length_short`
- `temp_repo/src/asn1.py:_decode_null`
- `temp_repo/src/asn1.py:_emit_length_long`
- `temp_repo/src/asn1.py:_decode_boolean`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:write`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_emit_tag_short`
- `temp_repo/src/asn1.py:start`
- `temp_repo/src/asn1.py:_encode_integer`
- `temp_repo/src/asn1.py:_encode_object_identifier`
- `temp_repo/src/asn1.py:_read_bytes`
- `temp_repo/src/asn1.py:_end_of_input`
- `temp_repo/src/asn1.py:_encode_boolean`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_emit_tag_long`
- `temp_repo/src/asn1.py:_encode_null`
- `temp_repo/src/asn1.py:output`
</details>

#### Analysis
```python
Function test_error_no_length_bytes Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_missing_length_bytes`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:leave`
- `temp_repo/src/asn1.py:_emit_length_short`
- `temp_repo/src/asn1.py:_decode_null`
- `temp_repo/src/asn1.py:_emit_length_long`
- `temp_repo/src/asn1.py:_decode_boolean`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:write`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_emit_tag_short`
- `temp_repo/src/asn1.py:start`
- `temp_repo/src/asn1.py:_encode_integer`
- `temp_repo/src/asn1.py:_encode_object_identifier`
- `temp_repo/src/asn1.py:_read_bytes`
- `temp_repo/src/asn1.py:_end_of_input`
- `temp_repo/src/asn1.py:_encode_boolean`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_emit_tag_long`
- `temp_repo/src/asn1.py:_encode_null`
- `temp_repo/src/asn1.py:output`
</details>

#### Analysis
```python
Function test_error_missing_length_bytes Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_too_many_length_bytes`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:leave`
- `temp_repo/src/asn1.py:_emit_length_short`
- `temp_repo/src/asn1.py:_decode_null`
- `temp_repo/src/asn1.py:_emit_length_long`
- `temp_repo/src/asn1.py:_decode_boolean`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:write`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_emit_tag_short`
- `temp_repo/src/asn1.py:start`
- `temp_repo/src/asn1.py:_encode_integer`
- `temp_repo/src/asn1.py:_encode_object_identifier`
- `temp_repo/src/asn1.py:_read_bytes`
- `temp_repo/src/asn1.py:_end_of_input`
- `temp_repo/src/asn1.py:_encode_boolean`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_emit_tag_long`
- `temp_repo/src/asn1.py:_encode_null`
- `temp_repo/src/asn1.py:output`
</details>

#### Analysis
```python
Function test_error_too_many_length_bytes Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_no_value_bytes`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:start`
- `temp_repo/src/asn1.py:_emit_length_long`
- `temp_repo/src/asn1.py:_emit_length_short`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_encode_integer`
- `temp_repo/src/asn1.py:_emit_tag_long`
- `temp_repo/src/asn1.py:_encode_object_identifier`
- `temp_repo/src/asn1.py:_emit_tag_short`
- `temp_repo/src/asn1.py:_encode_boolean`
- `temp_repo/src/asn1.py:_encode_null`
</details>

#### Analysis
```python
Function test_error_no_value_bytes Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_missing_value_bytes`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:start`
- `temp_repo/src/asn1.py:_emit_length_long`
- `temp_repo/src/asn1.py:_emit_length_short`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_encode_integer`
- `temp_repo/src/asn1.py:_emit_tag_long`
- `temp_repo/src/asn1.py:_encode_object_identifier`
- `temp_repo/src/asn1.py:_emit_tag_short`
- `temp_repo/src/asn1.py:_encode_boolean`
- `temp_repo/src/asn1.py:_encode_null`
</details>

#### Analysis
```python
Function test_error_missing_value_bytes Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_non_normalized_positive_integer`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_error_non_normalized_positive_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_non_normalized_negative_integer`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_error_non_normalized_negative_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_non_normalised_object_identifier`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_error_non_normalised_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_error_bitstring_with_too_many_unused_bits`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function test_error_bitstring_with_too_many_unused_bits Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_big_negative_integer`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_big_negative_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `test_mix_context_universal`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_mix_context_universal Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `assert_encode_decode`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function assert_encode_decode Validates expected behavior and Makes API requests and Performs comparisons
```

---

### `test_boolean`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_boolean Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `test_big_numbers`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_big_numbers Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `test_big_negative_numbers`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_big_negative_numbers Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `test_bitstring`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function test_bitstring Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `test_octet_string`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function test_octet_string Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `test_null`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_null Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `test_real_object_identifier`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_real_object_identifier Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `test_long_object_identifier`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_long_object_identifier Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `test_enumerated`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_enumerated Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `test_utf8_string`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function test_utf8_string Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `test_printable_string`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function test_printable_string Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `test_ia5_string`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function test_ia5_string Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `test_utc_time`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_utc_time Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `test_generalized_time`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function test_generalized_time Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `test_unicode_string`
**Location**: `test_asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function test_unicode_string Validates expected behavior and Makes API requests and Handles string operations and Performs comparisons
```

---

### `__init__`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function __init__ Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `start`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `bytes`
- `isinstance`
- `Error`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function start Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `enter`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `Error`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function enter Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `leave`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `len`
- `Error`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function leave Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `construct`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function construct Makes API requests and Handles string operations
```

---

### `write`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `isinstance`
- `len`
- `Error`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function write Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `output`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `len`
- `Error`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function output Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_emit_tag`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _emit_tag Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_emit_tag_short`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `bytes`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _emit_tag_short Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_emit_tag_long`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `bytes`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _emit_tag_long Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_emit_length`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_emit_length_long`
- `temp_repo/src/asn1.py:leave`
- `temp_repo/src/asn1.py:_decode_boolean`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:write`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_encode_integer`
- `temp_repo/src/asn1.py:_decode_null`
- `temp_repo/src/asn1.py:_read_bytes`
- `temp_repo/src/asn1.py:_end_of_input`
- `temp_repo/src/asn1.py:output`
</details>

#### Analysis
```python
Function _emit_length Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_emit_length_short`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `bytes`

#### Called By:
- `temp_repo/src/asn1.py:_emit_length_long`
- `temp_repo/src/asn1.py:leave`
- `temp_repo/src/asn1.py:_decode_boolean`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:write`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_encode_integer`
- `temp_repo/src/asn1.py:_decode_null`
- `temp_repo/src/asn1.py:_read_bytes`
- `temp_repo/src/asn1.py:_end_of_input`
- `temp_repo/src/asn1.py:output`
</details>

#### Analysis
```python
Function _emit_length_short Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_emit_length_long`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `bytes`
- `len`

#### Called By:
- `temp_repo/src/asn1.py:_emit_length_long`
- `temp_repo/src/asn1.py:leave`
- `temp_repo/src/asn1.py:_decode_boolean`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:write`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_encode_integer`
- `temp_repo/src/asn1.py:_decode_null`
- `temp_repo/src/asn1.py:_read_bytes`
- `temp_repo/src/asn1.py:_end_of_input`
- `temp_repo/src/asn1.py:output`
</details>

#### Analysis
```python
Function _emit_length_long Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_emit`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `isinstance`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _emit Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_encode_value`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _encode_value Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_encode_boolean`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `bytes`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _encode_boolean Performs unit testing and Validates input data and Handles string operations
```

---

### `_encode_integer`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `bytes`
- `len`
- `range`

#### Called By:
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function _encode_integer Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_encode_octet_string`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `isinstance`

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function _encode_octet_string Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations
```

---

### `_encode_bit_string`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `isinstance`

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function _encode_bit_string Performs unit testing and Validates expected behavior and Validates input data and Handles string operations
```

---

### `_encode_null`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `bytes`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _encode_null Performs unit testing and Validates input data and Handles string operations
```

---

### `_encode_object_identifier`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `bytes`
- `list`
- `map`
- `Error`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _encode_object_identifier Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `__init__`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function __init__ Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `start`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `bytes`
- `isinstance`
- `Error`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function start Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `peek`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `Error`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function peek Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `read`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `Error`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function read Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `eof`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function eof Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `enter`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `Error`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function enter Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `leave`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `len`
- `Error`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function leave Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_read_tag`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `Tag`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _read_tag Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_read_length`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `Error`
- `int`

#### Called By:
- `temp_repo/src/asn1.py:_emit_length_long`
- `temp_repo/src/asn1.py:leave`
- `temp_repo/src/asn1.py:_decode_boolean`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:write`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_encode_integer`
- `temp_repo/src/asn1.py:_decode_null`
- `temp_repo/src/asn1.py:_read_bytes`
- `temp_repo/src/asn1.py:_end_of_input`
- `temp_repo/src/asn1.py:output`
</details>

#### Analysis
```python
Function _read_length Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_read_value`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _read_value Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_read_byte`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `Error`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _read_byte Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_read_bytes`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `len`
- `Error`

#### Called By:
- `temp_repo/src/asn1.py:start`
- `temp_repo/src/asn1.py:_emit_length_long`
- `temp_repo/src/asn1.py:_emit_length_short`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_encode_integer`
- `temp_repo/src/asn1.py:_emit_tag_long`
- `temp_repo/src/asn1.py:_encode_object_identifier`
- `temp_repo/src/asn1.py:_emit_tag_short`
- `temp_repo/src/asn1.py:_encode_boolean`
- `temp_repo/src/asn1.py:_encode_null`
</details>

#### Analysis
```python
Function _read_bytes Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_end_of_input`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `len`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _end_of_input Performs unit testing and Validates expected behavior and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_decode_boolean`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `len`
- `Error`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _decode_boolean Performs unit testing and Validates input data and Handles string operations and Performs comparisons
```

---

### `_decode_integer`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `range`
- `len`
- `Error`
- `int`

#### Called By:
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function _decode_integer Performs unit testing and Validates expected behavior and Validates input data and Handles string operations and Performs comparisons
```

---

### `_decode_octet_string`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function _decode_octet_string Handles string operations
```

---

### `_decode_null`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `len`
- `Error`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _decode_null Performs unit testing and Validates input data and Handles string operations and Performs comparisons
```

---

### `_decode_object_identifier`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `list`
- `map`
- `range`
- `str`
- `len`
- `Error`
- `int`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function _decode_object_identifier Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `_decode_printable_string`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function _decode_printable_string Makes API requests and Handles string operations
```

---

### `_decode_bitstring`
**Location**: `asn1.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `len`
- `range`
- `bytes`
- `bytearray`
- `Error`
- `int`

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function _decode_bitstring Performs unit testing and Validates input data and Handles string operations and Performs comparisons
```

---

### `read_pem`
**Location**: `dump.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `ValueError`

#### Called By:
- No incoming calls
</details>

#### Analysis
```python
Function read_pem Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `tag_id_to_string`
**Location**: `dump.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:pretty_print`
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function tag_id_to_string Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `class_id_to_string`
**Location**: `dump.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `ValueError`

#### Called By:
- `temp_repo/examples/dump.py:pretty_print`
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function class_id_to_string Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `object_identifier_to_string`
**Location**: `dump.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- No outgoing calls

#### Called By:
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function object_identifier_to_string Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `value_to_string`
**Location**: `dump.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `str`
- `isinstance`
- `repr`
- `object_identifier_to_string`

#### Called By:
- `temp_repo/examples/dump.py:pretty_print`
- `temp_repo/examples/dump.py:value_to_string`
- `temp_repo/src/asn1.py:_decode_object_identifier`
</details>

#### Analysis
```python
Function value_to_string Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

### `pretty_print`
**Location**: `dump.py`

<details>
<summary>Dependencies</summary>

#### Calls:
- `tag_id_to_string`
- `value_to_string`
- `pretty_print`
- `class_id_to_string`

#### Called By:
- `temp_repo/src/asn1.py:_decode_object_identifier`
- `temp_repo/src/asn1.py:_decode_integer`
- `temp_repo/src/asn1.py:_decode_bitstring`
- `temp_repo/examples/dump.py:pretty_print`
- `temp_repo/src/asn1.py:_read_length`
</details>

#### Analysis
```python
Function pretty_print Performs unit testing and Makes API requests and Validates input data and Handles string operations and Performs comparisons
```

---

## Code Analysis

### setup.py
```python
# File: temp_repo/setup.py
No description available
```

### conf.py
```python
# File: temp_repo/docs/conf.py
No description available
```

### test_asn1.py
```python
# File: temp_repo/tests/test_asn1.py
No description available
```

### asn1.py
```python
# File: temp_repo/src/asn1.py
No description available
```

### dump.py
```python
# File: temp_repo/examples/dump.py
No description available
```

## Function Call Stacks

