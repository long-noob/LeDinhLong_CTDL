def quicksort(A, low, high): #sắp xếp nhanh trên mảng A từ chỉ số low đến chỉ số high.
    if low < high:#đảm bảo rằng mảng cần sắp xếp có ít nhất 2 phần tử. Nếu không, mảng đã được sắp xếp và không cần thực hiện thêm công việc nào.
        pi = partition(A, low, high)#Hàm partition được gọi để chia mảng thành 2 phần và trả về chỉ số của phần tử pivot sau khi đã được đưa về đúng vị trí.
        quicksort(A, low, pi-1)#Đệ quy gọi hàm quicksort trên nửa bên trái của pivot (các phần tử nhỏ hơn pivot).
        quicksort(A,pi+1,high)#Đệ quy gọi hàm quicksort trên nửa bên phải của pivot (các phần tử lớn hơn pivot).

def partition(A, low, high):#thực hiện việc chọn một phần tử pivot từ mảng và đảm bảo rằng các phần tử nhỏ hơn pivot được đặt bên trái và các phần tử lớn hơn được đặt bên phải.
    pivot = A[low]#Phần tử pivot được chọn là phần tử đầu tiên của mảng.
    i = low + 1 #Khởi tạo biến chỉ số i. i sẽ tăng dần từ bên trái.
    j = high ##Khởi tạo biến chỉ số j. j giảm dần từ bên phải.
    while True:#loop
        while i <= j and A[i] <= pivot:#Tìm phần tử lớn hơn hoặc bằng pivot từ bên trái.
            i = i + 1
        while i<= j and A[j] > pivot:#ìm phần tử nhỏ hơn pivot từ bên phải.
            j = j - 1
        if i <= j:# swamp: Nếu i vẫn nhỏ hơn hoặc bằng j, thì hoán đổi A[i] và A[j].
            A[i], A[j] = A[j], A[i]
        else:#Nếu i không còn nhỏ hơn hoặc bằng j, dừng lại.
            break
    A[low], A[j] = A[j], A[low]#đảo vị trí của pivot với A[j] để đưa pivot về đúng vị trí cuối cùng của nó.
    return j#Trả về chỉ số j (chỉ số cuối cùng của pivot).

A = [3, 5, 8, 9, 6, 2]
print('Orriginal array:', A)# In ra mảng ban đầu
quicksort(A, 0, len(A)-1)# Gọi hàm quicksort để sắp xếp mảng A từ vị trí đầu (0) đến vị trí cuối cùng (len(A)-1).
print('Sorted array:', A)#In ra mảng đã được sắp xếp.



    
       

