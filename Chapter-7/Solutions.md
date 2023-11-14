## 1. What is the function that creates Regex objects?

import re
re.compile()

## 2. Why are raw strings often used when creating Regex objects?

This is because regular expressions use backslash in themselves.

## 3. What does the search() method return?

The search() method returns if you find a regex pattern is found in a string.

## 4. How do you get the actual strings that match the pattern from a Match object?

We can use group(). 

## 5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

group 0: (\d\d\d)-(\d\d\d-\d\d\d\d).

group 1: (\d\d\d).

group 2: (\d\d\d-\d\d\d\d).

## 6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

r'()'.

## 7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

list of strings: THis has no groups and returns ['(\d\d\d)-(\d\d\d-\d\d\d\d)']

list of tuples of strings: This has groups and returns [('(\d\d\d)','(\d\d\d)','(\d\d\d\d)')]

## 8. What does the | character signify in regular expressions?

It is called a pipe. It is used to match two expressions.

## 9. What two things does the ? character signify in regular expressions?

It matches zero or one of the group before the ? character.

## 10. What is the difference between the + and * characters in regular expressions?

+ character: match one or more group that is before the plus character.

* character: match zero or more group that is before the star character.

## 11. What is the difference between {3} and {3,5} in regular expressions?

{3}: This wil replicate the regex three times.

{3,5}: This will replicate the three times, then four times, and then five times.

## 12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

\d: Numbers from 0-9.

\w: The numbers, alphabets, and underscores.

\s: Spaces.

## 13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

\D: Characters except numbers 0-9.

\W: Characters except alphabets, numbers, and underscores.

\S: Characters except spaces.

## 14. What is the difference between .* and .*??

.*: Uses greedy mode. It also uses the longest string.

.*?: Uses non-greedy mode. It also uses the shortest string.

## 15. What is the character class syntax to match all numbers and lowercase letters?

[a-z0-9]

## 16. How do you make a regular expression case-insensitive?

re.i

## 17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?

The . character helps to match to a character except newline. With re.DOTALL, you cn make all characters except newline character matched.

## 18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

'X drummers, X pipers, five rings, X hens'

## 19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

It helps to remove spaces and comments.

## 20. How would you write a regex that matches a number with commas for every three digits? It must match the following:

c=re.compile(r'(^\d{1,3})(\d{3})*$')
c.search('12,34,567').group()

## 21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

f=re.compile(r'[A-Z]\w [A-Z]\w')
s=f.findall('Haruto Watanabe, haruto Watanabe, Alice Watanabe, Robocop Watanabe, Mr.Watanabe, Haruto watanabe')
s.group()

## 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:

s=re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs).', re.I|re.DOTALL)
s.findall('''Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
'Robocop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.''')


    'Alice eats apples.'
    'Bob pets cats.'
    'Carol throws baseballs.'
    'Alice throws Apples.'
    'BOB EATS CATS.'

but not the following:

    'RoboCop eats apples.'
    'ALICE THROWS FOOTBALLS.'
    'Carol eats 7 cats.
