vec = [5, 6, 7, 8, 8, 10]
target = 8
output = [3, 4]

def find_start_end(vec, target):
    if target in vec:
        return target
    else:
        return vec

def test_find_start_end():
    