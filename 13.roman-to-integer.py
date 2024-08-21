class Solution:
    def romanToInt(self, s: str) -> int:
        point = 0
        num = 0
        while point < len(s):
            match s[point]:
                case 'M':
                    num += 1000
                    point += 1
                case 'D':
                    num += 500
                    point += 1
                case 'C':
                    if point + 1 < len(s):
                        if s[point+1] == 'M':
                            num += 900
                            point += 2
                        elif s[point+1] == 'D':
                            num += 400
                            point += 2
                        else:
                            num += 100
                            point += 1
                    else:
                        num += 100
                        point += 1
                case 'L':
                    num += 50
                    point += 1
                case 'X':
                    if point + 1 < len(s):
                        if s[point+1] == 'C':
                            num += 90
                            point += 2
                        elif s[point+1] == 'L':
                            num += 40
                            point += 2
                        else:
                            num += 10
                            point += 1
                    else:
                        num += 10
                        point += 1
                case 'V':
                    num += 5
                    point += 1
                case 'I':
                    if point + 1 < len(s):
                        if s[point+1] == 'X':
                            num += 9
                            point += 2
                        elif s[point+1] == 'V':
                            num += 4
                            point += 2
                        else:
                            num += 1
                            point += 1
                    else:
                        num += 1
                        point += 1

        return num
