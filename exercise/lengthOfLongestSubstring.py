# -*- coding: utf-8 -*-#

"""
 Name:         lengthOfLongestSubstring
 Description:  
 Author:       xiaoyuLuo
 Date:         2019/4/25
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strLen = len(s)
        resultInt = 0
        for i in range (strLen):
            subStrList = []
            for j in range(i, strLen):
                try:
                    subStrList.index(s[j])
                    if len(subStrList) > resultInt: resultInt = len(subStrList)
                    break
                except:
                    subStrList.append(s[j])
                    if j == (strLen - 1):
                        if len(subStrList) > resultInt: resultInt = len(subStrList)

        return resultInt

    def lengthOfLongestSubstringTwo(self, s: str) -> int:
        st = {}
        i, resultInt = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                print(i)
                print(j)
                print(s[j])
                # 前一个重复出现字符串的位置
                i = max(st[s[j]], i)

            resultInt = max(resultInt, j - i + 1)
            print(s[j])

            st[s[j]] = j + 1
            print(st)
        return resultInt;

if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.lengthOfLongestSubstringTwo("abcaefghibcdbcd"))
