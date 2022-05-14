import math
class Solution:
    def reverse(self, x: int) -> int:
        positive=True
        if(x<0):
            positive=False
        minInt=-math.pow(2,31)
        maxInt=-1*minInt-1
        val=0
        mul=1
        while(x!=0):
            mod=x% 10
            x=int(x/10)
            #print('mod',x, mod)
            if positive:
                if int((maxInt-mod)/10)<val:
                    return 0
                else:
                    val=val*10+mod
            else:
                #print('x',x,(minInt-mod+10)/10,val)
                if int((minInt-mod+10)/10)>val:
                    return 0
                else:
                    val=val*10+mod
                    if mod!=0:
                        val=val-10
                #print('final val',val)
        return val