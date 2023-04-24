# You need to find and display all indices of non-unique (duplicate) values in tuple.
# Display the result as a string of numbers separated by spaces.

nums = (5, 4, -3, 2, 4, 5, 10, 11)

print(*tuple(i for i, v in enumerate(nums) if nums.count(v) > 1))
