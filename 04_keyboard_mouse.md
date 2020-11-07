[Previous: Conditions](03_conditions.md) - [[TOC](README.md)]

---

# Keyboard and mouse events

In Processing, to use the keyboard and mouse to their full potential, we need to define new areas of code that are linked to some events.

## List of events
```python
def mousePressed():
    print("Mouse has been pressed down")

def mouseReleased():
    print("Mouse has been released")

def keyPressed():
    print("Key has been pressed down")

def keyReleased():
    print("Key has been released")
```

## Keyboard keys

In the keyboard events, we can use the `key` and `keyCode` variables to know which key the user interacted with.

```python
def keyPressed():
    if key == "w":
        print("Move forward")
    elif key == "s":
        print("Move backward")
```

## Using inputs during `draw()`

Sometimes it is useful to store the state of some keys to use them later in the `draw()` part of the code. For instance:

```python
# Current position of the character on the x axis
position_x = 0

# True if the "D" key is held down, False otherwise
d_key_is_pressed = False

def setup():
    size(400, 400)

def draw():
    global position_x

    background(25)

    # Only move right if the "D" key is currently held down
    if d_key_is_pressed:
        position_x = position_x + 5

    rect(position_x, 0, 50, 50)

def keyPressed():
    global d_key_is_pressed

    if key == "d":
        d_key_is_pressed = True

def keyReleased():
    global d_key_is_pressed

    if key == "d":
        d_key_is_pressed = False
```

## Challenges
- Move a circle or rectangle with WASD
- For the drawing app we made in [03_conditions](03_conditions.md), add a list of colors to pick from. Display each colors as a small rectangle on the screen, then detect when the mouse is pressed and check the position of it to know which "color" was pressed. Then draw the following lines/shapes with this color
- Create a character (recangle, circle or image) that can jump and fall with gravity, just like the Mario game. The floor would be the bottom of the screen.
- Recreate the [Pong game](https://en.wikipedia.org/wiki/Pong)
    - Bounching ball
    - Moving paddles
    - Collisions (hard)

------

[Next: Loops](05_loops.md) - [[TOC](README.md)]