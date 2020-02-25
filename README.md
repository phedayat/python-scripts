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
digit separately.

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

This script finds all the generators of the multiplicative group ![Group](images/group.gif). In group theory, $a \in \mathbb{Z}$ is a generator if $a^i$ for $1 \leq i \leq |\mathbb{Z}^{*}_{n}| = \varphi(n)$ produces every element in the group without repetition. $a^{\varphi(n)} = 1$.

For prime $n$, $\mathbb{Z}^{*}_{n} = \mathbb{Z}_n-\{0\}$, because an element $a \in \mathbb{Z}_n$ is a unit if it's coprime to $n$, i.e. $\gcd{a, n} = 1$. Thus, all elements of $\mathbb{Z}_n$ except 0 are coprime to $n$.

