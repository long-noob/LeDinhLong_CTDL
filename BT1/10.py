def shellsort(A):#Định nghĩa một hàm shellsort nhận một mảng A là đối số.
    n = len(A)#Tính độ dài của mảng A và lưu vào biến n.
    gap = n // 2#Khởi tạo khoảng cách ban đầu bằng nửa độ dài của mảng. Khoảng cách này được sử dụng để chia mảng thành các phần nhỏ hơn để sắp xếp.
    while gap > 0:#Bắt đầu vòng lặp chính, với điều kiện rằng khoảng cách vẫn lớn hơn 0.
        i = gap#Khởi tạo biến i bằng giá trị khoảng cách.
        while i < n:# Duyệt qua mảng từ i đến n-1.
            temp = A[i]#Lưu giá trị của A[i] vào biến temp.
            j = i - gap#Khởi tạo biến j bằng i - gap.
            while j >= 0 and A[j] > temp:#Duyệt ngược từ j đến 0 và kiểm tra xem A[j] có lớn hơn temp hay không.
                A[j + gap] = A[j]
                j = j - gap #Giảm j đi khoảng cách.
            A[j + gap] = temp# Đưa temp vào vị trí đúng.
            i = i + 1#Tăng i để duyệt tiếp.
        gap = gap // 2#Giảm khoảng cách đi nửa.


A = [3, 5, 8, 9, 6, 2]
print('Original Array:', A)
shellsort(A)#Gọi hàm shellsort để sắp xếp mảng A.
print('Sorted Array:', A)

