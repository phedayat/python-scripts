# python-scripts

## Purpose

As I write more Python scripts, I'll add them here.
They're nothing impressive or groundbreaking, just simple scripts that allow me
to work on my Python and general programming skills.

## Scripts

### spaceMaker.py

Meant to put spaces and commas between digits of a long number. I used it as
part of a Project Euler problem I was working on in Java. Basically I wanted
to test my code and needed a lot of numbers, so I decided to generate a random
1000 digit number and use spaceMaker to add commas and spaces to evaluate each
digit separately. Realistically, can be modified to use any delimiter.

### turt.py

Uses Python with Turtle for graphics. I originally wrote this as part of an
interview. Used it again later to begin teaching a friend of mine Python. I
started toying around with it and have been getting some cool results.
Currently, it uses some basic geometry to create stars with n points.

* n ≤ 2 creates a line
* n = 3 creates a triangle
* n = 4 creates a square
* n ≥ 5 creates stars with n points

### Heap.py

A script that shows how Heap's Algorithm works. Heap's Algorithm is meant 
for finding all the permutations of a list. If you have a list of length
3, the number of permutations will be 3! or 6.

### Fern.py

Uses Python with Turtle to draw a Barnsley Fern, a fractal that uses four 
affine transformations to plot out a fern.

### generators.py

This script finds all the generators of the multiplicative group ![Group](https://latex.codecogs.com/gif.latex?%28%5Cmathbb%7BZ%7D%5E%7B*%7D_%7Bn%7D%2C%20%5Ccdot%29). In group theory, ![ainznstar](https://latex.codecogs.com/gif.latex?a%20%5Cin%20%5Cmathbb%7BZ%7D%5E%7B*%7D_%7Bn%7D) is a generator if ![ai](https://latex.codecogs.com/gif.latex?a%5Ei) for ![inequality](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20i%20%5Cleq%20%7C%5Cmathbb%7BZ%7D%5E%7B*%7D_%7Bn%7D%7C%20%3D%20%5Cvarphi%28n%29) produces every element in the group without repetition. ![aphi](https://latex.codecogs.com/gif.latex?a%5E%7B%5Cvarphi%28n%29%7D%20%3D%201).

For prime n, ![znnozero](https://latex.codecogs.com/gif.latex?%5Cmathbb%7BZ%7D%5E%7B*%7D_%7Bn%7D%20%3D%20%5Cmathbb%7BZ%7D_n-%5C%7B0%5C%7D), because an element ![ainzn](https://latex.codecogs.com/gif.latex?a%20%5Cin%20%5Cmathbb%7BZ%7D_%7Bn%7D) is a unit if it's coprime to n, i.e. ![gcd](https://latex.codecogs.com/gif.latex?%5Cgcd%7Ba%2C%20n%7D%20%3D%201). Thus, all elements of ![zn](https://latex.codecogs.com/gif.latex?%5Cmathbb%7BZ%7D_n) except 0 are coprime to n. This means all elements of ![zn](https://latex.codecogs.com/gif.latex?%5Cmathbb%7BZ%7D_n) except 0 are units and in ![znstar](https://latex.codecogs.com/gif.latex?%5Cmathbb%7BZ%7D%5E%7B*%7D_%7Bn).

### Convex Hull Algorithm

This project is meant to test my skills and to recreate the Graham Scan convex hull algorithm (via [The Algorithm Design Manual](http://www.algorist.com/)).

* `graphicalHull.py`: This is the main file that runs a Graham Scan. Not to be confused with `main.py`, which is an outdated main file for this project.
* `point.py`: The class that defines a point.
* `main.py`: An outdated main file from the beginning of this project. Instead of a Graham Scan, `main.py` is attempting to perform a Jarvis March; however, there are problems with it and it doesn't always catch all the points within the convex hull. Might return to fix it later.
