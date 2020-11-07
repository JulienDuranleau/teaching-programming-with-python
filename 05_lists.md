[Previous: Keyboard and Mouse](04_keyboard_mouse.md) - [[TOC](README.md)]

---

# Lists and Dictionaries

## Lists
Lists are a type of value which is simply a container for multiple values. 

We define a list with square brackets `[ ]`.

```python
grades = [100, 59, 12, 79, 92]
```

We can then access each value contained inside the list by using the variable followed by the *index* inside of `[ ]`. The *index* is the position, **counting from zero**.

```python
grades = [100, 59, 12, 79, 92]
#          0    1   2   3   4

print( grades[0] ) # first grade
print( grades[4] ) # last grade
```

We can also create an empty array
```python
ranked_game_wins = []
```

And then add things to it later in the code

```python
ranked_game_wins.append(True)
ranked_game_wins.append(False)
ranked_game_wins.append(True)
ranked_game_wins.append(True)

# ranked_game_wins is now equal to [True, False, True, True]
```

Or remove things
```python
# Deletes the second value (index 1, counting from 0)
del ranked_game_wins[1]

# ranked_game_wins is now equal to [True, True, True]
```

## Dictionaries

Dictionaries are similar to lists, but you can define names for each indexes. They are quite useful to regroup multiple values that have a common theme. E.g. a character with it's hp, position, speed, ...

We define a list with curly brackets `{ }`.

```python
player_hero = {
    "name" : "Mercy",
    "hp" : 200,
    "healing_per_second" : 50,
    "nerf_count": 174,
    "need_buff": True,
}

print( player_hero["name"] ) # Mercy
print( player_hero["hp"] )   # 200
```

To add a new value:
```python
player_hero["useless_genji_in_team"] = True
```

To remove it:
```python
del player_hero["useless_genji_in_team"]
```

## Challenges
1. Draw circles with the mouse and store each of them in an array. Everytime the `draw()` function is executed, redraw all of them after clearing the background. This will allow you to change the color of all of them even if they've been drawn before! (e.g. use the spacebar to change the color randomly)
2. Transform the bouncing ball example to use a dictionary for positions (e.g. `position["x"]` and `position["y"]`)

------

[Next: Loops](06_loops.md) - [[TOC](README.md)]