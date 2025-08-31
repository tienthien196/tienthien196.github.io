# Computer Network

## Map

```
+-------------------------------------------------------------+
|                       LAYER 7: Application                  |
|   [User] Gõ: https://google.com                             |
|   → HTTP Request: "GET / HTTP/1.1"                          |
|   → Dữ liệu bắt đầu từ đây                                  |
+-------------------------------------------------------------+
                             ↓
+-------------------------------------------------------------+
|                     LAYER 6: Presentation                   |
|   → Mã hóa dữ liệu (TLS/SSL):                               |
|      - HTTP → HTTPS (mã hóa bằng AES)                       |
|      - Dữ liệu trở thành: [Encrypted Blob]                  |
+-------------------------------------------------------------+
                             ↓
+-------------------------------------------------------------+
|                       LAYER 5: Session                      |
|   → Thiết lập phiên làm việc (session)                      |
|   → Nếu dùng WebSocket, gRPC, hay WireGuard: tạo session ID |
+-------------------------------------------------------------+
                             ↓
+-------------------------------------------------------------+
|                      LAYER 4: Transport                     |
|   → Chia nhỏ dữ liệu thành segment                          |
|   → Gắn port:                                               |
|        - Source Port: 54321 (ngẫu nhiên)                    |
|        - Dest Port: 443 (HTTPS)                             |
|   → Giao thức: TCP (hoặc UDP nếu dùng DNS, WireGuard)       |
+-------------------------------------------------------------+
                             ↓
+-------------------------------------------------------------+
|                       LAYER 3: Network                      |
|   → Gắn địa chỉ IP:                                         |
|        - Source IP: 192.168.1.10 (IP nội bộ)                |
|        - Dest IP: ??? → Cần DNS để biết!                    |
+-------------------------------------------------------------+
                             ↓
+-------------------------------------------------------------+
|                      LAYER 2: Data Link                     |
|   → Gắn MAC Address:                                        |
|        - Source MAC: aa:bb:cc:dd:ee:ff                      |
|        - Dest MAC: MAC của router (gateway)                 |
|   → Frame: [MAC][IP][TCP][Data]                             |
+-------------------------------------------------------------+
                             ↓
+-------------------------------------------------------------+
|                      LAYER 1: Physical                      |
|   → Chuyển thành tín hiệu: Wi-Fi, Ethernet, 4G              |
|   → Gửi đến router                                          |
+-------------------------------------------------------------+
                             ↓
                       [ROUTER]
                             ↓
+-------------------------------------------------------------+
|                         NAT & FIREWALL                      |
|   → NAT: Đổi IP nội bộ → IP công cộng                       |
|        192.168.1.10:54321 → 103.123.45.67:54321             |
|   → Firewall: Kiểm tra xem có cho phép kết nối ra không     |
+-------------------------------------------------------------+
                             ↓
                        [ISP NETWORK]
                             ↓
+-------------------------------------------------------------+
|                           DNS QUERY                         |
|   → Client gửi: "google.com?"                               |
|   → ISP DNS Server trả về: 142.250.180.78                   |
|   ⚠️ Nếu bị chặn: ISP không trả lời hoặc trả IP sai          |
|   ✅ Nếu dùng DoH: Gửi qua HTTPS đến 1.1.1.1                |
+-------------------------------------------------------------+
                             ↓
                     [INTERNET BACKBONE]
                             ↓
+-------------------------------------------------------------+
|                      TÙY THUỘC: Proxy hay VPN?              |
+-------------------------------------------------------------+

        ┌───────────────────────┐
        │       CASE 1: PROXY   │
        └───────────────────────┘

[Client] → Gửi đến Proxy: "CONNECT 142.250.180.78:443"
   ↓
[ISP] → Thấy: kết nối đến IP proxy (ví dụ: 203.0.113.5:8080)
   ↓
[PROXY SERVER] → Giải mã (nếu dùng HTTPS proxy)
                → Kết nối đến google.com:443
                → Gửi dữ liệu qua Internet
   ↓
[GOOGLE SERVER] ← Nhận yêu cầu như thể từ proxy
   ↓
[PROXY] ← Nhận phản hồi → gửi về client
   ↓
[Client] ← Nhận dữ liệu

🔹 Ai thấy gì?
- ISP: Thấy bạn dùng proxy, không thấy nội dung (nếu mã hóa)
- Proxy: Thấy toàn bộ dữ liệu (có thể log, chèn quảng cáo)
- Google: Thấy IP của proxy, không thấy IP thật bạn

─────────────────────────────────────────────────────────────

        ┌───────────────────────┐
        │       CASE 2: VPN     │
        └───────────────────────┘

[Client] → Gửi đến Server VPN: [UDP][Encrypted IP Packet]
         → Trong đó: "ping 142.250.180.78:443"
   ↓
[ISP] → Thấy: UDP packet đến IP_VPN:51820
      → Payload: dữ liệu ngẫu nhiên (do mã hóa)
      → Không biết nội dung, không thấy DNS
   ↓
[SERVER VPN] → Giải mã bằng WireGuard
             → Lấy ra IP packet gốc
             → Gửi ra Internet: "Từ tôi (IP_VPN) → google.com"
   ↓
[GOOGLE SERVER] ← Nhận yêu cầu từ IP_VPN
   ↓
[SERVER VPN] ← Nhận phản hồi → mã hóa lại → gửi về client
   ↓
[Client] ← Giải mã → nhận dữ liệu

🔹 Ai thấy gì?
- ISP: Thấy bạn kết nối đến IP_VPN, không thấy nội dung
- Server VPN: Thấy dữ liệu, nhưng nếu dùng HTTPS → không đọc được nội dung web
- Google: Thấy IP của server VPN
- Bạn: An toàn, như đang dùng mạng riêng

─────────────────────────────────────────────────────────────

                             ↓
+-------------------------------------------------------------+
|                     SERVER ĐÍCH (Google)                    |
|   ← Nhận gói tin từ:                                        |
|      - Proxy: IP proxy                                       |
|      - VPN: IP server VPN                                  |
|   → Xử lý request, trả về HTML đã mã hóa (HTTPS)            |
|   → Gói tin quay lại theo đường cũ                          |
+-------------------------------------------------------------+
                             ↓
           ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
           Gói tin quay về theo đường ngược lại
           (qua cùng các tầng, nhưng ngược chiều)
           ↓
+-------------------------------------------------------------+
|                       KẾT QUẢ TRÊN TRÌNH DUYỆT               |
|   → Hiển thị trang Google                                   |
|   🔒 Biểu tượng khóa (HTTPS) hiện lên                        |
+-------------------------------------------------------------+
```

## Mục Lục


- [MAP mô phỏng  (Networking )](#map)
- [OSI ↔ TCP/IP ](./module/OSImodel.md)
- [Các giao thức mạng chính](./module/Protocol.md)
- [Luồng phân giải DNS](./module/DNS.md)
- [Bảo mật, nén, mã hoá](./module/ZTA_AAA.md)
- [Bản đồ PORT-](./module/Ports.md)
- [Thiết bị & Kỹ thuật mạng](./module/Physical.md)
- [Các loại mạng](./module/Networks.md)
- [Các kỹ thuật tối ưu hóa mạng](./module/Physical.md#các-kỹ-thuật-tối-ưu-hóa-mạng)
- [Cloud Networking](#cloud-networking)
- [Network Monitoring](#network-monitoring)
- [Wireless Security](#wireless-security)


- [(cheatsheet)](./organization.md)

