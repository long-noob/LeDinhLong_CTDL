def insertionsort(A):   # hàm sắp xếp kiểu insertionsort
    n= len(A) # gán n là chiều dài của A
    for i in range(1,n): #duyệt từ phần tử thứ 2 đến n-1
        cvalue=A[i]  # biến cvalue lưu giá trị đang xét
        position=i  # gán i là giá trị position
        while position >0 and A[position-1]>cvalue:    # so sánh giá trị cần chèn với các giá trị đứng trước nó
            A[position]=A[position-1] # đổi giá trị cần chèn với giá trị đứng trước nó
            position=position-1 # giảm giá trị position để duyệt tới phần tử trước nó, 
        A[position]=cvalue # đưa giá trị đang xét lúc đầu vào vị trí position nơi cần sắp xếp

A=[3,5,8,9,6,2]
print("Original Array :",A)
insertionsort(A) # sắp xếp kiểu insertionsort
print("Sorted Array:",A)