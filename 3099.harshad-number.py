class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        baiwei = x // 100
        y = x % 100
        shiwei = y // 10
        gewei = y % 10
        t = baiwei + shiwei + gewei
        if 0 != x % t:
            return -1
        else:
            return t