1. What is []?

List

2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

spam[2]='hello'

For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

3. What does spam[int(int('3' * 2) // 11)] evaluate to?

'd'

4. What does spam[-1] evaluate to?

'd'

5. What does spam[:2] evaluate to?

['a','b']

For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

6. What does bacon.index('cat') evaluate to?

1

7. What does bacon.append(99) make the list value in bacon look like?

[3.14, 'cat', 11, 'cat', True, 99]

8. What does bacon.remove('cat') make the list value in bacon look like?

[3.14, 11, 'cat', True, 99]

9. What are the operators for list concatenation and list replication?

. List concatenation: +
  List replication: *

10. What is the difference between the append() and insert() list methods?

append(): This is used insert a value at the end of the list.

insert(): This is written as insert(index,value). At the index position, the index is written and the value will be placed at the position of index.

11. What are two ways to remove values from a list?

remove() and del

12. Name a few ways that list values are similar to string values.

List and String values are comma separated values.
The can be concatenated as well as replicated.

13. What is the difference between lists and tuples?

Lists are comma separated values enclosed within parenthesis while tuples are enclosed within curly brackets.
Lists are mutable while tuples are immutable.

14. How do you type the tuple value that has just the integer value 42 in it?

tuple=(42)

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

Tuple form of a list= tuple([])
List form of a tuple= list(())

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

They contain references.

17. What is the difference between copy.copy() and copy.deepcopy()?

copy.copy(): This is used to copy the values of the list in the same manner as it is.
copy.deepcopy(): This is used to copy the values of the list that contains lists as well.

