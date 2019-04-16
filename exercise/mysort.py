# !/usr/bin/env python
# -*- coding: utf-8 -*-#

"""
 Name:         Sort
 Description:  参照：https://www.cnblogs.com/wuxinyan/p/8615127.html
 Author:       xiaoyuLuo
 Date:         2019/4/16
"""

class ClassicSort:

    def bubble_sort(self, data_list):
        list_lens = len(data_list)
        for i in range(1, list_lens):
            print(str(i))
            for j in range(0, list_lens - i):
                print(str(j) + " next")
                if data_list[j] > data_list[j+1]:
                    data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
                    print(data_list)

        return data_list


if __name__ == '__main__':
    mySort = ClassicSort()
    print(mySort.bubble_sort([11, 2, 9, 10, 8, 5]))
