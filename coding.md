## Coding interview

`
题目理解(关键概念)+提出问题(输入输出类型/edge cases/算法使用环境要求)+讨论可行方案(分析时间空间复杂度)+确定最合理方案(保证在规定时间内可以写完/合理简化问题)+coding(write test cases)+follow up（1）做LC的时候我按照算法类别做题， 每周主攻一个topic，（2）中档题目如果最多半小时内自己找不到思路，就看discussion，然后按照discussion自己写一遍。(3)每个专题的题目，先把所有题目题干过一遍，把每类型的题目分类，相似的归为一个小组，合在一起做。（4）每个专题在做题的时候把各种错误和好的思路都用文档记录下来，把重要信息都高亮显示。
`

刚开始刷 别自己蛮干，有钱可以考虑上个班突击，或者看几个大神那一系列的视频，跟着大神的视频把基本的20几个tag先过一遍，或者把最简单的10个左右能cover easy level的tag先过一遍， 最最高频，最最基础的的 BS二分，分治，二叉树，链表，DFS BFS， 。。etc 先过一遍
DP ， segment tree/BIT 这些起码 medium 以上的先留一留
搜一下 残酷刷题群 或者 youtube 每日一题，找那个 excel文档，guan大神每个tag基本要连着刷 3~5题，按这个刷 进阶
还有花花酱 和 古城算法 也不错，不过残酷群是目测几年来一直在update更新的，有些大神已经上岸了所以不再更新的

每个类别，dfs，bfs，queue，stack，trie tree，binary tree，graph， binary search，等各刷了10道题

youtube上面有个叫花花还有古城算法，你按照那个刷。尤其推荐花花，我记得他有个刷题单子。核心就是相近的题目得放在一起刷，技能体会细节的不同，又能知道哪些是通用的。

# 项目简介

算法面试圣经(俗称cc150)《Cracking the Coding Interview: 150 Programming Interview Questions and Solutions》。LeetCode上很多的题目都是来自这本书的。

这本书覆盖了后端开发知识体系的方方面面。([第六版](https://www.ituring.com.cn/book/1876))。官方给出的是Java版，这整理了第六版的Python实现。由于是个人的业余实现，可能存在错误。

本项目使用jupyter编写，导出markdown格式。这样既可以像阅读ppt一样浏览，也可以随时动手验证自己的想法。

- [使用指南](#使用指南)
- [备注](#备注)
- [第六版题目列表](#第六版题目列表)
- [计划表](#计划表)

## 使用指南

```bash
# 安装jupyter
pip3 install jupyter

# 进入项目下的jupter目录,启动jupyter服务器.访问地址http://localhost:8888/tree
jupyter notebook
```

## 备注

- 链表节点的定义：
```python
# Definition for singly-linked list.
class ListNode:
    
    def __init__(self, x):
        self.val = x
        self.next = None
```
- 相关的公共放在了`jupyter/common`目录，引入方式如下：
```python
import os
import sys
sys.path.insert(0, os.path.abspath('./common'))
```

## 第六版题目列表

| 序号           | 题目           | 描述           |
| ------------- |----------------|----------------|
|        | | <h4>数组与字符串<h4> |
| 1.1    | [**判定字符是否唯一**](https://github.com/panxl6/cc150/blob/master/markdown/1.1%20判断字符串是否有重复的字符.md) | 实现一个算法,确定一个字符串的所有字符是否全都不同。假使不允许使用额外的数据结构,又该如何处理? |
| 1.2    | [**判定是否互为字符重排**](https://github.com/panxl6/cc150/blob/master/markdown/1.2%20判定是否互为字符重排.md) | 给定两个字符串,请编写程序,确定其中一个字符串的字符重新排列后,能否变成另一个字符串。 |
| 1.3    | [**URL化**](https://github.com/panxl6/cc150/blob/master/markdown/1.3%20URL化.md) | 编写一种方法,将字符串中的空格全部替换为 %20 。假定该字符串尾部有足够的空间存放新增字符,并且知道字符串的“真实”长度。(注:用 Java 实现的话,请使用字符数组实现,以便直接在数组上操作。) <br>*示例*:<br>*输入:* "Mr John Smith", 13 <br>*输出:* "Mr%20John%20Smith" |
| 1.4    | [**回文排列**](https://github.com/panxl6/cc150/blob/master/markdown/1.4%20回文排列.md)  | 给定一个字符串,编写一个函数判定其是否为某个回文串的排列之一。回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。回文串不一定是字典当中的单词。<br>*示例:*<br>*输入:* Tact Coa<br>*输出:* True (排列有 "taco cat" 、 "atco cta" ,等等) |
| 1.5    | [**一次编辑**](https://github.com/panxl6/cc150/blob/master/markdown/1.5%20一次编辑.md)  | 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。给定两个字符串,编写一个函数判定它们是否只需要一次(或者零次)编辑。<br>*示例:* <br> pale, ple -> true <br>pales, pale -> true <br>pale, bale -> true <br> pale, bake -> false |
| 1.6    | [**字符串压缩**](https://github.com/panxl6/cc150/blob/master/markdown/1.6%20字符串压缩.md)  | 利用字符重复出现的次数,编写一种方法,实现基本的字符串压缩功能。比如,字符串 aabcccccaaa 会变为 a2b1c5a3 。若“压缩”后的字符串没有变短,则返回原先的字符串。你可以假设字符串中只包含大小写英文字母(a 至 z) |
| 1.7    | **旋转矩阵**  | 给定一幅由 N × N 矩阵表示的图像,其中每个像素的大小为 4 字节,编写一种方法,将图像旋转 90 度。不占用额外内存空间能否做到? |
| 1.8    | [**零矩阵**](https://github.com/panxl6/cc150/blob/master/markdown/1.8%20零矩阵.md)  | 编写一种算法,若 M × N 矩阵中某个元素为 0,则将其所在的行与列清零。 |
| 1.9    | [**字符串轮转**](https://github.com/panxl6/cc150/blob/master/markdown/1.9%20字符串轮转.md)  | 假定有一种 isSubstring 方法,可检查一个单词是否为其他字符串的子串。给定两个字符串 s1 和 s2 ,请编写代码检查 s2 是否为 s1 旋转而成,要求只能调用一次isSubstring (比如, waterbottle 是 erbottlewat 旋转后的字符串)。 |
|        | | <h4>链表<h4> |
| 2.1    | [**移除重复节点**](https://github.com/panxl6/cc150/blob/master/markdown/2.1%20移除重复节点.md)  | 编写代码，移除未排序链表中的重复节点。<br> *进阶：* 如果不得使用临时缓冲区，该怎么解决？ |
| 2.2    | [**返回l倒数第k个节点**](https://github.com/panxl6/cc150/blob/master/markdown/2.2%20返回倒数第k个节点.md)  | 实现一种算法，找出单向链表中倒数第k 个节点。 |
| 2.3    | [**删除中间节点**](https://github.com/panxl6/cc150/blob/master/markdown/2.3%20删除中间节点.md)  | 实现一种算法，删除单向链表中间的某个节点（除了第一个和最后一个节点，不一定是中间节点），假定你只能访问该节点。<br> *示例：* <br> *输入：*  单向链表a->b->c->d->e->f 中的节点c <br> *结果：* 不返回任何数据，但该链表变为a->b->d->e->f |
| 2.4    | [**分割链表**](https://github.com/panxl6/cc150/blob/master/markdown/2.4%20分割链表.md)  | 编写程序以x 为基准分割链表，使得所有小于x 的节点排在大于或等于x 的节点之前。如果链表中包含x，x 只需出现在小于x 的元素之前（如下所示）。分割元素x只需处于“右半部分”即可，其不需要被置于左右两部分之间。<br> 示例：<br>输入：3 -> 5 -> 8-> 5 -> 10 -> 2 -> 1 [分节点为5] <br>输出：3 -> 1 -> 2 -> 10 -> 5-> 5 -> 8 |
| 2.5    | [**链表求和**](https://github.com/panxl6/cc150/blob/master/markdown/2.5%20链表求和.md)  | 给定两个用链表表示的整数，每个节点包含一个数位。这些数位是反向存放的，也就是个位排在链表首部。编写函数对这两个整数求和，并用链表形式返回结果。 <br>示例：<br> 输入：(7-> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295 <br>输出：2 -> 1 -> 9，即912 <br> 进阶：假设这些数位是正向存放的，请再做一遍。 <br><br>示例：<br>输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295 <br> 输出：9 -> 1 -> 2，即912|
| 2.6    | [**回文链表**](https://github.com/panxl6/cc150/blob/master/markdown/2.6%20回文链表.md)  | 编写一个函数，检查链表是否为回文。 |
| 2.7    | [**链表相交**](https://github.com/panxl6/cc150/blob/master/markdown/2.7%20链表相交.md)  | 给定两个（单向）链表，判定它们是否相交并返回交点。请注意相交的定义基于节点的引用，而不是基于节点的值。换句话说，如果一个链表的第k 个节点与另一个链表的第j 个节点是同一节点（引用完全相同），则这两个链表相交。 |
| 2.8    | [**环路检测**](https://github.com/panxl6/cc150/blob/master/markdown/2.8%20环路检测.md)  | 给定一个有环链表，实现一个算法返回环路的开头节点。有环链表的定义：在链表中某个节点的next 元素指向在它前面出现过的节点，则表明该链表存在环路。 <br>示例：<br>输入：A -> B -> C -> D -> E -> C（C 节点出现了两次）<br>输出：C|
|  | | <h4>栈和队列<h4> |
| 7.10    | **扫雷**  | 设计和实现一个基于文字的扫雷游戏。扫雷游戏是经典的单人电脑游戏，其中在N × N 的网格上隐藏了B 个矿产资源（或炸弹）。网格中的单元格后面或者是空白的，或者存在一个数字。数字反映了周围8 个单元格中的炸弹数量。游戏开始之后，用户点开一个单元格。如果是一个炸弹，玩家即失败。如果是一个数字，数字就会显示出来。如果它是空白单元格，则该单元格和所有相邻的空白单元格（直到遇到数字单元格，数字单元格也会显示出来）会显示出来。当所有非炸弹单元格显示时，玩家即获胜。 玩家也可以将某些地方标记为潜在的炸弹。这不会影响游戏进行，只是会防止用户意外点击那些认为有炸弹的单元格。（读者提示：如果你不熟悉此游戏，请先在网上玩几轮。） <br>![扫雷](https://raw.githubusercontent.com/panxl6/blog/master/Images/7-10.png)|
| 9.8    | **文本分享**  | 设计一个类似于 Pastebin 1 的系统,用户输入一段文本,就可以得到一个随机生成的 URL 来访问该系统。 |
|  | | <h4>排序与查找<h4> |
| 10.1    | [**合并排序的数组**](https://github.com/panxl6/cc150/blob/master/markdown/10.1%20合并排序的数组.md)  | 给定两个排序后的数组 A 和 B ,其中 A 的末端有足够的缓冲空间容纳B 。编写一个方法,将 B 合并入 A 并排序。 |


## LeetCode题目归类
cc150的题目，知识面广，但是难度相对较小，相当于leetcode的easy题。但是在这些题型中受到启蒙以后，leetcode的题型也会打开思路的。为了扩充一些题量，整理leetcode的类型总结。

## 计划表

- [x] 统一代码格式
- [x] 美化文字格式，提升阅读体验
- [ ] 增加LeetCode的相关专题
- [ ] 完成后续的章节
- [ ] 增加示意图或动画
- [x] 增加第六版的内容
- [x] 对比官方的Java版答案，校验一次
- [ ] 抽象测试用例运行框架，实现一个Online judge
