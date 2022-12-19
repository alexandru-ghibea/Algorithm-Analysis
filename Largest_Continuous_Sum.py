# Given an array of integers (positive and negative) find the largest continuous sum.


def large_cont_sum(arr):
    new_arr = iter(arr)
    suma = 0
    sums=[]
    while True:
        if len(arr) > 2:
            try:
                for item in arr:
                    suma += next(new_arr)
                    if suma >=0:
                        sums.append(suma)
            except StopIteration:
                return (max(sums))
                break
        else:
            return (max(arr))
            break
