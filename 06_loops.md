[Previous: Lists and Dictionaries](05_lists.md) - [[TOC](README.md)]

---

# Loops

Loops, just like conditions, change the flow of code. They allow us to tell some lines to repeat multiple times.

## `for` loop
Using the `range()` function, we can specify the amount of times to repeat the lines.

```python
for number in range(0, 5):
    print(number)

# == Prints:
# 0
# 1
# 2
# 3
# 4
```

Or we can repeat for each value of a list
```python
names = ["Julien", "Stephanie", "Bob"]

for name in names:
    print(name)

# == Prints:
# Julien
# Stephanie
# Bob
```

## `while` loop

A while loop uses the same structure as an `if` condition, but repeats the lines until the condition (boolean) becomes `False`

```python
count = 0

while count < 5:
    print(count)
    count = count + 1
```

## `break` and `continue`

`break` breaks a loop early.

```python
names = ["Julien", "Stephanie", "Bob"]

for name in names:
    print(name)

    if name == "Stephanie":
        break

# == Prints:
# Julien
# Stephanie
```

`continue` skips one of the value in the loop

```python
grades = [65, 2, 20, 100]

for grade in grades:
    if grade < 60:
        continue

    print(grade)

# == Prints:
# 65
# 100
```

## Getting parts of a list

It is often useful to get only a specific part of a list value to loop on.

Here's a few possibilities:

```python
nums = [1, 2, 3, 4, 5]
#       0  1  2  3  4  indexes

nums[1:3]   # From index 1 to 3 => [2, 4]
nums[2:]    # Starting from index 2 => [3, 4, 5]
nums[:3]    # From beginning until index 3  => [1, 2, 3]
nums[::2]   # Selecting every second entry => [1, 3, 5]
nums[::-1]  # Reverse the order => [5, 4, 3, 2, 1]

for n in nums[2:]:
    print(n)
```


------

[Next: Files](07_files.md) - [[TOC](README.md)]