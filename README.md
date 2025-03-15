# first_unique_element
Find first unique non-repeating element of an giving array of integers.

# Problem Statement:
Find first single element in a sorted array whose value not repeated.

```
Input:
[1,1,2,2,2,3,3,3,3,3,3,4,5,5,5,5,6,6,7,7,7,9,9,9,10,10,10]

Output
4
```

# Solution:
- Loop through array.
- Use double indices i and j.
- For each i in array, create a second loop j starting from i. 
- If j -i longer than 1, advance i index to j and repeat algorithm. 
- Break the loop when length of j - i == 1.