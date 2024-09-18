import math
"""
In the change making problem we have certain types of coins called denomination e.g 19¢
12¢,5¢,1¢
Using as many as each denomination we want to make it to a certain target value, say 16¢ using the least amount of given coins above

We can make some certain assumptions to formalize this problem the only way to guarantee we can always reach the target is if one of 
the denominations is 1¢

so to get the target we will have 

                      19¢     12¢       5¢     1¢

          16¢  =      NA   +  NA  +    5¢ 5¢  + 1¢
                                        5¢

a total of four coins if we use the 5 cents coin and the 1 cent coin

Breaking Down:

F(i,t) = Minimum # of coins needed to make 
          t¢ with
        d0, d1 ..... di



        
f(i,t) summary:
Formula: ( f(i, t) )
Definition: Represents the minimum number of coins needed to make ( t ) cents 
using the ( i+1 ) lowest value denominations ( d_0 ) through ( d_i )

which can be solved using two steps:

1. Using the highest denominations:

    ( f(i, t) = 1 + f(i, t - d_i) )

    in the above instance using 12¢ coin:-
    - In these case we still have the same denominations(coins) available to us
    - But Our new target value (t) will reduce by the highest denomination value to 4¢

2. Skipping the highest denomination:
    
    ( f(i, t) = f(i-1, t) )

    So we don't use the coin with the highest denomination that in this instance 12¢
    - This reduces the value i(denominations) by one but the target(t) stays the same


From the above two steps we would go with the step that will utilise the least amount of coins
"""
#Python solution
# use memoization

def change_making(denominations, target):
    cache = {}

    def subproblem(i, t):
        if (i,t) in cache: return cache[(i,t)] #memoization
        #compute the lowest number of coins we need if choosing to take a coin
        #of the current denomination
        val = denominations[i]
        if val > t:
            #current denomination is too large
            choice_take = math.inf
        elif val == t:
            #target reached
            choice_take = 1
        else:
            #take and recurse
            choice_take = 1 + subproblem(i, t - val)

        #compute the lowest number of coins we need if not taking any more 
        # coins of the current denomination.
        if i == 0:
            #not an option if no more denominations
            choice_leave = math.inf
        else:
            #recursive with the remaining denominations
            choice_leave = subproblem(i-1, t)

        optimal = min(choice_take, choice_leave)
        cache[(i,t)] = optimal
        return optimal
    return subproblem(len(denominations) - 1, target)


if __name__ == '__main__':
    print(
        'change_making([1,5,12,19], 16) = '
        f'{change_making([1,5,12,19], 400)}'
    )

