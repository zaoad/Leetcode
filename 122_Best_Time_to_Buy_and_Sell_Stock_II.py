class Solution:
    def maxProfit(self, prices: List[int]) -> int:            
        ans = 0
        l= len(prices)
        min = prices[0]
        max = prices[0]
        for k, v in enumerate(prices):
            if v<min:
                min = v
            if v>max:
                max = v
            if k == l-1:
                ans += max-min
                break;
            if v>prices[k+1]:
                ans += max - min
                max= prices[k+1]
                min = prices[k+1]
                
        return ans
