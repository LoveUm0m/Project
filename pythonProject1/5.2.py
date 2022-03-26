
#1
def odd_nums(max_value):
    n=1
    while n <= max_value:
        yield n
        n +=2
odd_to_15=odd_nums(15)

#2
max_val = 3
odd_nums_gen = (n for n in range(1, max_val +1,2))
print(next(odd_nums_gen))

#3
-