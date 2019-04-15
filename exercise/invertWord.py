# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__mtime__ = '2019/4/15'
"""

class Invert:
    def invert(self, origin_string):
        new_str_list = []
        str_len = len(origin_string)
        for i in range(str_len):
            new_char = self.trans(origin_string[str_len - 1 - i])
            new_str_list.append(new_char)

        return "".join(new_str_list)

    def trans(self, original_char):
        if original_char.islower():
            return original_char.upper()
        else:
            return original_char.lower()


if __name__ == "__main__":
    myclass = Invert()
    print(myclass.invert("Hello World!"))

