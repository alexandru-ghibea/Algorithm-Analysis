
# Problem

# Given an integer array, output all the ** unique ** pairs that sum up to a specific value k.

# So the input:

# pair_sum([1,3,2,2],4)

# would return 2 pairs:

#  (1,3)
#  (2,2)

def pair_sum(arr,k):
    if len(arr) < 2:
        return
    seen = set()
    output = set()
    
    for number in arr:
        target = k - number
        
        if target not in seen:
            seen.add(number)
        else:
            output.add( ((min(number, target)), max(number,target)))
    return len(output)
