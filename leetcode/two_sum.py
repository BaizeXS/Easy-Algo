def two_sum_brute_force(nums: list[int], target: int):
    """方法一：暴力枚举"""
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]
    return []


def two_sum_hash_table(nums: list[int], target: int) -> list[int]:
    """方法二：辅助哈希表法"""
    hash_map = {}
    for i in range(len(nums)):
        if target - nums[i] in hash_map:
            return [hash_map[target - nums[i]], i]
        hash_map[nums[i]] = i
    return []


if __name__ == '__main__':
    num = [3, 2, 4]
    print(two_sum_hash_table(num, 6))
