
# Poker Hand Evaluator

## Overview
A Python program that generates a random five-card poker hand and automatically determines its hand ranking using custom classification algorithms.

## Features
- Generates a standard 52-card deck
- Draws cards without replacement
- Extracts card ranks and suits
- Counts rank and suit frequencies
- Detects all ten poker hand rankings
- Supports both ace-high and ace-low straights
- Validates user input
- Includes 36 test cases covering individual functions and complete hand evaluation

## Project Structure

| File | Purpose |
|---|---|
| main.py | User interaction and program execution |
| deck.py | Deck generation and card drawing |
| evaluator.py | Hand classification algorithms |
| test_evaluator.py | Function and integration testing |

## Concepts Learned
- Dictionaries and frequency counting
- Sets and duplicate detection
- List sorting
- String manipulation
- Exception handling
- Module imports
- Separation of concerns
- Algorithm design
- Automated testing with assertions
- Debugging and edge-case testing

## How to Run

```bash
python3 main.py
```

Press Enter to generate and evaluate a five-card hand.

## Example Output

```text
Press enter to see your hand:
Queen of Hearts
5 of Spades
9 of Diamonds
9 of Hearts
10 of Spades
One pair
```

## Testing

```bash
python3 test_evaluator.py
```

## Current Limitations
- Evaluates exactly five valid cards
- Classifies hand categories without comparing kickers
- Does not yet determine the best five-card combination from seven cards

## Future Improvements
- Seven-card Texas Hold'em evaluation
- Hand strength comparison
- Multiple-player support
- Hand frequency simulations
