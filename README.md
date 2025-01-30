# NumWord

![Manual Test](https://github.com/HarshitDalal/numword/actions/workflows/manual_test.yml/badge.svg)
![Daily Test](https://github.com/HarshitDalal/numword/actions/workflows/daily_test.yml/badge.svg)
![PyPI](https://img.shields.io/pypi/v/NumWord)
![PyPI Downloads](https://img.shields.io/pypi/dm/NumWord)
![License MIT](https://img.shields.io/github/license/HarshitDalal/numword)
![Code Coverage](https://img.shields.io/codecov/c/github/HarshitDalal/numword)

NumWord is a Python package that converts numbers written in words to their numerical representation.

## Features

- Convert single digits, two digits, large numbers, decimal numbers, and mixed numbers from words to numbers.
- Convert numbers to words.
- Supports English language.

## Installation

To install the package, use pip:

```bash
pip install -r requirements.txt
```

## Usage
Here is an example of how to use the NumWord package:

```python
from NumWord import WordToNumber, NumberToWord

# Convert words to numbers
word_to_num_converter = WordToNumber(lang='en')
result = word_to_num_converter.convert("one hundred twenty three point four five six")
print(result)  # Output: 123.456

# Convert numbers to words
num_to_word_converter = NumberToWord(lang='en')
result = num_to_word_converter.convert(123.456)
print(result)  # Output: one hundred twenty three point four five six
``` 
## Running Tests
To run the tests, use the following command:
```bash
python -m unittest discover tests
```

## License
This project is licensed under the MIT License - see the MIT License file for details.

