# Rotate Array — DSA

A technical implementation and presentation of the Rotate Array problem using Python, covering multiple approaches from brute force to optimized solutions.

## Problem Statement

Given an integer array nums and an integer k, rotate the array to the right by k positions.

### Example

Input:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

Output:
[5, 6, 7, 1, 2, 3, 4]


## Approaches

### 1. Brute Force Approach

The array is rotated one position at a time for k rotations.

- Time Complexity: O(n × k)
- Space Complexity: O(1)

Implementation:
[bruteforceapproach.py](./bruteforceapproach.py)


### 2. Reversal Algorithm — Manual Implementation

The array is reversed using a two-pointer technique and divided into sections to achieve the required rotation.

- Time Complexity: O(n)
- Space Complexity: O(1)

Implementation:
[approach2.py](./approach2.py)


### 3. Reversal Algorithm — Python Implementation

The reversal technique is implemented using Python's built-in list operations.

- Time Complexity: O(n)
- Space Complexity: O(1)

Implementation:
[optimalsolution.py](./optimalsolution.py)


## Complexity Comparison

| Approach | Time Complexity | Space Complexity |
|---|---|---|
| Brute Force | O(n × k) | O(1) |
| Reversal — Manual | O(n) | O(1) |
| Reversal — Python | O(n) | O(1) |


## Presentation

The presentation explains the problem, different approaches, implementations, and complexity analysis.

[View Presentation](./rotate-array-presentation.pptx)


## Presentation Video

[Watch the Presentation](https://drive.google.com/file/d/1DMk0UUv8jL6f4i9FVkaJ5EisFO3NJbJQ/view?usp=sharing)


## Technologies Used

- Python
- Data Structures & Algorithms
- Array Manipulation


## Key Learning

- Understanding different approaches to solve the same problem
- Comparing time and space complexity
- Implementing the array reversal technique
- Improving a solution from brute force to an optimized approach
- Presenting and explaining a DSA problem clearly
