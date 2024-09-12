def fib(n):
    if n == 0: return 1
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

#memoization algorithm for fibonnaci
"""
memoization: is a technique for speeding up computations by caching results
of repeated calculations
"""
# we wan't to maintain a cache typically represented as a dictionary
#supposed we want to calculate F3 we start by checking for 3 in cache if yes return corresponding value
# If no perform the calculation normally but then store the result in the cache under the key 3 before returning the result
# Now we would not have to to this calculation again. Applying this technique eliminates many of the repeated calculation from the overall computetation
# So when we are computing the result of F4 we would nedd to reso the calculation of F1, F2, F3  so we end up saving time at the expense of space haha!!!

def fib_memoized(n, cache=None):
    if n == 0: return 1
    if n == 1: return 1
    if cache is None: cache = {}
    if n in cache: return cache[n]

    result = fib_memoized(n-1, cache) + fib_memoized(n-2, cache)
    cache[n] = result
    return result

#Dynamic programming bottom up approach
# we will only need to store the result of the last two sub problems
# think of it like this base cases will be FO, F1
# To get F2 we will need FO and F1 so F2 depends on the last two subproblems
# To get F3 we will need F1 and F2 so we can discard FO
# To get F4 we will need F2, and F3 so we can dicard F1 
# and so on and so forth so here we can save on space by only caching or having the result of the last two sub problems
def fib_dynamic(n):
    a = 1
    b = 1

    for i in range(2, n+1):
        a, b = b, a +b
    return b
