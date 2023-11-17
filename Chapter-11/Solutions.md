## 1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.

assert spam<10

## 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).

assert eggs.upper() != bacon.upper()

## 3. Write an assert statement that always triggers an AssertionError.

assert False

## 4. What are the two lines that your program must have in order to be able to call logging.debug()?

import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')

## 5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?

import logging
logging.basicConfig(filename='programLog.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

## 6. What are the five logging levels?

DEBUG, INFO, WARNING, ERROR, CRITICAL.

## 7. What line of code can you add to disable all logging messages in your program?

logging.disable(logging.CRITICAL)

## 8. Why is using logging messages better than using print() to display the same message?

We can disable the logging messages with a single line of code using the logging.disable() function.

## 9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

Step Over: This will execute the function call.

Step In: This will move the debugger into the function call.

Step Out: This will execute the rest of the code till it steps out of the function call.

## 10. After you click Continue, when will the debugger stop?

It will stop when it has reached the end of the program with a breakpoint.

## 11. What is a breakpoint?

This will stop the debugger when the program execution comes to a particular line.

## 12. How do you set a breakpoint on a line of code in Mu?

Click the line number which makes a red dot will be there near the breakpoint.
