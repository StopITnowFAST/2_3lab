import json

my_list = ["foo", "bar"]

# вариант 1
contents = json.dumps(my_list)
with open("foo.txt", "w", encoding="utf-8") as f:
    f.write(contents)

# вариант 2
with open("foo.txt", "w", encoding="utf-8") as f:
    json.dump(my_list, f)
