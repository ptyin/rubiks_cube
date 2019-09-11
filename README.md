# Rubik's Cube

## Algorithm

- No Search, no IDA*, no Kociemba(Two Phase)
- Just simulation

# Usage
```python
"""
                 |************|
                 |*U1**U2**U3*|
                 |************|
                 |*U4**U5**U6*|
                 |************|
                 |*U7**U8**U9*|
                 |************|
     ************|************|************|************
     *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*
     ************|************|************|************
     *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*
     ************|************|************|************
     *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*
     ************|************|************|************
                 |************|
                 |*D1**D2**D3*|
                 |************|
                 |*D4**D5**D6*|
                 |************|
                 |*D7**D8**D9*|
                 |************|
"""
from cube import Cube
cube = Cube("YBYWYWBWWWOWGWWRGYWBGRBYRGGOYORGORRBBGOBOBYYBRRGORYOOG")
cube.solve()
cube.print_command()
print(cube)

```

Input serial string in sequence as "U1U2U3U4U5U6U7U8U9 D1D2D3D4D5D6D7D8D9 F1F2F3F4F5F6F7F8F9 B1B2B3B4B5B6B7B8B9 L1L2L3L4L5L6L7L8L9 R1R2R3R4R5R6R7R8R9"

# Other Function
```python
from cube import Cube
cube = Cube()
cube.formula("U D F B L R U' D' F' B' L' R'")
cube.step1()  # 1st step of 7 steps
print(cube)  # output cube's status after the 1st step
cube.step2()
print(cube)
cube.step3()
print(cube)

...
```