## 1. What does the code for an empty dictionary look like?

d={}

## 2. What does a dictionary value with a key 'foo' and a value 42 look like?

d={'foo':42}

## 3. What is the main difference between a dictionary and a list?

Dictionary is within curly brackets while list has paranthesis.
List has comma seperated values while dictionary has comma seperated key-value pairs.

## 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

'foo' doesnt exist on the dictionary and returns an Error message.

## 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

'cat' in spam checks if cat is a key in spam.
'cat' in spam.keys() checks the same as above.

## 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

'cat' in spam will check if 'cat' is a key in spam.
'cat' in spam.values() checks if 'cat' os a value in spam'.

## 7. What is a shortcut for the following code?

spam.setdefault('color','black)

## 8. What module and function can be used to “pretty print” dictionary values?

pprint module
pprint.pprint(d)

