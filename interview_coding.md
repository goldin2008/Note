### Python
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
- `Inheritance`
When you create a child class, the parent class must be part of the current file and must appear before the child class in the file.
The `super() function ❹` is a special function that allows you to call a method from the parent class.

```python
❶ class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

❷ class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

❸     def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
❹         super().__init__(make, model, year)
❶         self.battery_size = 40

❷     def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
```

- `Instances as Attributes`
For example, if we continue adding detail to the ElectricCar class, we might notice that we’re adding many attributes and methods specific to the car’s battery. When we see this happening, we can stop and move those attributes and methods to a separate class called Battery. Then we can use a Battery instance as an attribute in the ElectricCar class:

```python
class Car:
    --snip--

class Battery:
    """A simple attempt to model a battery for an electric car."""

❶     def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

❷     def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
❸         self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
```
In the ElectricCar class, we now add an attribute called self.battery ❸. This line tells Python to create a new instance of Battery (with a default size of 40, because we’re not specifying a value) and assign that instance to the attribute self.battery.
❸ This line tells Python to look at the instance my_leaf, find its battery attribute, and call the method describe_battery() that’s associated with the Battery instance assigned to the attribute.

- `Importing a Single Class`

```python
❶ from car import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```
The import statement ❶ tells Python to open the car module and import the class Car.

- `Storing Multiple Classes in a Module`
You can store as many classes as you need in a single module, although each class in a module should be related somehow. The classes Battery and ElectricCar both help represent cars, so let’s add them to the module car.py.

```python
"""A set of classes used to represent gas and electric cars."""

class Car:
    --snip--

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
```

- `Importing Multiple Classes from a Module`
You import multiple classes from a module by separating each class with a comma ❶. Once you’ve imported the necessary classes, you’re free to make as many instances of each class as you need.
```python
❶ from car import Car, ElectricCar

❷ my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
❸ my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
```

- `Importing an Entire Module`

```python
❶ import car

❷ my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

❸ my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
```

- `Styling Classes`
Class names should be written in CamelCase. To do this, capitalize the first letter of each word in the name, and don’t use underscores. Instance and module names should be written in lowercase, with underscores between words.
Every class should have a docstring immediately following the class definition. The docstring should be a brief description of what the class does, and you should follow the same formatting conventions you used for writing docstrings in functions. Each module should also have a docstring describing what the classes in a module can be used for.
You can use blank lines to organize code, but don’t use them excessively. Within a class you can use one blank line between methods, and within a module you can use two blank lines to separate classes.
If you need to import a module from the standard library and a module that you wrote, place the import statement for the standard library module first. Then add a blank line and the import statement for the module you wrote. In programs with multiple import statements, this convention makes it easier to see where the different modules used in the program come from.

#### Unit Tests and Test Cases
A `unit test` verifies that one specific aspect of a function’s behavior is correct. A `test case` is a collection of unit tests that together prove that a function behaves as it’s supposed to, within the full range of situations you expect it to handle.
A good test case considers all the possible kinds of input a function could receive and includes tests to represent each of these situations. A test case with full coverage includes a full range of unit tests covering all the possible ways you can use a function. Achieving full coverage on a large project can be daunting. It’s often good enough to write tests for your code’s critical behaviors and then aim for full coverage only if the project starts to see widespread use.

```python
# test_name_function.py
from name_function import get_formatted_name

❶ def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
❷     formatted_name = get_formatted_name('janis', 'joplin')
❸     assert formatted_name == 'Janis Joplin'
```

- `Using Fixtures`
In testing, a fixture helps set up a test environment. Often, this means creating a resource that’s used by more than one test. We create a fixture in pytest by writing a function with the decorator `@pytest.fixture`. A decorator is a directive placed just before a function definition; Python applies this directive to the function before it runs, to alter how the function code behaves. Don’t worry if this sounds complicated; you can start to use decorators from third-party packages before learning to write them yourself.
```Python
import pytest
from survey import AnonymousSurvey

❶ @pytest.fixture
❷ def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

❸ def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
❹     language_survey.store_response('English')
    assert 'English' in language_survey.responses

❺ def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
❻         language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
```
When a parameter in a test function matches the name of a function with the `@pytest.fixture` decorator, the fixture will be run automatically and the return value will be passed to the test function. In this example, the function `language_survey()` supplies both `test_store_single_response()` and `test_store_three_responses()` with a language_survey instance.
When you want to write a fixture, write a function that generates the resource that’s used by multiple test functions. Add the `@pytest.fixture` decorator to the new function, and add the name of this function as a parameter for each test function that uses this resource. Your tests will be shorter and easier to write and maintain from that point forward.

## Scale AI
OOD是经典卡牌题, 52张扑克牌，给定六条规则（类似于德扑里同花顺、顺子的规则），如果一个手牌（hand）符合其中任意一条规则，就返回True，不valid的情况返回False。Followup是如果有wildcard怎么办。

开始coding 一样也是52张卡但是game像UNO，那么在一小时内完成会给你的CARD 和 DECK 的classes。
一开始给你4个玩家，每个玩家可以分到 X牌，然后需要整理卡的 RANK 和SUIT顺序。
游戏开始会deck出random一张牌，然后每个玩家会照一个指定的顺序打出一样 RANK/SUIT的 combination牌。打出的牌的RANK+SUIT 也有分数需要统计。没有相对的牌需要从DECK抽进HAND里。一旦一个人打完整个牌游戏结束。最后算出赢家。

Use OOP to code aspects of a poker game. The functions should check for poker patterns like flush, straight, full house, 4-of-a-kind, etc. Input is a list of cards and output is a boolean whether there is a pattern or not. The follow-up is to modify the functions to consider the Joker a wildcard. The wildcard can be used to match any rank and suit.
part of the problem is checking if the hand has 5 cards. So, the hand may have any number but if the hand does not have 5 cards, it should return False immediately.

地里提过的card game
有已经setup的code structrue (card, hand class)
用到了python enum
需要sort
计算max


## Meta (2021.12 ~ Now)
8, 987, 133, 1091, 270, 958, 227, 314, 680, 1650, 1762, 1446, 1249, 71, 528, 65, 347, 791, 408, 680, 528, 938, 1249, 4, 1382, 121, 987, 622, 66, 227, 16, 791, 88, 23, 228, 766, 560, 605, 282, 1650, 215, 1249, 523, 938, 23, 1249, 162, 20, 1249, 42, 380, 14, 219, 451, 227, 1762, 50, 31, 138, 987, 162, 560, 314, 987, 528, 1249, 162, 236, 34, 1762, 215, 415, 605, 494, 282, 209, 47, 270, 42, 1249, 938, 88, 211, 939, 963, 1004, 127, 56, 34, 224,


推荐系统，问了objective function for embedding 和 classifier, 包括softmax细节。Evaluation on/offline 自己主动说的，面试官点头而过


## Amazon (2021.12 ~ Now)



## Google (2021.12 ~ Now)
