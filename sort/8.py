def bubblesort(A):#Định nghĩa một hàm bubblesort nhận một mảng A là đối số.
    n = len(A)#Tính độ dài của mảng A và lưu vào biến n.
    for passes in range(n-1,0,-1):#Duyệt qua mảng passes từ n-1 đến 1 (kể từ cuối về đầu, mỗi lần giảm đi 1).
        for i in range(passes):#Duyệt qua mảng i từ 0 đến passes-1.
            if A[i] > A[i+1]:#So sánh hai phần tử liền kề. Nếu A[i] lớn hơn A[i+1], đổi chỗ chúng.
                temp = A[i]#Lưu giá trị của A[i] vào biến tạm thời temp.
                A[i] = A[i+1]# Gán A[i+1] vào A[i].
                A[i+1] = temp#Gán temp vào A[i+1], hoàn thành việc đổi chỗ.

A = [3,5,8,9,6,2]
print('Original Array:',A)#In ra mảng ban đầu.    
bubblesort(A)#Gọi hàm bubblesort để sắp xếp mảng A.
print('Sorted Array:',A)#In ra mảng đã được sắp xếp.  
