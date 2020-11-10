[Previous: Installing Processing](01_processing_install.md) - [[TOC](README.md)]

---

# Using Processing

Documentation: https://py.processing.org/reference/

## Initial code
```python
def setup():
    size(800, 600)

def draw():
    pass
```

Both `setup` and `draw` define code "areas" in which we'll write our code. We call them *function definitions*.
- `setup` : Executed once when the project launches
- `draw` : Executed 60 times per seconds (60fps)

## Comments
Anything  that follows a `#` is ignored by the computer when reading our code. Even if it is a line of code.

```python
# This line is ignored
1 + 1 # This part after the 1+1 is ignored
```

## Drawing commands (*functions calls*)

```python
command()
command(a)
command(a, b)
command(a, b, c)
command(a, b, c, ...)
   ^    ^  ^  ^
  name  parameters
```

Each command has a name and possibly some parameters inside the `()` to change some details about what the command does.

```python
# Sets the size of the drawing 800 (width) by 600 (height)
size(800, 600)
```

```python
# Draws a rectangle at x:10, y:20, width:100, height:50
rect(10, 20, 100, 50)
```

List of commands (functions) : https://py.processing.org/reference/

**To get started:**
- [size](https://py.processing.org/reference/size.html) - Sets the size of the drawing area. Must be in `setup():`

Colors
- [background](https://py.processing.org/reference/background.html) - Clear the whole screen with a color
- [fill](https://py.processing.org/reference/fill.html) - Defines the color to use inside the shapes drawn after to this line
- [noFill](https://py.processing.org/reference/noFill.html) - Remove the color inside the shapes drawn after to this line
- [noStroke](https://py.processing.org/reference/noStroke.html) - Remove the border around the shapes drawn after to this line
- [stroke](https://py.processing.org/reference/stroke.html) - Defines the color to use for the border of the shapes drawn after to this line
- [strokeWeight](https://py.processing.org/reference/strokeWeight.html) - Changes the weight of the border around the shapes drawn after to this line

Shapes
- [rect](https://py.processing.org/reference/rect.html) - Draws a rectangle
- [circle](https://py.processing.org/reference/circle.html) - Draws a circle
- [triangle](https://py.processing.org/reference/triangle.html) - Draws a triangle
- [line](https://py.processing.org/reference/line.html) - Draws a line
- [ellipse](https://py.processing.org/reference/ellipse.html) - Draws a ellipse
- [point](https://py.processing.org/reference/point.html) - Draws a point
- [quad](https://py.processing.org/reference/quad.html) - Draws a quad
- [arc](https://py.processing.org/reference/arc.html) - Draws an arc

Random
- [random](https://py.processing.org/reference/random.html) - Get a random number
- [noise](https://py.processing.org/reference/noise.html) - Get a random number that is similar to the previous one

Debugging
- [print](https://py.processing.org/reference/print.html) - Display some value in the black console at the bottom (useful for variables)


## Variables

Variables are the memory of the computer. We associate a name with a value.

The name of the variable **cannot** contain spaces. To combine multiple words, we use either:
- camelCase: `longCamelCaseSentence`
- snake_case: `long_snake_case_sentence`

```python
# my_variable_name = value
character_health = 100
```

#### Simple value types

- int : Integer number (e.g. : `155`, `0`, `-159125`)
- float: Floating point number (e.g. : `10.5125`, `3.14159`, `-159.5`)
- boolean: `True` or `False`
- string: Text that isn't code.  (e.g. : `"My name is Stephanie"` )
    - Must be surrounded by double quote `"`

More types exists, we'll see them later.

#### Operators
`+`: Add
`-`: Subtract
`/`: Divide
`*`: Multiple
`%`: Remainder of a division
`**`: Exponential

```python
result = 1 + 4     # 5
result = 8 - 4     # 3
result = 8 / 2     # 4
result = 2 * 4     # 8
result = 10 % 3    # 1
result = 10 ** 2   # 100
```

## Processing variables
- `width` : Width of the drawing area
- `height` : Height of the drawing area
- `mousePressed` : If the mouse is *currently* pressed
- `mouseX` : Current position on the x-axis of the mouse
- `mouseY` : Current position on the y-axis of the mouse
- `pmouseX` : Last frame position on the x-axis of the mouse
- `pmouseY` : Last frame position on the y-axis of the mouse

## Global variables

To have a variable **keep it's value through time**, we need to declare it outside the `setup` and `draw` area. We call those global variables, and declare them like so:
```python
position_x = 0
#^^^^^^^^^

def setup():
    size(800, 600)

def draw():
    background(255)
```

However, if we want to **change** the variable value **inside** of a function (e.g. `setup` or `draw`), we need to explicitely say it is a global variable:

```python
position_x = 0
#^^^^^^^^^

def setup():
    size(800, 600)

def draw():
    global position_x             # Tell Python we need to modify the global variable
    #^^^^^^^^^^^^^^^^^

    background(25)
    rect(position_x, 0, 50, 50)   # Draws a rectangle using the position_x as x-axis
    #    ^^^^^^^^^^

    position_x = position_x + 1   # Adds 1 to the current value of position_x
    #^^^^^^^^^   ^^^^^^^^^^
```

## Challenges
1. Create a "painting" using the drawing functions
2. Move a shape from top to bottom across the screen
3. Draw a triangle that spread from the bottom left to the bottom right and hits the top center. Ideally, when you change the `size()`, the triangle still reaches the same corners.
4. Create a variable `a` which stores the value of `40` plus `2`. Mutliply `a` by 3 and store the result inside of `b`. Divide `b` by 10 and store the final result inside a `result` variable. Finally, print `result` to the black console.
5. Use the `draw` area to create some shapes (with transparency?) at random position and with random colors
6. Use the `draw` area to change the color of a shape as time passes by
7. Use processing variables (e.g. `mouseX`, `mouseY`) to change the color or position of things as they get drawn

------

[Next: Conditions](03_conditions.md) - [[TOC](README.md)]
