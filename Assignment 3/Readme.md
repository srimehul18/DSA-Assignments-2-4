# Sorting Performance Analyzer (SPA)

## Overview
This project implements and compares three sorting algorithms: Insertion Sort, Merge Sort, and Quick Sort. The aim is to study their performance on different types of datasets and relate practical results with theoretical time complexity.

## Algorithms Implemented
- Insertion Sort
- Merge Sort
- Quick Sort (using random pivot and optimization)

## Features
- Sorting algorithms implemented from scratch
- Dataset generation for:
  - Random data
  - Sorted data
  - Reverse sorted data
- Performance measurement using execution time
- Comparative analysis of results

## Dataset Sizes
- 1000
- 5000
- 10000

## How to Run
1. Save the file as `spa_sorting.py`
2. Open terminal in the project folder
3. Run:
   python spa_sorting.py

## Output
- Displays correctness check of sorting algorithms
- Prints performance table with execution time (in milliseconds)

## Observations
- Insertion Sort performs well for small or nearly sorted data
- Merge Sort gives consistent performance for all cases
- Quick Sort is fast on average but depends on pivot selection

## Conclusion
The choice of sorting algorithm depends on input size and data type. Merge Sort is reliable, Quick Sort is efficient on average, and Insertion Sort is useful for small datasets.
