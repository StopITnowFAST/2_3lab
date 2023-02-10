import json

#вариант 1
with open("foo.txt", "r") as f:
    contents = f.read()
my_list = json.loads(contents)

#вариант 2
with open("foo.txt", "r") as f:
    my_list = json.load(f)
