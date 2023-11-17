## 1. Does PyInputPlus come with the Python Standard Library?

No. 

## 2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?

It's a shorter way to write the PyInputPlus function.

## 3. What is the difference between inputInt() and inputFloat()?

inputInt(): Takes the input in integer format.

inputFloat(): Takes the input in Float format.

## 4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?

pyip.inputNum('>',min=0,lessThan=100)

## 5. What is passed to the allowRegexes and blockRegexes keyword arguments?

They take a list of regular expression in strings to see the pyip function will accept or block th required value.

## 6. What does inputStr(limit=3) do if blank input is entered three times?

It stops the input to appear maximum three times.

## 7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?

It stops the input to appear maximum three times and if the third input is wrong, then the default value 'hello' is placed.
