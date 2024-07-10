import numpy as np

class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
            x=-x
        else:
            sign=1

        exception = 0
        [x,q]=divmod(x,10)
        while x:
            exception = exception*10+q
            [x,q]=divmod(x,10)

        if exception>214748364:
            return 0
        elif exception==214748364:
            if sign==1 and q>7:
                return 0
            elif sign==-1 and q>8:
                return 0
            else:
                return sign*(exception*10+q)
        else:
            return sign*(exception*10+q)
            