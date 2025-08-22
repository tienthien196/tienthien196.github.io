### ***NOTE***
> ***TÀI LIỆU BUILD BY @TIẾN THIỆN*** [(truy cập chi tiết)](https://tienthien196.github.io/ecosys.portfolioBNJ/)

>đầu tiên là hiểu về OSI model

> giao thức là gì /ko nhầm với API :
> - nó là các quy tắc chung đặt ra cho máy tính để chia sẽ data
> - giao thức là luật chia sẽ dữ liệu

> tại sao phải phân tầng OSI
> - thực ra thì có thể làm 
> - nhưng nếu làm vậy thì 
  - đòi hỏi chrome phải biết viết code  IP , TCP, MAC, driver 
  - làm khó debug tìm lỗi , kém linh hoạt 

> tại sao viết code phải dùng thư viện network
>- Nó giúp gọi các services mạng của  hệ điều hành lấy ra và dùng 

---
tầng 7
    DNS
    tạo ra dữ liệu n từ gói tin , 
    giao thức  đặt quy tắt -> add header 

tầng 6: 
    mã hoá __package__ , cer , bảo mật , nén gói tin 

tầng 5: 
    session, token , cookie

tầng 4 : 
    giao thức đáng tin cậy , port 

tầng 3 :
    add IP

tầng 2  :
    add MAC 
    đóng gói __package__

tầng 1 : 
    truyền bit qua CAP (sóng, ánh sáng )


