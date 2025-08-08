# Cyber Security: A Comprehensive Guide

> Tài liệu này được xây dựng để cung cấp một cái nhìn toàn diện về An ninh mạng (Cyber Security), từ các khái niệm cơ bản đến các kỹ thuật nâng cao, phục vụ mục đích lưu trữ và tham khảo cho các dự án IT. Tài liệu được thiết kế để hỗ trợ cả người mới bắt đầu và những người có kinh nghiệm muốn hệ thống hóa kiến thức. Cyber Security được xem là một phần của Application Software vì nó bao gồm các ứng dụng bảo mật, công cụ phân tích, và các giải pháp phần mềm để bảo vệ hệ thống và dữ liệu.

---

## Mục Lục

- [Giới thiệu về Cyber Security](#giới-thiệu-về-cyber-security)
- [Các khái niệm cốt lõi](#các-khái-niệm-cốt-lõi)
  - [Confidentiality, Integrity, Availability (CIA Triad)](#confidentiality-integrity-availability-cia-triad)
  - [Authentication and Authorization](#authentication-and-authorization)
  - [Encryption](#encryption)
  - [Vulnerability and Exploit](#vulnerability-and-exploit)
- [Các loại mối đe dọa an ninh mạng](#các-loại-mối-đe-dọa-an-ninh-mạng)
  - [Malware](#malware)
  - [Phishing](#phishing)
  - [DDoS Attacks](#ddos-attacks)
  - [SQL Injection and XSS](#sql-injection-and-xss)
- [Các kỹ thuật và công cụ bảo mật](#các-kỹ-thuật-và-công-cụ-bảo-mật)
  - [Intrusion Detection/Prevention Systems (IDS/IPS)](#intrusion-detection-prevention-systems-ids-ips)
  - [Penetration Testing](#penetration-testing)
  - [Security Information and Event Management (SIEM)](#security-information-and-event-management-siem)
  - [Firewalls and Endpoint Protection](#firewalls-and-endpoint-protection)
- [Checklist học tập và nghiên cứu](#checklist-học-tập-và-nghiên-cứu)
- [Công cụ đề xuất](#công-cụ-đề-xuất)
- [Kinh nghiệm thực hành](#kinh-nghiệm-thực-hành)
- [Tài liệu tham khảo](#tài-liệu-tham-khảo)

---

## Giới thiệu về Cyber Security

An ninh mạng (Cyber Security) là lĩnh vực tập trung vào việc bảo vệ hệ thống máy tính, mạng, dữ liệu, và ứng dụng khỏi các mối đe dọa như truy cập trái phép, tấn công mạng, hoặc mất dữ liệu. Trong bối cảnh **Application Software**, an ninh mạng bao gồm các phần mềm và công cụ được thiết kế để phát hiện, ngăn chặn, và xử lý các vấn đề bảo mật, từ phần mềm diệt virus đến các công cụ kiểm tra lỗ hổng.

- **Mục đích chính**:
  - Đảm bảo tính bảo mật (Confidentiality), toàn vẹn (Integrity), và sẵn sàng (Availability) của dữ liệu và hệ thống.
  - Phát hiện và phản ứng nhanh với các cuộc tấn công mạng.
  - Bảo vệ ứng dụng khỏi các lỗ hổng như SQL Injection, XSS.

- **Ứng dụng thực tế**:
  - Phần mềm diệt virus như Kaspersky, Malwarebytes.
  - Công cụ kiểm tra bảo mật web như Burp Suite.
  - Hệ thống IDS/IPS như Snort để giám sát mạng.

---

## Các khái niệm cốt lõi

### Confidentiality, Integrity, Availability (CIA Triad)
- **Mô tả**: Bộ ba CIA là nền tảng của an ninh mạng.
  - **Confidentiality**: Đảm bảo dữ liệu chỉ được truy cập bởi người có quyền.
  - **Integrity**: Đảm bảo dữ liệu không bị thay đổi trái phép.
  - **Availability**: Đảm bảo hệ thống và dữ liệu luôn sẵn sàng khi cần.
- **Ví dụ thực tế**:
  - Sử dụng HTTPS để mã hóa dữ liệu (Confidentiality).
  - Kiểm tra checksum để phát hiện thay đổi file (Integrity).
  - Load balancer để duy trì uptime server (Availability).

### Authentication and Authorization
- **Authentication**: Xác minh danh tính của người dùng hoặc hệ thống.
  - Công nghệ: Password, Multi-Factor Authentication (MFA), Biometrics.
  - Ví dụ: Đăng nhập bằng OAuth 2.0.
- **Authorization**: Quyết định quyền truy cập của người dùng.
  - Công nghệ: Role-Based Access Control (RBAC), Access Control Lists (ACL).
  - Ví dụ: Chỉ admin có quyền sửa cơ sở dữ liệu.

### Encryption
- **Mô tả**: Mã hóa dữ liệu để ngăn chặn truy cập trái phép.
- **Loại mã hóa**:
  - **Symmetric Encryption**: Sử dụng một khóa (AES, DES).
  - **Asymmetric Encryption**: Sử dụng cặp khóa công khai/riêng tư (RSA, ECC).
- **Ví dụ thực tế**:
  - Mã hóa dữ liệu trên ổ cứng bằng BitLocker (AES).
  - Sử dụng SSL/TLS cho kết nối HTTPS.

### Vulnerability and Exploit
- **Vulnerability**: Lỗ hổng trong hệ thống hoặc ứng dụng có thể bị khai thác.
  - Ví dụ: Lỗ hổng XSS trong ứng dụng web.
- **Exploit**: Mã hoặc kỹ thuật lợi dụng lỗ hổng để tấn công.
  - Ví dụ: Script khai thác SQL Injection để truy cập cơ sở dữ liệu.

---

## Các loại mối đe dọa an ninh mạng

### Malware
- **Mô tả**: Phần mềm độc hại như virus, ransomware, spyware, hoặc trojan.
- **Cách lây nhiễm**: Email, tải xuống phần mềm, lỗ hổng ứng dụng.
- **Ví dụ thực tế**: Ransomware WannaCry mã hóa dữ liệu và đòi tiền chuộc.

### Phishing
- **Mô tả**: Tấn công lừa đảo để đánh cắp thông tin nhạy cảm (mật khẩu, thẻ tín dụng).
- **Kỹ thuật**: Email giả mạo, website giả.
- **Ví dụ thực tế**: Email giả mạo từ "ngân hàng" yêu cầu nhập thông tin đăng nhập.

### DDoS Attacks
- **Mô tả**: Tấn công từ chối dịch vụ phân tán, làm quá tải hệ thống để ngăn người dùng truy cập.
- **Kỹ thuật**: Botnet, flood HTTP, SYN flood.
- **Ví dụ thực tế**: Tấn công DDoS vào website của một công ty thương mại điện tử.

### SQL Injection and XSS
- **SQL Injection**: Chèn mã SQL độc hại để thao túng cơ sở dữ liệu.
  - Ví dụ: Chèn `SELECT * FROM users WHERE id=1; DROP TABLE users;` vào form đăng nhập.
- **XSS (Cross-Site Scripting)**: Chèn mã JavaScript độc hại vào website.
  - Ví dụ: Chèn `<script>alert('Hacked');</script>` để hiển thị popup trên website.

---

## Các kỹ thuật và công cụ bảo mật

### Intrusion Detection/Prevention Systems (IDS/IPS)
- **Mô tả**: Hệ thống phát hiện (IDS) và ngăn chặn (IPS) các hành vi xâm nhập trái phép.
- **Chức năng chính**:
  - IDS: Giám sát lưu lượng mạng, phát hiện hành vi bất thường.
  - IPS: Chặn các gói tin độc hại trước khi đến đích.
- **Ví dụ thực tế**: Snort, Suricata để giám sát và bảo vệ mạng.

### Penetration Testing
- **Mô tả**: Kiểm tra thâm nhập để tìm và sửa lỗ hổng trong hệ thống hoặc ứng dụng.
- **Kỹ thuật**:
  - Network Scanning: Tìm cổng mở và dịch vụ.
  - Web Application Testing: Kiểm tra XSS, SQL Injection.
  - Social Engineering: Mô phỏng tấn công phishing.
- **Ví dụ thực tế**: Sử dụng Metasploit để kiểm tra lỗ hổng trên server.

### Security Information and Event Management (SIEM)
- **Mô tả**: Hệ thống thu thập và phân tích log để phát hiện và phản ứng với sự cố bảo mật.
- **Chức năng chính**:
  - Thu thập log từ nhiều nguồn (server, firewall, ứng dụng).
  - Phân tích thời gian thực để phát hiện mối đe dọa.
- **Ví dụ thực tế**: Splunk, ELK Stack để giám sát log.

### Firewalls and Endpoint Protection
- **Firewalls**: Kiểm soát lưu lượng mạng dựa trên quy tắc.
  - Ví dụ: pfSense, iptables trên Linux.
- **Endpoint Protection**: Bảo vệ thiết bị đầu cuối (PC, mobile) khỏi malware.
  - Ví dụ: CrowdStrike, Windows Defender.

---

## Checklist học tập và nghiên cứu

- [ ] Hiểu rõ bộ ba CIA và vai trò trong an ninh mạng.
- [ ] Nắm vững các khái niệm: Authentication, Authorization, Encryption.
- [ ] Tìm hiểu các mối đe dọa: Malware, Phishing, DDoS, SQL Injection, XSS.
- [ ] Nghiên cứu các công cụ bảo mật: Wireshark, Metasploit, Burp Suite.
- [ ] Thực hành kiểm tra lỗ hổng trên môi trường thử nghiệm như Hack The Box.
- [ ] Đọc sách *Hacking: The Art of Exploitation* của Jon Erickson.
- [ ] Tìm hiểu về IDS/IPS và cách cấu hình Snort.
- [ ] Thực hành sử dụng Kali Linux để kiểm tra bảo mật.
- [ ] Nghiên cứu về mã hóa: AES, RSA, và SSL/TLS.
- [ ] Tìm hiểu về SIEM với Splunk hoặc ELK Stack.

---

## Công cụ đề xuất

- **Wireshark**: Phân tích gói tin mạng để phát hiện lưu lượng bất thường.
- **Metasploit**: Framework kiểm tra thâm nhập.
- **Burp Suite**: Công cụ kiểm tra bảo mật ứng dụng web.
- **Kali Linux**: Hệ điều hành tích hợp công cụ bảo mật.
- **Nmap**: Quét mạng để tìm cổng mở và dịch vụ.
- **Snort**: IDS/IPS mã nguồn mở.
- **Splunk**: Hệ thống SIEM để phân tích log.
- **OWASP ZAP**: Kiểm tra lỗ hổng web (XSS, SQL Injection).
- **Hashcat**: Công cụ bẻ khóa mật khẩu.
- **OpenSSL**: Công cụ mã hóa và quản lý chứng chỉ SSL.

---

## Kinh nghiệm thực hành

1. **Phân tích lưu lượng mạng**:
   - Sử dụng Wireshark để bắt và phân tích gói tin HTTP/HTTPS.
   - Phát hiện các gói tin bất thường trong mạng nội bộ.

2. **Kiểm tra thâm nhập**:
   - Sử dụng Metasploit để kiểm tra lỗ hổng trên máy ảo (Metasploitable).
   - Thực hành kiểm tra XSS và SQL Injection với OWASP ZAP.

3. **Cấu hình bảo mật**:
   - Cài đặt và cấu hình firewall với pfSense hoặc iptables.
   - Thiết lập VPN với OpenVPN để mã hóa kết nối.

4. **Giám sát và phân tích log**:
   - Sử dụng ELK Stack để thu thập và phân tích log từ server.
   - Cấu hình Snort để phát hiện xâm nhập mạng.

5. **Dự án thực tế**:
   - Xây dựng một hệ thống giám sát bảo mật với Snort và Splunk.
   - Thực hiện pentest trên ứng dụng web tự phát triển để tìm lỗ hổng.
   - Tạo một script Python để tự động quét lỗ hổng với Nmap.

---

## Tài liệu tham khảo

1. **Sách**:
   - *Hacking: The Art of Exploitation* bởi Jon Erickson.
   - *The Web Application Hacker’s Handbook* bởi Dafydd Stuttard và Marcus Pinto.
   - *Network Security Essentials* bởi William Stallings.
   - *Practical Malware Analysis* bởi Michael Sikorski và Andrew Honig.
2. **Khóa học trực tuyến**:
   - Udemy: *The Complete Cyber Security Course* bởi Nathan House.
   - Coursera: *Cybersecurity Specialization* bởi University of Maryland.
   - TryHackMe: Các bài thực hành bảo mật thực tế.
3. **Website**:
   - OWASP: https://owasp.org/
   - NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
   - Metasploit Documentation: https://docs.metasploit.com/
4. **Tài nguyên cộng đồng**:
   - Stack Overflow: Câu hỏi và trả lời về an ninh mạng.
   - Reddit: r/cybersecurity, r/netsec.
   - Hack The Box: https://www.hackthebox.com/ (môi trường thực hành pentest).

---

> **Lưu ý**: Tài liệu này sẽ được cập nhật liên tục để bổ sung các khái niệm mới, công cụ, và kinh nghiệm thực tế. Nếu bạn có đề xuất hoặc cần thêm chi tiết, hãy liên hệ với **@author**!