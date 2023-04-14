#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

if __name__ == "__main__":
    my_list = ["foo", "bar"]

    # вариант 1
    contents = json.dumps(my_list)
    with open("foo.txt", "w", encoding="utf-8") as f:
        f.write(contents)

    # вариант 2
    with open("foo.txt", "w", encoding="utf-8") as f:
        json.dump(my_list, f)
