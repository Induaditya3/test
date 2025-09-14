import check50

@check50.check()
def exists():
    """check if file exists"""
    check50.exists("pascal.py")

@check50.check(exists)
def prints_level_1():
    """prints first level of pascal triangle correctly"""
    check50.run("python3 pascal.py").stdin(1).stdout("[1]").exit(0)

@check50.check(exists)
def prints_level_2():
    """prints level 2 of pascal triangle correctly"""
    check50.run("python3 pascal.py").stdin(2).stdout("[1, 2, 1]").exit(0)

@check50.check(exists)
def print_level_5():
    """prints level 5 of pascal triangle correctly"""
    check50.run("python3 pascal.py").stdin(5).stdout("[1, 5, 10, 10, 5, 1]").exit(0)
