# Error Handling and Pickling
*MShapiro, 8/25/22*

## Introduction

In this markdown document, I will explain the basics of how to display custom error messages for users of our Python scripts. I will also cover pickling (binary files). 

## Error Handling

When user input is required as part of running a script, this opens the door for user error. Any user can, and most likely will, introduce errors while running a program. As we know from developing code, when you make an error in Python, you will see a system generated error message in red text. But, these messages are sometimes too technical or not informative enough for a user. 
![Figure 1](https://github.com/meshapiro/IntroToProg-Python-Mod07/blob/main/docs/error_message.png "Figure 1")


We can instead add a "try-except" block to our code, which will allow the program to capture errors, and display more informative error message. 

To use try-except, all the code you are running (the main body, not necessarily the section where you define functions) can be enclosed in "try: " 

```
try:
    fltV1 = float(input("Enter value 1: "))
    fltV2 = float(input("Enter value 2: "))

    twoVals(fltV1, fltV2)
```  
Make sure to indent everything that happens within the "try." 
After the main body of the script enclosed in "try: ", you will add "except: " to tell Python how to handle exceptions (errors). You could just print a generic error message, like this:
```
except Exception as e:
    print("There was an error!")
```

That would solve the issue of the error message being too technical, but it doesn't help it be more informative. We can get the details of an error by using Python's Exception class:

```
except Exception as e:
  print(e, e.__doc__, type(e), sep='\n')
```
We can print the exception itself (e, the name we have given it) as well as more detailed documentation, and the type of error - type(e). 

Once we have these details, we can create separate Exceptions for each type of error that seems likely, and display custom messages for them. If we know the type of error, we can replace "Exception" in the "except Exception as e:" statement, with whatever the actual exception type is. For instance, I wrote a function that takes input for two numeric values and divides them. I wanted to see what would happen if I entered something non-numeric: 

```
try:
    fltV1 = float(input("Enter value 1: "))
    fltV2 = float(input("Enter value 2: "))

    twoVals(fltV1, fltV2)
    fltV1, fltV2, fltQuot = twoVals(fltV1, fltV2)  # unpack tuple

    output = displayVals(fltV1, fltV2, fltQuot)
    print(output)

except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
```
I tried running this but, when asked for my input for the first value, I entered "h"
![Figure 2](https://github.com/meshapiro/IntroToProg-Python-Mod07/blob/main/docs/ValueError.png "Figure 2")
Since I printed type(e), I now know that this incorrect entry caused a ValueError type of exception. So, now I can add a message for this specific case:
```
except ValueError as e:
    print("Input data must be numeric!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
```
I experimented with breaking my program in different ways and ended up adding an exception for trying to divide by 0 (ZeroDivisionError). I experimented with multiplying instead of dividing, and tried multiplying very large numbers together to see if I could create an infinite value error (something I thought I remembered from a different programming language), but Python didn't error over that, it just returned the value "inf." 

I also wrote my output to a file, and determined that if I tried to append data to a file that didn't already exist, I got a FileNotFoundError, so I added an exception for that as well. 
You can also look at Python's list of built in exceptions to try to anticipate which ones might be relevant for your program: https://docs.python.org/3/library/exceptions.html#bltin-exceptions

## Pickling



## Summary
