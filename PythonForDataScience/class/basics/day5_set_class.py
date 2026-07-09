# SET

# unordered collection, changable, no-duplication, set enclosed with {} and separated by ,(comma)

set_1 = {"ram", 1,2,3,4.444, True, False}

print(set_1)
print(len(set_1))
print(type(set_1))

# Access item

for i in set_1:
    print(i)

print(True in set_1)
print("hi" not in set_1)

song = {"guras", "komal", "saitaan","Chori"}
print("guras" not in song)
print("saitaan" in song)

# find the item in tuple
song_2 = ("guras", "komal", "saitaan","Chori")
print("salugu" in song_2)

song.add("Fulmaya")

print(song)

song.remove("Fulmaya")
print(song)

song.add(1)
print(song)

int_set = {1,2,3}
print(int_set)

song_title = ("guras", "komal", "saitaan","Chori")
artist = {"mt8848", "john", "albatross"}
artist.update(song_title)
print(artist)

q1 = {"q1", "q2", "q3"}
ans = ("ans1","ans2")
print(q1)

q1.update(ans)
print(q1)


# Removing data from set: remove, discat

# q1.remove(" ")
# print(q1)

best = {"alok", "pralad"}
best.discard(" ")
print(best)

# best.remove(" ")
# print(best)

best.pop()
print(best)

best.clear()
print(best)


# Join the set
# Union

a = {1,2,3,4,5,"Ram","Hari"}
b = {1,3,"Ram",5,7,8,9}


print(a|b)
print(a.union(b))

c = {1,2,3,4,5,"Ram","Hari"}
d = {1,3,"Ram",5,7,8,9}
d.update(c)
print(d)


# Intersection , &

e = {1,2,3,4}
f = {1,2,6,7,8,9}

print(e & f)
print(e.intersection(f))

# Difference

g = {1,2,3,4}
h = {1,2,6,7,8,9}

print(g - h)
print(g.difference(h))

# Symmmetric difference

i = {1,2,3,4,5}
j = {1,2,6,7,8,9}

print(i ^ j)
print(i.symmetric_difference(j))