from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sizeL=len(nums1)
        sizeR=len(nums2)
        if(sizeL==0 and sizeR==0):
            return float(0)
        if(sizeL==0):
            if(Solution().isEven(sizeR)):
                return (nums2[int(sizeR/2)-1]+nums2[int((sizeR/2))])/2
            else:
                return nums2[int((sizeR+1)/2)-1]
        if (sizeR == 0):
            if (Solution().isEven(sizeL)):
                return (nums1[int(sizeL / 2)-1] + nums1[(int(sizeL / 2))]) / 2
            else:
                return nums1[int((sizeL + 1) / 2)-1]

        if(sizeL<=sizeR):
            return Solution().binarySearch(nums1,nums2,sizeL,sizeR,0,sizeL)
        else:
            return Solution().binarySearch(nums2,nums1,sizeR,sizeL,0,sizeR)

    def binarySearch(self,numsL:List[int],numsR:List[int],sizeL:int,sizeR:int,left:int,right:int)->float:
        #print(numsL,numsR,sizeL,sizeR,left,right )
        inf=1000005
        if left>right:
            return 0
        midf = int((left+right)/2)
        mids = int((sizeL+sizeR+1)/2)-midf
        #print(midf,mids)
        x1=0
        x2=0
        y1=0
        y2=0
        if midf==0:
            x1=-inf
            x2=numsL[midf]
        if mids==0:
            y1=-inf
            y2=numsR[mids]
        if midf==sizeL:
            x1=numsL[midf-1]
            x2=inf
        if mids==sizeR:
            y1=numsR[mids-1]
            y2=inf
        if midf>0 and midf<sizeL:
            x1=numsL[midf-1]
            x2=numsL[midf]
        if mids>0 and mids<sizeR:
            y1=numsR[mids-1]
            y2=numsR[mids]
        #print(x1,x2,y1,y2)
        if(Solution().isCursorRight(x1,x2,y1,y2)==0):
            return Solution().ansValue(x1,x2,y1,y2,Solution().isEven(sizeL+sizeR))
        if(Solution().isCursorRight(x1,x2,y1,y2)==1):
            return Solution().binarySearch(numsL,numsR,sizeL,sizeR,midf+1,right)
        else:
            return Solution().binarySearch(numsL,numsR,sizeL,sizeR,left,midf-1)


    def isEven(self,size:int)->bool:
        if(size%2==1):
            return False
        else:
            return True
    def isCursorRight(self,x1,x2,y1,y2):
        if y1>x2:
            return 1
        if x1>y2:
            return -1
        return 0
    def ansValue(self,x1,x2,y1,y2,even)->float:
        #print("ansvalue",x1,x2,y1,y2,even)
        if even:
            ans=float((max(x1,y1)+min(x2,y2))/2)
        else:
            ans=float(max(x1,y1))
        return ans