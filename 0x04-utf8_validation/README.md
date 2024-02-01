#0x04.  UTF-8 Validation

## Description
UTF-8 is a character encoding capable of encoding all possible characters, known as Unicode characters. The encoding is variable-length, where each character can be represented by 1 to 4 bytes.

To ensure proper UTF-8 encoding, a sequence of bytes must adhere to the following rules:
1. For a single-byte character, the first bit must be 0.
2. For an n-byte character, the first byte starts with n 1's, followed by a 0. The following n-1 bytes all start with 10.
3. A character in UTF-8 can be from 1 to 4 bytes long.
4. For input strings containing multiple characters, the input bytes are broken down into groups. Each group is checked for valid UTF-8 encoding according to the above rules.

## Functionality
The implementation provides a function `utf8_validation` to validate whether a given list of integers representing bytes is a valid UTF-8 encoding.

### Method Signature
```python
def utf8_validation(data: List[int]) -> bool:
    pass
```

### Input
- `data`: A list of integers where each integer represents a byte.

### Output
- `True` if the given data is a valid UTF-8 encoding.
- `False` otherwise.

### Example
```python
data = [197, 130, 1]  # [11000101, 10000010, 00000001]
result = utf8_validation(data)
print(result)  # Output: True
```

## How to Use
1. Import the `utf8_validation` function from the module.
2. Provide a list of integers representing bytes as input to the function.
3. Receive the boolean output indicating whether the input data is a valid UTF-8 encoding.

## References
- [UTF-8 Encoding](https://en.wikipedia.org/wiki/UTF-8)
- [Unicode Characters](https://unicode-table.com/en/)
- [Python List](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
