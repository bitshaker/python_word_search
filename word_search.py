#!/usr/bin/env python3
"""
Word Search Solver

This program finds words in a letter grid (like a word search puzzle).
It searches in all 8 directions: horizontal, vertical, and diagonal,
both forward and backward.

Date: 2025
"""

import sys
from typing import List, Tuple

def load_grid(filename: str) -> List[List[str]]:
    """
    Load the letter grid from a text file.

    The grid file should have letters separated by spaces, one row per line.
    Empty lines are ignored.

    Args:
        filename (str): Path to the grid file

    Returns:
        List[List[str]]: 2D list where each inner list is a row of letters

    Example grid file:
        W I S D O M
        B C I A K D
        S H A I M E
    """
    grid = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()  # Remove whitespace from start/end
            if line:  # Skip empty lines
                # Split line by spaces and keep only non-empty parts
                letters = [char for char in line.split() if char]
                grid.append(letters)
    return grid

def load_words(filename: str) -> List[str]:
    """
    Load the list of words to search for from a text file.

    Each word should be on its own line. Words are converted to uppercase
    for case-insensitive matching.

    Args:
        filename (str): Path to the words file

    Returns:
        List[str]: List of uppercase words to search for

    Example words file:
        WISDOM
        GENESIS
        EXODUS
    """
    words = []
    with open(filename, 'r') as f:
        for line in f:
            word = line.strip().upper()  # Remove whitespace and make uppercase
            if word:  # Skip empty lines
                words.append(word)
    return words

def get_directions() -> List[Tuple[int, int, str]]:
    """
    Define all 8 possible directions to search for words.

    Each direction is represented as a tuple:
    (row_change, col_change, direction_name)

    The row_change and col_change values determine how to move:
    - Positive values move down/right
    - Negative values move up/left
    - Zero means no movement in that direction

    Returns:
        List[Tuple[int, int, str]]: List of (delta_row, delta_col, name) tuples

    Direction meanings:
    - horizontal_right: left to right (→)
    - horizontal_left: right to left (←)
    - vertical_down: top to bottom (↓)
    - vertical_up: bottom to top (↑)
    - diagonal_down_right: top-left to bottom-right (↘)
    - diagonal_down_left: top-right to bottom-left (↙)
    - diagonal_up_right: bottom-left to top-right (↗)
    - diagonal_up_left: bottom-right to top-left (↖)
    """
    return [
        (0, 1, "horizontal_right"),      # →
        (0, -1, "horizontal_left"),       # ←
        (1, 0, "vertical_down"),          # ↓
        (-1, 0, "vertical_up"),           # ↑
        (1, 1, "diagonal_down_right"),    # ↘
        (1, -1, "diagonal_down_left"),    # ↙
        (-1, 1, "diagonal_up_right"),     # ↗
        (-1, -1, "diagonal_up_left"),     # ↖
    ]

def is_valid_position(grid: List[List[str]], row: int, col: int) -> bool:
    """
    Check if a given row and column position is within the grid boundaries.

    Args:
        grid (List[List[str]]): The 2D letter grid
        row (int): Row index to check
        col (int): Column index to check

    Returns:
        bool: True if position is valid, False if out of bounds

    This prevents IndexError when accessing grid[row][col].
    """
    # Check row bounds: 0 <= row < number_of_rows
    # Check col bounds: 0 <= col < number_of_columns
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def find_word_in_direction(grid: List[List[str]], word: str, start_row: int, start_col: int,
                          delta_row: int, delta_col: int) -> bool:
    """
    Check if a word exists starting at a specific position and moving in a given direction.

    This function "walks" through the grid in the specified direction, checking
    if each letter of the word matches the corresponding grid position.

    Args:
        grid (List[List[str]]): The 2D letter grid
        word (str): The word to search for (already uppercase)
        start_row (int): Starting row position (0-based)
        start_col (int): Starting column position (0-based)
        delta_row (int): How much to change row for each letter (-1, 0, or 1)
        delta_col (int): How much to change column for each letter (-1, 0, or 1)

    Returns:
        bool: True if the entire word is found, False otherwise

    Example:
        If word="CAT", start_row=0, start_col=0, delta_row=0, delta_col=1:
        Checks grid[0][0]=='C', grid[0][1]=='A', grid[0][2]=='T'
    """
    # Loop through each character in the word
    for i, char in enumerate(word):
        # Calculate the position for this character
        row = start_row + i * delta_row
        col = start_col + i * delta_col

        # If position is out of bounds OR letter doesn't match, word not found
        if not is_valid_position(grid, row, col) or grid[row][col] != char:
            return False

    # All characters matched - word found!
    return True

def search_for_words(grid: List[List[str]], words: List[str]) -> List[Tuple[str, int, int, str]]:
    """
    Search the entire grid for all words in all 8 directions.

    This is the main search algorithm. It uses a brute-force approach:
    for each word, try every possible starting position, in every direction.

    Args:
        grid (List[List[str]]): The 2D letter grid
        words (List[str]): List of words to search for

    Returns:
        List[Tuple[str, int, int, str]]: List of found words with their details.
            Each tuple contains: (word, start_row_1based, start_col_1based, direction)

    Algorithm explanation:
    1. For each word in the list
    2. Try every possible starting position (every row, every column)
    3. For each starting position, try all 8 directions
    4. If word is found in any direction, record it and move to next word
    5. Return list of all found words

    Note: This finds the FIRST occurrence of each word. If a word appears
    multiple times, only the first one found is returned.
    """
    found_words = []  # Will store results: (word, row, col, direction)
    directions = get_directions()  # Get the 8 possible directions

    # Loop through each word we want to find
    for word in words:
        word_found = False  # Track if we found this word yet

        # Try every possible starting position in the grid
        for start_row in range(len(grid)):  # For each row
            for start_col in range(len(grid[0])):  # For each column

                # Try every possible direction from this starting position
                for delta_row, delta_col, direction in directions:

                    # Check if the word exists in this direction
                    if find_word_in_direction(grid, word, start_row, start_col, delta_row, delta_col):

                        # Found it! Convert to 1-based indexing for user-friendly output
                        # (computers use 0-based, but humans prefer 1-based counting)
                        found_words.append((word, start_row + 1, start_col + 1, direction))
                        word_found = True
                        break  # No need to check other directions for this word

                if word_found:
                    break  # No need to try other starting positions for this word

            if word_found:
                break  # Move to next word in the list

    return found_words

def main():
    """
    Main function that runs the word search program.

    This function:
    1. Checks command line arguments
    2. Loads the grid and word files
    3. Runs the word search
    4. Displays results on screen
    5. Saves results to a file

    Command line usage: python word_search.py <grid_file> <words_file>
    """

    # Check if user provided exactly 2 arguments (grid file and words file)
    if len(sys.argv) != 3:
        print("Usage: python word_search.py <grid_file> <words_file>")
        print("Example: python word_search.py letter_grid.txt words_to_search.txt")
        sys.exit(1)

    # Get filenames from command line arguments
    grid_file = sys.argv[1]   # First argument: grid file
    words_file = sys.argv[2]  # Second argument: words file

    try:
        # Step 1: Load the letter grid from file
        grid = load_grid(grid_file)

        # Step 2: Load the list of words to search for
        words = load_words(words_file)

        # Show user what we loaded
        print(f"Loaded grid with {len(grid)} rows and {len(grid[0])} columns")
        print(f"Searching for {len(words)} words...")
        print()  # Empty line for readability

        # Step 3: Search for all words in the grid
        found_words = search_for_words(grid, words)

        # Step 4: Display results on screen
        if found_words:
            print(f"Found {len(found_words)} words:")
            # Print table header with fixed-width columns
            print(f"{'Word':<15} {'Start Row':>9} {'Start Col':>9} {'Direction':<20}")
            print("-" * 55)  # Separator line

            # Print each found word in a nicely formatted row
            for word, row, col, direction in found_words:
                print(f"{word:<15} {row:>9} {col:>9} {direction:<20}")
        else:
            print("No words found in the grid.")

        # Step 5: Save results to a file for later reference
        with open('word_search_results.txt', 'w') as f:
            # Write the same formatted table to file
            f.write(f"{'Word':<15} {'Start Row':>9} {'Start Col':>9} {'Direction':<20}\n")
            f.write("-" * 55 + "\n")
            for word, row, col, direction in found_words:
                f.write(f"{word:<15} {row:>9} {col:>9} {direction:<20}\n")

        print("\nResults also saved to word_search_results.txt")

    except FileNotFoundError as e:
        # Handle case where input files don't exist
        print(f"Error: File not found - {e.filename}")
        print("Make sure both grid file and words file exist.")
        sys.exit(1)
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Error: {e}")
        print("Something went wrong. Check your input files are in the correct format.")
        sys.exit(1)

# This is a Python convention: if this file is run directly (not imported),
# call the main() function to start the program
if __name__ == "__main__":
    main()
