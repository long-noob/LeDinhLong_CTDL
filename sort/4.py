def seclectionsort(A):  # cố định danh sách a 
    n= len(A)  # n gán bằng giá trị của A
    for i in range(n-1): # vòng lặp xét từ i đến gần cuối (áp chót)
        position = i                 # gán biến này bằng biến kia 
        for j in range(i+1, n):      # gán j = i+1 và chạy trong khoảng i+1 đến n
            if A[j] < A[position]:   # nếu giá trị j bé hơn position 
                position =j          # gán position bằng j
        temp = A[i]                  # đổi vị trí và tiếp tục xét tiếp 
        A[i] = A[position]
        A[position] = temp

A = [3,5,8,9,6,2]
print('Original Array:', A)
seclectionsort(A)
print('Sorted Array:', A)
