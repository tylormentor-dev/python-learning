# Using Popular Python Packages

## Overview

Python packages and libraries provide ready-made functionality that we can use in our programs.

Python has built-in modules, such as `json`, and third-party libraries, such as NumPy, pandas, and NLTK.

Before using a module or library, import it into your program with an `import` statement.

```python
import json
```

Third-party libraries usually need to be installed before they can be imported.

## 1. NumPy

NumPy is a Python library used for numerical calculations and working with arrays. Its main data structure is the `ndarray`, which supports efficient numerical operations.

### Example

```python
import numpy as np

a = np.zeros(10)
print(a)

b = np.full((2, 10), 0.7)
print(b)

c = np.linspace(0, 25, 7)
print(c)

print(type(c))
```

### Explanation

- `np.zeros(10)` creates an array containing 10 zeros.
- `np.full((2, 10), 0.7)` creates a two-dimensional array with 2 rows and 10 columns, filled with `0.7`.
- `np.linspace(0, 25, 7)` generates 7 equally spaced values between 0 and 25, including both endpoints.
- `type(c)` returns the type of the array, which is `numpy.ndarray`.

### Output

```text
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

[[0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7]
 [0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7]]

[ 0.          4.16666667  8.33333333 12.5
 16.66666667 20.83333333 25.        ]

<class 'numpy.ndarray'>
```

The variables `a`, `b`, and `c` are all NumPy arrays of type `ndarray`. Unlike regular Python lists, NumPy arrays are designed for efficient numerical operations.

## 2. pandas

pandas is a Python library used to organize, analyze, and manipulate data. It works closely with NumPy and other data science libraries.

One of its main structures is the `DataFrame`, which organizes data into rows and columns.

### Example

```python
import pandas as pd

a = pd.DataFrame({
    "Animals": ["Dog", "Cat", "Lion", "Cow", "Elephant"],
    "Sounds": ["Barks", "Meow", "Roars", "Moo", "Trumpet"]
})

print(a)
print(a.describe())

b = pd.DataFrame({
    "Letters": ["a", "b", "c", "d", "e", "f"],
    "Numbers": [12, 7, 9, 3, 5, 1]
})

print(b.sort_values(by="Numbers"))

b = b.assign(new_values=b["Numbers"] * 3)
print(b)
```

### Explanation

- `pd.DataFrame()` creates a table from the supplied data.
- `describe()` provides summary information about the columns. For the text columns in this example, it displays statistics such as count, unique values, the most frequent value, and its frequency.
- `sort_values(by="Numbers")` sorts the rows by the values in the `Numbers` column, in ascending order by default.
- `assign()` creates a new column called `new_values`, calculated by multiplying each value in `Numbers` by 3.

### Output

The first DataFrame:

```text
    Animals   Sounds
0       Dog    Barks
1       Cat     Meow
2      Lion    Roars
3       Cow      Moo
4  Elephant  Trumpet
```

Summary from `describe()`:

```text
         Animals Sounds
count           5      5
unique          5      5
top           Dog  Barks
freq            1      1
```

Sorted DataFrame:

```text
  Letters  Numbers
5       f        1
3       d        3
4       e        5
1       b        7
2       c        9
0       a       12
```

DataFrame after adding the new column:

```text
  Letters  Numbers  new_values
0       a       12          36
1       b        7          21
2       c        9          27
3       d        3           9
4       e        5          15
5       f        1           3
```

pandas provides many additional tools for sorting, filtering, cleaning, and analyzing datasets.

## 3. NLTK

NLTK stands for Natural Language Toolkit. It is a Python library used for Natural Language Processing (NLP), which involves working with human language.

NLTK provides tools for tasks such as tokenizing text and accessing collections of common words.

### Example

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = (
    "Lorem Ipsum is simply dummy text of the printing and typesetting "
    "industry. Lorem Ipsum has been the industry's standard dummy text "
    "ever since the 1500s, when an unknown printer took a galley of type "
    "and scrambled it to make a type specimen book."
)

# Split text into words and punctuation
print(word_tokenize(text))

# Split text into sentences
print(nltk.tokenize.sent_tokenize(text))

# Remove common English stopwords
stop_words = stopwords.words("english")
new_text = []

for word in text.split():
    if word.lower() not in stop_words:
        new_text.append(word)

print(new_text)
```

### Explanation

**`word_tokenize()`**

Splits text into individual tokens, including words and punctuation. It can also separate contractions into multiple tokens.

**`sent_tokenize()`**

Splits a block of text into individual sentences.

**Stopwords**

Stopwords are common words, such as "the", "a", and "is", that may be removed in some NLP tasks because they contribute less to the particular analysis.

**`stopwords.words("english")`**

Returns a list of common English stopwords.

**The `for` loop**

The loop checks each word against the stopword list. Words that are not stopwords are added to `new_text`.

Using `word.lower()` makes the comparison case-insensitive, so words such as `"The"` and `"the"` are treated consistently.

### Important note

The example uses `text.split()` for the stopword-removal step. Unlike `word_tokenize()`, `split()` does not separate punctuation from words. As a result, words with attached punctuation may not match the stopword list exactly.

NLTK contains many modules and subpackages. Import only the functionality your program needs rather than importing everything.

## Key Takeaways

- Use `import` to make a module or library available in your program.
- NumPy is used for numerical calculations and arrays.
- pandas is used for organizing and analyzing structured data.
- NLTK provides tools for processing human language.
- Import specific functions when appropriate to keep your code clear.
- Understand what a function does before using it in your program.

## Suggested Commit Message

`Add Using Popular Python Packages notes`

## Installing Python Packages

Python includes built-in modules, such as `json`, that do not normally require separate installation. Third-party packages, such as NumPy, pandas, and NLTK, generally need to be installed before they can be imported.

### Installation Commands

Use `pip` to install third-party packages from the command line or terminal.

```bash
python -m pip install numpy
python -m pip install pandas
python -m pip install nltk
```

You can install multiple packages in one command:

```bash
python -m pip install numpy pandas nltk
```

### Importing Packages

After installation, import the packages into your Python program.

```python
import numpy as np
import pandas as pd
import nltk
```

The names used during installation can differ from the aliases used when importing a package. For example, NumPy is commonly imported as `np`, and pandas as `pd`.

### Important Notes

- Install a third-party package before importing it into your program.
- Run installation commands in the terminal, not inside a regular Python script.
- If you are using a virtual environment, activate it before installing packages so they are installed in the correct environment.
- Some libraries, including NLTK, may require additional data downloads before certain features work.

### Useful Commands

Check your pip version:

```bash
python -m pip --version
```

Check which packages are installed:

```bash
python -m pip list
```

Upgrade a package:

```bash
python -m pip install --upgrade pandas
```