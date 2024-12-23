def find_closest_to_zero(arr):
    
    arr.sort()
    n = len(arr)
    left = 0
    right = n - 1
    closest_sum = float('inf')
    closest_pair = (arr[left], arr[right])

    while left < right:
        current_sum = arr[left] + arr[right]
        

        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            closest_pair = (arr[left], arr[right])
        
        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return closest_pair

arr1 = [15, 5, -20, 30, -45]
arr2 = [15, 5, -20, 30, 25]

print(find_closest_to_zero(arr1))  
print(find_closest_to_zero(arr2))  
