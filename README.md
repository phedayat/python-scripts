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

* $n \leq 2$ creates a line
* $n = 3$ creates a triangle
* $n = 4$ creates a square
* $n \geq 5$ creates stars with n points

### Heap.py

A script that shows how Heap's Algorithm works. Heap's Algorithm finds 
all the permutations of a list. For example, if you have a list of length
$3$, the number of permutations will be $3!$ or $6$.

### Fern.py

Uses Python with Turtle to draw a Barnsley Fern, a fractal that uses four 
affine transformations to plot out a fern.

### generators.py
This script finds all the generators of the multiplicative group $(\mathbb{Z}^{*}_{n}, \cdot)$. 

In group theory,

$$a \in \mathbb{Z}^{*}_n$$

is a generator if $a^i$ for $1 \leq i \leq \lvert \mathbb{Z}^{*}_{n} \rvert = \phi(n)$ produces every element in the group without repetition. $a^{\phi(n)} = 1$.

For prime $n$, 

$$\mathbb{Z}^{*}_n = \mathbb{Z}_n - \{0\}$$

because an element $a \in \mathbb{Z}_n$ is a unit if it's coprime to $n$, i.e. $\gcd{a, n} = 1$. Thus, all elements of $\mathbb{Z}_n$ except $0$ are coprime to $n$. This means all elements of $\mathbb{Z}_n$ except $0$ are units and in $\mathbb{Z}^{*}_n$.

### Convex Hull Algorithm

This project is meant to test my skills and to recreate the Graham Scan convex hull algorithm (via [The Algorithm Design Manual](http://www.algorist.com/)). Unfinished; `graphicalHull.py` still needs to be fixed, but the convex hulls produced are much better than before.

* `graphicalHull.py`: This is the main file that runs a Graham Scan. Not to be confused with `main.py`, which is an outdated main file for this project.
* `point.py`: The class that defines a point.
* `main.py`: An outdated main file from the beginning of this project. Instead of a Graham Scan, `main.py` is attempting to perform a Jarvis March; however, there are problems with it and it doesn't always catch all the points within the convex hull. Might return to fix it later.

### Gram-Schmidt Process

This project was originally only supposed to compute the result of running the [Gram-Schmidt]() process on a basis. It became a fun exercise to visualize not only the projections across varying dimensions of bases, but the error of each approximation of $\sin{x}$.

The original motivator for this script was a problem from Sheldon Axler's [*Linear Algebra Done Right*]() regarding the minimization of an integral on the interval $[-\pi, \pi]$ by finding a polynomial approximation of $\sin(x)$ of at most degree 5. Since we operate in the space of continuous real-valued functions within our interval, our inner product is an integral, and this becomes increasingly tedious to compute. It was also because of the inner product space we were working in that I had to use `sympy` to compute the projections. 

Running the script will produce two windows:
1. The projections of $\sin{x}$ onto polynomial subspaces of varying dimensions. $P_i = \\{p(x) \mid \text{deg}(p) < i\\}$ for $i = 2, 3, ..., {\tt MAX}$. The maximum is determined by the number of subplots to create
2. The MSE loss per basis dimension of the projection and $\sin{x}$

The script is customizable in 2 ways: function and interval. Changing the function `f` to any function representable by `sympy` will produce results. Changing `DISP_INTERVAL` will change the interval we're approximating within.

__[WARNING]__ The larger the interval, the longer it'll take to finish.
