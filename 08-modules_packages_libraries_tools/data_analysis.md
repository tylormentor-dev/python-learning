# Python Data Analysis Packages

## Overview

Python is widely used in data analysis and data science because it has many libraries for working with, analyzing, and visualizing data.

This lesson covers five popular libraries: NumPy, pandas, SciPy, Matplotlib, and Scikit-learn.

## 1. NumPy

NumPy stands for Numerical Python. It is used for numerical calculations and working with multidimensional arrays.

### Common uses

- Performing mathematical calculations.
- Working with arrays and matrices.
- Supporting scientific computing and data analysis.

### Installation and import

```bash
python -m pip install numpy
```

```python
import numpy as np
```

### Example: Performing calculations on an array

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])

print(numbers.mean())
print(numbers.max())
print(numbers * 2)
```

**Output**

```text
25.0
40
[20 40 60 80]
```

**Explanation**

- `np.array()` creates a NumPy array.
- `mean()` calculates the average.
- `max()` returns the largest value.
- `numbers * 2` multiplies every element by 2.

NumPy's main data structure is the `ndarray`, which supports efficient numerical operations.

## 2. pandas

pandas is used to organize, clean, manipulate, and analyze structured data.

### Common uses

- Reading CSV and JSON files.
- Organizing data into rows and columns.
- Calculating statistics.
- Sorting and filtering datasets.

### Important data structures

- **Series:** A one-dimensional structure, similar to a single column.
- **DataFrame:** A two-dimensional, table-like structure with rows and columns.

### Installation and import

```bash
python -m pip install pandas
```

```python
import pandas as pd
```

### Example: Analyzing student scores

```python
import pandas as pd

data = pd.DataFrame({
    "Student": ["Alex", "Sam", "Jordan"],
    "Score": [75, 90, 85]
})

print(data)
print(data["Score"].mean())
```

**Output**

```text
  Student  Score
0    Alex     75
1     Sam     90
2  Jordan     85

83.33333333333333
```

**Explanation**

- `pd.DataFrame()` creates a table of student names and scores.
- `data["Score"]` selects the `Score` column.
- `mean()` calculates the average score.

pandas is useful when working with structured datasets that need to be analyzed or transformed.

## 3. SciPy

SciPy is a scientific computing library built on NumPy. It provides additional tools for mathematics, statistics, optimization, and scientific calculations.

### Common uses

- Statistical analysis.
- Scientific and technical calculations.
- Optimization problems.
- Working with mathematical functions.

### Installation and import

```bash
python -m pip install scipy
```

```python
from scipy import stats
```

### Example: Calculating a statistical value

```python
from scipy import stats

scores = [70, 80, 80, 90, 100]

result = stats.mode(scores, keepdims=False)

print(result.mode)
```

**Output**

```text
80
```

**Explanation**

- `stats.mode()` finds the most frequently occurring value.
- The mode of this list is `80`, because it appears twice.

SciPy provides specialized scientific functions that extend the capabilities of NumPy.

## 4. Matplotlib

Matplotlib is a data visualization library used to create graphs and charts.

### Common uses

- Displaying data visually.
- Comparing values.
- Showing trends and distributions.
- Creating static, interactive, and animated visualizations.

### Installation and import

```bash
python -m pip install matplotlib
```

```python
import matplotlib.pyplot as plt
```

### Example: Creating a bar chart

```python
import matplotlib.pyplot as plt

students = ["Alex", "Sam", "Jordan"]
scores = [75, 90, 85]

plt.bar(students, scores)
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")

plt.show()
```

**Explanation**

- `plt.bar()` creates a bar chart.
- `plt.title()` adds a chart title.
- `plt.xlabel()` labels the horizontal axis.
- `plt.ylabel()` labels the vertical axis.
- `plt.show()` displays the chart.

Matplotlib helps turn numerical data into visual representations that are easier to understand.

## 5. Scikit-learn

Scikit-learn is a machine learning library used to build and evaluate predictive models. It supports supervised and unsupervised learning.

### Common uses

- **Classification:** Predicting categories.
- **Regression:** Predicting numerical values.
- **Clustering:** Grouping similar data points.
- **Model evaluation:** Measuring model performance.
- **Dimensionality reduction:** Reducing the number of features in a dataset.

### Installation and import

```bash
python -m pip install scikit-learn
```

### Example: Making a simple prediction

```python
from sklearn.linear_model import LinearRegression

# Training data
hours = [[1], [2], [3], [4]]
scores = [50, 60, 70, 80]

model = LinearRegression()
model.fit(hours, scores)

prediction = model.predict([[5]])

print(prediction)
```

**Output**

```text
[90.]
```

**Explanation**

- `LinearRegression()` creates a linear regression model.
- `fit()` trains the model using the example data.
- `predict()` estimates the score for a student who studies for 5 hours.

The model learns a simple linear relationship from the training data. This example is for learning purposes and does not mean real student scores can always be predicted accurately from study time alone.

The package is installed as `scikit-learn`, but its modules are imported using the name `sklearn`.

## Installing All Five Libraries

You can install all five libraries in one terminal command:

```bash
python -m pip install numpy pandas scipy matplotlib scikit-learn
```

## Quick Reference

| Library | Main purpose | Common import |
|---|---|---|
| NumPy | Numerical calculations and arrays | `import numpy as np` |
| pandas | Data analysis and manipulation | `import pandas as pd` |
| SciPy | Scientific and statistical calculations | `from scipy import stats` |
| Matplotlib | Charts and visualizations | `import matplotlib.pyplot as plt` |
| Scikit-learn | Machine learning and predictions | `from sklearn.linear_model import LinearRegression` |

## Key Takeaways

- NumPy works with arrays and numerical calculations.
- pandas organizes and analyzes structured data.
- SciPy provides specialized scientific and statistical functions.
- Matplotlib creates charts and graphs.
- Scikit-learn provides tools for training machine learning models.
- These libraries can be combined in a single data analysis project.

