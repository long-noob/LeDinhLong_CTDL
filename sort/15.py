def mergesort(A,left,right):#Định nghĩa một hàm mergesort nhận ba đối số: A (danh sách cần sắp xếp), left (chỉ số bên trái của phần tử đầu tiên), và right (chỉ số bên phải của phần tử cuối cùng).
    if left < right:#iểm tra xem có hơn một phần tử trong phần danh sách hiện tại hay không. Nếu không, có nghĩa rằng chỉ còn một phần tử hoặc không có gì để sắp xếp nữa.
        mid = (left+right) // 2#Tính chỉ số mid của array.
        mergesort(A, left, mid)#Gọi đệ quy hàm mergesort với nửa bên trái của danh sách.
        mergesort(A, mid+1, right)#Gọi đệ quy hàm mergesort với nửa bên phải của danh sách.
        merge(A,left, mid, right)#Hàm merge được gọi để kết hợp hai phần đã sắp xếp từ nửa bên trái và nửa bên phải.

def merge(A, left, mid, right):#Hàm merge nhận danh sách A và ba chỉ số left, mid, right để kết hợp các phần đã sắp xếp.
    i = left #Khai báo biến
    j = mid + 1#khai báo biến
    k = left#Khai báo biến
    B = [0] * (right + 1)#Tạo một danh sách tạm thời B với độ dài bằng với danh sách A.      
    while i <= mid and j <= right:#Lặp qua các phần tử của hai nửa danh sách đã sắp xếp.
          if  A[i] < A[j]:#So sánh hai phần tử A[i] và A[j].
               B[k] = A[i]#Gán giá trị nhỏ hơn vào danh sách tạm thời B.
               i = i + 1#Di chuyển chỉ số i tùy thuộc vào phần tử nào đã được sử dụng.
          else:
               B[k]= A[j]#án giá trị nhỏ hơn vào danh sách tạm thời B.
               j = j + 1#Di chuyển chỉ số j tùy thuộc vào phần tử nào đã được sử dụng.
          k = k + 1#Di chuyển chỉ số của danh sách kết quả B.
    while i <= mid:#Đảm bảo rằng tất cả các phần tử từ nửa danh sách còn lại cũng được đưa vào danh sách kết quả.
         B[k] = A[i]
         i = i + 1
         k = k + 1
    while   j <= right:#Đảm bảo rằng tất cả các phần tử từ nửa danh sách còn lại cũng được đưa vào danh sách kết quả.
         B[k] = A[j]
         j = j + 1
         k = k + 1
    for x in range(left, right+1):#Copy danh sách kết quả B vào danh sách ban đầu A.
         A[x] = B[x] 


A = [3,5,8,9,6,2]
print('Orignal Array:' ,A)#In ra danh sách ban đầu.
mergesort(A, 0, len(A)-1)#Gọi hàm mergesort để bắt đầu quá trình sắp xếp.
print('Sorted Array:' ,A)#In ra danh sách đã được sắp xếp.             








