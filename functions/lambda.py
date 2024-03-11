# Single time unnamed function

square = lambda num: num ** 2

print(square(3))

my_nums = [1, 2, 3, 4, 5, 7, 12, 13, 43, 544]

nums_mapped = map(lambda num:num**2, my_nums)

nums_even = filter(lambda num:num%2 == 0, my_nums)

print(list(nums_mapped))
print(list(nums_even))