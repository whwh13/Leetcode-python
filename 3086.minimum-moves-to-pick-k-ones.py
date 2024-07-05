class Solution:
    def minimumMoves(self, nums, k: int, maxChanges: int) -> int:
        indices = [i for i, num in enumerate(nums) if num == 1]
        [point,step]=self.easypoint(nums,indices)
        if point>=k:     # 如果easypoint足够就直接使用easypoint
            return k-1
        else:
            if k-point<=maxChanges:  # easypoint不够但是maxchange+easypoint够
                return step+2*(k-point)
            else: # maxchange+easypoint不够则maxchange需要全部利用，剩下的转化为m取n
                step=2*maxChanges
                point=maxChanges


        return step+self.picknfromm(indices,k-maxChanges)


    def picknfromm(self,indices,n):   # 这是在m个数中选择n个数，并返回其整体距离最小值

        current_dis = self.calStep(indices[:n],n)
        min_dis = current_dis
        for jj in range(n,len(indices)):

            current_dis = self.calStep(indices[jj-n+1:jj+1],n)

            min_dis = min(min_dis, current_dis)
        
        return min_dis


    def calStep(self,arr,n): # 计算n个数组时对应的距离值
        if n % 2:
            return sum(arr[n//2+1:]) - sum(arr[:n//2])
        else:
            return arr[n-1]-arr[n//2-1]+self.calStep(arr[:-1],n-1)

    def easypoint(self,nums, indices): # 分类讨论，有些点数极易获得
        totalpoint = sum(nums)
        if totalpoint==0:
            return [0,0]
        elif totalpoint==1:
            return [1,0]
        elif totalpoint==2:
            if indices[1]-indices[0]==1:
                return [2,1]
            else:
                return [1,0]
        else:

            twoCon=False
            for ii in range(0,totalpoint-2):
                if indices[ii+1]-indices[ii] == 1:
                    twoCon=True
                    if indices[ii+2]-indices[ii+1] == 1:
                        return [3,2]
            if not twoCon:
                if indices[totalpoint-1]-indices[totalpoint-2] == 1:
                    return [2,1]
                else:
                    return [1,0]
            else:
                return [2,1]
        