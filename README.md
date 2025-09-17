# Word Search Solver

A Python program that finds words in a letter grid, just like solving a word search puzzle!

## What This Program Does

This program automatically searches for words in a grid of letters. It can find words that go:
- **Horizontal**: left to right (→) or right to left (←)
- **Vertical**: top to bottom (↓) or bottom to top (↑)
- **Diagonal**: in all 4 diagonal directions (↘ ↙ ↗ ↖)

For each word found, it tells you:
- The word name
- Which row and column it starts at
- Which direction it goes

## How It Works

The program uses a **brute-force search algorithm**:

1. **Load the grid**: Read letters from a text file into a 2D list
2. **Load the words**: Read words to search for from another text file
3. **Search systematically**: Try every possible starting position, in every direction
4. **Check each possibility**: For each position + direction, see if the word fits
5. **Record results**: Save where each word was found

## Files in This Project

- `word_search.py` - The main Python program
- `letter_grid.txt` - A 17×17 grid of letters containing hidden words
- `words_to_search.txt` - List of 42 Bible book names to find
- `word_search_results.txt` - Output file showing where each word was found
- `README.md` - This file explaining everything

## How to Run

Make sure you have Python 3 installed, then:

```bash
python3 word_search.py letter_grid.txt words_to_search.txt
```

### Command Line Arguments

The program requires exactly 2 arguments:

```bash
python word_search.py <grid_file> <words_file>
```

- `<grid_file>`: Path to the text file containing the letter grid (e.g., `letter_grid.txt`)
- `<words_file>`: Path to the text file containing the list of words to search for (e.g., `words_to_search.txt`)

**Examples:**
```bash
# Using default files
python3 word_search.py letter_grid.txt words_to_search.txt

# Using custom files
python3 word_search.py my_grid.txt my_words.txt

# Using absolute paths
python3 word_search.py /path/to/grid.txt /path/to/words.txt
```

If you provide the wrong number of arguments, you'll see:
```
Usage: python word_search.py <grid_file> <words_file>
Example: python word_search.py letter_grid.txt words_to_search.txt
```

## Input File Formats

### Grid File (letter_grid.txt)
Letters separated by spaces, one row per line:
```
W I S D O M
B C I A K D
S H A I M E
```

### Words File (words_to_search.txt)
One word per line:
```
WISDOM
GENESIS
EXODUS
```

## Sample Output

```
Loaded grid with 17 rows and 17 columns
Searching for 42 words...

Found 42 words:
Word            Start Row Start Col Direction
-------------------------------------------------------
AMOS                   14         1 diagonal_up_right
BARUCH                 14        10 horizontal_left
CHRONICLES              8        12 diagonal_down_left
...
```

## Learning Python Concepts

This program teaches important programming ideas:

### Data Structures
- **Lists**: Store the grid as `List[List[str]]` and words as `List[str]`
- **Tuples**: Store direction data as `(delta_row, delta_col, name)`
- **2D Arrays**: Navigate a grid using `[row][column]` indexing

### Algorithms
- **Brute Force**: Try all possibilities systematically
- **Grid Traversal**: Move through a 2D space in different directions
- **String Matching**: Compare characters one by one

### Programming Techniques
- **File I/O**: Reading from and writing to text files
- **Command Line Arguments**: Getting filenames from the user
- **Error Handling**: Dealing with missing files and other problems
- **Functions**: Breaking code into reusable parts
- **Type Hints**: Using `-> List[str]` to show what functions return

### Key Functions Explained

#### `load_grid(filename)`
Reads a text file and converts it into a 2D list of letters.

#### `get_directions()`
Returns all 8 possible directions as tuples: `(row_change, col_change, name)`

#### `is_valid_position(grid, row, col)`
Checks if a position is inside the grid boundaries (prevents crashes!)

#### `find_word_in_direction(grid, word, start_row, start_col, delta_row, delta_col)`
The core search function - walks through the grid in one direction to see if a word fits.

#### `search_for_words(grid, words)`
Main search algorithm - tries every word at every starting position in every direction.

## Try It Yourself!

1. **Modify the grid**: Add your own letters to `letter_grid.txt`
2. **Change the words**: Add different words to `words_to_search.txt`
3. **Experiment**: Try making the grid bigger or smaller
4. **Extend it**: Add features like finding ALL occurrences (not just the first)

## Understanding Directions

The 8 directions use coordinate changes:
- `(0, 1)` = horizontal_right: same row, column increases
- `(1, 0)` = vertical_down: row increases, same column
- `(1, 1)` = diagonal_down_right: both row and column increase
- `(-1, -1)` = diagonal_up_left: both row and column decrease

## Why 1-Based vs 0-Based Indexing

- **Computers** use 0-based indexing: `grid[0][0]` is the top-left corner
- **Humans** prefer 1-based: "Row 1, Column 1" is easier to understand
- The program converts from computer-style (0-based) to human-style (1-based) for output

---

**Created for learning Python programming concepts!** 🎓
