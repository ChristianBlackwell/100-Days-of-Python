# Day 19 – Instances, State, Higher Order Functions

## What I Built

- Turtle race game + (commented) Etch-a-sketch key controls.

## Useful Pattern I Reinforced

- Creating multiple objects in a loop and storing them in a list:
  - `all_turtles.append(new_turtle)`
- Simple game loop:
  - while racing → update each turtle → check win condition

## Tiny Gotchas

- User input normalization (case/spacing) matters when comparing strings.
- Break out of loops once a winner is found to avoid extra updates.
