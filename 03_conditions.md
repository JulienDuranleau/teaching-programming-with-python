[Previous: The Basics](02_basics.md) - [[TOC](README.md)]

---


# `if` conditions

Conditions allow us to control the flow of code by adding conditions to the execution of specific lines of code. 

Use the `<tab>` key on your keyboard to create some space before the lines restricted by the condition.

```python
if something_is_true:
    # then do this
    print("Yay! The condition is true")

# Always do the rest of it
# since it isn't indented (space at beginning)
print("The end. Always shows")
```

## Booleans
Following the `if` part, we must give something which is `True` or `False`, also known as a boolean.

Booleans can be written in many ways:
```python
result = True
result = False

result = 10 > 5   # 10 is greater than 5
result = 5 < 10   # 5  is less    than 10

result = 5 >= 5   # 5  is greater than or equal to 5
result = 5 <= 5   # 5  is less    than or equal to 5

result = 5 == 5   # 5  is equal     to   5
result = 5 != 6   # 5  is not equal to 6

result = not 10 > 5  # not inverts the boolean value that follows

result = 10 > 5 and 3 < 4  # True if both   sides are True
result = 10 > 5 or  3 < 1  # True if either sides are True
```

## Conditions with booleans
```python
number = 0

def setup():
    size(800, 600)

def draw():
    global number
    
    number = number + 1

    if number < 100:
        print("Number is smaller than 100")

    if number > 100:
        print("Number is bigger than 100")
```

## `else`

It is also possible to do something if the conditions fails (is `False`).
```python
if 10 < 5:
    print("Yay! The condition is true")
else:
    print("Boo! The condition is false") 
    
print("The end. Always shows")
```

## `elif`
If we want to be fancy, we can even test multiple possibilities with `elif`. Only the first one which is true is actually executed. If none of the `if` or `elif` are `True`, then the `else` part is executed.

```python
number = 5

if number > 10:
    print("number is bigger than 10.")
elif number < 10:
    print("number is smaller than 10.")
else:
    print("number is 10.")
```

## Challenges
1. Split the screen in two colors. The left half is one color and the other half is a different color. When the mouse moves past the middle, the colors switch sides. When the mouse comes back, they switch again to be back at their original positions.
2. Draw a circle under the cursor only when the mouse is pressed (see Processing variables in [02_basics](02_basics.md)
    - Try disabling the border to get a smoother effect
    - (harder) Use the `line()` function with the `pmouseX` and `pmouseY` to draw a real line instead of a bunch of circles
3. Draw a square, and change it's color only when the cursor is over it. Again, you'll need some of the Processing variables.
4. Create a bouncing ball
    - Create a speed_x and speed_y variable and change their value to a negative number when the ball hits a side. Use the speeds to change the positions each time the `draw` is executed
    - Change the ball's color depending on where it is on the screen.

------

[Next: Keyboard and Mouse](04_keyboard_mouse.md) - [[TOC](README.md)]