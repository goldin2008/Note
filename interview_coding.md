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


## Amazon
- Example: # Question: Given an array of numbers a and another array of numbers b, # find k nearest elements from a for each element in b. # a = [1, 2, 10, 100, 102, 205] # b = [3, 80] # k = 2 # output = [[1,2], [100, 102]]

## Bloomberg
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
