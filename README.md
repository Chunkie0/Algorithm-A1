# Bubble Sort Algortithm
## Bubble sorting algorithm where each element is compared to the one next to it and they are swapped if the one on the left is larger than the one on the right.

### A short description of how the code works:

This part of code will convert string into an array of letters
```
letters = list(name)
```

This will help while loop to keep looping until its value is changed to false
```
not_sorted = True
```

By assigning not_sorted to false, it will exit the while loop if it reaches the end of while loops block without its value changed back to true
```
not_sorted = False
```

Will loop through range of numbers starting from 0 to the length of the array and assign it to i
```
for i in range(len(letters)-1):
```

Checks whether decimal number of the given character in the ascii table is higher then the one on the right
```
if ord(letters[i]) > ord(letters[i+1]):
```
and if it's true, code below will swap them and change not_sorted from false to true, to not end the while loop, so it can check again whether or not its sorted
```
letters[i], letters[i+1] = letters[i+1], letters[i]
not_sorted = True
```

Returns sorted letters
```
return "".join(letters).strip()
```
