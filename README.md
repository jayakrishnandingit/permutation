# permutation
Algorithm to permutate a string with or without repeating characters.
## Equation
- If the string contains `n` unique characters, then,
`no. of permutations = n!`
- If the string contains `n` characters out of which there are `a` and `b` number of repeating characters, then,
`no. of permutations = n! / a! x b!`

# How to run?
```
cd permutation
python3 permutate.py bike
# if you count them there should be 24 (4!) unique permutations.
['bike', 'biek', 'bkie', 'bkei', 'beik', 'beki', 'ibke', 'ibek', 'ikbe', 'ikeb', 'iebk', 'iekb', 'kbie', 'kbei', 'kibe', 'kieb', 'kebi', 'keib', 'ebik', 'ebki', 'eibk', 'eikb', 'ekbi', 'ekib']

python3 permutate.py book
# if you count them there should be 12 (4!/2!) unique permutations, because "o" repeats twice.
['book', 'boko', 'bkoo', 'obok', 'obko', 'oobk', 'ookb', 'okbo', 'okob', 'kboo', 'kobo', 'koob']
```

How to run tests?
```
cd permutation
python3 -m unittest
```
