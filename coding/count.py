# import OS module
import os

def get_file_list(): 
    # Get the list of all files and directories
    path = "./leetcode/"
    dir_list = os.listdir(path) 
    print("Files and directories in '", path, "' :")
    # prints all files
    print(len(dir_list))

    print("Python Program to print list the files in a directory.")
    Direc = path
    files = os.listdir(Direc)
    files = [f for f in files if os.path.isfile(Direc+'/'+f)] #Filtering only the files.
    # print(*files, sep="\n")
    print(len(files))

    return files


import re

def count_file(files):
    patterns = ['_AR_', '_LL_', '_HM_', '_ST_',
               '_PP_', '_QU_', '_BS_', '_BT_',
               '_GD_', '_DD_', '_DP_', '_EX_']

    # result = re.match(pattern, test_string)
    # indices = [i for i, x in enumerate(files) if re.search(pattern, x)]
    # indices = [x for i, x in enumerate(files) if re.findall(pattern, x)]
    tot = 0
    for p in patterns:
        indices = [x for x in files if re.findall(p, x)]
        print(p, len(indices))
        tot += len(indices)
    
    print('Total: ', tot)

# 数组 AR | 6 ?
# 链表 LL | 8 ?
# 哈希表 HM | 9 ?
# 字符串 ST | 7 ?
# 双指针 PP | 10 ?
# 栈和队列 QU | 8 ?
# 二叉树 BS| 34 ?
# 回溯 BT | 21 ?
# 贪心 GD | 24 ?
# 单调栈 DD | 5
# 动态规划 DP | 38
# 额外 EX | 35
# 总数 | 205

if __name__ == "__main__":
    files = get_file_list()
    count_file(files)
