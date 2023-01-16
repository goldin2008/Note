import config

def test():
    config.Config.a = 4

def test1():
    print(config.Config.a)
    
if __name__ == "__main__":
    test()
    test1()
