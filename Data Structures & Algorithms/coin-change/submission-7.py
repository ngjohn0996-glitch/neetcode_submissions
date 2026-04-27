class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #tabulation-solution
        new_table = [float("inf")] * (amount+1)   #amount-coin table
        new_table[0] = 0

        #1)start_new_table index=1/amount_01(imagine amount_last)
        for curr_amount in range(1, amount+1):
            
            #2)find curr_node
            #2.1)loop through coin
            for coin in coins:
                #2.2)find previous_amount's coin + 1(curr_coin) 
                previous_amount = curr_amount - coin 
                if previous_amount >=0:
                    new_table[curr_amount] = min(new_table[curr_amount], new_table[previous_amount] + 1)

        return new_table[amount] if new_table[amount] != float("inf") else -1