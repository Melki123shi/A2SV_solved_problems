def countSwaps(a):
    # Write your code here
    count = 0
    for j in range(len(a)):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                count +=1
    return count
