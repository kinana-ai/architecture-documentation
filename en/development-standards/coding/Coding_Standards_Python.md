# Python Style Guide

## Primary Reference

**Official**: [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

This document highlights key conventions for Python development on the AI workstation. For comprehensive coverage, reference PEP 8.

---

## Use Case Context

**Primary Use**: AI model development and experimentation on Ubuntu GPU workstation  
**Environment**: Python 3.11+, virtual environments, Jupyter notebooks (likely)  
**Focus**: Research scripts, data processing, model training

---

## File Organization

### Project Structure
```
ai-project/
├── src/                    # Source code
│   ├── __init__.py
│   ├── models/            # ML models
│   ├── data/              # Data processing
│   └── utils/             # Utility functions
├── notebooks/             # Jupyter notebooks
├── tests/                 # Unit tests (future)
├── data/                  # Data files (not in git)
├── requirements.txt       # Dependencies
├── setup.py              # Package setup
└── README.md             # Project documentation
```

### File Naming
- **snake_case** for all files: `data_loader.py`, `train_model.py`
- **Modules**: Short, lowercase names
- **Packages**: Short, lowercase, no underscores if possible

---

## Naming Conventions

### Variables and Functions
```python
# snake_case for variables and functions
user_name = "John"
def get_user_profile():
    pass

# PascalCase for classes
class UserProfile:
    pass

# UPPER_CASE for constants
MAX_ITERATIONS = 1000
API_BASE_URL = "https://api.kinana.com"

# _ prefix for "private" (by convention)
def _internal_helper():
    pass

# __ prefix for name mangling (rare)
class MyClass:
    def __mangled_method(self):
        pass
```

### Boolean Variables
```python
# Use is/has/can for booleans
is_active = True
has_permission = False
can_edit = user.role == 'admin'
should_retry = errors > 0
```

---

## Code Style

### Indentation
```python
# 4 spaces per indentation level (no tabs)
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```

### Line Length
```python
# Maximum 79 characters (PEP 8)
# Break long lines appropriately
result = some_function_that_takes_arguments(
    'argument one',
    'argument two',
    'argument three'
)
```

### Imports
```python
# Standard library first, then third-party, then local
import os
import sys

import numpy as np
import pandas as pd
import torch

from .models import BaseModel
from .utils import load_data

# Avoid wildcard imports
from module import *  # ❌ Bad

# Import specific items
from module import Class1, function1  # ✅ Good
```

---

## Type Hints (Python 3.11+)

### Function Signatures
```python
# ✅ Good - type hints for clarity
def get_user(user_id: str) -> dict[str, any]:
    return {"id": user_id, "name": "John"}

def process_data(data: list[int], threshold: float = 0.5) -> list[int]:
    return [x for x in data if x > threshold]

# For complex types
from typing import Optional, Union

def find_user(user_id: str) -> Optional[dict]:
    # May return None
    pass

def get_value(key: str) -> Union[int, str]:
    # Returns either int or str
    pass
```

### Type Aliases
```python
# For complex types
Vector = list[float]
Matrix = list[list[float]]

def multiply_matrix(a: Matrix, b: Matrix) -> Matrix:
    pass
```

---

## Docstrings

### Module Docstrings
```python
"""
Data processing utilities for Kinana AI models.

This module provides functions for loading, preprocessing, and augmenting
training data for the AI content recommendation system.
"""
```

### Function Docstrings
```python
def train_model(data: pd.DataFrame, epochs: int = 10) -> Model:
    """
    Train a content recommendation model.
    
    Args:
        data: Training data as pandas DataFrame
        epochs: Number of training epochs (default: 10)
    
    Returns:
        Trained model instance
    
    Raises:
        ValueError: If data is empty or malformed
    """
    pass
```

### Class Docstrings
```python
class ContentRecommender:
    """
    AI model for recommending educational content to students.
    
    This model uses collaborative filtering and content-based features
    to suggest relevant documents, videos, and podcasts.
    
    Attributes:
        model_path: Path to saved model weights
        embedding_dim: Dimension of content embeddings
    """
    
    def __init__(self, model_path: str, embedding_dim: int = 128):
        """Initialize the recommender with model parameters."""
        self.model_path = model_path
        self.embedding_dim = embedding_dim
```

---

## Error Handling

### Specific Exceptions
```python
# ✅ Good - catch specific exceptions
try:
    data = load_data(file_path)
except FileNotFoundError:
    print(f"File not found: {file_path}")
    data = load_default_data()
except json.JSONDecodeError as e:
    print(f"Invalid JSON format: {e}")
    raise

# ❌ Bad - bare except
try:
    risky_operation()
except:  # Don't do this!
    pass
```

### Context Managers
```python
# ✅ Good - automatic resource cleanup
with open('data.txt', 'r') as f:
    data = f.read()
    # File automatically closed

# For custom resources
class DatabaseConnection:
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
```

---

## Data Science Patterns

### Pandas Best Practices
```python
import pandas as pd

# ✅ Good - method chaining
df = (
    pd.read_csv('data.csv')
    .dropna()
    .query('age > 18')
    .groupby('category')
    .agg({'value': 'mean'})
    .reset_index()
)

# ✅ Good - vectorized operations
df['total'] = df['price'] * df['quantity']  # Fast

# ❌ Bad - iterating rows
for index, row in df.iterrows():  # Slow!
    df.at[index, 'total'] = row['price'] * row['quantity']
```

### NumPy Best Practices
```python
import numpy as np

# ✅ Good - vectorized operations
arr = np.array([1, 2, 3, 4, 5])
result = arr * 2 + 1  # Fast

# ❌ Bad - loops
result = [x * 2 + 1 for x in arr]  # Slower
```

### PyTorch/TensorFlow Patterns
```python
import torch

# ✅ Good - device-agnostic code
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = MyModel().to(device)
data = data.to(device)

# ✅ Good - gradient management
with torch.no_grad():
    predictions = model(test_data)  # No gradient computation
```

---

## Virtual Environments

### Always Use Virtual Environments
```bash
# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Freeze dependencies
pip freeze > requirements.txt
```

### Requirements.txt
```text
# Pin versions for reproducibility
numpy==1.24.0
pandas==2.0.0
torch==2.0.0
scikit-learn==1.3.0

# Or use range for flexibility
requests>=2.28.0,<3.0.0
```

---

## Jupyter Notebooks

### Notebook Organization
```python
# Cell 1: Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cell 2: Configuration
%matplotlib inline
pd.set_option('display.max_columns', None)

# Cell 3: Load data
data = pd.read_csv('data.csv')

# Subsequent cells: Analysis steps
```

### Notebook Best Practices
- One logical step per cell
- Clear markdown headings between sections
- Restart & Run All before sharing
- Export to .py for production code
- Don't commit large outputs (use nbstripout)

---

## Performance Considerations

### List Comprehensions
```python
# ✅ Good - list comprehension
squares = [x**2 for x in range(100)]

# ❌ Bad - loop with append
squares = []
for x in range(100):
    squares.append(x**2)
```

### Generators for Large Data
```python
# ✅ Good - generator for memory efficiency
def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield process_line(line)

# Usage
for item in read_large_file('huge_file.txt'):
    process(item)
```

### Use Built-ins
```python
# ✅ Good - built-in functions are optimized
result = sum(numbers)
maximum = max(values)

# ❌ Bad - manual implementation
result = 0
for n in numbers:
    result += n
```

---

## Testing (Future)

### Test Structure
```python
# test_data_loader.py
import pytest
from src.data_loader import load_data

def test_load_data_success():
    data = load_data('test_data.csv')
    assert len(data) > 0
    assert 'user_id' in data.columns

def test_load_data_missing_file():
    with pytest.raises(FileNotFoundError):
        load_data('nonexistent.csv')
```

---

## Code Formatting

### Black (Auto-formatter)
```bash
# Install
pip install black

# Format file
black script.py

# Format directory
black src/

# Check without modifying
black --check src/
```

### Configuration (pyproject.toml)
```toml
[tool.black]
line-length = 88
target-version = ['py311']
include = '\.pyi?$'
```

---

## Linting

### Flake8
```bash
# Install
pip install flake8

# Run
flake8 src/

# Configuration in .flake8
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = .git,__pycache__,venv
```

### mypy (Type Checking)
```bash
# Install
pip install mypy

# Run type checking
mypy src/
```

---

## Comments

### When to Comment
```python
# ✅ Good - explains WHY
# Use exponential backoff to avoid overwhelming the API
time.sleep(2 ** retry_count)

# ✅ Good - complex algorithm
# Implements the Sieve of Eratosthenes for finding primes
def find_primes(n):
    pass

# ❌ Bad - states the obvious
# Increment counter
counter += 1
```

---

## Common Patterns

### Context Managers
```python
# File handling
with open('data.txt') as f:
    content = f.read()

# Database connections
with database.connect() as conn:
    result = conn.query('SELECT * FROM users')
```

### Decorators
```python
# Timing decorator
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
```

### Property Decorator
```python
class User:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
    
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    @full_name.setter
    def full_name(self, value):
        first, last = value.split()
        self._first_name = first
        self._last_name = last
```

---

## Resources

- **PEP 8**: https://peps.python.org/pep-0008/
- **Google Python Style Guide**: https://google.github.io/styleguide/pyguide.html
- **Real Python**: https://realpython.com/
- **Black Formatter**: https://black.readthedocs.io/
- **Type Hints**: https://docs.python.org/3/library/typing.html

---

*Last Updated: November 2025*  
*Version: 1.0*
