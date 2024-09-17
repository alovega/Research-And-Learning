'''
    We have a flower box with few places to plant flowers.
    Each Location has nutrients that ingluence how tall the flower will be.
    You can't plant the flowers next to each other.
    We want to maximise the total height of all the planted flowers
    The greedy approach of picking the most nutrients dense location doesn't always work

    Here we can use dynamic programming to get the maximum height we can use in planting flowers

    f(i) = { f(i-2) + Vi}
    f(i) = {f(i-1)}

    It's just actually the same as the fibonacci sequence
'''
#define a function flowerbox that takes in an array of nutrient values
# We have two variables a, b to store the result from the last two sub problems
# this are initialized
# We should Iterate (we work our way up to f(n-1) ) combining the results of the last to sub problems
def flowerbox(nutrients_values): 
    a = 0 # f(i-1)
    b = 0 # f(i-2)

    for val in nutrients_values:
        a,b = b, max(a + val, b)
        print(f'val = {val}, a = {a},b = {b}')

    return b

if __name__ == '__main__':
    print(f'flowrbox([3,1 0,3,1,2]) = {flowerbox([3,10,3,1,2])}')
    print(f'flowerbox([9,10,9] ) = {flowerbox([9,10,9])}')