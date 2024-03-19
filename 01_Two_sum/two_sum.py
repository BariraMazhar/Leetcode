def two_num(self, nums, target):
    lookup={}
    for index,value in enumerate(nums):
        if (target-value) in lookup:
            return(lookup[target-value],index)
        lookup[value]=index