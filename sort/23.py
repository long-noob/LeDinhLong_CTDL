def radixsort(A):#Định nghĩa một hàm radixsort nhận một mảng A là đối số.
    n = len(A)#Tính độ dài của mảng A và lưu vào biến n.
    maxelement = max(A)#Tìm giá trị lớn nhất trong mảng A và lưu vào biến maxelement. Đây sẽ là giới hạn cho số các chữ số cần được xem xét.
    digits = len(str(maxelement))#Tính số lượng các chữ số của số lớn nhất. Điều này sẽ xác định số lần lặp qua các chữ số.
    l = []#Khởi tạo một danh sách rỗng l
    bins = [l] * 10#Khởi tạo một mảng bins với 10 phần tử, mỗi phần tử đều trỏ đến cùng một danh sách rỗng l.
    for i in range(digits):#Vòng lặp chạy qua từng chữ số (từ hàng đơn vị đến hàng cao hơn).
        for j in range(n):#Duyệt qua mỗi phần tử A[j] trong mảng A.
            e = int((A[j] / pow(10, i)) % 10)#Tính chữ số thứ i của A[j]. pow(10, i) đại diện cho 10 mũ i và (A[j] / pow(10, i)) % 10 lấy ra chữ số tương ứng.
            if len(bins[e]) > 0:#Xem xét danh sách tại e đã được tạo hay chưa.
                bins[e].append(A[j])#Nếu đã có danh sách, thêm A[j] vào danh sách đó.
            else:#Nếu danh sách chưa được tạo, tạo một danh sách mới chứa A[j] và gán vào bins[e].
                bins[e] = [A[j]]
        k = 0#Khởi tạo biến k để theo dõi chỉ số trong mảng A.
        for x in range(10):#Duyệt qua các bin từ 0 đến 9.
            if len(bins[x]) > 0:# Kiểm tra xem bin x có phần tử hay không.
                for y in range(len(bins[x])):#Gán phần tử đầu tiên của bin vào A[k] và loại bỏ nó khỏi bin.
                    A[k] = bins[x].pop(0)
                    k = k + 1#Tăng k để chuẩn bị cho phần tử tiếp theo.
                    
A = [63, 250, 835, 947, 651, 28]
print('original array:', A)#In ra mảng ban đầu.
radixsort(A)#Gọi hàm radixsort để sắp xếp mảng A.
print('Sorted array:', A)#In ra mảng đã được sắp xếp.





