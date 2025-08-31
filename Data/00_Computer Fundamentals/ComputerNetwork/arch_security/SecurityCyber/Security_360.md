# BLoger kể chuyện về An ninh 360  
    hay còn gọi là chiến lược an ninh 
![image](../../Resource/resources_security/360_of_security.jpg)


> Thiết kế trung tâm điều hành an ninh (SOC) 

> Xây dựng lộ trình cải tiến an ninh theo từng lớp.

1. **"Bảo vệ tổ chức từ nhiều góc độ khác nhau"**
    - Không chỉ tập trung vào một điểm (ví dụ: Tường lửa), mà phủ sóng khắp các cạnh của hoạt động công nghệ và kinh doanh.
    - Trong thế giới số hiện nay, mối đe dọa đến mọi nơi : **mạng internet, thiết bị di động, ứng dụng, dữ liệu, nhân viên, hệ thống máy chủ, vv**
    - >Vì vậy, bảo vệ từ nhiều góc độ nghĩa là:
        - Có nhiều lớp phòng thủ (phòng thủ theo chiều sâu).
        - Mỗi lớp xử lý một loại mối đe dọa cụ thể.
        - Nếu một lớp thất bại, các lớp khác vẫn có thể ngăn chặn 

2. **Bảo mật dữ liệu**
    - Mục tiêu : Đảm bảo dữ liệu được bảo vệ khi lưu trữ và truyền tải.
    - Biện pháp :
        - Mã hóa dữ liệu : Mã hóa dữ liệu để ngăn chặn rò rỉ.
        - Ngăn chặn rò rỉ dữ liệu (DLP) : Ngăn chặn rò rỉ dữ liệu nhạy cảm.

3. **An ninh hạ tầng (Bảo mật hạ tầng)**
    - Mục tiêu : Bảo vệ IT hỗ trợ hoạt động nền tảng dịch vụ.
    - Biện pháp :
        - Bảo mật DNS : Phòng chống tấn công giả mạo DNS (ví dụ: giả mạo DNS).
        - Mail Security : Bảo vệ email khỏi virus, lừa đảo, spam.
        - Truyền thông hợp nhất : Bảo mật các kênh giao tiếp như video call, chat.
        - Quản lý sự kiện và thông tin bảo mật (SIEM) : Thu thập và phân tích - sự kiện an ninh.
        - Phân tích dương tính sai và nhật ký : Phân tích nhật ký để phát hiện - hành động bất ngờ.
        - Theo dõi lỗ hổng Zero Day : Theo dõi các ổ lỗi chưa có bản vá.
    > ✅ Tầm quan trọng : Hạ tầng là xương tồn tại của hệ thống IT, nếu bị tấn công sẽ ảnh hưởng toàn bộ. 

4. **Bảo mật hệ thống (Bảo mật hệ thống)**
    - Mục tiêu : Bảo vệ máy chủ và hệ điều hành.
    - Biện pháp :
        - Bảo mật máy chủ Windows/Linux : Cấu hình toàn bộ cho hệ điều hành máy chủ.
        - Vulnerability/Patch Management : Quản lý và vá hệ thống lỗi.
        - Tự động quét lỗ hổng : Tự động quét ổ khóa bất kỳ.

5. **Bảo mật ứng dụng**
    - Mục tiêu : Đảm bảo các ứng dụng (web, di động, phần mềm) không có lỗi.
    - Biện pháp :
        - Bảo mật ứng dụng web : Bảo vệ ứng dụng web.
        OWASP Top 10 & SANS CWE Top 25 : Tuân thủ danh sách các ổ phổ biến.
        Giám sát hoạt động cơ sở dữ liệu : Giám sát hoạt động trên cơ sở dữ liệu.
        - Bảo mật nội dung : Kiểm soát nội dung được truyền tải.
        - Truyền file an toàn : Truyền file an toàn (SSL/TLS, SFTP...).
        - Tường lửa ứng dụng web (WAF) : Lọc yêu cầu HTTP/HTTPS.
        - Thực hành mã hóa an toàn : Viết mã an toàn ngay từ đầu.
        - Kiểm tra xác thực lỗ hổng : Kiểm tra xác thực lỗ hổng.
        - Kiểm tra thâm nhập ứng dụng : Kiểm tra thử xâm nhập ứng dụng.
        - Secure Code Review : Xem xét mã nguồn để phát hiện lỗi bảo mật.
    >✅ Tầm quan trọng : Ứng dụng là cửa ngõ chính mà hacker thường tấn công. 

6. **Mobile Security**
    - Mục tiêu : Bảo vệ thiết bị di động (điện thoại, máy tính bảng) và dữ liệu trên đó.
    - Biện pháp :
        - Authentication & On-Boarding : Xác thực người dùng và đăng ký thiết bị.
        - Phát hiện điểm truy cập giả mạo : Phát hiện điểm truy cập giả mạo.
        - Giao thức bảo mật không dây : Sử dụng WPA3, TLS...
        - OWASP Mobile App Top 10 : Tuân thủ các ổ phổ biến trên ứng dụng di động.
        - Quét tự động ứng dụng di động : Quét tự động ứng dụng.
        - Dynamic Mobile App Analysis : Phân tích ứng dụng đang chạy.
        - Thực hành mã hóa an toàn : Viết mã an toàn cho ứng dụng di động.
        - Kiểm tra thâm nhập thiết bị di động : Kiểm tra xâm nhập thiết bị di động.
        - Đánh giá mã an toàn : Kiểm tra mã nguồn ứng dụng di động.
    > ✅ Tầm quan trọng : Ngày càng nhiều dữ liệu được truy cập qua thiết bị di động. 

7. **Bảo vệ mối đe dọa nâng cao**
    - Mục tiêu : Phát hiện và phản ứng với các mối đe dọa phức tạp, tinh vi.
    - Biện pháp :
        - Botnet Protection : chặn thiết bị nhiễm độc botnet.
        - Phân tích phần mềm độc hại & Giải pháp chống phần mềm độc hại : Phân tích mã độc và phòng chống.
        - Sandboxing and Emulation : Chạy mã độc trong môi trường cách ly để nghiên cứu.
        - Danh sách trắng ứng dụng : Chỉ cho phép chạy các ứng dụng được phê duyệt.
        - Network Forensics : Phân tích lưu lượng mạng để truy tìm vết tấn công.
        - Automated Security Analytics : Phân tích dữ liệu an ninh tự động để phát hiện hành động bất ngờ.
    >✅ Tầm quan trọng : Đối phó với mối đe dọa tinh vi như APT (Mối đe dọa dai dẳng nâng cao). 

8. **Quản trị rủi ro & Tuân thủ **
    > Mục tiêu : Bảo đảm tổ chức thủ công các quy định pháp lý và chuẩn mực an ninh.
     - Biện pháp :
        - ISO 27001 / HIPAA / PCI / SOC : Tuân thủ các tiêu chuẩn quốc tế.
        - Quản lý và tuân thủ tường lửa : Đảm bảo tường lửa được cấu hình đúng.
        - Nhận xét vật lý và logic : Kiểm tra vật lý và kỹ thuật số.
        - Tuân thủ cấu hình : Đảm bảo cấu hình chuẩn hệ thống.
        - Phân tích Kiểm toán và Tuân thủ : Kiểm tra
    > ✅ Tầm quan trọng : Giúp tránh phạt nặng, mất uy tín và bảo vệ dữ liệu khách hàng. 