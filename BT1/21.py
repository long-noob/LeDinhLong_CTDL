def countsort(A):#Định nghĩa một hàm countsort nhận một mảng A là đối số.
    n = len(A)#Tính độ dài của mảng A và lưu vào biến n
    maxsize = max(A)#Tìm giá trị lớn nhất trong mảng A và lưu vào biến maxsize. Đây sẽ là kích thước của mảng đếm.
    carray = [0] * (maxsize + 1)#Tạo một mảng đếm carray có kích thước là maxsize + 1 và các phần tử được khởi tạo bằng 0.
    for i in range(n):#Duyệt qua mỗi phần tử A[i] trong mảng A.
        carray[A[i]] = carray[A[i]] + 1#ăng giá trị của carray tại vị trí A[i] lên 1. Điều này đếm số lần xuất hiện của mỗi phần tử trong mảng A.
    i = 0
    j = 0
    while i < maxsize + 1:#Lặp cho đến khi i vượt qua giá trị lớn nhất của mảng.
        if carray[i] > 0:#Kiểm tra xem phần tử i có xuất hiện trong mảng không.
            A[j] = i#Đưa giá trị i vào mảng A tại vị trí j
            j = j + 1#Tăng chỉ số j lên 1 để chuẩn bị cho phần tử tiếp theo.
            carray[i] = carray[i] - 1#Giảm giá trị của carray[i] đi 1 vì chúng ta đã sử dụng một phần tử i.
        else:#Nếu carray[i] bằng 0, tức là không có phần tử i nào trong mảng, thì tăng i lên 1 để kiểm tra phần tử tiếp theo.
            i = i + 1

A = [3, 5, 8, 9, 6, 2, 3, 5, 5, 5]
print('Original array:', A)#In ra mảng ban đầu.
countsort(A)#Gọi hàm countsort để sắp xếp mảng A.
print('Sorted array:', A)# In ra mảng đã được sắp xếp.