import random

# Given a list of COUNT numbers, each in the range [MIN_VAL, MAX_VAL], print the list
# of triplets whose sum is 0. A triplet is a set of any 3 numbers from this list
# such that a number at a given index occurs at most once in the triplet.
# Each triplet should be printed with both the numbers it contains and the indexes
# of these numbers in the original list.
# The program should also print the number of zero-sum triplets and its percentage from
# the total number of possible triplets.

# Example:
# ---- Numbers ----
# [38, -43, 16, -24, 20, -26, -36, -47, 20, -27]
# ---- Zero-sum triplets ----
# [ 2]:  16        + [ 4]:  20     + [ 6]: -36 = 0   
# [ 2]:  16        + [ 6]: -36     + [ 8]:  20 = 0   
# ---- Zero-sum triplets: 2 = 1.66% of 120.0

COUNT = 10
MIN_VAL = -50
MAX_VAL = 50


def format_triplet(triplet):
    """Format an indexed triplet as a printable line and return its sum.
    Args:
        triplet: List of (index, value) pairs for exactly three numbers.
    Returns:
        A tuple (line, total), where line is the formatted string and total is the sum.
    """
    first = True
    total = 0
    line = ""
    for (i, num) in triplet:
        total += num
        if not first:
            line += "\t + "
        line += f"[{i:2d}]:{num:4d}"
        first = False
    line += f" = {total:<4d}"
    return line, total

def print_triplets(nums):
    """Print all zero-sum triplets from nums and return how many were found.
    Args:
        nums: List of integers to scan.
    Returns:
        The number of printed triplets with sum equal to 0.
    """
    count = len(nums)
    count_triplets = 0
    for i in range(count):
        for j in range(i+1, count):
            for k in range(j+1, count):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = [(i, nums[i]), (j, nums[j]), (k, nums[k])]
                    line, _ = format_triplet(triplet)
                    print(line)
                    count_triplets += 1
    return count_triplets

def count_triplets(nums):
    """Return the number of distinct index triplets that can be formed from nums.
    Args:
        nums: List of values; equal values at different indexes are allowed.
    Returns:
        The combinations count C(n, 3), where n is len(nums).
    """
    n = len(nums)
    return n * (n-1) * (n-2) / 6

if __name__ == "__main__":
    nums = []
    for i in range(COUNT):
        nums.append(random.randint(MIN_VAL, MAX_VAL))

    print("---- Numbers ----")
    print(nums)    
    total_triplets = count_triplets(nums)
    print("---- Zero-sum triplets ----")
    zero_triplets = print_triplets(nums)
    zero_pct = int(zero_triplets / total_triplets * 10000) / 100
    print(f"---- Zero-sum triplets: {zero_triplets} = {zero_pct}% of {total_triplets}")

