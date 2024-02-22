# Rotate 2D Matrix

## Description
This is a simple Python script that rotates a given 2D matrix (list of lists) by 90 degrees clockwise. The rotation is performed in place, meaning the original matrix is modified rather than creating a new one.

## Usage
To use this script, follow these steps:

1. Ensure you have Python installed on your system.
2. Download or clone the repository containing the script.
3. Navigate to the directory containing the script in your terminal or command prompt.
4. Run the script using Python with the following command:
    ```
    python rotate_2d_matrix.py
    ```
5. Follow the prompts to input the 2D matrix you want to rotate.

## Example
Suppose you have the following 2D matrix:
```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```
After rotating it 90 degrees clockwise, the resulting matrix will be:
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Implementation Details
The script accepts user input for the dimensions of the matrix (number of rows and columns) and the elements of the matrix. It then rotates the matrix in place by performing a series of swaps between elements. The rotation algorithm involves iterating through each layer of the matrix and swapping elements within that layer.

## License
This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
![Author](https://img.shields.io/badge/Author-Azuka%20Uteh-blue.svg)
