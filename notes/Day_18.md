# Day 18 – Turtle & GUI

## What I Built

- A Turtle graphics “dot painting” that draws a 10×10 grid (100 dots total).
- Each dot is a random RGB color, using `turtle.colormode(255)`.
- Before reaching the final version, I experimented with:
  - Drawing polygons (triangle → decagon)
  - Random walks
  - A spirograph
  - Different dotted-line patterns

## What Was New for Me

- First time using the **Turtle graphics** module:
  - `turtle.colormode(255)` for RGB colors.
  - `dot()` for placing circular dots.
  - Movement with `setheading()` vs relative turns.
- Understanding how Turtle is basically a tiny GUI environment.

## What Was Mostly Review

- Loops, ranges, and counters (used to track when to move up a row).
- Basic function creation.
- Using randomness with `random.randint()`.
- General drawing logic & movement patterns.

## Reusable Snippets / Patterns

This RGB randomizer is clean and satisfying — definitely keeping it for future GUI or drawing projects:

```python
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color
```
