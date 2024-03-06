# 0x09. Island Perimeter

This Python function, `island_perimeter`, calculates the perimeter of an island based on the given grid.

## Function Signature

```python
def island_perimeter(grid: List[List[int]]) -> int:
    pass
```

## Parameters

- `grid`: A list of lists of integers representing the island. Each cell contains:
  - `0`: Water
  - `1`: Land

## Constraints

- The grid is rectangular, with its width and height not exceeding 100.
- Cells are connected horizontally/vertically (not diagonally).
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## Example

```python
grid = [
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]

perimeter = island_perimeter(grid)
print(perimeter)
```

## Output

```
16
```

## Explanation

The perimeter is calculated based on the 1's (land) and 0's (water) in the grid. The result, in this case, is 16.
