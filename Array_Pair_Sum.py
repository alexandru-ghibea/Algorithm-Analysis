

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
