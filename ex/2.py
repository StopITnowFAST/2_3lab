#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

if __name__ == "__main__":
    # вариант 1
    with open("foo.txt", "r") as f:
        contents = f.read()
    my_list = json.loads(contents)

    # вариант 2
    with open("foo.txt", "r") as f:
        my_list = json.load(f)
