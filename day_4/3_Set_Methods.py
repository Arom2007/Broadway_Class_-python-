# copy()

s1 = {1, 2, 3}
s2 = s1.copy()
print(s2)  # {1, 2, 3}


# difference()
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
diff = s1.difference(s2)  # s1-s2
print(diff)  # {1, 2}

diff = s2.difference(s1)
print(diff)  # {5, 6}

# intersection()
inters = s1.intersection(s2)
print(inters)  # {3, 4}


# union()
union = s1.union(s1)
print(union)  # {1, 2, 3, 4, 5, 6}


# isdisjoint()
print(s1.isdisjoint(s2))  # False


s1 = {1, 2, 3, 4, 5}
s2 = {2, 3}

print(s2.issubset(s1))  # True
print(s1.issuperset(s2))  # True