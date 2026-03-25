# Ray Transfer Matrix Analysis
Author: Lukas Niggl
Semester: 23S

### Idea behind the project
This program focuses on the change of the angle from a light beam, when it's refracted at a boundary layer between air
and a glass block and vice versa for diverse optical instruments (various lenses). Additionally, the angle change of a
simple plane mirror is given. The physical topic is called: "Ray Transfer Matrix Analysis".

The idea was basically to transfer physics into programming. Solving this task manually with pen and paper is simply
time-consuming, since for every input 5 respectively 10 matrix-vector-products have to be evaluated. So having an
automated process accelerates this task in the long term.

### Implementation
Since my topic was changed last minute, and I initially was focused on something different, there wasn't really a fixed
starting point I had in mind. This is also why the topic specification in the Google document, varies from the actual
implementation, since Matthias simply had to fill something in to be in time (The functions turned out to be different).

First, I simply refreshed my mind about the topic (since this topic was taught a couple semesters ago) and started
collecting the necessary data provided in the `config.py` file. Then I've created the function which multiplies a vector
to a matrix. The second function, which takes an angle and uses the previous function to determine the angle after a
refraction/reflection process, followed. For these two functions I've tried to implement them by test driven
development, meaning I've written most of their tests in separate file (`tests.py`) beforehand (Could've also included
test in `main.py`. Didn't do so for clarity). Though as I was coding the functions, better ideas on how to implement
them came up, which would cause fails in some tests. That's why I had to vary the tests during the function coding in
some ways (mainly for the *get_angles()* function). The general ideas of the various tests were constant though. The
third function then simply prints the angle outputs in a nice format. The tests for this function were added after the
function was coded, since I wasn't sure how exactly the output would look like. Additionally, I've created a file for
user inputs (`user.py`) and my goal was to make it as stable as possible for wrong inputs. Though, since we were told
not to focus too much on user inputs and also this code would exceed the required lines of code, I/you can treat it as
an additional *"nice to have"* file.
Overall the implementation wasn't the hardest job to do for me and I haven't really encountered larger errors or
implementation difficulties, of which I'm quite happy about. Only the `user.py` file took a bit longer to get result I
had in mind.

### Extensions

Possible extensions of the project could be to add more optical instruments, meaning more matrices that represent them.
I've chosen the simpler instruments, since the larger ones are represented by more complex matrices, and some even need
an additional function to determine the matrix-matrix-product. And also since this task was about programming and not
about difficult physical problems, I've chosen the simpler matrices.
Also, one could make the focal point variable as an argument for the *get_angles()* function. Same would apply to
different media, with their corresponding refractive indices. Also also, one could build a function that determines the
angle of a beam going through several optical devices. This would also lead to matrix-matrix-product function, since the
whole optical system can be represented simply by matrix products of the individual matrices.

### Conclusion

All in all I'm quite happy how everything went :)