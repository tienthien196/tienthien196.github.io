# 📘 OSI Model

## 🔹 Mục Lục
- [Giới thiệu](#giới-thiệu)
- [Sơ đồ OSI (ASCII Art)](#sơ-đồ-osi-ascii-art)
- [7 tầng trong mô hình OSI](#7-tầng-trong-mô-hình-osi)
  - [Physical Layer](#1️⃣-physical-layer-tầng-vật-lý)
  - [Data Link Layer](#2️⃣-data-link-layer-tầng-liên-kết-dữ-liệu)
  - [Network Layer](#3️⃣-network-layer-tầng-mạng)
  - [Transport Layer](#4️⃣-transport-layer-tầng-giao-vận)
  - [Session Layer](#5️⃣-session-layer-tầng-phiên)
  - [Presentation Layer](#6️⃣-presentation-layer-tầng-trình-diễn)
  - [Application Layer](#7️⃣-application-layer-tầng-ứng-dụng)
- [Encapsulation & Decapsulation](#cách-dữ-liệu-đi-qua-các-tầng-encapsulation--decapsulation)
- [OSI vs TCP/IP Model](#osi-vs-tcpip-model)
- [Các khái niệm liên quan](#các-khái-niệm-liên-quan)
- [Tóm tắt OSI theo cách dễ nhớ](#tóm-tắt-osi-theo-cách-dễ-nhớ)
- [Mô hình OSI (Chi tiết & Thực tiễn)](#mô-hình-osi-7-tầng--chi-tiết--thực-tiễn)
  - [Sơ đồ nhanh](#sơ-đồ-nhanh)
  - [Chức năng từng tầng](#chức-năng-từng-tầng)
  - [Encapsulation/Decapsulation](#encapsulationdecapsulation)
  - [PDU, thiết bị, ví dụ giao thức](#pdu-thiết-bị-ví-dụ-giao-thức)
  - [OSI vs TCP/IP](#osi-vs-tcpip)
  - [Troubleshooting theo lớp](#troubleshooting-theo-lớp)
  - [Transport chuyên sâu: TCP & UDP](#transport-chuyên-sâu-tcp--udp)

---

## 🔹 Giới thiệu
**OSI Model (Open Systems Interconnection)** là khung lý thuyết chia quá trình truyền thông mạng thành **7 tầng**, chuẩn hóa cách dữ liệu di chuyển từ ứng dụng người gửi đến người nhận. Đây không phải giao thức cụ thể mà là mô hình tham chiếu giúp thiết kế, phân tích, và bảo mật mạng.

---

## 🔹 Sơ đồ OSI 
```
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║            📘 OSI MODEL 7 TẦNG – MASTER DIAGRAM (ASCII ART)               ║
    ║         "Hiểu mạng từ vật lý đến ứng dụng – Bảo mật từng lớp"              ║
    ╚════════════════════════════════════════════════════════════════════════════╝

                                      ▲
                                      │
                                      ▼
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║        🔶 TẦNG 7: APPLICATION (Ứng dụng) – Giao diện người dùng            ║
    ╠════════════════════════════════════════════════════════════════════════════╣
    ║  • Chức năng: Cung cấp dịch vụ trực tiếp cho ứng dụng (web, email, v.v.)  ║
    ║  • Đơn vị: Data (dữ liệu ứng dụng)                                        ║
    ║  • Giao thức: HTTP/HTTPS, DNS, SSH, FTP, SMTP, IMAP, QUIC                 ║
    ║  • Ví dụ: Chrome, Outlook, Discord                                        ║
    ║  • Bảo mật: AAA, Zero Trust (ZTNA), OAuth, API keys                       ║
    ╚════════════════════════════════════════════════════════════════════════════╝
                                      ▲
                                      │ Dữ liệu (Data)
                                      ▼
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║       🔶 TẦNG 6: PRESENTATION (Trình diễn) – Mã hóa & Định dạng             ║
    ╠════════════════════════════════════════════════════════════════════════════╣
    ║  • Chức năng: Dịch, nén, mã hóa dữ liệu giữa hệ thống                     ║
    ║  • Đơn vị: Data (sau xử lý)                                               ║
    ║  • Giao thức: TLS/SSL, MIME, ASCII/Unicode, JPEG, PNG                     ║
    ║  • Ví dụ: HTTPS (TLS), DoH (DNS over HTTPS)                               ║
    ║  • Bảo mật: Mã hóa end-to-end, chống nghe lén                             ║
    ║  • Công cụ: OpenSSL, Let's Encrypt                                        ║
    ╚════════════════════════════════════════════════════════════════════════════╝
                                      ▲
                                      │ Dữ liệu (Data)
                                      ▼
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║         🔶 TẦNG 5: SESSION (Phiên) – Quản lý kết nối                       ║
    ╠════════════════════════════════════════════════════════════════════════════╣
    ║  • Chức năng: Thiết lập, duy trì, đóng phiên (session)                    ║
    ║  • Đơn vị: Data (trong phiên)                                             ║
    ║  • Giao thức: Kerberos, RPC, NetBIOS, SIP                                 ║
    ║  • Ví dụ: Session ID trong website, video call                             ║
    ║  • Bảo mật: Ngăn session hijacking, fixation, token theft                 ║
    ║  • Phòng chống: Secure cookies, JWT, token expiration                     ║
    ╚════════════════════════════════════════════════════════════════════════════╝
                                      ▲
                                      │ Segment (TCP) / Datagram (UDP)
                                      ▼
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║       🔶 TẦNG 4: TRANSPORT (Truyền tải) – Truyền tin cậy                   ║
    ╠════════════════════════════════════════════════════════════════════════════╣
    ║  • Chức năng: Đảm bảo truyền dữ liệu giữa 2 host                          ║
    ║  • Đơn vị: Segment (TCP), Datagram (UDP)                                  ║
    ║  • Giao thức: TCP, UDP, SCTP, QUIC                                        ║
    ║  • Cổng (Ports): HTTP:80, HTTPS:443, SSH:22, DNS:53                       ║
    ║  • Bảo mật: SYN flood, port scanning, session hijacking                   ║
    ║  • Công cụ: Wireshark, Nmap                                               ║
    ╚════════════════════════════════════════════════════════════════════════════╝
                                    ▲
                                    │ Packet (gói tin)
                                    ▼
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║         🔶 TẦNG 3: NETWORK (Mạng) – Định tuyến & Địa chỉ                   ║
    ╠════════════════════════════════════════════════════════════════════════════╣
    ║  • Chức năng: Định tuyến (routing), chọn đường đi giữa các mạng           ║
    ║  • Đơn vị: Packet                                                         ║
    ║  • Giao thức: IPv4/IPv6, ICMP, IPSec, OSPF, BGP                           ║
    ║  • Thiết bị: Router, Layer 3 Switch                                       ║
    ║  • Bảo mật: IP spoofing, DDoS, traceroute tấn công                        ║
    ║  • Phòng chống: ACL, Firewall, Anti-spoofing                              ║
    ╚════════════════════════════════════════════════════════════════════════════╝
                                  ▲
                                  │ Frame (khung dữ liệu)
                                  ▼
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║     🔶 TẦNG 2: DATA LINK (Liên kết dữ liệu) – MAC & Frame                  ║
    ╠════════════════════════════════════════════════════════════════════════════╣
    ║  • Chức năng: Đóng gói dữ liệu thành frame, kiểm soát lỗi                 ║
    ║  • Đơn vị: Frame                                                          ║
    ║  • Giao thức: Ethernet, Wi-Fi (802.11), PPP, VLAN, ARP                    ║
    ║  • Thiết bị: Switch, Bridge, Access Point                                 ║
    ║  • Bảo mật: ARP spoofing, MAC flooding, VLAN hopping                      ║
    ║  • Phòng chống: Port Security, DHCP Snooping, 802.1X                      ║
    ╚════════════════════════════════════════════════════════════════════════════╝
                                  ▲
                                  │ Bit (0 và 1)
                                  ▼
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║       🔶 TẦNG 1: PHYSICAL (Vật lý) – Tín hiệu & Môi trường                 ║
    ╠════════════════════════════════════════════════════════════════════════════╣
    ║  • Chức năng: Truyền bit (0/1) qua cáp, sóng, ánh sáng                    ║
    ║  • Đơn vị: Bit                                                            ║
    ║  • Chuẩn: RJ45, USB, Bluetooth, 1000BASE-T, 5G NR                         ║
    ║  • Thiết bị: Hub, Repeater, NIC, cáp, anten                               ║
    ║  • Bảo mật: Tấn công vật lý, nghe lén cáp                                 ║
    ║  • Phòng chống: Faraday cage, cáp quang                                   ║
    ╚════════════════════════════════════════════════════════════════════════════╝
```
---
```

                                ▲
                                │
                                │ Dữ liệu đi xuống: Encapsulation (Gói dữ liệu)
                                │ Dữ liệu đi lên: Decapsulation (Mở gói)
                                ▼

    ╔════════════════════════════════════════════════════════════════════════════╗
    ║      🔐 MỐI LIÊN HỆ BẢO MẬT & ZERO TRUST THEO TẦNG OSI                     ║
    ╠════════════════════════════════════════════════════════════════════════════╣
    ║  • Tầng 7: Zero Trust (ZTA), ABAC, PEP, AAA → "Không tin ai, luôn xác minh"║
    ║  • Tầng 6: TLS → Mã hóa end-to-end                                         ║
    ║  • Tầng 5: Session management → Ngăn hijacking                             ║
    ║  • Tầng 4: Firewall, WAF → Kiểm soát truy cập dựa trên port/IP             ║
    ║  • Tầng 3: IPSec, ACL, Anti-spoofing → Bảo vệ mạng                         ║
    ║  • Tầng 2: 802.1X, Port Security → Xác thực thiết bị                       ║
    ║  • Tầng 1: Physical Security → Kiểm soát truy cập vật lý                   ║
    ╚════════════════════════════════════════════════════════════════════════════╝

```
---

##  OSI ↔ TCP/IP (Mapping nhanh)
- [(xem chi tiết OSI model)](./a/OSImodel.md)


```
     ┌──────────────┐
     │ Application  │◄──────────────────────┐
     └───────┬──────┘                       │
     ┌───────▼────────┐   TCP/IP            │
     │ Presentation   │   Application Layer │
     └───────┬────────┘                     │
     ┌───────▼───────┐                      │
     │ Session       │◄─────────────────────┘
     └───────┬───────┘
     ┌───────▼───────────┐   ┌──────────────┐
     │ Transport         │──►│ Transport    │
     └───────┬───────────┘   └─────┬────────┘
     ┌───────▼───────────┐         │
     │ Network           │──►┌─────▼────────┐
     └───────┬───────────┘   │ Internet     │
     ┌───────▼───────────┐   └─────┬────────┘
     │ Data Link         │──►┌─────▼────────┐
     └───────┬───────────┘   │ Link         │
     ┌───────▼───────────┐   └──────────────┘
     │ Physical          │
     └───────────────────┘
```
---
```
                  Máy Gửi (Sender)                     Máy Nhận (Receiver)
              ─────────────────────              ─────────────────────
              | 7. Application    |              | 7. Application    |
              | 6. Presentation   |              | 6. Presentation   |
              | 5. Session        |              | 5. Session        |
              | 4. Transport      |◄──TCP──►     | 4. Transport      |
              | 3. Network        |◄──IP───►     | 3. Network        |
              | 2. Data Link      |◄─Frame─►     | 2. Data Link      |
              | 1. Physical       |◄─Bit───►     | 1. Physical       |
              ─────────────────────              ─────────────────────
                    ▼                                      ▲
                Encapsulation                         Decapsulation
```


## 🔹 7 tầng trong mô hình OSI

### 1️⃣ Physical Layer (Tầng vật lý)
- **Chức năng**: Truyền bit (0/1) qua cáp, sóng vô tuyến, hoặc ánh sáng.
- **Đơn vị dữ liệu**: Bit
- **Thiết bị**: Hub, repeater, NIC, cáp quang, anten.
- **Chuẩn**: RJ45, USB, Bluetooth, 1000BASE-T, 5G NR (New Radio).
- **Nhiệm vụ**:
  - Mã hóa tín hiệu (Encoding/Decoding).
  - Điều chế sóng (Modulation).
  - Quản lý tốc độ, điện áp, tần số.
- **Ví dụ thực tế**: Kết nối cáp Cat6 trong mạng LAN.
- **Bảo mật**: Ngăn nghe lén cáp (dùng cáp quang, Faraday cage).

### 2️⃣ Data Link Layer (Tầng liên kết dữ liệu)
- **Chức năng**: Đóng gói bit thành frame, kiểm soát lỗi, truy cập môi trường.
- **Đơn vị dữ liệu**: Frame
- **Giao thức**: Ethernet, Wi-Fi (802.11), PPP, VLAN, ARP.
- **Thiết bị**: Switch, Bridge, Access Point.
- **Nhiệm vụ**:
  - Địa chỉ MAC (48-bit).
  - Kiểm tra lỗi (CRC).
  - Phân tách mạng (VLAN).
- **Ví dụ thực tế**: Switch Cisco xử lý frame Ethernet.
- **Bảo mật**: Ngăn ARP spoofing (dùng DHCP Snooping, 802.1X).
  ```bash
  # Cấu hình Port Security trên switch Cisco
  switchport port-security maximum 2
  switchport port-security violation restrict
  ```

### 3️⃣ Network Layer (Tầng mạng)
- **Chức năng**: Định tuyến gói tin từ nguồn đến đích.
- **Đơn vị dữ liệu**: Packet
- **Giao thức**: IPv4, IPv6, ICMP, IPSec, OSPF, BGP.
- **Thiết bị**: Router, Layer 3 Switch.
- **Nhiệm vụ**:
  - Địa chỉ IP (IPv4: 32-bit, IPv6: 128-bit).
  - Định tuyến (static/dynamic).
  - Phân mảnh packet.
- **Ví dụ thực tế**: Router định tuyến gói tin qua OSPF.
- **Bảo mật**: Ngăn IP spoofing (dùng ACL, firewall).

### 4️⃣ Transport Layer (Tầng giao vận)
- **Chức năng**: Đảm bảo truyền dữ liệu giữa hai ứng dụng.
- **Đơn vị dữ liệu**: Segment (TCP), Datagram (UDP).
- **Giao thức**: TCP, UDP, SCTP, QUIC.
- **Nhiệm vụ**:
  - Quản lý cổng (port numbers: HTTP:80, HTTPS:443).
  - Kiểm soát luồng và tắc nghẽn (TCP).
  - Phân mảnh và tái lắp dữ liệu.
- **Ví dụ thực tế**: TCP handshake cho HTTPS:
  ```bash
  # Phân tích TCP handshake bằng Wireshark
  tshark -i eth0 -f "tcp port 443" -Y "tcp.flags.syn==1"
  ```
- **Bảo mật**: Ngăn SYN flood, port scanning (dùng firewall).

### 5️⃣ Session Layer (Tầng phiên)
- **Chức năng**: Quản lý phiên giao tiếp giữa ứng dụng.
- **Đơn vị dữ liệu**: Data
- **Giao thức**: Kerberos, RPC, NetBIOS, SIP.
- **Nhiệm vụ**:
  - Thiết lập, duy trì, đóng phiên.
  - Đồng bộ hóa dữ liệu (checkpoint/recovery).
- **Ví dụ thực tế**: Session ID trong đăng nhập website.
- **Bảo mật**: Ngăn session hijacking (dùng secure cookies, JWT).

### 6️⃣ Presentation Layer (Tầng trình diễn)
- **Chức năng**: Dịch, nén, mã hóa dữ liệu.
- **Đơn vị dữ liệu**: Data
- **Giao thức**: TLS/SSL, MIME, ASCII/Unicode, JPEG.
- **Nhiệm vụ**:
  - Chuyển đổi định dạng (EBCDIC ↔ ASCII).
  - Nén dữ liệu (lossy/lossless).
  - Mã hóa (TLS 1.3).
- **Ví dụ thực tế**: HTTPS mã hóa dữ liệu bằng TLS.
  ```bash
  # Kiểm tra chứng thư TLS
  openssl s_client -connect example.com:443
  ```
- **Bảo mật**: Mã hóa end-to-end, chống nghe lén.

### 7️⃣ Application Layer (Tầng ứng dụng)
- **Chức năng**: Cung cấp dịch vụ mạng cho người dùng.
- **Đơn vị dữ liệu**: Data
- **Giao thức**: HTTP/HTTPS, DNS, FTP, SMTP, SSH, QUIC.
- **Ví dụ thực tế**: Truy cập `https://example.com` qua Chrome.
- **Bảo mật**: Áp dụng Zero Trust (ZTNA), OAuth:
  ```bash
  # Cấu hình OAuth trên ứng dụng
  curl -X POST https://api.example.com/oauth/token -d "grant_type=client_credentials"
  ```

---

## 🔹 Cách dữ liệu đi qua các tầng (Encapsulation & Decapsulation)

- **Encapsulation** (Sender):
  1. Application tạo **Data**.
  2. Presentation mã hóa/nén.
  3. Session quản lý phiên.
  4. Transport chia thành **Segment** (TCP) hoặc **Datagram** (UDP).
  5. Network đóng gói thành **Packet** (thêm IP header).
  6. Data Link đóng gói thành **Frame** (thêm MAC header).
  7. Physical truyền **Bit**.
- **Decapsulation** (Receiver): Mở gói theo chiều ngược lại.

---

## 🔹 OSI vs TCP/IP Model
- **TCP/IP**: 4 tầng (Application, Transport, Internet, Link).
- **OSI**: 7 tầng, chi tiết hơn, dùng để phân tích và học tập.
- **So sánh**:
---

## 🔹 Các khái niệm liên quan
- **Encapsulation/Decapsulation**: Gói và mở gói dữ liệu qua các tầng.
- **Protocol Data Unit (PDU)**:
  - Application/Presentation/Session: Data
  - Transport: Segment (TCP), Datagram (UDP)
  - Network: Packet
  - Data Link: Frame
  - Physical: Bit
- **Port Number**: Định danh dịch vụ (HTTP:80, HTTPS:443).
- **TCP vs UDP**:
  - TCP: Reliable, connection-oriented (SYN, ACK, FIN).
  - UDP: Fast, connectionless (DNS, streaming).
- **Zero Trust**: Không tin tưởng, luôn xác minh (ZTNA, ABAC).

---

## 🔹 Tóm tắt OSI theo cách dễ nhớ

| Tầng | Chức năng chính            | PDU            | Ví dụ giao thức         |
|------|----------------------------|----------------|-------------------------|
| 7    | Giao diện người dùng       | Data           | HTTP, DNS, SSH, QUIC    |
| 6    | Mã hóa, nén, dịch dữ liệu  | Data           | TLS, JPEG, MIME         |
| 5    | Quản lý phiên              | Data           | RPC, NetBIOS, SIP       |
| 4    | Truyền dữ liệu tin cậy     | Segment/Datagram | TCP, UDP, QUIC        |
| 3    | Định tuyến, địa chỉ IP     | Packet         | IP, ICMP, OSPF          |
| 2    | Đóng gói frame, MAC        | Frame          | Ethernet, Wi-Fi, VLAN   |
| 1    | Truyền bit qua môi trường  | Bit            | RJ45, 5G NR, Bluetooth  |

---

## 🔹 Mô hình OSI (7 tầng) – Chi tiết & Thực tiễn

### Sơ đồ nhanh
```
┌───────────────────────┐ 7. Application  (HTTP, DNS, SMTP, SSH, QUIC...)
├───────────────────────┤ 6. Presentation (TLS/SSL, nén, mã hóa, chuyển mã)
├───────────────────────┤ 5. Session      (thiết lập/duy trì/kết thúc phiên)
├───────────────────────┤ 4. Transport    (TCP/UDP/QUIC, cổng, kiểm soát luồng)
├───────────────────────┤ 3. Network      (IP, ICMP, IPSec, OSPF)
├───────────────────────┤ 2. Data Link    (Ethernet, Wi-Fi, MAC, VLAN)
└───────────────────────┘ 1. Physical     (bit, cáp/sóng, 5G NR)
```

### Chức năng từng tầng
1. **Physical**: Truyền bit (0/1) qua cáp, sóng. Chuẩn: RJ45, 5G NR.
2. **Data Link**: Đóng gói frame, địa chỉ MAC, kiểm tra lỗi (CRC). Thiết bị: Switch.
3. **Network**: Định tuyến packet, địa chỉ IP. Thiết bị: Router.
4. **Transport**: Truyền dữ liệu end-to-end (TCP, UDP, QUIC). Quản lý cổng.
5. **Session**: Quản lý phiên, đồng bộ hóa. Giao thức: RPC, SIP.
6. **Presentation**: Chuyển mã, nén, mã hóa (TLS/SSL).
7. **Application**: Giao diện dịch vụ (HTTP, DNS, QUIC).

### Encapsulation/Decapsulation
- **Sender**: Data → Segment/Datagram (TCP/UDP header) → Packet (IP header) → Frame (MAC header) → Bit.
- **Receiver**: Ngược lại.

### PDU, thiết bị, ví dụ giao thức
| Tầng | PDU              | Thiết bị chính        | Ví dụ giao thức/chuẩn |
|------|------------------|-----------------------|-----------------------|
| 7    | Data             | Ứng dụng (Chrome, Outlook) | HTTP, HTTPS, DNS, QUIC |
| 6    | Data             | TLS library           | TLS/SSL, JPEG, MIME   |
| 5    | Data             | OS stack (session mgmt) | RPC, NetBIOS, SIP   |
| 4    | Segment/Datagram | OS stack              | TCP, UDP, QUIC        |
| 3    | Packet           | Router/L3 Switch      | IPv4/IPv6, ICMP       |
| 2    | Frame            | Switch/Bridge/AP      | Ethernet, Wi-Fi, VLAN |
| 1    | Bit              | NIC, Hub, Repeater    | RJ45, 5G NR, Bluetooth |

### OSI vs TCP/IP
- **TCP/IP**: 4 tầng (Application, Transport, Internet, Link).
- **OSI**: 7 tầng, chi tiết hơn, lý thuyết hơn.
- **Ứng dụng**: OSI dùng để học, phân tích lỗi; TCP/IP là thực tiễn Internet.

### Troubleshooting theo lớp
1. **Physical**: Link up? Cáp đúng? Tốc độ/duplex?
2. **Data Link**: MAC/VLAN? CRC lỗi? Port-security?
3. **Network**: IP/subnet/gateway? Route? ICMP?
4. **Transport**: Port mở? TCP handshake? Timeout?
5. **Session**: Session ID hợp lệ? Token timeout?
6. **Presentation**: TLS certificate? Mã hóa đúng?
7. **Application**: DNS resolve? HTTP status code?

### Transport chuyên sâu: TCP & UDP
- **TCP**:
  - Reliable, connection-oriented (3-way handshake: SYN, SYN/ACK, ACK).
  - Cờ: SYN (bắt đầu), ACK (xác nhận), FIN (kết thúc), RST (reset), PSH (push data), URG (ưu tiên).
  - Quản lý luồng (window), tắc nghẽn (slow start, AIMD).
  - Ví dụ: `tshark -i eth0 -f "tcp port 443" -Y "tcp.flags.syn==1"`.
- **UDP**:
  - Connectionless, nhanh, ít overhead.
  - Dùng cho DNS, VoIP, streaming.
  - Kiểm tra loss/jitter, MTU.
- **QUIC**:
  - Kết hợp TCP+UDP, dùng cho HTTP/3, cải thiện tốc độ và bảo mật.
  - Ví dụ: Truy cập website qua QUIC (port 443/UDP).

---

## 🔹 Kết luận
Mô hình OSI là nền tảng để hiểu cách mạng máy tính hoạt động, từ truyền bit đến ứng dụng người dùng. Nắm rõ từng tầng giúp:
- Thiết kế và triển khai mạng.
- Phân tích lỗi (troubleshooting).
- Tăng cường bảo mật (Zero Trust, TLS, 802.1X).
- Thực hành: TryHackMe Network Fundamentals (https://tryhackme.com/room/networkfundamentals).


### ***NOTE***
> ***TÀI LIỆU BUILD BY @TIẾN THIỆN*** [(truy cập chi tiết)](https://tienthien196.github.io/ecosys.portfolioBNJ/)


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


| OSI Layer            | TCP/IP Layer       | Ví dụ                     |
|----------------------|--------------------|---------------------------|
| 7. Application       | Application        | HTTP, DNS, SMTP, SSH      |
| 6. Presentation      | Application        | TLS/SSL, JSON, ASN.1      |
| 5. Session           | Application        | RPC, SMB, PPTP            |
| 4. Transport         | Transport          | TCP, UDP, SCTP            |
| 3. Network           | Internet           | IP, ICMP, IPSec, OSPF     |
| 2. Data Link         | Link               | Ethernet, 802.11, ARP, VLAN |
| 1. Physical          | Link               | Cáp, tín hiệu, NIC, Hub   |

> Nắm các tầng giúp **khoanh vùng lỗi** và hiểu **encapsulation/PDU** (bit/frame/packet/segment).





