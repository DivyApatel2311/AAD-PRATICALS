def compare_chefs(a, b):
    chef1_points = 0
    chef2_points = 0

    for i in range(3):
        if a[i] > b[i]:
            chef1_points += 1
        elif a[i] < b[i]:
            chef2_points += 1
    
    return chef1_points, chef2_points


a = [27, 48, 70]
b = [89, 26, 7]

result = compare_chefs(a, b)
print(result) 
