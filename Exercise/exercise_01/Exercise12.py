class SetInfo(object):
    def __init__(self, my_set):
        self.sett = my_set

    def add_setinfo(self, keyname):
        self.sett.add(keyname)
        return self.sett

    def get_intersection(self, unioninfo):
        # 写法一：
        # return self.sett.intersection(unioninfo)
        # 写法二：
        if isinstance(unioninfo, set):
            return self.sett & unioninfo
        else:
            return "你传入的不是集合"

    def get_union(self, unioninfo):
        # 写法一：
        # return self.sett.union(unioninfo)
        # 写法二：
        if isinstance(unioninfo, set):
            return self.sett | unioninfo
        else:
            return "你传入的不是集合"

    def get_difference(self, unioninfo):
        # 写法一：
        # return self.sett.difference(unioninfo)
        # 写法二：
        if isinstance(unioninfo, set):
            return
            return self.sett - unioninfo
        else:
            return "你传入的不是集合"


A = set([1, 2, 3, 4, 5])
my_set = SetInfo(A)
B = set([5, 6, 3])
print(my_set.add_setinfo(6))
print(my_set.get_intersection(B))
print(my_set.get_union(B))
print(my_set.get_difference(B))
print(A)