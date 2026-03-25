# Ray Transfer Matrix Analysis
#### HowTo file
Author: Lukas Niggl
Semester: 23S

### Data

The main *physical* data used in the other files can be found in `config.py`.

### Main functions

To simply run the program, one has to execute the `main.py` file. Documentation of the functions can be found there.
There, two example scenarios are hard-coded. To change outcome, one has to change the values within the code. One
example execution looks like the following:
```
The resulting incoming angles due to refraction (between air and glass)/reflection for an outgoing angle of 33.07° at a distance of 0.005m from the optical axis are:
Refraction at plane: 50.25°
Refraction at sphere: 50.38°
Refraction at focussing thin lens: 33.57°
Refraction at defocussing thin lens: 32.57°
Reflection at plane mirror: 33.07°
```

### User input

To run the program with user inputs, one has to execute the `user.py` file. An example execution looks like the
following:
```
(1) Do you want to get the outgoing angles from entering an incoming angle value?
(2) Or do you want to determine the incoming angle values for a given entered outgoing angle?
Type 1 or 2: 1
Enter angle between [0°, 90°] up to three decimals: 25
Enter a distance from the optical axis smaller than 0.02m but greater than 0: 0.002

The resulting outgoing angles due to refraction (between air and glass)/ reflection for an incoming angle of 25.0° at a distance of 0.002m from the optical axis are:
Refraction at plane: 16.45°
Refraction at sphere: 16.42°
Refraction at focussing thin lens: 24.8°
Refraction at defocussing thin lens: 25.2°
Reflection at plane mirror: 25.0°
```

### Testing

For testing the function, one has to run the `tests.py` file.