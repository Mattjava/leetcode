import Solution

my_list = [1, 2, 2, 3, 4]

is_monotone = Solution.isMonotonic(my_list)

if is_monotone:
    print(f"My list ({my_list}) is monotonic.")
else:
    print(f"My list ({my_list}) is not monotonic.")