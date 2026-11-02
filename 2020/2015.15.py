from collections import defaultdict

nums = [0,3,6]

hash = defaultdict(int)
for num in nums:
    hash[num] += 1

while len(nums) < 2020:
    l = nums[-1]
    if hash[l] > 1: #spoken before
        last = len(nums)-1
        for i in range(last-1, -1, -1):
            if nums[i] == l:
                seclast = i
                break
        nums.append(last-seclast)
        hash[last-seclast] += 1
    else:
        hash[0] += 1
        nums.append(0)

    if len(nums)%10000 == 0:
        print(len(nums))

print(nums[2020-1])
print(nums)



