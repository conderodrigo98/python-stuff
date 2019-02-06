# python-stuff
A folder with some python scritps

## lev.py
A script that calculates the Levenshtein distance between two given strings.

## maze.py
A script that solves a maze given in a txt file (maze.txt) using Lee's algorithm. For the program to work, the txt file should follow this format: the start should be marked with an 'S' and should be the first character, the end should be marked with an 'E' and can be anywhere, paths ahould be marked with a '0' and walls with '#' or whatever non-numerical character you please. The script returns a string of symbols N,E,S,W.
### Example usage:
Input: 

S000#

###0#

E000#

Output:

EEESSWW
