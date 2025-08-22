# roadmap for cyber security 

> nêu toàn bô quỳ trình cần thực hành với an ninh mạng  "

## Mục Lục
- lí thuyết
    -
- thực hành 


### Attack Types
- **OS**: Tấn công cấu hình mặc định của hệ điều hành
- **App level**: Tấn công mã ứng dụng
- **Shrink Wrap**: Tận dụng cos sẵng
- **Misconfiguration**: Cấu hình kém



1. Một số chứng chỉ về an ninh Digital, chữ kí số Các Mô Hình Tin Cậy (Trust Models), (Digital Certificate):
    - toán từ tìm kiếm thông tin từ google 
    - netowrk: máy chủ  DNS, TCP Header Flags, DHCP DORA , IP/CIDR, ICMP, Ports 3 loại, http status, IDS/IPS, ip v4 v6 MAC Address, NAT, 
        SNMP ko mã hoá :HTTP, FTP, Telnet, SNMPv2
        HTTP Tunnelling , stateless firewall,  IDS Evasion Tactics, Kerberos
    - window : SAM ,  Windows Registr -> root keys

    - Social Engineering
        - Human-based Attacks (Tấn công dựa trên con người)
        - Computer-based Attacks (Tấn công qua máy tính)
    
    -  Web-based Hacking (Tấn công dựa trên web)
        - CSRF (Cross-Site Request Forgery)
        - Dot-Dot-Slash Attack (Directory Traversal)
        - Unicode / Un-validated Input Attack
        - SQL Injection (SQLi)
        - Buffer Overflow
        - Stack Overflow
        - Heap Overflow
        - NOP Sled (Trượt NOP)
        - Dangerous SQL Functions (Hàm C nguy hiểm)
        - Application Layer DoS (L7 DoS) -> Web Application Firewall (WAF), Rate limiting theo IP, CAPTCHA, CDN với bot management

    - Wireless Network Hacking (Tấn công mạng không dây)
        - Wireless Sniffing
        -  802.11 Specifications & Security
        - Giao thức bảo mật không dây: WEP, WPA, WPA/TKIP, WPA2, WPA3
    
    - Bluetooth Attacks
        - Bluesmacking, Bluejacking, Bluesniffing, Bluesnarfing
    
    - Trojans & Virus Types
        - Boot Sector Virus, Camo (Camouflage) Virus, Cavity Virus, Macro Virus, Multipartite Virus, Metamorphic Virus,
        Network Virus, Polymorphic Virus, Shell Virus, Stealth Virus
    
    - DoS Types 
        - SYN Attack , SYN Flood-> khắc chế bằng SYN Cookies , Firewall/IDS, giới hạn ss
        - ICMP Flood (Ping Flood)
        -  Smurf Attack dùng ICPM -> Tắt IP directed broadcast trên router, Cấu hình firewall chặn ICMP đến broadcast
        - Fraggle Attack dùng UDP ->  Tắt các dịch vụ UDP cũ (echo, chargen), chặn broadcast.
        - Ping of Death

    - một số CVE 




2. PHẦN THỰC HÀNH 
    Snort IDS, write shark , nmap ,  Span Port , tcpdump syntax
    các thuật toán mã hoá dữ liệu 
