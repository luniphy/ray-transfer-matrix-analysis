[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Ray Transfer Matrix Analysis

A Python tool that computes how a light ray's angle changes when it interacts with optical elements using [Ray Transfer Matrix Analysis](https://en.wikipedia.org/wiki/Ray_transfer_matrix_analysis).

## Overview

In geometric optics, any optical element can be represented as a 2×2 matrix. Multiplying a ray vector `(height, angle)` by an element's matrix yields the transformed ray after the interaction.

This project automates this calculation for five optical devices:

| Optical Element                  | Description                                 |
| -------------------------------- | ------------------------------------------- |
| Refraction at plane boundary     | Air ↔ glass at flat surface                 |
| Refraction at spherical boundary | Air ↔ glass at curved surface (radius 2 cm) |
| Focussing thin lens              | Converging lens with focal length: 1 cm     |
| Defocussing thin lens            | Diverging lens with focal length: −1 cm     |
| Flat mirror                      | Reflection at plane mirror                  |

## Features

- Compute outgoing angles from a given incoming angle across all five optical elements in one call
- Compute incoming angles from a given outgoing angle (inverse mode)
- Adjustable beam distance from the optical axis
- Interactive CLI (`user.py`) with input validation
- Full doctest suite covering correct usage, math, type errors and value errors

## Project Structure

```
ray-transfer-matrix-analysis/
├─ src/
│  ├─ config.py     # Constants, refractive indices, error messages and optical/inverse matrices
│  ├─ main.py       # Matrix-vector multiplication, angle calculations and result printing
│  ├─ tests.py      # Doctests for core functions
│  └─ user.py       # Interactive CLI with validated user input
├─ LICENSE
└─ README.md
```

## Example output

```
The resulting outgoing angles due to refraction (between air and glass)/ reflection
for an incoming angle of 47° at a distance of 0.01m from the optical axis are:
Refraction at plane: 30.93°
Refraction at sphere: 30.76°
Refraction at focussing thin lens: 46.0°
Refraction at defocussing thin lens: 48.0°
Reflection at plane mirror: 47.0°
```

## License

MIT © [luniphy](https://github.com/luniphy)
