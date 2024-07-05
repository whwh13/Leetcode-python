class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        l=len(s)
        m=2*numRows-2
        [p,q]=divmod(l,m)
        string_array=[""]*numRows

        for ii in range(1,p+1):
            for jj in range(0,m):  # python从0开始的编号真恶心人

                [x,y] = divmod(jj,numRows)
                y = (numRows - 2 - y) if x == 1 else y
                string_array[y] += s[(ii-1)*m+jj]

        if q:
            for kk in range(0,q):
                [x,y] = divmod(kk,numRows)
                y = (numRows - 2 - y) if x == 1 else y
                string_array[y] += s[p*m+kk]

        return "".join(string_array)
