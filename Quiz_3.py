score = [90, 45, 64, 9, 17, 29]
results =[]
for i in score:
    if i >= 71:
        results.append('A')
    elif i >= 41:
        results.append('B')
    elif i >= 11:
        results.append('C')
    else:
        results.append('D')
print(results)
