### python
Python refers to values that cannot change as immutable, and an immutable `list` is called a `tuple`.

#### Functions
- `Making an Argument Optional`
Calling this function with a first and last name is straightforward. If we’re using a middle name, however, we have to make sure the middle name is the last argument passed so Python will match up the positional arguments correctly.
`def get_formatted_name(first_name, last_name, middle_name=''):`

- `Passing an Arbitrary Number of Arguments`
Python allows a function to collect an arbitrary number of arguments from the calling statement.
`def make_pizza(*toppings):`
The `asterisk` in the parameter name `*toppings` tells Python to make a `tuple` called toppings, containing all the values this function receives.

- `Mixing Positional and Arbitrary Arguments`
If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition. Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.
`def make_pizza(size, *toppings):`
For example, if the function needs to take in a size for the pizza, that parameter must come before the parameter `*toppings`.

- `Using Arbitrary Keyword Arguments`
Sometimes you’ll want to accept an arbitrary number of arguments, but you won’t know ahead of time what kind of information will be passed to the function. In this case, you can write functions that accept as many `key-value pairs` as the calling statement provides.
You’ll often see the parameter name `**kwargs` used to collect nonspecific keyword arguments.
`def build_profile(first, last, **user_info):`
The definition of build_profile() expects a first and last name, and then it allows the user to pass in as many name-value pairs as they want. The double asterisks before the parameter `**user_info` cause Python to create a dictionary called user_info containing all the extra name-value pairs the function receives. Within the function, you can access the key-value pairs in user_info just as you would for any dictionary.

- `Styling Functions`
If you specify a default value for a parameter, no spaces should be used on either side of the equal sign:
`def function_name(parameter_0, parameter_1='default value')`

#### Classes
```python
❶ class Dog:
    """A simple attempt to model a dog."""

❷     def __init__(self, name, age):
        """Initialize name and age attributes."""
❸         self.name = name
        self.age = age

❹     def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
```




## Meta (2021.12 ~ Now)
8, 987, 133, 1091, 270, 958, 227, 314, 680, 1650, 1762, 1446, 1249, 71, 528, 65, 347, 791, 408, 680, 528, 938, 1249, 4, 1382, 121, 987, 622, 66, 227, 16, 791, 88, 23, 228, 766, 560, 605, 282, 1650, 215, 1249, 523, 938, 23, 1249, 162, 20, 1249, 42, 380, 14, 219, 451, 227, 1762, 50, 31, 138, 987, 162, 560, 314, 987, 528, 1249, 162, 236, 34, 1762, 215, 415, 605, 494, 282, 209, 47, 270, 42, 1249, 938, 88, 211, 939, 963, 1004, 127, 56, 34, 224,


推荐系统，问了objective function for embedding 和 classifier, 包括softmax细节。Evaluation on/offline 自己主动说的，面试官点头而过


## Amazon (2021.12 ~ Now)



## Google (2021.12 ~ Now)
