# Computer Network: A Comprehensive Guide

> Tài liệu này được xây dựng để cung cấp một cái nhìn toàn diện về Mạng Máy tính, từ các khái niệm cơ bản đến các kỹ thuật nâng cao, phục vụ mục đích lưu trữ và tham khảo cho các dự án IT. Tài liệu được thiết kế để hỗ trợ cả người mới bắt đầu và những người có kinh nghiệm muốn hệ thống hóa kiến thức.

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

## Mục Lục

- [Giới thiệu về Computer Network](#giới-thiệu-về-computer-network)
- [MAP ASCII hệ thống hoá kiến thức (Networking & Security)](#map-ascii-hệ-thống-hoá-kiến-thức-networking--security)
- [OSI ↔ TCP/IP (Mapping nhanh)](#osi--tcpip-mapping-nhanh)
  - [Mô hình OSI](#mô-hình-osi)
  - [Mô hình TCP/IP](#mô-hình-tcpip)
- [Các giao thức mạng chính](#các-giao-thức-mạng-chính)
  - [Giao thức tầng ứng dụng](#giao-thức-tầng-ứng-dụng)
  - [Giao thức tầng giao vận](#giao-thức-tầng-giao-vận)
  - [Giao thức tầng mạng](#giao-thức-tầng-mạng)
  - [Giao thức tầng liên kết dữ liệu](#giao-thức-tầng-liên-kết-dữ-liệu)
- [Luồng phân giải DNS](#luồng-phân-giải-dns)
- [Bảo mật, nén, mã hoá](#bảo-mật--nén--mã-hoá)
  - [AAA/RADIUS – Chu trình xác thực](#aaaradius--chu-trình-xác-thực)
  - [Crypto & PKI](#crypto--pki)
  - [Zero Trust – Khối thành phần](#zero-trust--khối-thành-phần)
- [Bản đồ PORT ↔ Dịch vụ](#bản-đồ-port--dịch-vụ)
- [Thiết bị & Kỹ thuật mạng](#thiết-bị--kỹ-thuật-mạng)
  - [Router](#router)
  - [Switch](#switch)
  - [Access Point](#access-point)
  - [Firewall](#firewall)
- [Các loại mạng](#các-loại-mạng)
- [Các kỹ thuật tối ưu hóa mạng](#các-kỹ-thuật-tối-ưu-hóa-mạng)
  - [Load Balancing](#load-balancing)
  - [Quality of Service (QoS)](#quality-of-service-qos)
  - [Software-Defined Networking (SDN)](#software-defined-networking-sdn)
- [Cloud Networking](#cloud-networking)
- [Network Monitoring](#network-monitoring)
- [Wireless Security](#wireless-security)
- [Pentest Roadmap](#pentest-roadmap)
- [Network Security](#network-security)
- [Checklist học tập và nghiên cứu](#checklist-học-tập-và-nghiên-cứu)
- [Công cụ đề xuất](#công-cụ-đề-xuất)
- [Kinh nghiệm thực hành](#kinh-nghiệm-thực-hành)
- [Tài liệu tham khảo](#tài-liệu-tham-khảo)
- [Ghi chú nguồn](#ghi-chú-nguồn)

---

# MAP hệ thống hoá kiến thức (Networking & Security)

```
                                ┌───────────────────────────────────────────┐
                                │         NETWORKING & SECURITY KB         │
                                │              (System Map)                │
                                └───────────────┬───────────────┬──────────┘
                                                │               │
                                   ┌────────────┘               └─────────────┐
                                   │                                          │
                     ┌─────────────▼─────────────┐               ┌────────────▼────────────┐
                     │        MÔ HÌNH & LỚP      │               │   GIAO THỨC & CỔNG (PORT)│
                     │  OSI (7) ↔ TCP/IP (4/5)   │               │   Dịch vụ thông dụng     │
                     └───────┬───────────┬───────┘               └───────────┬──────────────┘
                             │           │                                   │
                ┌────────────▼───┐  ┌───▼──────────┐         ┌──────────────▼───────────────┐
                │ Encapsulation  │  │ Troubleshoot │         │ Bản đồ: 22=SSH, 53=DNS,     │
                │ PDU/Thiết bị   │  │ theo lớp     │         │ 80=HTTP, 443=HTTPS, 445=SMB │
                └────────────────┘  └──────────────┘         └──────────────────────────────┘

        ┌───────────────────────┐        ┌────────────────────────┐         ┌───────────────────────────┐
        │          DNS          │        │ AAA / RADIUS / 2FA     │         │   ZERO TRUST (NIST 1800)  │
        │ Phân giải tên↔IP      │        │ AuthN/AuthZ/Acct       │         │ PEP/PE/PA, posture, ZTNA  │
        └──────────┬────────────┘        └──────────┬─────────────┘         └──────────┬────────────────┘
                   │                                 │                                   │
     ┌─────────────▼────────────┐        ┌───────────▼───────────┐            ┌──────────▼─────────────┐
     │ Record: A/AAAA, CNAME,   │        │ RADIUS: 1812/1813 UDP │            │ Micro‑segmentation,    │
     │ MX, NS, SOA, TXT, SRV... │        │ CHAP/PAP/MS‑CHAPv2    │            │ continuous evaluation   │
     └──────────────────────────┘        └───────────────────────┘            └─────────────────────────┘

  ┌───────────────────────────┐  ┌───────────────────────────────┐            ┌───────────────────────────┐
  │     CRYPTO BASICS         │  │       PENTEST ROADMAP         │            │    THIẾT BỊ & KỸ THUẬT    │
  │ Symmetric/Asymmetric,     │  │ Recon → Scan → Access →       │            │ Router, Switch, AP,       │
  │ Hash, PKI, TLS            │  │ Maintain → Cover Tracks       │            │ Firewall; NAT, QoS, LB    │
  └───────────────────────────┘  └───────────────────────────────┘            └───────────────────────────┘
```

---



##  OSI ↔ TCP/IP (Mapping nhanh)
- [(xem chi tiết OSI model)](./a/OSImodel.md)

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
- **IP**: Định tuyến gói tin (IPv4, IPv6).
- **ICMP**: Kiểm tra trạng thái mạng (`ping`, `traceroute`).
- **ARP**: Ánh xạ IP sang MAC.
- **OSPF**: Giao thức định tuyến động.
- **Ví dụ thực tế**:
  - IPv6: Sử dụng `2001:0db8::1` cho mạng hiện đại.
  - ICMP: Kiểm tra kết nối bằng `ping 8.8.8.8`.

### Giao thức tầng liên kết dữ liệu
- **Ethernet**: Giao thức LAN phổ biến.
- **Wi-Fi (IEEE 802.11)**: Kết nối không dây (802.11ax/Wi-Fi 6).
- **PPP**: Kết nối điểm-điểm.
- **VLAN**: Phân tách lưu lượng mạng.
- **Ví dụ thực tế**:
  - Ethernet: Kết nối máy tính qua cáp Cat6.
  - VLAN: Tách mạng khách và nhân viên trong doanh nghiệp.

---

## Luồng phân giải DNS
- [(Xem chi tiết về DNS)](./a/DNS.md)
```
+-----------+        query         +------------------+
|  Client   | -------------------> | Recursive Resolver|
| (Stub)    |                      +---------+--------+
+-----------+                                |
                                             | referrals
                                   +---------v----------+
                                   |   Root (.)  NS     |
                                   +---------+----------+
                                             |
                                   +---------v----------+
                                   |     TLD (.com)     |
                                   +---------+----------+
                                             |
                                   +---------v----------+
                                   | Authoritative NS   |
                                   +---------+----------+
                                             |
                                           answer
                                             |
+-----------+                                |
|  Client   | <------------------------------+
+-----------+
```
- **Quy trình**:
  1. Client gửi truy vấn DNS đến Recursive Resolver.
  2. Resolver hỏi Root NS, sau đó TLD NS (.com, .org).
  3. TLD NS trỏ đến Authoritative NS, trả về IP.
  4. Resolver trả IP về client.
- **Khái niệm quan trọng**:
  - **DNSSEC**: Bảo mật DNS, ngăn giả mạo bằng chữ ký số.
  - **DoT (DNS over TLS)**: Mã hóa truy vấn DNS qua TLS.
  - **DoH (DNS over HTTPS)**: Truy vấn DNS qua HTTPS (cổng 443).
  - **DoQ (DNS over QUIC)**: DNS qua QUIC, cải thiện tốc độ.
- **Ví dụ thực tế**: Phân giải `google.com` với DoH qua Cloudflare (1.1.1.1).

> Thực hành: nắm **record types**, **TTL/cache**, **delegation/glue**, **DNSSEC**, **DoT/DoH/DoQ**.

---

##  Bảo mật , nén , mã hoá  
  [(xem chi tiết)](./a/ZTA_AAA.md)

###  AAA/RADIUS – Chu trình xác thực (ví dụ FortiGate)
```
[User] → credentials → [RADIUS Client (FortiGate)]
    └─► ACCESS-REQUEST ─────────────────────────────►
                    [RADIUS Server]
           (PAP/CHAP/MS-CHAPv2/EAP, VSA)
   ◄─ ACCESS-ACCEPT / ACCESS-REJECT / ACCESS-CHALLENGE ─┘

Accounting:
[RADIUS Client] ── Start/Interim/Stop → [RADIUS Server] (UDP 1813)
```
> Mẹo: cấu hình **secret**, khai báo client trên server, **test connectivity/credentials**, cân nhắc **2FA/OTP**.

- **AAA**: Authentication (xác thực), Authorization (phân quyền), Accounting (ghi log).
- **RADIUS**: Giao thức xác thực qua UDP 1812 (auth), 1813 (accounting).
- **Ví dụ thực tế**: Cấu hình FortiGate với RADIUS server để xác thực VPN users, sử dụng 2FA (FortiToken).

---

### Crypto & PKI (rút gọn)

| Loại        | Mô tả                              | Ví dụ             |
|-------------|------------------------------------|-------------------|
| Symmetric   | Nhanh, dùng chung khóa            | AES-256, ChaCha20 |
| Asymmetric  | Khóa đôi (public/private)         | RSA, ECC, DH      |
| Hash        | Đảm bảo toàn vẹn dữ liệu          | SHA-256, SHA-3    |
| PKI         | Hệ thống quản lý chứng thư số     | Root CA, SubCA    |
| TLS         | Mã hóa kết nối (HTTPS, VPN)       | TLS 1.3           |

- **Chứng thư số**: Chứa Subject, Issuer, Validity, SAN (Subject Alternative Name).
- **Mô hình tin cậy**: Hierarchical (Root CA → SubCA) hoặc Web of Trust.
- **Ví dụ thực tế**: Sử dụng Let’s Encrypt để cấp chứng thư TLS cho website.

---

### Zero Trust – Khối thành phần
```
Identities ──┐
Devices ─────┼─►  Policy Engine (PE) ─► Decision
Network ─────┤
Posture ─────┤           ▲
Telemetry ───┘           │
                  Policy Admin (PA)
                        │
                  Policy Enforcement Point (PEP)
                        │
                     Allow/Deny + Continuous Eval
```
- **Mô tả**: Zero Trust giả định không tin tưởng bất kỳ ai, yêu cầu xác thực liên tục.
- **Thành phần**:
  - **PE (Policy Engine)**: Ra quyết định dựa trên chính sách.
  - **PEP (Policy Enforcement Point)**: Thực thi quyết định (cho phép/chặn).
  - **PA (Policy Admin)**: Quản lý chính sách.
  - **Posture**: Kiểm tra trạng thái thiết bị (cập nhật, bảo mật).
- **Ví dụ thực tế**: ZTNA (Zero Trust Network Access) trong Cisco Secure Access.

---

## Bản đồ PORT ↔ Dịch vụ (mẫu)
- [(xem chi tiet)](./a/network_protocols_ports.md)

```
Port   Proto    Dịch vụ / Ghi chú
────────────────────────────────────────────────
22     TCP      SSH (điều khiển từ xa, tunnel)
25     TCP      SMTP (chuyển thư máy‑chủ)
53     UDP/TCP  DNS (truy vấn / zone transfer)
80     TCP      HTTP (web không mã hoá)
123    UDP      NTP (đồng bộ thời gian)
389    TCP/UDP  LDAP (thư mục)
443    TCP      HTTPS (web mã hoá)
445    TCP/UDP  SMB (chia sẻ tài nguyên Windows)
1812   UDP      RADIUS AuthN (alt 1645)
1813   UDP      RADIUS Accounting (alt 1646)
3306   TCP      MySQL
3389   TCP      RDP (Remote Desktop)
```
> Ghi nhớ: **mở port = mở bề mặt tấn công** → firewall, principle of least privilege, ưu tiên giao thức mã hoá.

---

## Thiết bị & Kỹ thuật mạng (tóm tắt)
| Thiết bị/Kỹ thuật | Tầng | Mô tả                              |
|-------------------|------|------------------------------------|
| Router            | L3   | Định tuyến IP, NAT, ACL            |
| Switch            | L2   | MAC table, VLAN, STP               |
| Access Point      | L2   | Kết nối Wi-Fi, WPA2/3, roaming     |
| Firewall          | L3/L7 | Stateful, NAT, IDS/IPS, WAF        |
| NAT               | L3   | Ánh xạ địa chỉ IP                  |
| QoS               | L3/L7 | Ưu tiên lưu lượng                  |
| Load Balancing    | L4/L7 | Phân phối lưu lượng                |

---

## Các thiết bị mạng

```
 [Laptop]───┐
            │ Wi-Fi
        ┌───▼───┐
        │  AP   │
        └───┬───┘
            │ Ethernet
       ┌────▼────┐
       │ Switch  │
       └────┬────┘
            │
   ┌────────▼─────────┐
   │     Router       │───Internet (WAN)
   └────────┬─────────┘
            │
      ┌─────▼──────┐
      │  Firewall  │
      └────────────┘

```

### Router
- **Mô tả**: Chuyển tiếp gói tin giữa các mạng, hoạt động ở tầng 3.
- **Chức năng**: Định tuyến, NAT, DHCP, ACL.
- **Ví dụ thực tế**: TP-Link Archer C6 cho mạng gia đình.

### Switch
- **Mô tả**: Kết nối thiết bị trong cùng mạng, hoạt động ở tầng 2.
- **Chức năng**: Chuyển khung dữ liệu dựa trên MAC, VLAN.
- **Ví dụ thực tế**: Cisco Catalyst 9200 cho doanh nghiệp.

### Access Point
- **Mô tả**: Cung cấp kết nối Wi-Fi.
- **Chức năng**: Mở rộng mạng, hỗ trợ WPA3, roaming.
- **Ví dụ thực tế**: Ubiquiti UniFi 6 Pro.

### Firewall
- **Mô tả**: Kiểm soát lưu lượng dựa trên quy tắc.
- **Chức năng**: Chặn truy cập trái phép, IDS/IPS.
- **Ví dụ thực tế**: Fortinet FortiGate 60F.

---

### Các loại mạng
```
           ┌───────────┐
           │   LAN     │ (Văn phòng, nhà ở)
           └─────┬─────┘
                 │
 ┌───────────┐   │   ┌───────────┐
 │   WAN     │<──┼──>│   MAN     │
 │ (Internet)│   │   │ (Thành phố)│
 └───────────┘   │   └───────────┘
                 │
          ┌──────▼──────┐
          │    PAN      │ (Bluetooth, USB)
          └──────┬──────┘
                 │
          ┌──────▼──────┐
          │    VPN      │ (Mạng riêng ảo)
          └─────────────┘
```
- **LAN (Local Area Network)**: Mạng nội bộ, phạm vi nhỏ (văn phòng, nhà ở).
- **WAN (Wide Area Network)**: Mạng diện rộng, kết nối các khu vực địa lý (Internet).
- **MAN (Metropolitan Area Network)**: Mạng đô thị, kết nối trong một thành phố.
- **PAN (Personal Area Network)**: Mạng cá nhân (Bluetooth, USB).
- **VPN (Virtual Private Network)**: Mạng riêng ảo, mã hóa dữ liệu qua Internet. [(xem chi tiết VPN)](./a/VPN.md)
- **Ví dụ thực tế**:
  - LAN: Mạng Wi-Fi trong nhà.
  - WAN: Kết nối Internet giữa các quốc gia.
  - VPN: Sử dụng OpenVPN để truy cập mạng công ty từ xa.



## Các kỹ thuật tối ưu hóa mạng

### Load Balancing

```
           ┌─────────────┐
 Client ──►│ LoadBalancer│───► [Server1]
           └──────┬──────┘      [Server2]
                  │             [Server3]
                  ▼
              Phân phối request

```

- **Mô tả**: Phân phối lưu lượng mạng đều trên nhiều server để tăng hiệu suất và độ tin cậy.
- **Các kỹ thuật**:
  - Round-robin: Phân phối tuần tự.
  - Least connections: Gửi lưu lượng đến server ít kết nối nhất.
- **Ví dụ thực tế**: Sử dụng NGINX làm load balancer cho web server.

### Quality of Service (QoS)
```
 ┌─────────────┐
 │   Router    │
 └──────┬──────┘
        │
 ┌──────▼───────────────────────────────┐
 │   QoS Queue:                         │
 │   [VoIP] ─ High Priority             │
 │   [Video] ─ Medium Priority          │
 │   [Web/HTTP] ─ Normal                │
 │   [Bulk Download] ─ Low              │
 └──────────────────────────────────────┘

```

- **Mô tả**: Quản lý và ưu tiên lưu lượng mạng để đảm bảo hiệu suất cho các ứng dụng quan trọng.
- **Các kỹ thuật**:
  - Traffic shaping: Giới hạn băng thông cho một số ứng dụng.
  - Packet prioritization: Ưu tiên gói tin VoIP hoặc video.
- **Ví dụ thực tế**: QoS trên router để ưu tiên băng thông cho Zoom trên router MikroTik.

### Software-Defined Networking (SDN)
- **Mô tả**: Tách biệt tầng điều khiển (control plane) và tầng chuyển tiếp (data plane), quản lý mạng qua phần mềm.
- **Ứng dụng**: OpenFlow, Cisco ACI, VMware NSX.
- **Ví dụ thực tế**: Mininet mô phỏng SDN cho mạng doanh nghiệp.

---

## Cloud Networking
- **Mô tả**: Quản lý mạng trong môi trường cloud (AWS, Azure, GCP).
- **Khái niệm chính**:
  - **VPC (Virtual Private Cloud)**: Mạng riêng trong cloud, cô lập tài nguyên.
  - **Container Networking**: Kết nối container trong Kubernetes (CNI plugins như Calico, Flannel).
  - **SD-WAN**: Mạng diện rộng điều khiển bằng phần mềm, tối ưu chi phí và hiệu suất.
- **Ví dụ thực tế**: Tạo VPC trên AWS với subnets và NAT Gateway.

---

## Network Monitoring
- **Mô tả**: Theo dõi hiệu suất và bảo mật mạng.
- **Giao thức**:
  - **SNMP (Simple Network Management Protocol)**: Thu thập dữ liệu từ thiết bị mạng.
  - **NetFlow/sFlow**: Phân tích lưu lượng mạng.
- **Công cụ**: Zabbix, Nagios, Prometheus + Grafana.
- **Ví dụ thực tế**: Sử dụng Zabbix để giám sát băng thông router.

---

## Wireless Security
- **Mô tả**: Bảo vệ mạng Wi-Fi khỏi tấn công.
- **Kỹ thuật**:
  - **WPA3**: Chuẩn mã hóa Wi-Fi mới, bảo mật hơn WPA2.
  - **Rogue AP Detection**: Phát hiện điểm truy cập giả mạo.
  - **Deauthentication Attack Mitigation**: Chặn tấn công ngắt kết nối Wi-Fi.
- **Công cụ**: Aircrack-ng, Kismet.
- **Ví dụ thực tế**: Sử dụng Kismet để phát hiện rogue AP trong mạng doanh nghiệp.

---

### Pentest Roadmap – Pipeline tổng quát
```
Recon/Footprinting → Scanning/Enumeration → Gaining Access →
Maintaining Access → Covering Tracks
    │                    │                         │
    │                    ├─ nmap, banner grab,     ├─ password/crack, exploit
    │                    │  SNMP/LDAP enum         │  web app, lateral move
    ├─ OSINT, DNS, WHOIS │                         │
    │  Google dorks      └─ service/port mapping   └─ logs cleanup, evasion
```
> Bộ công cụ: Wireshark/tcpdump, nmap, Nessus/Nikto, Burp, Hydra/John, Aircrack, Scapy…

- **Recon/Footprinting**:
  - Kỹ thuật: OSINT (Google dorks, WHOIS), DNS enumeration.
  - Công cụ: Maltego, theHarvester.
- **Scanning/Enumeration**:
  - Kỹ thuật: Quét cổng (Nmap), banner grabbing, SNMP/LDAP enum.
  - Công cụ: Nmap, Nessus, OpenVAS.
- **Gaining Access**:
  - Kỹ thuật: Khai thác lỗ hổng (Metasploit), tấn công mật khẩu (Hydra).
  - Ví dụ: Khai thác CVE-2021-44228 (Log4j) bằng Metasploit.
- **Maintaining Access**:
  - Kỹ thuật: Backdoor, privilege escalation.
  - Công cụ: Netcat, Meterpreter.
- **Covering Tracks**:
  - Kỹ thuật: Xóa log, che giấu lưu lượng.
  - Công cụ: Auditpol, CCleaner.
- **Ví dụ thực tế**: Sử dụng Burp Suite để tấn công web (SQL Injection).

---

### Network Security

```
 ┌──────────────────────┐
 │ Application Security │ (WAF, AuthN/AuthZ, TLS)
 └───────────┬──────────┘
             │
 ┌───────────▼───────────┐
 │ Network Security      │ (Firewall, IDS/IPS, VPN)
 └───────────┬───────────┘
             │
 ┌───────────▼───────────┐
 │ Endpoint Security     │ (AV, EDR, Patching)
 └───────────┬───────────┘
             │
 ┌───────────▼───────────┐
 │ Physical Security     │ (Access Control, CCTV)
 └────────────────────────┘

```

- **Mô tả**: Bảo vệ mạng khỏi các mối đe dọa như tấn công DDoS, malware, hoặc truy cập trái phép.
- **Các kỹ thuật**:
  - Mã hóa: Sử dụng HTTPS, VPN(IPSec, WireGuard).
  - Authentication: Sử dụng giao thức như RADIUS, LDAP.
  - IDS/IPS (Intrusion Detection/Prevention System): Phát hiện và ngăn chặn tấn công.
- **Ví dụ thực tế**: Sử dụng Wireshark để phát hiện lưu lượng đáng nghi.
  ```bash
  # Cấu hình firewall rule trên pfSense
  pass in quick on $LAN proto tcp from any to 192.168.1.0/24 port 443
  ```

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

### Công cụ đề xuất

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
   - Sử dụng Wireshark để bắt lưu lượng HTTP/DNS.
   - Ví dụ: `tshark -i eth0 -f "tcp port 80"`.
2. **Thiết lập mạng LAN**:
   - Cấu hình router với DHCP/NAT.
   - Thiết lập VLAN trên switch Cisco.
3. **Mô phỏng mạng**:
   - Sử dụng GNS3 để thử nghiệm OSPF.
   - Lab trên TryHackMe: https://tryhackme.com/room/networkfundamentals.
4. **Bảo mật mạng**:
   - Cài pfSense, cấu hình VPN:
     ```bash
     # OpenVPN server trên pfSense
     openvpn-server --port 1194 --proto udp --mode server
     ```
   - Quét mạng bằng Nmap: `nmap -sV 192.168.1.0/24`.
5. **Dự án thực tế**:
   - Giám sát mạng với Prometheus + Grafana.
   - Triển khai SD-WAN với Cisco Meraki.

---

### Tài liệu tham khảo

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

### Ghi chú nguồn
- OSI chi tiết & mapping, PDU/thiết bị, troubleshoot: xem tài liệu OSI & Computer Network.
- Port–Service bảng mẫu và khuyến nghị bảo mật: tài liệu Ports/Protocols.
- DNS: record/TTL/delegation & sơ đồ phân giải.
- AAA/RADIUS/FortiToken: khái niệm AAA, cổng 1812/1813, flow ACCESS-*; cấu hình FortiGate.
- Pentest roadmap & toolset: cheat sheet CEH/roadmap.
- Zero Trust: NIST SP 1800-35B tóm tắt (PE/PEP/PA, posture, micro‑segmentation).

### ***NOTE***
> ***TÀI LIỆU BUILD BY @TIẾN THIỆN*** [(truy cập chi tiết)](https://tienthien196.github.io/ecosys.portfolioBNJ/)


