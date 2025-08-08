# Computer Network: A Comprehensive Guide

> Tài liệu này được xây dựng để cung cấp một cái nhìn toàn diện về Mạng Máy tính, từ các khái niệm cơ bản đến các kỹ thuật nâng cao, phục vụ mục đích lưu trữ và tham khảo cho các dự án IT. Tài liệu được thiết kế để hỗ trợ cả người mới bắt đầu và những người có kinh nghiệm muốn hệ thống hóa kiến thức.

---

## Mục Lục

- [Giới thiệu về Computer Network](#giới-thiệu-về-computer-network)
- [Các khái niệm cơ bản](#các-khái-niệm-cơ-bản)
  - [Mô hình OSI](#mô-hình-osi)
  - [Mô hình TCP/IP](#mô-hình-tcp-ip)
  - [Các loại mạng](#các-loại-mạng)
- [Các giao thức mạng chính](#các-giao-thức-mạng-chính)
  - [Giao thức tầng ứng dụng](#giao-thức-tầng-ứng-dụng)
  - [Giao thức tầng giao vận](#giao-thức-tầng-giao-vận)
  - [Giao thức tầng mạng](#giao-thức-tầng-mạng)
  - [Giao thức tầng liên kết dữ liệu](#giao-thức-tầng-liên-kết-dữ-liệu)
- [Các thiết bị mạng](#các-thiết-bị-mạng)
  - [Router](#router)
  - [Switch](#switch)
  - [Access Point](#access-point)
  - [Firewall](#firewall)
- [Các kỹ thuật tối ưu hóa mạng](#các-kỹ-thuật-tối-ưu-hóa-mạng)
  - [Load Balancing](#load-balancing)
  - [Quality of Service (QoS)](#quality-of-service-qos)
  - [Network Security](#network-security)
- [Checklist học tập và nghiên cứu](#checklist-học-tập-và-nghiên-cứu)
- [Công cụ đề xuất](#công-cụ-đề-xuất)
- [Kinh nghiệm thực hành](#kinh-nghiệm-thực-hành)
- [Tài liệu tham khảo](#tài-liệu-tham-khảo)

---

## Giới thiệu về Computer Network

Mạng máy tính là tập hợp các thiết bị được kết nối với nhau để chia sẻ tài nguyên, trao đổi dữ liệu và cung cấp các dịch vụ. Mạng máy tính đóng vai trò quan trọng trong mọi lĩnh vực từ giao tiếp cá nhân, doanh nghiệp, đến các ứng dụng công nghệ cao như trí tuệ nhân tạo và blockchain.

- **Tầm quan trọng**:
  - Kết nối toàn cầu thông qua Internet.
  - Hỗ trợ các ứng dụng thời gian thực như video streaming, VoIP, và game online.
  - Là nền tảng cho các công nghệ hiện đại như cloud computing và IoT.

- **Ứng dụng thực tế**:
  - Xây dựng mạng nội bộ (LAN) cho doanh nghiệp.
  - Triển khai hệ thống cloud (AWS, Azure).
  - Phát triển các ứng dụng phân tán (blockchain, P2P).

---

## Các khái niệm cơ bản

### Mô hình OSI
- **Mô tả**: Mô hình OSI (Open Systems Interconnection) là một khung tham chiếu lý thuyết chia quá trình truyền thông mạng thành 7 tầng (Layers).
- **Các tầng**:
  1. **Physical Layer**: Truyền tín hiệu vật lý (cáp, tín hiệu điện, quang).
  2. **Data Link Layer**: Đảm bảo truyền dữ liệu không lỗi giữa các nút liền kề (MAC address, Ethernet).
  3. **Network Layer**: Định tuyến và chuyển tiếp gói tin (IP address, routing).
  4. **Transport Layer**: Đảm bảo truyền dữ liệu đáng tin cậy (TCP, UDP).
  5. **Session Layer**: Quản lý phiên giao tiếp giữa các ứng dụng.
  6. **Presentation Layer**: Chuyển đổi định dạng dữ liệu (mã hóa, nén).
  7. **Application Layer**: Giao diện cho người dùng (HTTP, FTP, DNS).
- **Ưu điểm**: Cung cấp cách tiếp cận chuẩn hóa để thiết kế và phân tích mạng.
- **Ví dụ thực tế**: Phân tích gói tin bằng Wireshark dựa trên các tầng OSI.

### Mô hình TCP/IP
- **Mô tả**: Mô hình TCP/IP là một mô hình thực tiễn, đơn giản hơn OSI, gồm 4 tầng, được sử dụng rộng rãi trong Internet.
- **Các tầng**:
  1. **Link Layer**: Tương ứng với Physical và Data Link Layer của OSI.
  2. **Internet Layer**: Tương ứng với Network Layer (IP).
  3. **Transport Layer**: Tương ứng với Transport Layer (TCP, UDP).
  4. **Application Layer**: Bao gồm Session, Presentation, và Application Layer của OSI.
- **Ưu điểm**: Đơn giản, thực tiễn, là nền tảng của Internet.
- **Ví dụ thực tế**: Giao thức HTTP chạy trên TCP/IP để truy cập website.

### Các loại mạng
- **LAN (Local Area Network)**: Mạng nội bộ, phạm vi nhỏ (văn phòng, nhà ở).
- **WAN (Wide Area Network)**: Mạng diện rộng, kết nối các khu vực địa lý (Internet).
- **MAN (Metropolitan Area Network)**: Mạng đô thị, kết nối trong một thành phố.
- **PAN (Personal Area Network)**: Mạng cá nhân (Bluetooth, USB).
- **VPN (Virtual Private Network)**: Mạng riêng ảo, mã hóa dữ liệu qua Internet.
- **Ví dụ thực tế**:
  - LAN: Mạng Wi-Fi trong nhà.
  - WAN: Kết nối Internet giữa các quốc gia.
  - VPN: Sử dụng OpenVPN để truy cập mạng công ty từ xa.

---

## Các giao thức mạng chính

### Giao thức tầng ứng dụng
- **HTTP/HTTPS**: Giao thức truyền siêu văn bản, sử dụng cho web.
- **DNS**: Chuyển đổi tên miền thành địa chỉ IP.
- **FTP/SFTP**: Truyền tệp tin giữa client và server.
- **SMTP/POP3/IMAP**: Giao thức cho email.
- **Ví dụ thực tế**:
  - Truy cập website qua HTTPS (port 443).
  - Sử dụng DNS để phân giải `google.com` thành `172.217.167.78`.

### Giao thức tầng giao vận
- **TCP (Transmission Control Protocol)**: Đảm bảo truyền dữ liệu đáng tin cậy, có kết nối, kiểm tra lỗi.
- **UDP (User Datagram Protocol)**: Truyền dữ liệu nhanh, không cần kết nối, không đảm bảo lỗi (dùng cho streaming, game).
- **Ví dụ thực tế**:
  - TCP: Tải xuống tệp tin qua FTP.
  - UDP: Truyền video trực tiếp qua Zoom.

### Giao thức tầng mạng
- **IP (Internet Protocol)**: Định tuyến gói tin qua mạng (IPv4, IPv6).
- **ICMP**: Giao thức kiểm tra trạng thái mạng (dùng cho `ping`).
- **ARP**: Ánh xạ địa chỉ IP sang địa chỉ MAC.
- **Ví dụ thực tế**:
  - IPv4: `192.168.1.1` cho mạng nội bộ.
  - ICMP: Sử dụng lệnh `ping` để kiểm tra kết nối.

### Giao thức tầng liên kết dữ liệu
- **Ethernet**: Giao thức phổ biến cho mạng LAN.
- **PPP (Point-to-Point Protocol)**: Kết nối trực tiếp giữa hai nút.
- **Wi-Fi (IEEE 802.11)**: Giao thức cho mạng không dây.
- **Ví dụ thực tế**:
  - Ethernet: Kết nối máy tính qua cáp RJ45.
  - Wi-Fi: Kết nối không dây qua chuẩn 802.11ac/ax.

---

## Các thiết bị mạng

### Router
- **Mô tả**: Chuyển tiếp gói tin giữa các mạng khác nhau, hoạt động ở tầng mạng.
- **Chức năng**: Định tuyến, NAT (Network Address Translation), DHCP.
- **Ví dụ thực tế**: Router Wi-Fi TP-Link Archer cung cấp kết nối Internet cho mạng gia đình.

### Switch
- **Mô tả**: Kết nối các thiết bị trong cùng một mạng, hoạt động ở tầng liên kết dữ liệu.
- **Chức năng**: Chuyển tiếp khung dữ liệu (frame) dựa trên địa chỉ MAC.
- **Ví dụ thực tế**: Switch Cisco Catalyst cho mạng doanh nghiệp.

### Access Point
- **Mô tả**: Thiết bị cung cấp kết nối Wi-Fi cho các thiết bị.
- **Chức năng**: Kết nối không dây, mở rộng phạm vi mạng.
- **Ví dụ thực tế**: Ubiquiti UniFi AP cho mạng Wi-Fi doanh nghiệp.

### Firewall
- **Mô tả**: Thiết bị bảo mật, kiểm soát lưu lượng mạng dựa trên quy tắc.
- **Chức năng**: Ngăn chặn truy cập trái phép, bảo vệ mạng khỏi tấn công.
- **Ví dụ thực tế**: pfSense, Fortinet Firewall cho mạng doanh nghiệp.

---

## Các kỹ thuật tối ưu hóa mạng

### Load Balancing
- **Mô tả**: Phân phối lưu lượng mạng đều trên nhiều server để tăng hiệu suất và độ tin cậy.
- **Các kỹ thuật**:
  - Round-robin: Phân phối tuần tự.
  - Least connections: Gửi lưu lượng đến server ít kết nối nhất.
- **Ví dụ thực tế**: Sử dụng NGINX làm load balancer cho web server.

### Quality of Service (QoS)
- **Mô tả**: Quản lý và ưu tiên lưu lượng mạng để đảm bảo hiệu suất cho các ứng dụng quan trọng.
- **Các kỹ thuật**:
  - Traffic shaping: Giới hạn băng thông cho một số ứng dụng.
  - Packet prioritization: Ưu tiên gói tin VoIP hoặc video.
- **Ví dụ thực tế**: QoS trên router để ưu tiên băng thông cho Zoom.

### Network Security
- **Mô tả**: Bảo vệ mạng khỏi các mối đe dọa như tấn công DDoS, malware, hoặc truy cập trái phép.
- **Các kỹ thuật**:
  - Mã hóa: Sử dụng HTTPS, VPN.
  - Authentication: Sử dụng giao thức như RADIUS, LDAP.
  - IDS/IPS (Intrusion Detection/Prevention System): Phát hiện và ngăn chặn tấn công.
- **Ví dụ thực tế**: Sử dụng Wireshark để phát hiện lưu lượng đáng nghi.

---

## Checklist học tập và nghiên cứu

- [ ] Hiểu rõ mô hình OSI và TCP/IP, so sánh sự khác biệt.
- [ ] Nắm vững các giao thức chính: HTTP, TCP, IP, DNS, Ethernet.
- [ ] Tìm hiểu các loại mạng: LAN, WAN, VPN, PAN.
- [ ] Thực hành phân tích gói tin bằng Wireshark.
- [ ] Thiết lập một mạng LAN đơn giản với router và switch.
- [ ] Tìm hiểu về bảo mật mạng: Firewall, VPN, IDS/IPS.
- [ ] Đọc sách *Computer Networking: A Top-Down Approach* của Kurose & Ross.
- [ ] Thực hành cấu hình router và switch bằng Cisco Packet Tracer.
- [ ] Tìm hiểu về IPv6 và cách chuyển đổi từ IPv4.
- [ ] Nghiên cứu các công nghệ mạng hiện đại như SDN (Software-Defined Networking).

---

## Công cụ đề xuất

- **Wireshark**: Phân tích gói tin mạng, hỗ trợ debug và bảo mật.
- **Cisco Packet Tracer**: Mô phỏng mạng, lý tưởng cho học tập và thử nghiệm.
- **GNS3**: Mô phỏng mạng phức tạp, hỗ trợ thiết bị thực tế.
- **Postman**: Kiểm tra API (HTTP, REST).
- **Nmap**: Quét mạng để phát hiện thiết bị và cổng mở.
- **pfSense**: Phần mềm firewall mã nguồn mở.
- **Mininet**: Mô phỏng mạng SDN.
- **Netcat**: Công cụ linh hoạt để kiểm tra kết nối mạng.

---

## Kinh nghiệm thực hành

1. **Phân tích gói tin**:
   - Sử dụng Wireshark để bắt và phân tích lưu lượng HTTP, DNS, TCP.
   - Tìm hiểu cách xác định các gói tin bất thường hoặc tấn công.

2. **Thiết lập mạng LAN**:
   - Cấu hình router Wi-Fi với DHCP và NAT.
   - Thiết lập VLAN trên switch để tách biệt lưu lượng mạng.

3. **Mô phỏng mạng**:
   - Sử dụng Cisco Packet Tracer để thiết kế một mạng doanh nghiệp nhỏ.
   - Thử nghiệm định tuyến tĩnh và động (RIP, OSPF).

4. **Bảo mật mạng**:
   - Cài đặt pfSense để cấu hình firewall và VPN.
   - Thực hành quét mạng bằng Nmap để tìm lỗ hổng.

5. **Dự án thực tế**:
   - Xây dựng một hệ thống giám sát mạng sử dụng Prometheus và Grafana.
   - Triển khai một VPN server sử dụng OpenVPN.

---

## Tài liệu tham khảo

1. **Sách**:
   - *Computer Networking: A Top-Down Approach* bởi James F. Kurose và Keith W. Ross.
   - *TCP/IP Illustrated, Volume 1: The Protocols* bởi W. Richard Stevens.
   - *Network Security Essentials* bởi William Stallings.
2. **Khóa học trực tuyến**:
   - Coursera: *Introduction to Computer Networking* bởi Stanford University.
   - Udemy: *Cisco CCNA 200-301 Complete Course*.
3. **Website**:
   - Cisco Networking Academy: https://www.netacad.com/
   - Wireshark Documentation: https://www.wireshark.org/docs/
   - IETF (Internet Engineering Task Force): https://www.ietf.org/
4. **Tài nguyên cộng đồng**:
   - Stack Overflow: Câu hỏi và trả lời về mạng máy tính.
   - Reddit: r/networking, r/sysadmin.

---

> **Lưu ý**: Tài liệu này sẽ được cập nhật liên tục để bổ sung các khái niệm mới, công cụ, và kinh nghiệm thực tế. Nếu bạn có đề xuất hoặc cần thêm chi tiết, hãy liên hệ với **@author**!