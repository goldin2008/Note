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


## Google


## Meta
E7面试总共六轮，两轮ml design, 一轮coding, 一轮behavior, 一轮cross functional collaboration, 一轮tech retrospect.
Xfn这轮相当于另一轮behavior 重点在和pm以及其他非eng以及跨org eng的合作上
Tech retrospect讲一个你过去做的项目然后deep dive.
E5+昂赛五轮，两轮coding+两轮ai design+一轮bq

`店面`
电面是一轮一小时，40分钟coding(两道题）+20分钟BQ
第一题是easy版的560，只需要输出有没有可行的sequence （True or False）。首先是有负数的情况下怎么做，写了个presum，然后follow up问全正数的条件下怎么继续优化，提示下用two pointer优化了空间复杂度。
第二题是这个 梨蔻，但是matrix是正方形。follow up是如果有duplicate number该怎么改算法，对时间空间复杂度有没有影响。
https://leetcode.com/discuss/post/125301/find-longest-consecutive-path-in-a-matri-vgq9/
二面 就是利口： 1570 这题到处都看到有人面， 第二道题没见过后来尝试找也没找到， 有点像403。然后条件特别多也记不清了。这道题不太熟悉，只说了个思路，写到一半也没时间了。
129, 215   19(问能不能不traverse两边list), 1570
346-follow up：deque是static data structure还是dynamic，what if two threads call this at same time
162- no n[i]!=n[i+1] assumption, no need strictly greater than
follow up: what if we need to do strictly greater than, can you still use binary search?
125, 1249   133, 给两个list of interval，两个都sort过了，把两个merge起来
https://leetcode.com/discuss/post/124616/facebook-merge-two-interval-lists-by-eva-th6a/
1249, 415    339, 973     528, 270    1004,         938, 71     938, 复杂版56（双列）  415,139变形
打印矩阵对角线
给定一个整数矩阵，按从 右上到左下 的方向打印其对角线上的值。每条对角线都向 左下 方向移动。每条对角线的输出之间应有换行。[[1,  2,  3,  4],
[5,  6,  7,  8],
[9, 10, 11, 12]]
输出:1  
2 5
3 6 9
4 7 10
8 11  
12  
最大化最长假期
一个字符数组，其中包含 H 或 W：
H = 假期（Holiday）
W = 工作日（Workday）
有一定数量的个人休假天数，需要尽可能使的最长假期时间最大化。
例如：arr = [W, H, H, W, W, H, W], PTO = 2  
你可以最大化的假期长度为 5 天。[W, H, H, W, W, H, W]
    P  P
1  2  3  4  5
极简版伊斯刘146，只需要建一个class，可以get，put，remove不要求复杂度
528 follow-up有没有更快的方法sample
703 Variant get the larget nubmer from a data stream (call an API) where the the order is messed for at most K steps -> heap
Create a generator to return in order from a BST -> in order traversal with stack
第一题是给一个string类似 139依散酒的变形
s = "catanddog"
复制代码
和一个list of str作为dictionary,
d = ["cat", "and", "dog"]
复制代码
，问
s
复制代码
是否能够由
d
复制代码
中的单词表示，可以无限用。总感觉是lc的题，但没搜到，有知道的大神欢迎补充。交流了几种方法，后来决定用backtracking，应该是写得差不多，但后来问复杂度的时候有点发蒙，引导纠正了几次才过去。经提醒第一题应该是依散酒的变形，因为面试的时候其实还要求如果能被拆分，要输出拆分后的结果，所以在DP和backtracking之间选了backtracking，但现在想想DP也行
第二题是酒气伞973的变种，除了给一堆points
复制代码
以外，还给一个
query
复制代码
坐标，问最近的k个。follow up是如果
points
复制代码
的量特别大怎么办。
62变种，需要返回所有的unique path
第一题很像560，但是多了一个里面数值大于零的条件。
如果所有数值大于零，挪动 right pointer guarantees increament in subarray sum, 挪动 left pointer vice versa
当 subarray < k，++right 直到 subarray sum >= k, 当 subarray sum > k, ++left 标准解法用prefix sum 如果有大于零条件，可以用two pointers
第二题是109，要求不能用额外的资料结构。



`BQ`
The worst / best collaboration
A time when you find others know something you need but you don't know;
The most challenging experience that you cannot make the deadline
A time you need to learn something new rapidly
Why join phd? Why go back to the industry？
How do you take constructive suggestion
constructive feedback, conflict time, etc
constructive feedback; project without enough information
go beyond your scope, deal with hard people, constructive feedback, how to measure impact
conflicts/ cosntructive feedback/ do you have failed project
最骄傲项目，如何合作，被pushback，老板的反馈



`Coding`
第一题留领悟，感谢高抬贵手。
第二题没找到原题，island题，给定地图，要求在水上找建立一个新岛，不能和现存的岛四向接触，返回最大的岛的面积。DFS
跑两遍，第一遍用DFS把每个岛屿的面积算出来，第二遍跑岛屿相邻的0，把这个0的相邻所有的岛的面积相加
第一题夭柳嘶寺，要求Time O(depth) 空间 O(1)。空间复杂度最优的方案卡了很久在提示下才做出来。刷题的时候就没太注意，果然宰了跟头。幸好在不直接提示解法的情况下想到了。parent pointer的情况下，真的可以Time O(depth) Space O(1)
第二题简单版计算器，只考虑加减，要求时间O(N) 空间O(1)。空间复杂度最优上出了小小问题，again刷题还是要精才行。
1. Count how many times a given number shows up in a sorted array.
countOccurrences(20, {10, 10, 20, 20, 30, 30}) => 2
2.Given a 2D grid of 0s and 1s, what is the maximum area of an island that can be formed by flipping at most one 0 to 1? An island is formed by connected 1s, where connectivity is horizontal and vertical only (not diagonal) 下面这个example，答案是5[
  [1, 0],
  [0, 1],
  [1, 1]
]
1. 236
2. 一个data storage
# interface AbstractDataTypeWithLast<K, V> {
#     void put(K k, V v);
#     V get(K k);
#     K last();
#     void delete(K k);
# }
# last() return the most recent accessed key in the store.
# put("a", 1)
# put("b", 2)
# get("a")
# last() --> "a"
# delete("a")
# last() --> "b"
215, 1570
227 只有加号乘号，followup：所有符号和有括号时候； 236， 佛咯啊噗：不是Binary树怎么办， 如果有无数children怎么办；721 说思路
coding 1: baisic calculator & LRU cache; coding 2: valid parenthesis & simplify path;
coding 3: merge sorted arrays & find local minimum in an array； calculator限制不能用stack诸如此类
88, 314    95(h), 827    34, 💃陸苓 variant: non-negative input; follow-up: integer input
record most listened top 3 songs for each user
left + right side views of binary tree
121, 1197, 76
1.一个简单的calculator，只有加号和乘号
2. 回文，最多删除一个character判断是否是回文
3. 给几个城市人口，根据人口比例sample 城市 input: cities = [20,30,50]
call function: sample()
20% return 0, 30% return 1, 50% return 2
4. 最小parent
Coding1: （印度小哥，人狠话不多，原题基础上不停加限制条件，一会不准这个一会不准那个，搞麻了）636， follow up how to deal with multi thread. 1091，follow up 1: print the full path, follow up 2: change to non-binary matrix with ints, each int represent a cost to visit that position. Find the path with minimum cost
Coding 2: （国人小姐姐人超级nice,感谢放水！！）1644，560
528, 56   543, 398
528, 827
- round1: 215和变种 变种就是实现一个类封装起来(215这个高频题的解法的确不常规，需要一定沟通和验证，尤其是如果使用了3-way partition)注意关键词 3-way partition, 正常的快选用得是2-way.普通的快选都是二分，但215这个题后来可能是新加了个test case，里面有大量的重复值，二分的话会tle，需要用三分.用count sort一般需要知道数值范围，所以正常情况下其实不太考虑用count sort。一般都默认数据量最多是10^5，但数值范围不做限制，比如允许 -10^9~10^9，这时count sort可能就不太方便了。面试时面试官一般也不会告知数值范围是多少。当然感觉可以作为一个讨论点跟面试官聊
- round2: 346 207
coding 1 查树直径，合并三个有序数组；
coding 2 二叉搜索树范围内求和，造一个大岛屿
Coding的题目很简单，第一道题973，第二道题是IoU求交并比。我不确定题号是啥，可能是面试官自己想的，题目就是输入是2个字符串数组，求2个字符串数组的交集和并集的比例，不能使用额外空间。我的解法很简单，就是用字典计数来做。
coding 1:
14
💃陸苓 variant: non-negative input; follow-up: integer input
coding 2:
record most listened top 3 songs for each user
left + right side views of binary tree
coding 1: 680, follow up: 1216; 314
coding 2: 346
第二题很奇葩, leetcode没有, 叫 compress graph,不过他一直循循善诱, 先问我, 怎么判断要不要merge, 实现一个func来判断给定两个node需不需要merge, 然后写 Merge的code, 然后问,给一个图怎么compress. 要用到前面写的两个function 🔗 leetcode.com 给我直接干蒙了, 写完了前面两个, 写到第三个没写完就到40 分钟了.
https://leetcode.com/discuss/post/715406/facebook-merge-graph-nodes-by-anonymous_-7qmx/
88 follow-up n个array怎么merge, 543    253, 往返机票min price问题，总结其他帖子说的，应该是给两个数组，一个代表出发的机票价格，一个代表返回的机票价格，index就是日期，求往返机票最低价格。比如出发：[2,6,1,3]，返程：[2,4,3,5]，输出结果是5，选取第0天出发，第2天返回。有的面试官允许当天往返，那上面的例子结果就是4. There are 2 arrays which denote departing and returning flights with the respective indexes being time and the values of the array being the cost it takes for the flight. Return the minimum cost for a round trip provided the return flight can only be taken at a time post departing flight time (i.e if departing at time i, one can catch a returning flight only from time (i+1) onwards). For eg departing = [1,2,3,4] and returning = [4,3,2,1], the minimum cost for round trip will be 2 i.e departing[0] + returning[3]. Solve this is O(n) time.
https://leetcode.com/discuss/post/4288566/e4-meta-phone-screen-qs-by-anonymous_use-s6ug/
987, 43     76, 300 刚收到消息通知挂在第二轮了，因为用了dp，虽然都做出来了但是还是挂
四个编程题目，第一个是只含有0和1的数组算<仙叙盒 先序和>，
https://leetcode.com/discuss/post/4392657/meta-phone-screen-e4-by-anonymous_user-e92p/
第二个是三个<有序数组合并>，第三个是链表交换两个指定index的节点，第四个是<两个二叉树>，同时遍历，按序打印（不需要返回，就是打印）假如两个树的中序遍历分别是(1,3,4,5,7)和(2,5,6,9)，那同时遍历两个的话，打印出来就是(1,2,3,4,5,5,6,7,9)，这个打印出来的东西就是题目想要的输出。 题目给了两个树的根节点。可以想象一下给了两个有序数组，然后同时遍历，按顺序打印。然后把有序数组换成两个树，做同样的事
1249 created a cache to store left bracket, asked to optimize space complexity, changed to store the number of remaining open left bracket
return if a tree is complete
415 variant with demicals there -> 2 pointers
find a cheese in a maze, you don't have the map but API to tell you if you can move certain direction and if you find the cheese -> backtracking, stucked on how to represent visited without map, get hint on relative indexing and solved it
力扣 1249 Minimum Remove to Make Valid Parentheses。名义上是中等&实际上简单难度题，用栈来解，O(n) time + O(n) space worst case, 没有太多可以说的。
力扣 56(Merge Intervals)的变种,给两个已经按start time排好序的interval lists，要求返回一个排序的无重叠的interval list。做过这道题 + 对merge sort实现(双指针combine two sorted lists)熟悉的朋友，将二者结合起来即可。也许有更优的解法，只是当时我写出来的是这种
没有找到力扣原题，第一题比较简单: Check if 180-degree flip of input number string is the same, return a boolean.
Example:
101 → True
86098 → True
23 → False
1668 → False
解法有很多种了，时间复杂度应该是O(n),空间复杂度O(1)。
第二题是尧耳舞寺1254(Number of Closed Islands)的变种，不需要计算有多少closed islands，而需要找到最大closed island size。在原有BFS/DFS实现基础上, return local island size + 记住global max即可。



`MLSD`
1. 经典推广搜，在chat app上给用户推广告，给了很多方便条件narrow down问题。十分感谢!
2. Design a yelp-like system for places recommendation. 设计一个推荐附近event的系统，感觉类似yelp. 推荐一些像是餐厅酒吧活动之类的，一共有6个category，要求两个场景，一个是不分category推，一个是分category推（类似用户可以filter）. design a system to recommend new events for a user.
Yelp那轮侧重high level design,需要讲怎么做retrieval怎么做ranking。感觉面试官的重点在怎么设计metric和eval/testing去满足business need。模型设计也聊了，但时间所限没有讲太多细节（基本上就是name drop, e.g. 2-tower model,DCN, SENet, Transformer, etc)。
Classification那轮面得更细节一些（毕竟没什么high level architecture好讲）。few shot learning一般不会用于online serving（太贵），做offline data labeling(+human raters) 可以，但我没聊这个话题（面试官让我assume可以随意获取需要的labeled training data)。主要还是针对metric,多给几个建模方案（从最轻量到最复杂），讲清楚pros/cons, 再讲一讲online learning+unsupervised learning，最后说清楚怎么serving+testing，时间就差不多了.基本都是我在说，面试官没有给什么feedback，也不知道是不是说在他的考点上。serving就是谈一谈模型上线后可能遇到的问题和需要做什么优化（毕竟不是MLops岗，这里聊得很粗浅），testing就是分offline和online讲，说清楚各自怎么做/为什么要做/怎么分析和决策
3. recommendation 变种hashtag，没见过，问了各种embedding长啥样，loss function什么
4. video recommendation
5. 偵測武器 harmful content detection
请问unsupervised learning 在harmful content detection怎么应用啊？
可以参考下Contrastive learning, 尤其是BYOL一类的论文用到的的joint predictive embedding方法。meta自己的DINO也是类似的方法去训练图像embedding。最后在提炼的feature上面加相应的prediction heads就行了。因为面试官让我考虑posting里包含image/video的情况，我就顺带聊了聊。当然这类模型普遍需要参数量较大，刚好可以一起把model distillation讲一讲
6. reels short video recommendation， model部分主要在讨论结构 和方案选型
7. Research design问了如何设计一个多模态的推荐系统，lz当时alex xu看的不够仔细准备的不好，可能也是挂的主要原因。
8. news feed in fb reel
9. Design a notification filtering system -> ranking model by user, notification, time and locale infomration, plus a ruled based layer to filter on push frequencies



## Amazon
- Example: # Question: Given an array of numbers a and another array of numbers b, # find k nearest elements from a for each element in b. # a = [1, 2, 10, 100, 102, 205] # b = [3, 80] # k = 2 # output = [[1,2], [100, 102]]


## Bloomberg
`MLE`
ML SDE电面，先聊聊做过的ML project，问的挺细的，需要自己准备准备。
然后大概30mins问ML的问题，问我什么是supervised/unsupervised learning，举几个例子。然后问我logistics regression，问的很细。。要写cost function，然后怎么optimize求parameter，一直要写公式，中间还问我什么是EM和cross entropy，GG了。。
后面小半个小时coding，利口要斯留原题。

有一陣子很常在LinkedIn上看到的職缺 Bloomberg Law Senior machine Learning Engineer
網投後大概一週收到HR面，一週後接著電面，再一週通知reject
1. HR面
大概問了一下Why Bloomberg跟Do you know Bloomberg Law，樓主算是在相關產業工作所以跟hr聊了5mins就直接安排下一輪電面了
2. 電面
ML輪，問了非常多NLP / ML / DL / Resume 的細節
Random chat
1. Why BB Law? What’s your interest?
2. What’s the most recent paper you read and like the most?
Resume / ML Chat
1. Describe your most recent project in very high-level statement
2. How do you explore your dataset? Which dataset are you working on?
3. How do you pre-process / clean the dataset?
4. How do you build the vocabulary set?
5. What's the word vector? How do you use the embedding?
6. Why do you choose the model you mentioned (LSTM-CRF)?
7. What's a sequential model?
8. What’s LSTM? Can you explain that a bit? What problem is solved?
9. What problem still exists in LSTM compare to vanilla RNN?
10. How do you do model evaluation?
11. What metrics do you choose to evaluate the model, name a few (accuracy, F1-score, ......)
12. How do you compare / testing the results in unseen dataset, while you don’t have labels?
13. How do you retrain the model in production?

HR在linkedin上勾搭。2轮店面，4轮onsite。
店面第一轮：过了一遍简历，问了一些基础的BERT问题。
店面第二轮：不是LC题目，implement a tokenizer，需要识别alphanumeric, whitespace和punctuation。code中提供了判别alphanumeric和whitespace和punctuation的API。
onsite第一轮：ML design，从文件中识别出法律条款并且linking，基础的NER和entity resolution问题，还问了如何获取labeled data。
onsite第二轮：现场load一个dataset，用的pandas，需要对数据进行处理，比如说处理label，解决imbalance的问题，解决missing feature的问题，建议提前熟悉下pandas语法，可以google。
onsite第三轮：Senior HM 聊天，过简历
onsite第四轮：HM和tech lead聊天，过简历

ML position
1) CODING题•            im_stream: A stream (generator) that produces IMPosts. Calling next(im_stream) will yield a new post.
•            target_sender_id: a string, the sender_id of the user we want to get a context for
•            window_size: The number of posts before and after the target post that should be included
•             in the context.
•            
•            Returns: An iterable (anything we can iterate over) containing the posts from the first conversational context found in im_stream.
•            A context consists of an "target post" sent by target_sender_id, plus the window_size posts immediately
•            before and after the anchor post that were made in the same chatroom.
2) ML 题
Consider an equity trader who chats with other traders on an instant messaging app:
- She is in several chatrooms, exposed to various kinds of chatter:
news about the market (e.g, "Oil prices are spiking")
trade negotiations (e.g, "I want to buy Tesla stock")
relationship building (e.g., "Lovely weather!")
- When flooded with unread messages (e.g., after stepping away from her desk or if the incoming message volume is high):
she'd like an automated way to discover actionable unread posts
i.e., posts in which people have indicated interest in buying/selling equities

面的是Bloomberg MLE.
phone screen(两轮)
第1轮 简历和ml knowledge，
面试第一轮问了简历(没有coding)，深挖了一个NER的项目(LSTM + CRF)，貌似这个team很多工作都有NER的使用，所有面试官问了整个build NER 的细节: 怎么采集数据，怎么验证你收集的数据，包括你在哪个平台上用什么样的格式收集tagged data，以至于到后来network architecture， CRF 的input和output是啥, 很具体.
第2轮coding，
写一个tokenizer，不用包写一个tokenizer把一句话分成三种tag的token(word, punctuation, 还有一个啥忘了)
VO(4轮):
VO1: 设计NER 一个具体case， 也是从头到尾设计一套NER， 和两个engineer一起讨论.
VO2:  codepad上面的一个jupyternotebook, 数据都load好了，你要先做EDA，数据里面各种问题， category 太多， data unbalanced, 有的column全是空，有的column只有几个有值，你一边写pandas code 一边和面试官讨论，允许查api但是感觉最好不要太频繁，所有pandas的语法最好熟悉。 最后写一个model 做classificatiion，我最后都没写model的code， 描述了一下要干啥，怎么evaluation， code要写的话估计我要去查scikit-learn的api了.
HM: 然后半小时后hiring manager: 两个人，就是问简历，各种深挖简历项目，没有特别technical, 但是沟通和对简历的熟悉比较重要。
vo1一行代码都没写，纯说话.
vo2写了pandas的code。 比如说你说你要看下某一个column是不是都是0， 然后你就写一点点code， 验证一下，解释清楚了之后，然后就接着讨论。然后你又想把某一个categorical feature转成one-hot encoding， 你又写一行代码，看看对不对，然后再接着讨论。

随手海投被recruiter捞了，2轮电面
第一轮是个国人小哥，问了基础的ML知识，外加一个coding，是sparse vector/matrix multiplication。 写得很一般但是他很nice地给了很多hints帮忙
第二轮是个白人EM，问了一个ML design是如何给群聊里面的会话分类：如果在time t 有人说了句“good”，这个good是接前面哪一个对话的，或者这是又开了一个新对话。我这一轮回答的很不好，把这个问题想偏了。
然后10分钟让我快速写了个personalized Pagerank类似的random walk统计，我写了个乱七八糟😂
两天后居然通知过了，让我进VO
VO每一轮改成两个人，而且每组俩人好像是随机搭配的。
第一轮，混血华裔+天竺： 问ML design，题目具体忘记了，但很常规。
第二轮，俩ABC面coding，又是sparse vec/mat multiplication那个题目。但是这次要求详细写class，exception，各种意外的处理等等。果断写得不好。而且这种coding被俩人盯着写很不爽，俩人都七嘴八舌各种问你问题挑战你。我到后面各种typo，打错函数什么的。
第三轮， 这一轮好像不评分，俩EMs陪你聊天，随便你问问题。
第四轮， 又是俩EMs好像。给了一个dictionary，里面的词建立一个trie/prefix trie然后用这个trie去试图match一个string里面所有可能的词。开写后我也是脑残想着优化一下提前terminate。结果俩面试官里有一个好像不太coding的就看不懂了，问了一堆问题让我解释了十分钟到底怎么回事。另外一个面试官最后试图帮我就写了个例子，然后让我拿着例子解释。最后也干脆说你别优化了就用最straight forward的办法写吧。最后写完时间也基本用完。

VO1 应该是两个RS 都是phd 问了个open end的ML question: 如何实现一个只有integer precision的ML model，提了KNN和SVM 但trap在SVM的details上所以最后都没时间work on这个问题 大概率无了 当时答了类似mixed precision但可能不是想要的方向 现在感觉可能是想问类似mixed integer programming的问题 不过也不确定 希望有大神能解答下 ORZ
VO2 偏engineering 实现一个 instant chat message context retriver API 给定人名然后需要返回不同chat room里面的k-lines context 然后需要考虑是stream data 很快就写完了然后follow up问了下如果OOM怎么处理 也不太确定这轮是想问什么
HR 大概问了下experience 以及package range 很迷 HR还一直在打哈欠
VO3 感觉是infra team 先做了个简单的coding 给一段no space string 和 一个vocabulary dict 要做space parsing 然后问适不适合用ML来解决这个问题 感觉是个ML design 从data collection到model training，deployment，performance tracking。不过是个NLP task 不太熟悉感觉design有点失败。这轮interviewer很nice 但LZ不是很熟这一套所以估计两边都比较suffer

这周四三轮onsite
第一轮: ML modeling, 直接给你个dataframe的数据集，让你分析数据，设计模型，模型不用写出来，给思路就好
由于我最近没怎么写pandas, syntax又忘光了，面试官允许网上搜pandas的一些function
感觉整个面试都在纠结这个。。。
第二轮: ML modeling
直接给你他们目前在解决的问题，深入问了data annotation,
为什么选这个模型还有一些edge case问题
这轮感觉答得最好
第三轮 HM
deep dive了之前做的和开花堡这个组类似的项目，这轮很神奇是两个HM
中间还让设计了一个推荐系统
第二天recruiter说positive feedback, 又让约了一轮30分钟和大Boss的meeting

热乎乎的店面，面的是MLE职位；recruiter说phone screen有两轮，说这一轮是coding
结果面试聊了80分钟，全程无coding，然后被告知是ML model轮。。。。
面试官三哥哥人很nice，上来问项目，深入问项目的model，这里简单聊了transformer和 bert 介绍下model structure
没有问loss之类的
重点是model deployment 和evaluation
就evaluation又拓展问了evalution metrics 和 edge case，和benchmark
全是项目相关的问题
因为面的组和我目前做的很类似，所以聊的很开心，后面就是俩人一起吐槽data processing的问题，也是醉醉哒

第一面
面试官一个印度小哥，没有coding，问的是deep learning相关的问题：
1) 在train neural networks的时候，如果可以同时选 a) full-batch training; b) mini-batch training。 优先选哪个？
答案是b)。原因是mini-batch training带来的随机性可以：1. 在优化陷入saddle point的时候帮助跳出saddle point；2.一定程度上能加速training convergence（这点是小哥说的，我不是特别清楚）。
2) 解释一下train graph neural networks的时候有哪些hyper-parameters可以调。
3) Deep neural networks(DNN)有很多参数特别复杂。按照传统机器学习理论它应该过拟合，然后在测试集上表现不好。但是为什么在实际中DNN表现得不错？
我其实也不知道为啥。。。随便答了一个说可能data有low-dimensional structure。
4) Train graph neural networks (GNN) 的时候， 做aggregation可以用什么？
   答案是：max, mean, 或者用一个MLP。 然后有一个follow-up：有人用RNN来做aggregation，这有什么缺点？ 答案是：RNN的输出和输入的order有关; 如果用RNN做aggregation的话，aggregation的结果和nodes的labeling有关，这违反了我们希望GNN是permutation invariant的初衷。
5） GNN的hidden layer的维数一般倾向去选“比较大的维数”还是“比较小的维数”。我答的是"比较小"。原因是数据里可能有low-dimensional structures, 选比较小的维数能促使GNN去学这些low-dimensional structures.
6) Train GNN的时候，如果内存放不下一整个graph怎么办？回答是：可以采用mini-batch training，也就是每个epoch从graph中选a subset of nodes, 然在这个subset产生的小图(the graph induced from the subset) 上训练。
7) 解释一下GNN的工作原理。
就是把每个node的embedding怎么产生的简单描述一下。
8）解释一下Adam optimizer；  Adam在记录gradient的哪些信息（答案：一阶和二阶gradient信息）；Adam怎么发挥作用（答案：可以adaptively调整learning rate）。
     解释一下Batch normalization和Layer normalization。我答的是：batch normalization是通过(在每个mini batch上)减均值除方差的方式稳定training; layer normalization就不懂了。
9） 如果把batch size从128变成256， 那么learning rate应该怎么调？我答的是：batch size变大，那么在这个mini batch上的variance就变小了，相应地learning rate可以稍微增大一些。但具体应该增大多少没答出来。
第二面
同胞小哥，没有coding。问的是简历上的项目，以及两道机器学习和统计的题。
1） 推导一下ridge regression的weight estimator怎么算？这里第一步要记得说bias term单独估计; 第二步说loss function是convex的，所以可以求导以后通过让导数为0来求estimator; 第三步是推导weight estimator； 最后得到的estimator里有个矩阵求逆，小哥问了这个矩阵一定可逆吗？答案是“一定可逆”，原因是那个矩阵是个正定矩阵。
2） 假设X是一个服从标准正太分布的随机变量 (X ~ N(0, 1))， 写一个小程序计算P(X > 5)。 这题我用一个简单的蒙特卡洛来算，但是因为 X>5这个事件概率太小了，即使采样一百万次所有的样本都是小于5，所以最后错误地算出 P(X>5)=0...  正确答案是用 importance sampling来算。
第三面
同胞姐。没有coding，简历问了一点。
1） 手推Bias-Variance Tradeoff的公式。这题稍微有点无语没答出来。一般面试就是让解释一下Bias-Variance Tradeoff， 但这里要求精确地写出公式。。。面试官让考虑一个带高斯白噪声的linear regression model，基于这个model来推Bias-Variance Tradeoff。其实最后她要的就是这本书(https://hastie.su.domains/ElemSt ... LII_print12_toc.pdf)   242页的公式(7.9)的第二行。
这里吐槽一下这个姐讲话不清楚，然后用电脑上的手写板通过鼠标写公式给我看，根本看不懂她写的啥。。。。
2） 解释一下什么是Central Limit Theorem。给N个random samples：X_1, ..., X_N，它们的sample average （(X_1+...+X_N) / N）的variance是多少 (答案：Var(X_1) / N)。

2月中旬 猎头 linkedin 联系 职位是Sr MLE 应该是组招
2月末 店面邀请
3.月初 第一轮店面 是一个很有好的国人小哥哥 准备之前以为只有coding 没想到 其实是half ML half coding， 是1D candy crush 用的是一二零酒的逻辑 第一部分也是比较偏向设计 关于从文档中提取表格的metrics 之类的
两天之后 约第二轮
前几天 第二轮店面 是manager Level 的人walk through 一个具体的case （吐槽一下 我是真的没想到一整轮都是walk through 和recruiter联系 他感觉也不是很清楚 他说的是有coding和ML theory 和design
从句子里面提取NER相关信息 会比较发散的问比较多的细节 比如你会怎么设计， 如果结果不好了怎么办？ 提取的数据其实是不同的类型 还有什么其他方法 我一直很不安等待他问coding 结果没有问 中间突然说从英文转成数字用什么算法 我当时直接愣住了 我想的就是直接brute force转

突然想起来了，还有一个系统设计的题目，如何实时更新logging系统， logs在不同的cluster，怎么让user能pull log是chronic order。。。。

先说一下Timeline:
10/06 -- 内推+网申
10/15 -- recruiter电话聊天
10/20 -- 电面
10/25 -- 电面
11/04 -- VO
11/8 -- recruiter口头通知pass
11/9 -- 约team matching
VO一共4轮，每轮2个面试官，耗时1h。整个VO持续4.5hs。
第1轮：
Introduction, 从简历里扣research interest的一个方向问细节。然后开始ML design。假设你有一些house的信息（地理位置，price等），需要设计一个ML model，给定一个house，预测对应的price。
Follow up:  1) 怎么设计feature，预处理，high dimensional怎么办，怎么处理地址信息，怎么获得更多feature，怎么更好利用feature，还有什么实际情况需要考虑;  2) 用什么Model，lz举了linear regression和GBDT，于是针对两个model的细节都问了不少。比如convexity, gradient descent, regularization和GBDT的概念和参数等;  3) 怎么train，怎么evaluate。
第2轮：
Introduction，问实习project details，扣了下feature和model细节，why use A instead of B，model的最终performance如何。完了开始代码
面试官1问了下popular clustering model有哪些，都有什么联系和差别，然后implement Kmeans from scratch。可以用numpy。边实现边回答细节问题，比如怎么initialize centers和怎么choose k。码完后让自己写一个test case测试一下运行结果。
面试官2紧接着来了个经典的利口药尔灵舅，把题目的fixed k换成 k>=3。码完跑test case测试运行结果
前2轮结束后休息了30分钟，接着开始3-4轮。
第3轮：
Introduction，问了与DNN相关的project，然后让解释什么是NN，常见的NN strcuture有哪些，能否并行，怎么参数怎么更新等等，接下来又是一道ML design
bloomberg有很多document谈论某个公司的信息，设计ML model分类article的sentiment。Follow up: feature提取feature，RNN是什么，怎么定义，GRU和LSTM有什么区别，NN structure细节，结果怎么evaluate，label 不balanced怎么处理等等。
第4轮，HM面:
2个HM轮流介绍自己team的工作，然后让lz发问。lz针对hm的介绍问了两个具体问题，HM于是开始滔滔不绝，互问互答吹了30分钟。其后HM开始BQ。1) why BB, how does ur background fit BB。 2) what do you think about going from academia to industry。完了之后其中一个HM开溜了，另一个HM问我还有没有关于BB的其他问题。lz随口问了一下WLB和Internal mobility。完了后相互感谢商业互吹结束。
VO完了第2天（周五）发邮件给recruiter要feedback，recuriter说最早要周一才能给。于是约了周一phone catch up。周一通知pass。稍微说了一下lz整个过程的表现。特别需要mention的是面试时lz的coding part有些小bug以及需要面试官给hint，但过程中他们很看重collaborative problem solving skills。所以不要一味coding，该打嘴炮商业互吹时一定不要沉默不语。

bloomberg article有很多entity。需要写一个 data structure，输入text，累计每个entity出现次数，返回top-k frequently mentioned entity.
用hashmap counting + heapsort 秒了。问了下时空复杂度
Follow up: 如果经常访问top-k，能不能有更好解法。一开始没什么好思路，小哥给了个hint之后勉强搞了个O(n)解法，时间比较紧但刚好写完

一个support ticket system，用户写ticket主题内容后需要填分类，每个分类都有相应specialist处理。ticket按FIFO处理。如果分类错specialist需要按自己理解纠正分类，然后重新排期。设计一个ML系统降低用户和specialist的等待时间。
整个过程不停的扣细节，从特征到model到evaluation问得非常细。

上周面了VO
第一轮 两个题 一个是auto complete（应该用Trie 的 但是楼主当时概念不熟 没写出来
第二题就是coin change2的题， 只不过用了不同的题目问题（什么加油站之类的
（感觉这也不是Bloomberg高频题 = =
看到第一个题 心态就不稳了 导致这场coding其实表现的很不好 而且我一开始的时候是想和面试官说我的思路 我要怎么写 但是面试官就说这是你的代码 你就写呗 （没表现好
第二轮 是design的问题 给一堆没有空格的str 你怎么把空格复原 我觉得我答的算还行吧 主要是面试官很nice 一直沟通就感觉蛮好的
第三轮 是hiring manager面的 前面一部分是BQ 不知道为什么我觉得沟通起来也不是很顺畅 后面部分是relation extraction的design的问题 问的题比较发散

问题是level order traversal of binary tree
基本上树中的每个节点都是一个字符，我们必须打印字符串 by level order traversal of binary tree。我用了BFS，然后用hashmap保存每个level的字符as list.
Follow up:
1. 为什么在哈希图中使用列表而不是字符串？ 速度会如何变化？ 我回答说速度不会改变。 Asymptotically,它是相同的复杂性
2. 为什么要使用哈希图？ 你可以用orderedMap代替吗？ 我对orderedMAp 了解不多，但我告诉过hashmap 的插入时间为O(1)，所以我们可能无法做得更高效。

four rounds
第一 round
    a. 妖恶灵酒
    b. basic ML problem, starting from my previous project
第二 round
    a. 衣遛柒遛
    b. design a API to de-duplicate the same news article generated daily (There are 2M articles/day; same article: same title and same body)
第三 round
    a. design a ML system to identify different threads in a discussion log.
第四 round
    a. talking with HM
2b -> 类似leetcode 的 design 标籤题目 可以参考，大致要求就是要你写出interface 然后实作，因为这个例子规模小，不用任何distributed system setup.
3a -> deep-dive into a specific ML problem. 主要用叙述，pseudo-code表达自己意思，很随性。
重点在于从 data collection -> feature engineering -> data cleaning/preprocessing -> model choosing -> model training (tuning) -> model evaluation 都要能提出几个方案和自证这个方案是最可行的。
会需要大量互动，因为是open-ended question，他们也不一定有标准答案。我认为这就是典型的ML design interview，不过他们面试不包括model deployment 和 distributed system setup.

猎头主动找的, 面的是Senior Software Engineer (in AI/Machine learning)总共有两轮电面+4轮 virtual onsite
1. 电面1：
一个看起来很拽的年轻面试官，面了一个ML system design的问题，具体是怎么设计Named Entity Recognition system. 如果做过相关问题应该不难
因为楼主之前没怎么准备过，所以感觉答的不好，另外面试官有点盛气凌人，所以以为要挂了
结果还是过了，所以面试的感觉有时候不太准。。
2.电面2:
一个很和气的senior，design一个基于文本的fraud detection ML system. 因为是简单的supervised learning system, 所以答得还可以，可以看出来面试官也很高兴
3.Virtual onsite:
总共5轮，其中三轮是technical的，从早面到晚，因为是virtual onsite，所以连午饭时间都基本没有:(，因为还要自己赶快找点吃的。。。
1. 简单的coding+design NER; 这次楼主准备好了感觉答的还不错
2. ML design：search ranking
3. 吃饭+HR聊天
4. coding/design: 给定一个stream，要求写一个method，返回top k frequent elements, 有点类似leetcode 347, 不过因为要对stream经常调用这个method，所以需要设计一个比较好update的，时间complexity也比较好的；
这一轮楼主先打答了brute force的方法，然后讲了一个用heap的方法，method complexity 是 NlogK的；但是面试官不满意，一定要求想出kLogN的，在面试官提示下，最后写了一个dictionary+heap， 然后heap是从底层开始实现，需要有heap udpate （bubble up)的方法，花费了好大功夫。。。
不知道这题是不是曾经出现过在哪里？虽然最后写出来了，但感觉面这个题好像是烙印面试官在坑楼主一样的。。如果大家有什么想法或者知道leetcode题号可以跟大家说一下
5. director聊天，一个很年轻的director，一直在讲bloomberg onboarding process怎么好，对new grad怎么友善，话说我面的senior为什么要给我讲这个。。

回报地里报一个bloomberg ai 的面经
总共两轮技术电面 五轮onsite（包含三轮技术）
每轮技术面都是1-2道lc 和 ml/dl concepts 和 case study
遇到的题目有利口 1396 1029 146 380 （时间有点久了就记得这么多了）
还有implement 一些简单的ml算法
concept部分很简单 ex. l1l2 的区别 ， gradient boosting 和 random forest区别； pca的原理； 描述svm
case 部分 问了multi label classification （news topic）； sequential data ；

店面：两个天竺友人。现实聊了半小时简历+经验。然后问了一道tree的题。不在lc上。他们自己想的。但是dfs，recursion基本可以解决。
当天就通知VO。先面3轮，顺利的话再安排senior leader。
VO 前一天才prep call。也不告诉我面试官名字。
VO当天coordinator 跟我说了名字，发现全是友人。原来这是个5人组，4个烙印。
1. 两个人。第一个问了bipartite graph。但是input比较模糊。lz clarify了一阵子。写完之后，看了半天。总说不懂，手动run了4-5个test case。还是说confused。期间，第二个友人插过嘴，态度差。做了35分钟，开始第二题。类似word index count。第二个面试官态度很差，总是打断我说话，不想看code。这题主要问如何distribute，如何实现mapreduce
2. 店面的两个烙印。第一题 OO design online prediction service。第二题 system design bbg tv scale up。讨论了cdn，api。没仔细问partition，replication。
3. 一个白人小哥。冷脸。主要简历+system design process large logs。还是mapreduce。没任何引导，也不知道他想deep dive 啥。

9月16日第一轮电面
怎么选feature，怎么做prediction？linear regression，feature correlation怎么办？regularization 有哪些？L1 的作用是什么？如果有个变量range特别大怎么办？会发生什么？L1对这个情况有什么影响？怎么sample你的训练集，如果是time series的怎么办？
coding：就是飞机票打印那题Reconstruct Itinerary
9月30日第二轮电面
236, 235 + 时空复杂度，最坏情况？
Logistic Regression是什么？怎么做？怎么迭代更新？怎么split你的data，什么是cross validation？你的这种data split 什么情况下是无效的？那要怎么处理？

新鲜的开花堡电面加onsite
第一轮电面 基本过简历以及相关的dl知识，像是batchnormalizaion 什么的，给了一个case study ：news multi-topic怎么设计.就是有好多news，每个news有多个topic label，如何设计一个learning system来完成。
第二轮电面 coding，国人老哥，人很nice，没的说，乐扣 Add Strings 和 Multiply Strings
virtual onsite 六轮
第一轮 ml + case study, name entity
第二轮 coding topk
第三轮 两人闲聊半个小时
第四轮 hr聊半个小时
第五轮 ml + case study credit card fraud detection
第六轮 面见大boss Anju

电面1：ML project dive deep 然后问了一些ML基础相关的然后20分钟写道题，给个API
class LegacyDate:
    def isBizDay():
        return True/False
    def addDays(numDays):
然后实现
def nextMonday(d : LegacyDate):
    # d = Tuesday
    # return d.addDays(6)
电面2：
1. 乐扣雾医霸 需要输出最少硬币得到target的组合
2. 一个多叉树，每个节点有一个值，输出从跟节点到叶节点的max path sum。

1,  原题，longest substring without repeating characters
2, Trie, autocomplete

ML Eng, 第一轮店面，好像有两轮店面，国人小弟，挺友好
开始是ML的问题，问熟悉的classical classifier models, 具体问了logistic regression 和 random forest,  lost fuction, gradient descent, regularization.
后来进入深度学习，问了RNN, CNN
后半部分写程序，类似于word break, 不要求syntax correct, 后来扩展到如果 字典里的word有权重，要结果最大化平均权重怎么做，没有要求code

BB 家的AI research scientist， title是sales intelligient。九月份的时候就找人内推了，当时HR说只招2019/12 入职的，就搁置了，过了一个月HR又来联系说HC开了。大致流程是两轮店面，各一小时，35-40分钟ML剩下时间coding和问问题。
面试大哥是london打过来的，一开始问了ML基础：
evaluation metrics L1/L2 区别 data不balance怎么办，聊到decision tree和random forest 又问了training时候的区别。为什么data不imbalance也可以。我当时说是因为train的时候cosset function是totalloss， 所以即使有class很大也没关系
又问了logistic regression和SVM的区别。
提到了PCA但没细问，估计可能看出我不太熟PCA了。。。
最后问了为什么LSTM比RNN好之类的
感觉ML面就是很杂，但都不深，可能想general了解一下吧
coding是一道palindrom的题，太简单不太记得，目测easy难度

ML SDE电面，先聊聊做过的ML project，问的挺细的，需要自己准备准备。
然后大概30mins问ML的问题，问我什么是supervised/unsupervised learning，举几个例子。然后问我logistics regression，问的很细。。要写cost function，然后怎么optimize求parameter，一直要写公式，中间还问我什么是EM和cross entropy，GG了。。
后面小半个小时coding，利口要斯留原题。

Generative model & Discriminative model 区别
Decision tree & logistic regression区别
介绍常见的无监督算法，KMeans算法原理
对于Fraud transaction detection 设计feature和model
公交路线给定(swipe_in time, car_id,station_id), (swipe_out time, car_id,station_id), O(N)计算平均trip的时间

面的是腐国的AI组，聊ML细节，做过的project，问的比较细致，譬如怎么train embedding，w2v loss function是什么，input和output looks like，如何防止overfitting，和一道coding，一个sampler，大意就是给一个p vector（对应一个distribution）， 如何做一个符合这个distribution的sampler，如何优化，时间复杂度等等
第二轮从头开始implement node class， graph class， 然后就是利口找有方向图里面的圈，感觉oop弄清楚了， DFS会没啥问题，没刷过题就稍微有点一脸懵逼

一个图算法。
测试是不是DAG

1）怎么帮一个存成linked list （从高位到地位： 1234 --》 1--->2 ---> 3 ---> 4；2）如何用linkedlist 来做integer的加法。如这题： https://leetcode.com/problems/add-two-numbers-ii/

1. HR 店面之后的第一轮技术店面，问了很多我简历上的经历，包括PhD的研究用到的所有ML algorithm都问得很详细，我经历里有用到的Gaussian Process 和Random Forest 他都会让我详细解释一遍，例如decision tree 的impurity index公式一类的都让在online hackerrank上打出来。最后做了一道很简单的leetcode easy.
2. 主要是coding, 聊了一些behavioral (past experience, why bloomberg...)， 问了一些简单的NLP word embedding, 然后做了一道binary tree common ancester和一道anagram问题。hackerrank上写没有让跑。
3 Onsite 第一面是live coding，让写一个function 保存并输出data stream的mean，做的不是很好，一开始用binary search，后来interviewer提示用data structure，但是花了很长时间想最后时间不够就结束了。第二面问我一些ML的问题，有一题是data set 的 Golden standard， 怎么test 一个data set 是不是golden standard，这个到现在我也不知道怎么做。。。最后让我写一个能在GPU上跑的Kmean我就直接懵比了？？？？面完第二轮hiring manager告诉我他们临时有别的安排就先面这两轮然而我知道已经挂了

第一轮做45分钟presentation，
第二轮：一个印度瘦哥加一个美国胖哥，ML基础知识，问了logistic regression，各种loss，啥是reguarlization等等非常基础标准的问题
第三轮：一个中国大哥加一个印度小哥，第一题 里扣 二舅吾，第二题问了一个系统设计题（印度小哥说的是系统设计题，但我听起来感觉像LRU），无奈楼主实在没准备过这类问题，题目有些忘了，大概是bb有数据不断的stream in，先是问怎么来设计数据结构能够最快找到公司股价，并且返回某个公司最新的股价之类的
午饭：一个伊朗小哥和一个日本小哥带我吃饭，人都挺好的，聊得挺high
第四轮：HR: 我以为到此为止就跪了，结束了的，后来发现HR就给讲讲BB有好多好处，接下来会有两个hiring manager跟我聊
第五轮：一个孕妇大姐，人很好，看起来很和善，先问为啥选BB，然后问我如果让我做sentiment analysis我该咋做，接着问我如果数据没有label你咋办，在接着问我，如果我们给hedge fund提供信息，不想用deep learning那样复杂的方法，你咋办。
第六轮：一个大叔，眼神犀利，感觉快我把射穿了。。自称是所有ML的头，直接给CTO汇报啥的，所以比较紧张吧，然后先问为啥选BB，然后问了我一道非常奇怪的open question，楼主实在是记不起来题目的具体内容了，大概是什么有twitter的评价，但没label，要评分还是啥的，这个问题实在是非常古怪，感觉答得不。

不知道哪国大叔，聊实习项目，问了KNN,lasso regression, random forest, 然后coding实现decision tree，写完后又写了一个函数prune这个tree（就是假如leaf太多overfit了，如何减少leaf的数量），没写完，最后留了一点儿伪代码
听口音是亚裔或中国女，聊实习项目，类似前一轮的一些理论问题，然后coding kmeans。然后一个credit card fraud detection的case study

给定两个整数 n 和 k，建一棵有 n 个节点，每个节点有 k 个子节点的树。用 bfs 做就可以了。
Follow-up 是问如果每个节点可以有 1-k 个子节点，总共可以构建多少个不同的树。只要讲思路不要求实现，再提示下发现是个动规的问题，虽然最后感觉没有完全答对，还是给过了，感谢。
比如 n = 7，k = 3，得到的树就是：
              1
        2    3    4
      567

前半个小时是ML/NLP概念题：怎么处理overfitting/underfitting，什么是regularization，什么是convex optimization，什么是gradient vanish，LSTM用几层，keep gate的结构，Drop-out的结构…… 有一道题我不明白：Machine learning分为numerical和categorical两种，它们各自假设的分布是什么？我随口说一个连续、一个离散，他说是不是正态呢？我不知道怎么回答……
后半个小时是coding题：利扣x，x=我国一共多少个民族。因为我答的比较快，他又加了一道，就是贪心法的股票题，不过时间不够了我说说算法即可。



332, 987, 140, 1679, 642第二轮烙印，给个非tag的hard，还非要我把tire结构先画出来，不用说肯定跪了

`NON MLE`
第一面前10分鐘自介
coding 40 分鐘
Given a class to add price with the company name and get the most recent price by the given number for that company 
addPrice(Company, Price)
getPrice(Company , Number)
Follow Up 
1)If the limit number with 5 how do you change thing differently 
2)If you can add the past price 
Give a start time and end time of the event
Find the most busiest time of the event

第一轮
一个 N 叉树，要求找出一条到叶子节点的路径，让路径上的 节点值总和最小。
第二轮：
给一个字典和一组单词，需要根据该字典中的字母顺序对单词进行排序。
第三轮：
system design 展示 Top N 热门新闻

Senior engineer
BQ加问了一些experience和相关的project
第一题 一个array 只有1和0，比如[0 1 0 1 1 1 0 1 1]。如果可以flip一个0变成1，最多有多少个连续的
follow up：如果可以flip K次0变1，最多有多少个连续的 -》 sliding window
个人猜测第一问就希望你用滑动窗口做，然后follow-up直接让你稍微改一下原本代码，接着再给你出一题？我最近面别的onsite也遇到过类似情况，感觉倾向于需要你做两题如果原本题目只有lc medium难度的话，因为就这题它还能有follow up比如说在二维空间下怎么做。

然后做题 两道题
都是lc tag的
第一道是 给一个string 你可以remove其中的一个char 如果remove了以后所有string的frequency一样的话就true要不然就false
第二道是lc430原题
感觉面试官挺nice的 就是做题的时候用了counter()和deque啥的面试官不懂让我解释或者换一种东西用

一面：1/14: 過簡歷，離口：56，102，380
二面：2/4
上午：過簡歷，42, 1274
中午：過簡歷，79，meeting room變種。中間問到了Trie這種data structure. 大部分人大學應該都沒學過。
下午：HR面：為什麼選擇CS專業，薪水期望，需不需要sponsor，為什麼bloomberg，介紹職位。
​三面：3/5
EM面，純聊天，過簡歷。只面了45分鐘，中間一直是我在說話，感覺對方不怎麼搭理我。對我做過的東西好像不是特別感興趣。搞得我很暈。我到底是表現的好還是不好？有人有經驗麼。

力扣 1387变形题，dfs + memorization解决。这题轻松过
力扣 地铁系统变形题，主要是讨论的想法和数据结构，实现了进站方法。

Bloomberg 25ng 4轮挂经
vo1: word search + encode str(aabbcc->2a2b2c)
vo2: Collatz + decode str (2[a2[bc]] -> abcbcabcbc)
vo3: design browser history + followup（没答好）
hr: why bb, top priorities of applying for jobs / choosing offer, proud project+ 反问（反问没问够10mins)
timeline 1月中开始，每个vo隔一周， vo3和hr连一起
分享挂经攒人品，总结就是题没刷好。最好全部都完美+optimal解出来

BBG superday第一场就挂了，面试官台湾40+男性，开场聊的还行，第一题给了一道一维candy crush，很快就写完了。
他说你写得很快，给你一道难一点的，题目如下：
设计一个class ，用来判断stream of characters是否是palindrome。有两函数，track(char)，用于，添加新的char。isPalindrome()，用于判断当前是否是panlindrome，返回True/False。input stream could be Terra bytes.
例如track(“a”) track(“b”) track(“c”) track(“b”) track(“a”) isPalindrome() should return True.
时间复杂度要低于O(N).
我面试时尝试了指针，dp，说实话20分钟真的想不出来。事后查了下网上，有人说rolling hash，但在他给的这个terrabyte语境下collide很严重啊。不知地里各位大佬有没有更好的想法。真的自闭了，tag题3个月的我都会写，对bbg的题印象一直不难，结果面试给了这个飞天大锤😭
50分钟时说我第一题写的有问题，不是每到三个就crush，而是三个以上一起crush所有连续的。可是我读完题目的时候还跟他确认过，dry run也演示过，最后他改变了他对题目的理解。最后我花五分钟重写了一遍，他说我也不知道你这个对不对，我们没时间了，你有问题问我吗。

Spelling Bee:
Example Required: N
Example Optional: V C O D E Y
Goal: List all words that satisfy the following rules:
* Minimum 4 letters
* Required letter appears at least once
* Optional letters can appear any number of times (repeats allowed)
* No other letters allowed
Example valid words: ENCODE, NONCE, DONE, NODE
Required: O
Optional: G, L, E, P, T, N
Example: POLE, TONE, TOLL, GONE
TROPE
TON
# 1. define all necessary letters and possible letter and store them in hashset to reduce time complexity.
# 2. built in dictory which can be referred, it is dictory.
# 3. check if they are in dictory.
    # required = ['N']
    # Optional = ["V",  "C",  "O", "D", "E", "Y"]
    # dictionary = {all possible english words}

第一题
有一个function equiv可以检测两个 input是否同为基/偶数（也可以是别的逻辑面试官说就是一个返回true false的function），是的话返回true不然false
用这个equiv和一个input array把input分成equiv里都是true的subarray
基本思路就是有一个 result array 和 flag，loop input 用equiv 检查现在的值与result里每个subarray的第一个值是否相等，相等则加进一个subarray然后break，全找不到则自己建一个subarray，最后return result
第二题collatz
输入一个数字n，如果n为偶数则n = n/2,如果n是基数 则 n= 3n+1计算最后到1的时候要多少步
纯用if else写解，follow up问怎么提升performance，就是要用一个in memory cache (map就行)记住每次结果的步数，还可以用cache记在loop里每次经过的步数，这样在过程中cache查到一个数字也能直接查结果+当前已经走过的步数。。
follow up 真的挺巧思的，反正是学到了cache还能这么用。

店面 1h 一道colartz number一道design deck of card 第二题没写完 进入vo
vo
一轮 1h all path from src to dst+meeting rooms
二轮 1h 自己出的 encode number 输入1113344 输出312324 要求不能转成string做
三轮hr 30min why bb 选公司有几个方面 收到的negative feedback

首轮考了三道题
HR面：為什麼選擇CS專業，薪水期望，需不需要sponsor，為什麼bloomberg，介紹職位。

自創題： Given an input representing each node and its child, for example: NodeID: 1, child: 2; NodeID: 2, child: none; NodeID: 3, child: 1, find the root of the tree.

然后开始coding，给一个矩阵，求从起点到终点的最小cost，途径的weight加起来就是cost。先讲了dfs，然后说了dp的做法，最后实现dp的code，跑了一个case。20min搞定，小哥看时间还多，出了个脑筋急转弯，和位运算相关。题目很长，他自己都clarify了5分钟才说清楚。想了10min，一直交流但还是想不出来。告诉了我解法，大概其实和1000瓶水找出有毒的一瓶的解法有异曲同工。但题目是不一样的，方法类似。

第一轮：技术面 (coding)
两位面试官，最开始15min问了点简历上的project内容
后面45min在hackerrank上写两道题（不用跑测试）
LC 1347, 1209 题目还是很简单滴
第二轮：技术面 (coding)
Round 2 (60 min.): This round will focus on your coding skills and knowledge of data structures and algorithms.
前十分钟问了一些之前实习项目的内容，后面五十分钟做两道题（主题是重叠区间）
第一题是力扣253（最少meeting room），第二题是第一题的追加问题，计算最大重叠数量
第三轮：技术面 (project)
Round 3 (60 min.): Progressing from your previous interview, this one-hour virtual interview will further assess your technical skills. The focus of the interview will be to assess your technical skills through discussion of a real world problem. Your interviewer will be assessing your technical communication skills and problem solving from first principles.
邮件里说第三轮是further assess your technical skills，我以为是system design，结果问得之前实习项目经历等。主要问的是：
实习经历（遇到的挑战 有哪些可以改进的地方）
熟悉的编程语言（面试官提到bloomberg主要以python和c++为主）
平常如何track new technology
为什么申请这个岗位
第四轮：BQ (HR)
Round 4: This interview will not be technical and instead will focus more on your work and/or academic experience so far, as well as your motivations for becoming a Software Engineer at Bloomberg. For this interview you will meet with one of our recruiters.
这轮主要是BQ，问了：
团队合作的例子
团队发生冲突是如何解决
得到负反馈是如何对应的
第五轮：BQ (manager)
Round 5: This interview will last approx 60 mins and will be with one of our Engineering Managers. They will ask questions to learn more about your previous experiences and project work, with an emphasis on technical decisions and your impact on the project, team, or company as it applies to your background. They may ask you a question to gauge your problem solving and technical communication skills to understand how you leverage your knowledge to approach real-world applications. This will be another opportunity for you to learn about Bloomberg and ask any remaining questions.
这轮虽说是60min，面试官说面30min差不多了，问了几个问题后就让我自己问想问的问题了
之前的实习项目中如何处理real-time data的，有没有遇到什么挑战
未来对工作地点有什么要求

店面 lc: linkedlist 删除倒数第N个Node lc: LRU 秒
VO1 地里出现过题 BFS (followup dijkstra) 秒
VO2 easy + 地理的Underground 秒
HR + EM 全BQ，没准备现场想的，答得不好

两道题，一道类似lc200；还有一道类似lc 443 string compression，但input和output都是integer。

一共4轮
Coding 1
写一个Iterator，要求支持next(), hasNext(), reset()，这就是linkedlist 但是另外记录一下head保留着别扔。
running window medium
Coding + BQ
聊简历，聊对他们项目的看法
写一个统计学校里面成绩的代码，要求给出各科前10
SD + BQ
team lead聊简历，culture，然后设计一个挂单竞价系统
BQ
team lead 她老板，就聊聊motivation，passion之类的，没聊项目
感觉金融公司的面试题都是偏简单，可能面试者自己也搞不懂太难的题目。倒是他们很在乎你的motivation，很多问题都是侧重于看你是不是真的想去

Tl:
9.21 refer
9.26 apply
10.3 phone邀请
10.24 phone interview：
25分钟简历➕why bloomberg，做了LC445。
10.28 VO邀请：
on campus满了，virtual约到了11.7。
11.7 Back to back：
两轮VO+一轮HR：考了LC wordbreak minstack还有他们自己出的题
11.12拒信

都是利口变形 妖妖柳116 么尔斯久1249 伞拔冻380
还有一题找不到原题 是 grid 上找两点的 shortest path, 可能有 obstacle
HR 面 30min 主要是 bq 和介绍入职后的 training program
self intro, proudest project, why bloomberg, constructive feedback, top 3 priority choosing an offer
感觉对方在我回答时没什么兴趣听, 我也就尽快讲完重点

第一题很像舞遛零560，但是多了一个里面数值大于零的条件。如果所有数值大于零，挪动 right pointer guarantees increament in subarray sum, 挪动 left pointer vice versa
当 subarray < k，++right 直到 subarray sum >= k, 当 subarray sum > k, ++left. 标准解法用prefix sum 如果有大于零条件，可以用two pointers
第二题是腰零九109，要求不能用额外的资料结构。

经典题目LRU cache，只存value，最后return前K个values即可

面试一共五轮
前三轮都是lc technical，第四轮recruiter，第五轮em
sliding window
妻舅妻797
叁霸妻387
binary tree traversal
还有两题不记得了，都是easy-medium难度
em简单问了一下过去的project和简单的design。

2. You need to count the overlapping intervals. I put each start and end time in a list,
and then counted the maximum number of overlapping intervals, which was very similar to meeting rooms ii

第一道是霰妖司314变种，题目一样只是把数字换成了character，最后输出一个单词
第二道题是幺洱司酒1249原题

一面：齐救齐797、幺尔私酒1249
二面：给一系列股票操作，比如[[9.1, BUY, 100 (shares), $50], [9.3, SELL, 50 (shares), $80]，但是30天内sell不能超过buy price（不能赚钱）问怎么判断是否valid；先假设只有buy，followup是如果有的有sell怎么判断
三面：
1. 给一些fail的节点，每个节点知道自己的children，找到最开始fail的那个节点
2. 类似 耳零零200，但是找number of lakes

店面
coins 无线数量 【1,5,10,25】
给定一个target
按照给定格式
返回最小硬币数量的所有组合
散酒39
要求优化 好像意思是memorization 没搞出来

输入 stream of data, 有id, value 和 时间，
id       value  time
--------------------
5149，agru,  4
4349,   sret,   12
5663，t46u,  7
1549，a4y5, 13
依次输出 id       value  time其实就是留舞流656 和 药散就榴 的合体
但是是分成两个部分问的，千万不要被第一个迷惑了

分别是这两题：
1. 利口 two city scheduling
这题压中题了，轻松过
2. 药饵丝丝 1244, 要你设计一个解决方案 - input是股票的名字和交易数量，设计一个方程来储存这个input，会不停地被call到；然后设计另一个方程输出所有股票的名字和总交易数量，按交易量从大到小排序
这题我用一个priority queue做的，但是不是最优解，估计没有过


1249, 26, 399, 200, 314, 56, 102, 380, 42, 1274, 1347, 1209, 33, 443, 445, 116, 560, 109, 797, 387, 103, 146, 1472, 39, 656, 1396, 91, 1656, 428, 1244, 1029, 253(meeting room II)




## DE Shaw
给出一个没有括号的operation，比如1 + 2*3 + 4*5 + 6，让你在这其中添加任何数量的括号，问怎样添加可以得到最大者，最大值是多少。面试官一开始假设我们只有加号和乘号。我一开始想的比较多，直接开始套用LC的模板去解这题，然后想到用DP去做。后来看了一下才发现其实加括号是有规律的，比如上面这个例子就是 （1+2）* （3 + 4） * （5 + 6），其实就是在每一个连续乘积分的开始和结尾都括上就行。知道这个之后就用正常的计算器算法去解就可以了。这里需要对原算法有一定的了解感觉，不如解起来会有点麻烦。

CodeSignal, 一个半小时四道题,
第一道是换硬币, 给硬币面额和一个想凑成的数值, 选硬币来尽可能接近这个数值
第二道题找suffix, 给一个array元素是string, 输出互为suffix string pair数量
第三题砍树, 一个数值代表路的长度,一个array代表树的位置, 路被树分割开, 另外一个array代表每次要砍掉的树的位置, 输出每次砍完树之后最长的完整的路的长度

LC: 先问了 刷题网 儿耳 然后有followup
https://math.stackexchange.com/q ... alanced-parentheses
数学: fixed price auction
you have an unknown amount of coins in a jar. each coin is worth $1
n competitors, playing optimally
your goal: bid $X. the highest bidder wins; if you don't win, you lose nothing. if you win, you get all the coins in the jar.
you cannot see the bids of other bidders. what's the optimal strategy?

1. 力扣4
2. 2 sum，input不是sorted。4 sum不限制内存要做到O(n^2)时间
3. 一个长度n的array包含1。。n-1的数字。至少一个数字出现了2次或以上。找出这个数。input不允许修改。可以二分查找。也可以构图，要找出indegree > 1的点，就变成了力扣142
4. 模拟一个类似跳棋的单人游戏。棋盘是正三角形。0是空地，1是有棋子。每步选一个棋子跳一步，被跳过的棋子要被拿走。找出一个走法使得棋盘山最后只剩一个棋子。
0
1 1
1 1 1
1 1 1 1
5. 力扣188

DEShaw 7.22 OA，投的software engineer，当天完成，题目感觉比别家oa稍难。题目忘拍照了，只记了个大概
1. 给n次query，每次query插入或者删除一个数（如果是删除保证这个数存在），问每次query之后数组里有多少对相差为diff的数。例：query=["+4", "+5", "+2", "-4"]，diff=1，则答案为[0, 1, 1, 0]。query.size() <= 1e5, -1e9 <= query[i] <= 1e9
2. 给一个数组，求数组中满足如下条件的数的对数：对于一对数nums[i]和nums[j]，i<j并且交换nums[i]里至多两个digit可以使nums[i]==nums[j]。nums.size() <= 1e4，0<=nums[i]<=1e9
3. 在-1e9到1e9的范围里种树，每棵树占据一个数字空位，最开始数轴全空。总共种k次，求问每次种树后长度不小于minLength的segment个数。例：[1, 2, 3, 6, 7], minLength = 2, 答案：[0, 1, 1, 1, 2]
4. 一个1000*1000的矩阵，在矩阵中找满足以下条件的最大十字：十字中心元素大于等于其余所有元素，且十字四个方向等长。例子：[[2,1,2],[3,4,3],[1,4,2]]， 则以中间的4为中心的十字最大，臂长最大为1（不算中心点）

如果给一个data stream，让输出最近一百万个数里面的最大值。这题不需要写码，口头答就行。我说的是用monotonic queue，然后面试官问了worst case runtime，还问了能不能找到worst case runtime O(1) 的算法（这个没答上来）。然后给了道coding，输入是一个数组，在index i 的数表示二维坐标系上的点（i，arr[i]），还有一个输入是一个在y轴观测点的y坐标，问把数组里面的点连起来，从观测点能看到哪些点（折线会挡住右侧的一些点）。我直接算了最大和最小的tangent，然后每次看新的点在不在这个范围内（O(n)）。当场跑出来了，然后又问了followup，如果现在这个系统
有两个function，init和query，query输入是一个x坐标和一个观测点y坐标（同上）看能不能看到这个点，问怎么implement比较efficient。我答的有些模糊，不过大概就是init把每个点在y轴上最上面和最下面的观测界限记录下来，然后query就直接比较观测点在不在这个界限内。
这个window是递减的，所以可以用binary search应该是O(log(window size))。不要一个一个pop，直接用pointer指index就好了

第一轮
先问了二十分钟behavior，上一轮实习干嘛了，怎么处理团队之间的关系等
coding是 利口 而司令
第二轮是coin change变形，link在这里

一上来聊了很久的background, 还有简历。然后开始问memorization, 问什么东西可以given the same input, always give the same output. 我不知道，面试官很nice告诉我是pure function。
然后做题，先是best time to buy and sell stock I and II, 但是加了个条件，有initial cash的限制。
Follow up是IV, 不用写code, 就说一下思路，我感觉说的不是很清楚，加上个initial cash的限制，我只能做到O(k*n^2), 没法O(n*k)诶~大家有什么想法
III的最佳解法应该是state machine，IV也是适用的， 只要保证每个状态不小于零应该就好了？ O(k*n)  

打电话来的是个印度哥哥，口音不太重，还好，先介绍自己的resume，然后问为什么这公司，为什么这职位，三个词评价下自己，还有些乱七八糟的过场。。。然后开始tech面试。
1. 1000的阶乘有多少个trailing zeros，就是算多少个5啦。
2. 说下java里的final 和 c 里 static的用法。
3. 怎么在jvm里实现synchronize
4. 操作系统设计，给你cpu, hard disk, memory, 怎么做一个brand new operating system（给跪了，说了一堆，快死了）
5. 问了下stack的生长方向。
6. 最后终于有一个算法，问怎么sort array of strings。
最后问我还有没有什么问题，我一看都面了1小时20分钟，本来说好了就60分钟，我赶紧说，没问题了，88

1. n-queens, follow up 如何O(1) detect conflict
2. 52 cards, half red half black. Every round you are asked to guess the card on the top. You have two options: 1) call red 2) call pass. If you got the correct color, you get 1 points. Wrong color, -1 point. Pass, 0 point. If you have not guessed any cards, you have to call red at the final card. Return expected score using optimal strategy. (第二题我当时听完是懵逼的)
第二题用MDP


面试官年轻白人小哥刚毕业一年，面试体验很舒服，面试官友善氛围轻松
一共一小时，一道智力，两道算法，五道bq，一个小时很充实。不过因为题量大算法题没让写代码，口述每一步详细做什么，数据结构和时间空间复杂度
1. 自我介绍
2. N marbles, 每次只能秤两个石子，每个石子的重量都不一样，最少需要称多少次，答案N-1
  a. 想法一：拿两个石子称一次，取最重的和下一个称
  b. 想法二：binary search，每两个称一次，取最重的下一轮称，N/2+N/4+N/8+… = N-1
  c. 想法三：每个石子是在一个有向图里的，每称一个新的石子相当于创建一个edge放进有向图里面，需要把所有石子连起来至少要N-1个edge
3. 一个国际象棋棋盘，骑士从一个角落走到对面角落，刚好20步时到达，有多少条路径
  a. 想法一：用BFS或者dijkstra，浪费branch因为可以往回走，重复了
  b. 想法二：用dp记录每个格子有几种走法，循环20次
4. 如果有一个数据结构，你需要能够查询最近输入的k个数字里最大的一个，怎么设计
  a. 单调递减队列题型，用大小不超过k的deque储存，力扣耳叁玖变体，这道题正好之前狗家面过，感觉算高频题量
5. 描述一个你认为很有意思的项目和你采取的design decision
6. 说一个你需要改变交流方式跟别人合作的情况
7. 讲一个和合作者有分歧并且解决的情况
8. 说一个你浪费了很多时间但是事后发现不值得的情况，和你下一次会怎么做
9. 描述一个你上课学到的概念

D E shaw 面经， 连续两小轮共两小时（之前没有电面）是第一轮
估计是挂了，因为本来约的是10-13.30，结果12点过后hr和我说面完了，估计是不通过所以没有下午那一轮了
第一小轮：  面试官感觉是ABC，是做quant的（这家好像quant和software的面试题接近）
BQ
技术题目： 1.   给一个数组values和对应的weight，问weighted median是多少
我问weighted median定义是啥，他让我自己定义。所以只能自己YY一个
我用了排序方法解出来了，然后他问我能不能不排序
2. 请证明需要多少次比较才能从N个数中找出最大数
我说N-1，并且证明了上限是N-1次
他问我能不能证明下限是小于N-1还是也是N-1，我想了半天只能说下限应该也是N-1次，但不会证
第二小轮：  印度人面试官，没啥口音，也是做quant的
BQ
技术题目（全口述）： 1.  8*8国际象棋棋盘，马从左下走到右上有多少种走法，最多20步
这题不能直接用bfs，因为走法允许反复到达一个点，
而直接搜索的复杂度是指数级的
我想到用dp，在面试官的提醒下，我考虑到把走了多少步也纳入状态，即dp[x][y][k]，做出来了
然后面试官问我能不能再优化循环次数（本来的是8*8*20*8），他提示了可以用对称性
答案是把k从1-20优化到1-10，然后用对称性去计算答案（循环次数应该是8*8*10*8）
就是 res = sum ( dp[i][j][10] * dp[7- i][7-j][10] ) over (i,j)吧， 这样只用计算O(8 * 8 * 10 * 8).
就是走日的，国际象棋的knight，中国象棋的马
2.  （非技术题）如果你要投资一些检测疾病的试纸，请问你会问关于这些疾病的什么问题，去决定你怎么投资
他提示我可以用消费者角度考虑，我说的是  严重而且不明显的疾病，消费者会倾向于购买
总结：   D E shaw面试难度挺大的，而且会问很多证明，给我的感觉更像《算法导论》而不是leetcode，需要你想办法优化一切可能性，而不仅仅是时间空间复杂度




## Intuit
技术面半小时讲之前做过的项目，从model choice到data pipeline还有deployment都问了。 剩余半小时coding，力扣LRU原题。整体不算太难，能讲清思路就好
我看DS店面和你的MLE还蛮像的：
“The first 30 mins is dedicated to  learning about you (relevant experience, projects, etc.) and asking general ML questions which may include fundamental topics such as data sampling, modeling approaches, pros/cons of algorithms, cross-validation, etc. The last 30 minutes is a live coding session, which usually includes a focus on core Python data structures or data manipulation (arrays, dictionaries, Pandas, Numpy, etc.)“

leetcode 124， 一道题

利口咬吴起菱 follow up是1. 写一个unit test 2: How about the corner cases? 3. How should you design the API to handle the corner cases?
剩下的时间聊一个机器学习的算法，如何实现以及loss function

第三轮：过简历+coding，数据流中求median的问题，以及内存不够怎么处理。写出了第一问，内部不够的问题没有答好
第四轮：machine learning，讲两个最熟悉的算法，然后比较。还有一个product 问题，如何从银行流水中判断哪些是personal transaction，哪些是busineess transaction


## DataDog
讲项目
设计油管
window sum
log and query
BQ

两个地里出现的题目：
查找出现频率大于1的单词的数量
DFS求最大深度的那个题
第一题，去除,.的时候用了replace，后来debug的时候，自己发现并改成replaceAll，才run过
第二题，回答空间复杂度的时候，回答成O（1），脑抽了，面试官challenge了一下，立刻反应过来，回答出来average，和最差情况

强盗抢劫房子 蠡口 亿酒捌
做出后 follow up 了 尔亿伞

面试之前过了一遍Datadog所有面经 结合Recruitor发我的文档 我预计面试应该是10min project deep dive + 2道题目maybe 结果面试老哥来了之后简单互相介绍了下直接要开始做题了 我明确问有没有project deep dive环节 老哥说那是project round的事情 他只管做题, fine. 然后问了个这个题目 🔗 leetcode.com 有很多follow up, 问OOM的时候让我解释了recursion和iteration时候内存分配的区别 然后还问我有没有O(1) 空间复杂度的办法(就是读取 + parse absolute path str本身, 也挺精巧的)

here were 2 questions:
Find duplicate words in a paragraph. Words are duplicate if they are spelled the same, even if one is capitalized and the other is not.
Return the maximum amount of points gained in a maze game. In this game, you are given a graph representing a maze game and the amount of points awarded for entering each room. Add the total amount of points.

File system/File path题变种。给了写好的class FileEntry以及它的sub classes，可以是Directory也可以是File，需要写个method 算出来给的FileEntry底下所有文件size总和。
Follow up: Input 变成一个filepath 然后要求return这个filepath底下的所有entry的size

1. 给一段话，word count然后算总共重复的个数，注意大小写，只有period和comma。
2. 给一个file system tree和directory/file interface统计总共的文件大小，follow up是给一个path统计path下的文件

coding 1: log query
follow up: 怎么ensure thread safe
coding 2: buffer file
这题需要自己写一个MockFile class 这样才可以测试
follow up: 如果file.write 每次只能写最多n个bytes到disk -> flush function 里面加一个while loop
follow up: 怎么ensure thread safe --> lock
system design: flight ticket price notification system
project deep dive: 讲自己的project
values: 正常的BQ

1. maximum tree path sum
2. frequency of words

计算word重复次数，老面经题了（easy难度），简单hashmap，但是一定要注意corner case（去标点符号和换小写）。datadog很在意你代码能不能跑通，确实跟别的公司这点不太一样。
求一个文件夹里所有file的size，有的文件是file，有的是folder，他们都是基于相同的base class。如果你用java的话，你可以像我一样，用instanceof来区分（面试官允许你google）。就是一个最简单的recursion

Coding 1: BufferedFile
Coding 2: Log and Query
System design: A system to detect if someone shares your photo on Instagram. Assuming you have a Instagram post firehose, and ML model for facial detection.

第一题是换硬币，刷题的时候以为要用dp。结果看到题发现只用普通的遍历一遍就好了。follow up：edge case
第二题是max path sum to leaf，这么简单的题我还卡了一下，3分钟没debug出来。希望不会因为这个被挂

面的staff职位
coding：
地里常说的log and query。 很快就做出来了，还问了个bonous问题
SD：
design youtube，这个也聊感觉还好，最后面试官也不知道问什么了，就聊了聊他们组正在做的东西。但最后的feedback是我自己drive的不太够，让他们问了太多的问题
past project presentation：
这个感觉做的也还可以，主要是一个hiring team的director问了很多问题，最后还说这是一个很challenge很有意思的项目，然后就让我问问题了
HM behavior：
问了一堆标准问题。past project，how to handle conflict之类的
最后挂了，感觉也是尽力了。 SD我觉得auth不是很重要的部分，就没太细说，后来面试官就一直追着问auth怎么做，我心想auth不都是用cookie吗，都是标准做法，还有啥深入探讨的，没想到面试的人就因为这个觉得我lead的不够，我也是醉了

Coding 1: given a file system api, Implement a api to list, delete all files under given path.
followup: how to reduce resource usage.
coding 2: Given a File class, implement a bufferedfile to simulate file writer with buffer
follow up: optimize buffer
System D: design a web crawler system, how to scale, how to reduce resource usage.

给一个文件夹目录“/home”，“/home”里存有几个文件夹和几个文件。每一个文件file 都有一个size 大小，求根文件夹目录的总size。
题目连File class 和Directory class的inheritance都给摆好，自己添点啥方便自己的member或者function也允许。test case也写好了，不用自己写。 解法基本就是一trie的recursion。
很可惜楼主代码写完后有一个很tricky的bug最后没找出来，打印的size总不对，面试官和我研究了半天是不是答案有误，虽然两个人都觉得这代码没问题啊。。。然后。。。挂了。

数据狗电面:
1. 坐标系线性拟合, 补丢掉的坐标点那题. (写了一个小bug, 跑了两遍之后改了过来)
2. 令牌桶那个题. (bug free 一把过)

第一题 - 地里的找文章里重复单词的个数，follow up是问input可能会有什么问题，我说可能有其他特殊符号需要特殊处理。
第二题 - 给两个人的available time intervals，还有duration，求两个人都available的最早时间段，并且持续时间大于等于duration。我一开始想是不是可以merge interval，问他intervals是不是sorted，回答可以这么认为。然后开始写，写着写着发现code很杂乱，于是问brute force行不行，他说可以，于是又开始用两个loop来对比所有的interval，最先找到的就是最早available，写了一半突然问我在写什么。我一直在一边写一边解释，他好像有点走神没有跟上我的思路，第一题也有这种情况，一边说一边写，期间他没有打断我，写完了结果要我我从头把思路讲一遍，浪费了很多时间。最后第二题没写完，他让我把思路讲了一下，然后说I get what I want，就结束了。

都是面经里的题。第一轮电面的面试官是个美国小哥，问了我两题，第一个是文章段落找重复单词总数，第二个是直线上补齐缺失的点。面完以后很快HR通知virtual onsite。
onsite总共4轮，两轮coding一轮system design一轮experience。
experience轮详细问我之前的一个项目，让我画了这个项目的架构。system design轮是设计mint.com。coding第一轮是给3个function，问如何实现删除一个目录里所有文件的函数，followup是如果oom了该怎么办，我给了一个方案以后再问如果这个方案还是oom了该怎么办，最后说了思路时间就差不多了。coding第二轮是面经里的high performance filter，followup是如果数据量很大的话该如何优化。

第一题：given a string, find the number of repititions
第二题：a variant of max sum from root to leaf of a n-ary tree

3月初面的，贡献一份面经，求点大米，给别人加米不消耗自己的大米，求大佬们加点分
电面:
1. 简单的coding, 面的很久了，忘记了，挺简单的两个题，一个是线性拟合插入点
onsite
1.2轮都是coding，一个是带数字字符串的match，一个是挺不清晰的一个题，感觉是read4那个题 with buffer，实际上这轮交流占主要部分，第二题忘记了
3轮是bq，
4轮是system design，低价机票通知系统
5轮deep dive（system）这轮挂了，没准备deepdive project，还以为是第二轮system design结果上来不问system design，让说project
就是给(x1,y1)...(xn,yn)，然后有些点的间距不符合要求，有丢失的点，需要你补上那些点。 感谢加密

第一题是repetition 求重复的次数而非总数。给一个段落，记得去标点符号和换小写。
第二题是root 到leaf 最大路径和。 follow up是 dfs recursive变iterative和 多parent如何避免cycle

1. max sum from root to leaf.(n-ary tree)
2. minimum number of coin change. 用backtrack找combination，找到了直接return result

刚面完datadog就来地里回馈大家： 一上来一个白人小哥挺热情， 然后介绍了下流程，然后开始自我介绍，然后两道coding题，第一道是地里老题：给一个paragraph,求repetitions很简单，秒了。第二道是类似于求最大路径和，但是不能回溯，题目是一个video game的milestone, 给了mileston 结构体，然后求从root到leaf的最大和，当时代码写出来有点问题，然后面试官给了点提示，然后debug了一下通过了，希望不要挂我，整体面试体验很好，看得出来内部氛围也挺好，希望能过，分享给大家，攒rp.

coding1: log query
coding2: buffer write, follow up: what happen if multithread write same file
experience: 會問你一個你工作過的一個系統，要選一個複雜的系統，不要用太簡單的，我用了一個read only service with cache, 他們覺得太簡單。
value: how do you resolve conflict, handle a task under tight deadline
system design: design youtube, 對話要清楚解釋design原因,比如為什麼要RESTful，為什麼不用web socket等等,不要直接跳進去用一個tool/technology
# Assume we have a File class whose constructor takes a filepath string as an argument. It has a single method called write, which persists bytes directly to disk.

# f = File('/tmp/my/file.txt')
# f.write(b"hello world")
# Write a wrapper class for the file object which allows us to buffer the writes in-memory. The wrapper class, BufferedFile is initialized with a File class object and a buffer size. It has two methods: write and flush. The data should be flushed to disk when the buffer is full, or on demand with a method called flush. All bytes must be stored in the buffer first before being written to disk. The buffer cannot use more memory than the max bytes allowed.

# Example usage:

# f = File('/tmp/my/file.txt')
# buf_size = 1000

# b = BufferedFile(f, buf_size)
# b.write(b"hello world")
# b.flush()
很像依伍妻
follow up multi threading, 你可以說要加 lock = threading.Lock(), with lock:

Datadog Onsite 一共面了5轮
Values
Coding I
Coding II
Design
Experience
一开始打电话的时候说Staff很难给，基本说Senior除非面试表现特别出色。好久没面试了不懂路数以为Design和Value / Experience做自己就好，Coding我面试没挂过所以没准备。结果也是如我所料Coding feedback是很好但是剩下的都不好，连Senior都没给到。
Values：
career goals, motivations, 什么事情决策不对的后来怎么解决，和别人有conflict了后来怎么修复
Coding：
​在string 里面找最长的substring，里面不能有重复的字母
一个matrix里面有很多数字，找个路径使得数字和最大。路径只能选两个方向走。
Design：
设计个系统可以监测互联网上出现自己的脸，出现了消息提醒
Experience：
问了mentor别人的经验，问了向上管理，问了时间分配，特别是如果别人需要你帮忙，怎么看待花的时间
Behavior和SD回答的时候对方笑嘻嘻，还以为答的不错结果挂了

Datadog面经：sliding windows evaluate sum of last k value, filtered by tag, sorted by timestamp ascendingly
input = [{tag: ["env:prod", "prod1"}, timestamp: [1, 10, 3, 100, 2], value: [-1, 10, -10, 100, 2]}, k = 2, tag = "prod1"
Output
Step 1: filter
Step 2: sorted = [1, 2, 3, 10, 100], value = [-1, 2, -10, 10, 100])
Step 3: output = [1, -8, 0, 110]

1. count_repetition(String paragaph)
给一段string，找出 total reprtition of words
str = "hello， world, world hello"
hello -> 重复一次
world -> 重复一次
所以output 是1 + 1 = 2
注意把 str convert 成lowerCase 然后去除special chars 空格啥的。
2. Design a circular buffer/Queue with push(), pop(), peek(), size() functions
这题注意用2个point， front， rear 然后他们移动的时候用 （front + 1）% capacity 到下一个位置防止array out of index
这个题我pop的时候忘了用 （front + 1）% capacity 而是惯性的用了 front++ 导致有个testcase 没过
不过最后5分钟问面试官问题的时候我想起来了怎么改就顺嘴提了一句front移动下一位的公式用错了。

第一题> - 文章段落找重复单词总数
+ 老题字串里面, 计算word重复次数，用coderpad 做题，求每一字重复的总数。
第二道题
求一个文件夹里所有file的size，有的文件是file，有的是folder，他们都是基于相同的base class。如果你用java的话，你可以像我一样，用instanceof来区分（面试官允许你google）‍。
-给一个文件夹目录“/home”，“/home”里存有几个文件夹和几个文件。每一个文件file 都有一个size 大小，求根文件夹目录的总size。

coding考了几道常见题目，log and query, calcualte file size given a directory
design an alert system notify user when issue is detected
behaviror include experience deep dive, how to resolve conflict, why datadog

coin找零，组合一定是能greedy的，问了什么样的组合不能greedy
max path sum，从root开始


VO总共5轮
1. Coding I
给一系列字符串
[
"Q: Hello world";
"Q: Good morning";
"L: Hello my friend and the morning is good in this world";
"L: This morning is good"
"Q: Be quick"
"Q: Be carefully"
"L: Be quick and careful"
...
]
有的是Query，有的是Log。这些字符串是从左往右一个个按顺序进来的。每进来一个Query，你要打印出这个Query被assign的ID，比如第一个Query Hello world就需要打印1，第二个Query Good morning就需要打印2，以此类推3，4…。每进来一个Log，你要打印出有哪些之前进来的Query是match这个Log的。Match的定义就是该Query的所有单词都在该Log里出现，次序不重要。所以对于第一个Log，我们要打印Query 1和2都match，对于第二个Log，我们要打印Query 2是match。
我写的Brute Force，follow up是我们会收到超级多个Query，怎么优化。我给的办法就是Inverted Index，把每个Query肢解后，每个单词作为key存入Map，value就是对应的Query IDs （ArrayList）。这样子针对Log查找的时候，可以查验哪些Query有足够的单词presence。没时间implement了，但感觉面试官还算满意。
2. Coding II
套了一层FileWriter的外皮，其实就是有一个空的固定size的byte array，写一个method可以往里边从左到右append bytes，再写一个method可以flush/清空byte array里面的bytes。这个flush method可以直接被call，或者当append operation时候内部的byte array满了，就需要内部call flush之后再resume append operation。follow up就是每次flush operation不会全部清空所有的existing bytes，而是左边的一部分，至于具体多少呢，他会以数字的形式换会告诉你，你需要handle这个情况，知道完成flush的使命。
3. SD
设计一个Flight Deal Notification Service，其中Flights Crawler是个外部API，但是需要你告诉它crawl哪个或哪几个cities，而且Deal Decider是个外部API，需要你把Flight Ticket输进去，会告诉你这个flight ticket是不是好的deal。此外Notification也是个提供好的API。
4. BQ
闲聊，问了为啥想跳槽，conflict的例子和其他常规BQ
5. Project Deep Dive
在Excalidraw里手画了一个做过的Project架构图，谈一下要解决什么问题，技术难度有哪些，你都做了什么工作，timeline等等。


LinkedIn上recruiter reach out。首先和recruiter视频闲聊了一会，唠唠家常的感觉，就开始约店面Coding轮了。
店面前15min，自我介绍了下，然后着重讲了一个自己drive的project，回答了一个对方针对性的提问。不需要画图，纯口述。
第一题是给一个target sum，和[1,5,10,25]。问使用最少的数字个数来凑齐这个target sum。解答很简单：先用大数，再用小数，直到最后用1来凑齐。
第二题是给一个File System，input structure都提供好了，其实就是个N-ary Tree，每个tree node要么是directory with children nodes，要么是file with size value。需要输出total file sizes。解答很简单：DFS，遇到directory就继续recursion，否则就increase的total size。
跑完tests后时间还很多，就follow up了一下：如果给一个inner directory的path string，如何输出total file sizes。其实也很简单：recursion method里面carry当前的path，和一个当前是否已经进入到了目标子树的flag。

面的DataDog的Senior，但是recruiter发邮件说feedback mixed，愿意约时间go through the feedback。
他把每一个feedback一字一句的念给我，然后说Senior的signal不够Strong，属于介于High Mid到Senior之间的区域。所以这次没法给Senior的offer，但是也没有冷冻期，想明年上半年再找我。
他们还是想看到更多的mentorship/big scale conflict/project difficulty这些方面。

coding第一轮：删除目录，followup是什么情况会OOM以及怎么办
coding第二轮：write to a file with a buffer，followup是write可能部分成功（类似pwrite）
sys design轮：design mint，followup是怎么monitor这个系统，这轮比较轻松
value轮：常规bq问题，答的一般
experience轮：画了几个图没太认真做slides，感觉面试官技术水平一般，讲深了就听不懂


面试senior software engineer， fail了， hr反馈系统设计一般，整体体验还不错，感觉每个人都很chill，应该是个适合长待的地方。 顺便求点大米
第一轮： coding， 老题，query和log
写一个function，读入这组strings, 如果是query, 要register不同的query并给他们assign一个qid，如果是log, 找到match的query qid并print出来. match 的意思是query的words是 subset of log‘s words。
Input example:
["Q: hello world",
"Q: data failure",
"Q: world hello",
"L: hello world we have a data failure",
"L: oh no hello system error",
"Q: system error",
"L: oh no hello system error again",

"L: oh no hello world system error again"]
Output would be:
[ "Registered q1",
"Registered q2",
"Registered q1",
"Log q1, q2",
"Log no match",
"Registered q3",
"Log q3",

"Log q1, q3",

]
第二轮：系统设计， design mint
就是设计一个类似能看到花销的系统（可以下载个mint或者花销管理软件感受一下），你需要从外部的银行拿到用户的花费条目，不能访问bank太多次数。 同时内部要能够生产report。 最后为了一个如何灾备的问题，比如一个data center都坏了，如何引导用户流量去其他数据中心
第三轮： presentation
我准备了一个我lead项目， 主要时间最好把握在30分钟，这样他们能够留下30分钟的时间问问题。我感觉present和回答问题各占一半分数，一定要确保对present的系统每个环节都比较清楚，因为有3-4个面试官每个都很资深，会从各个角度问问题。
第四轮： BQ
1. 失败的项目。 2. 如何处理冲突。 3.领到过最大的项目
第5轮： 简历dive in
对简历上的项目进行询问，最好能说出一个能体现enginering excellence的项目

Datadog最近招人不少
第一轮面试：coding
给你一些文件的接口函数：
write(const uint8_t* bytes, int nBytes)
flush()
然后实现BufferedFile类，要求模拟一个memory storage
constructor： (File* f, int nMaxBufferedBytes)；nMaxBufferedBytes is memory size
write(const uint8_t* bytes, int nBytes)： 优先写入memory，memory FIFO写入disk
flush(): from mem to disk
第二轮面试：coding
给你一些文件的接口函数：
FindList(string path): find all sub dir and files in current path
Delete(string path): if file or empty dir, delete and return true.
isDir(string path): if path is dir, return true
然后实现rm -rf，删除path下所有内容
解法： recursion
follow up：what if you have out of memory issue?
===to do===
第三轮：design
第四轮：BQ

七月面的数据狗，题基本跟地里的面经差不多，除了系统设计不太一样
HR简单聊了以后，
第一轮 1H电面 简短自我介绍+两个题+简单QA
1. 换硬币, 建议直接从大到小直接遍历，follow up 就是leetcode那个DP的题，问你怎么优化，给定的硬币如果不一样了，能否从大到小继续这样做等等
2. 树DFS遍历求和，节点路径最大值，follow up就是问你如果树变成了图怎么办.
第二轮 四轮电面 1H coding *2 + 1H system design + 1H Deep dive
建议能拆开两天就两天面，连续4个小时有点累的
Coding
1. string match，地里一模一样的题
d3dog datadog
2. revert forward index，也是地里一样的题
输入就是两种
Q: a b c
L: log a b
L: log c a b d
问你如何快速找到所有的L, L包含Q里面提及的所有单词，单词按空格划分
上面第一个L不match，因为缺一个c
第二个match，因为包含a b c
System Design
设计一个油管，实现上传，搜索，观看三大功能
follow up一般就是
大文件如何cache: HLS一样分割成N second
怎么添加hot topic搜索功能: 看你具体怎么设计
网上很多类似的设计，建议查一查
Deep Dive
A场Star模型+自己准备一个自己做的比较复杂的项目

总体来说题库很小，题很简单。
面senior， 一轮sd一轮bq两轮coding。
第一轮sd：
要求设计一个系统可以通过用户的银行消费记录分析出用户在某类消费的数量和价值等信息。一开始搞错重点了想着要考设计payment这些，结果说到一半面试官建议就把我们当做一个3rd party就好具体payment部分不用关心，主要是分类整合用户信息……讨论metric设计， api/MQ， db（我自己的设计是单独一个db存每一条action的log，但感觉这个应该是不需要的），如何监控这个系统正常运行（我当时有点慌只想到了heartbeat，zookeeper欢迎大家补充）
第二轮bq：
一个director面得，第一个proj大概聊了半个小时，具体除了很多细节技术和我的职责，就是不经意间的bq常见问题： 组内组外协调，队员犯错或不同意见，遇到的困难，self motivation。后面时间不太够了有大概花了10min聊了聊其他的项目和我喜欢和讨厌现公司的点。
第三轮coding：
datadog -> d3dog follow up也基本一样（见其他面经，如果数字是两位数或多位数，用{1,3}表示等等）。我大概写了下代码， 用memorization 记录index。复杂度。
第四轮coding：
filter match也是常见题，因为面试官是manger感觉他也没想在这轮coding上做什么文章，大概跑了几个基本数据就过了总共不到20min。然后开始聊proj，聊bq，然后聊了些可能他自己比较感兴趣的话题（我司现在的一些技术）。
总体感觉人都很nice而且听起来就是他们公司很闲，wlb很好（每一轮面试官都在不同方面表示过类似观点）。但是最后没要我……我也很难受呀。


题很简单，第一题给一段文字查多少重复单词，用个set和counter跑一遍就可以了。第二题，给一个类似树的结构查max root to leaf path，dfs，bfs，divide and conqor都可以。follow up问输入可能会有什么问题影响答案，答正环。
刚刚开始出来面试，经验太少了，时间掌握的非常不好，两道题加follow up，用了不到15分钟，剩了20多分钟尬聊些有的没的，回头想想这样真是不好，第一题应该多少说一下解体思路，第二题follow up也应该展开说一下有正环可以用spfa，记录每个点的更新进queue次数，大于n-1次说明有正环，虽然有些算法面试官也不一定知道，但是说出来也么什么坏处，展示一下自己的知识量还是好的。大家一定记得不管多简单的题，一定要跟面试官先说你的思路，他说ok你再写。这种店面都是easy题，大家都能做出来，更重要的是沟通和表达能力的考查，你怎么表达清楚你的思路，千万不要因为题太简单就直接上手写。现在市场上供大于求，大家尽量把细节做好，别给别人挑毛病的机会。


基本上全面经阵容，但系统设计想得太复杂时间控制得不好，最终还是没过。把最重要的技术轮和大家分享下：
1. 系统设计：Flight Ticket Discount Notification system，要多确认需求，能简化不少设计。不能发重复的deal，只发邮件notificiation。不用考虑多个航程转机的细节，也不用考虑discount怎么来的，有一个推荐系统直接给定discount。大家一定注意时间，把重要模块讲清楚。
2. Coding1：几乎是面经里的High Performance Filter，有incoming stream，有filter list，根据filter list输出tags的补集。实际题里是metrics log，所以有一些分割符号需要处理，不仅是像之前面经里的逗号那么直接。总体思路还是inverted index没问题。
3. Coding2：简化版的Encoded String Match，datadog -> d3dog那道，输出是true、false，pattern和word是否match。只要求考虑0-9的数字，至少第一版不用想的太复杂（比如10以上的数字怎么办，是否需要处理特殊的escape character之类的）。
tech dive deep只要详细准备一个project就好。剩下的非技术轮关键是结合经历准备例子，相信大家都能弄好。
面试总体体验不错，绝大多数面试官都很nice，除了一个大叔比较闷。。。感觉他家的HC委员会和狗家比较像，最终会比较严格。
小女子马上有好几个onsite需要看面经准备，还差几十分不够，这篇是结合之前面经用心总结的，不是重复信息。希望大家走过路过多给点米支持下:D


coding 两题：
1. 给一个bucket_size和bucket_width和一堆input数字。最后返回每个bucket里装了多少个。我就用一个int array数数，每次除一除就知道是哪个bucket的了。有一个edge case，最后一个bucekt是所有大于max的加和。譬如，我有10个bucekt，每个size是1，如果我的input里有90，这个90算在最后一个bucekt里。
2. 多叉树path sum那题，leetcode里的二叉树改成loop就好了。最后问了一下input可能会有什么问题，我想半天没想出来。然后，小哥说，可能会有loop，然后问了我解决方法。我说，用个visited，但应该要跟着树的结构，不能直接是个array什么的。现在回想，其实可以用hashset，因为每个node都是一个object。（是不是这里挂了？）
感觉题都做出来了，聊得还算愉快，并没有冷场或者什么的，但两个小时后收到拒信。
之前看面经说，这家可以给feedback的，然而我问了recruiter，说不给specific feedback，说综合了两轮考虑，不要。
第二题求有环有向图最大路径，不确定是否存在正环的算法是spfa。就是写个bfs，记录一个访问过点的最大路径值，如果比之前的大，重新进queue，还得记录一个每个点被更新的次数，如果超过n-1次，则说明有正环，跳出。

## Scale AI
Tell me a time you made a hard decision, talk about the trade off.
Tell me a time you failed the project and need to redo it, and the hard work you did.
What do you see yourself in 3 years?

hiring manager问的behavior轮：问的以前最complex的项目，你的缺点等等

Engineering manager screen - Behavioral screen ("tell me about the hardest project you've worked on", "tell me about a time you faced failure", "tell me the biggest impact you've had")

第一轮系统设计题。外组abc小年轻，老大哥国人shadowing，体验不错。全程不为难你，让你顺着思路讲完。
设计ml embedding classification system，他们公司就是做这个的，所以不难猜到。
不需要提供ml的design，focus on pipeline，基本就是八股文: queue, redis, noSQL, batch processing之类的。


`1 play card game，有三轮，扑克游戏，52张扑克，属性是类别和数字，第一轮写出随机发牌后四个玩家手上的结果。第二轮四个玩家按照规则play，玩13轮，写出每轮play的结果，第三轮每轮按规则算分，算出每个玩家的总分。最后得出哪个玩家赢得游戏。手牌和每轮结果都是print出来的，所以并不需要考虑复杂的情况。
这题提供了基础的card class和player class，需要写出play function还有game的逻辑。 题目本身没有涉及到算法，都是数据结构和数据处理。

第一轮，60分钟写出一个卡牌游戏
有三个sub problem
有提供basic class 如 player 等等
卡牌有两种属性，suit and rank，suit and rank都是string
四人轮流抽牌，抽一张print 一句statement，最后sort和print 所有人手中的牌, 先按照suit, 再按照rank（2最小，A最大）
轮流出牌，第一个人出什么suit，余下的人都要出那个suit（任何rank都可以），如果手上已经没有该suit的牌，就可以随意出。赢的人（该suit最大的牌）成为下一轮的出牌者。
每次出牌都要print，例如：
玩家 1 出 2s
玩家 2 出 3s
玩家 3 出 4s
玩家 4 出 5c
那么下一轮print的可能长这样：
玩家 3 出 …
玩家 4 出 …       
玩家 1 出 …
玩家 2 出 …
算分，每一轮赢的人可得分，分数＝5* 多少张5 + 10*多少张10 or K
每一轮print出谁赢了, 拿了多少分
最后print 出每个人的分

第一轮是个 OOP 的店面。 60 分钟，题目是 card game 。一上来给了 suit 和 rank 的定义，也给了 card, deck, player 的 class 。让写三个部分。
第一部分是每个 player 轮流抽牌。
第二部分是每个 player 轮流打牌。每个人出牌有一定的规则，每一轮还要比较谁赢了，并作为下一轮的 starter 。
第三部分是算分。

第三个part是在第二轮的游戏规则上计分的，winner可以把这一轮出了5、10、K牌所对应的点数都加进去，最后打印每个玩家的总得分，和得分最高的玩家

店面卡牌游戏： 第一轮实现轮流打牌 第二轮算每轮的赢家 第三轮计分
最后面试官还说player的编号print出来要从1开始不能从0开始

面试是一个类似桥牌游戏，已经写了Card，Deck，Player，要求implement三个部分。Deck可以draw可以shuffle
第一部分要求一副牌发给4个玩家，每个玩家根据花色手牌排序
第二部分每个玩家轮流按花色出牌 牌最大的下一轮先出
第三部分计分，5 10 K是分 牌最大的得一轮的分 牌全出完算分最多的玩家

开始coding 一样也是52张卡但是game像UNO，那么在一小时内完成会给你的CARD 和 DECK 的classes。
一开始给你4个玩家，每个玩家可以分到 X牌，然后需要整理卡的 RANK 和SUIT顺序。
游戏开始会deck出random一张牌，然后每个玩家会照一个指定的顺序打出一样 RANK/SUIT的 combination牌。打出的牌的RANK+SUIT 也有分数需要统计。没有相对的牌需要从DECK抽进HAND里。一旦一个人打完整个牌游戏结束。最后算出赢家。

一种纸牌游戏的模拟，玩家轮流出牌、比较牌面大小以决定每轮胜者。游戏要进行13轮。
`


`具体问题就是给了六个rule，如果满足其中任意一个rule就是valid的hand。让你判断一个hand是不是valid。六个rule就是我们熟悉的德扑的rule：同花顺，顺子之类的。
第二问：如果有大小王可以代表任意一个牌的话，怎么做。

规则有变, 如果有同花顺怎么办, 如果有顺子怎么办, 如果有炸弹怎么办

OOD是经典卡牌题, 52张扑克牌，给定六条规则（类似于德扑里同花顺、顺子的规则），如果一个手牌（hand）符合其中任意一条规则，就返回True，不valid的情况返回False。Followup是如果有wildcard怎么办。

Use OOP to code aspects of a poker game. The functions should check for poker patterns like flush, straight, full house, 4-of-a-kind, etc. Input is a list of cards and output is a boolean whether there is a pattern or not. The follow-up is to modify the functions to consider the Joker a wildcard. The wildcard can be used to match any rank and suit.
part of the problem is checking if the hand has 5 cards. So, the hand may have any number but if the hand does not have 5 cards, it should return False immediately.

1. 给一个Card的class，里面有rank和suit。实现一个方法提供5个cards，判断是否符合德扑的一些规则（有6个）。如果符合return True，else return false
2. 手牌里可以有任意数量的JOKER牌，JOKER牌可以当作wildcard，可以当作任意rank和suit。返回是否valid。2的method同样也要能过1的test cases。
3. 提供两个人的手牌比大小，提供德扑各种rule的顺序。

还是扑克牌，五张牌，写 checker，用德扑的规则判断是不是 valid，followup 是 joker 当 wild card, 而且wildcard是任意数量
就是牌里如果有joker的话，joker就是万能牌，然后看能不能组成一个valid hand. 手牌是5张
`

Given already set-up code structure(card, hand class)
Uses python enum
Need to sort
Calculate max
Another card game:(OOP)
First need to generate 52 cards, 13 ranks in each of the four suits: clubs (♣), diamonds (♦), hearts (♥) and spades (♠), then implement draw cards function and shuffle function。Then create 2 Play/Hand, each player gets 5 cards from the deck, then 2 players compares with each other using their biggest card，who is bigger who wins, otherwise tie

地里提过的card game
有已经setup的code structrue (card, hand class)
用到了python enum
需要sort
计算max

首先要生成52张牌，13 ranks in each of the four suits: clubs (♣), diamonds (♦), hearts (♥) and spades (♠) 然后实现抽牌函数 (draw) 以及洗牌函数 (shuffle)。之后，创建2个Player/Hand，每个player从牌堆里抽5张牌，然后2个人用手里牌最大的比，谁更大谁就赢，如果一样就是平局。
