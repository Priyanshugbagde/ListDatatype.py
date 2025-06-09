# ListDatatype.py
To check the pop()and remove() operations/functions

Here’s a short and clear **README.md** file for your task on `pop()` and `remove()` functions in Python:

---

### 📝 README.md

````markdown
# List Operations in Python: `pop()` vs `remove()`

This program demonstrates the difference between `pop()` and `remove()` functions on a Python list.

## 🔧 Functions Explained

### 1. `pop([index])`
- Removes and returns the element **at the specified index**.
- If no index is given, it removes the **last element**.
- Raises `IndexError` if the index is out of range.

**Usage:**
```python
l.pop(2)    # Removes element at index 2
l.pop()     # Removes last element
````

---

### 2. `remove(value)`

* Removes the **first occurrence of the specified value** from the list.
* Raises `ValueError` if the value is not found.
* Does not work with indexes.

**Usage:**

```python
l.remove(40)   # Removes the value 40 from the list
```

---

## ❌ Common Mistakes

* `remove()` does not accept index:

  ```python
  l.remove(2)  # Works only if 2 is a value in the list
  ```

* Passing two arguments to either function causes an error:

  ```python
  l.remove(10, 20)  # ❌ Error: too many arguments
  l.pop(1, 2)       # ❌ Error: pop() takes at most 1 argument
  ```

* Calling `pop()` with an invalid index:

  ```python
  l.pop(10)  # ❌ IndexError if index is out of range
  ```

* Calling `remove()` with a value not present in the list:

  ```python
  l.remove(100)  # ❌ ValueError
  ```

---

## ✅ Good Practices

* Use `pop()` when you know the index (or want to remove the last item).
* Use `remove()` when you want to delete a specific value by content.

---

## Example List Used

```python
l = [10, 20, 30, 40, 50]
```

This project is helpful for understanding how Python list modifications behave and how to avoid common runtime errors.
