# Math formulas

Lib for geometric calculations

## Functions description

### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: S = a + b + c

### Circle

- `area` - returns area of circle
- `perimeter` - returns perimeter of circle

Example:

```python
from circle import area, perimeter

print(area(r=1))
# 3.14
print(perimeter(r=1))
# 6.28
```

### Triangle

- `area` - returns area of triangle
- `perimeter` - returns perimeter of triangle

Example:

```python
from triangle import area, perimeter

print(area(a=1, h=1))
# 0.5
print(perimeter(a=1, b=2, c=3))
# 6
```

### Rectangle

- `get_rectangle_area` - returns area of rectangle
- `get_rectangle_area` - returns perimeter of rectangle

Example:

```python
from rectangle import get_rectangle_area, get_rectangle_perimeter

print(get_rectangle_area(a=1, b=2))
# 2
print(get_rectangle_perimeter(a=1, b=2))
# 6
```

### Square

- `area` - returns area of square
- `perimeter` - returns perimeter of square

Example:

```python
from square import area, perimeter

print(area(a=1))
# 1
print(perimeter(a=1))
# 4
```

## Release Notes

```md
### 8ba9aeb3cea847b63a91ac378a2a6db758682460

- Added circle.py and square.py
```

```md
### d078c8d9ee6155f3cb0e577d28d337b791de28e2

- Updated README.md
```

```md
### 599dec455882dcca9c9f3fc6a3c2fcb70c786ac6

- Added rectangle.py
```

```md
### b4c63db61f16a6edca818c109c9c5748477db82f

- Fixed rectangle.py
- Added triangle.py
```

```md
### 50478ec2443d5bf1e53819bf8c8be35aacc747f3

- Update .gitignore
```

```md
### 0844b16b15ffa8571108f410296c71b99dc4ea13

- Fix .gitignore
```

```md
### c6743ee3a26f2a04d040b416c72ca22b1695784b

- Add tests
```

```md
### d54ed069606658d5fdf56320fe5cd59355beaa74

- Fix __init__.py
```



