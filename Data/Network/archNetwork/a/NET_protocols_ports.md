# 🌐 Internet Protocols, Ports & Networking – Resource for Developers

## 1. Internet Protocols Overview
Internet protocols are a **set of rules and conventions** that govern how data is transmitted and received over the Internet.  
They define standards for communication between devices and networks.

---

## 2. What is Protocol?
A **protocol** is a standardized set of rules that allow two or more entities in a communication system to transmit information.

Examples: HTTP, TCP, UDP, FTP, etc.

---

## 3. What is a Network Port?
A **network port** is a communication endpoint in a computer network.  
It is a **software construct** that allows devices or applications to send and receive data.

- Port numbers are **16-bit unsigned integers** → range from 0 to 65,535.  
- Each port number is associated with a **specific protocol or service**.

👉 Example:  
- HTTP → Port 80  
- HTTPS → Port 443  
- FTP → Port 21  

---

## 4. Port Numbers in Action
When a communication arrives at a server:
- **IP address** identifies the host.  
- **Port number** identifies the specific service/process.

📌 Example:  
- FTP (Port 21) for file transfers.  
- HTTP (Port 80) for websites.  
- SMTP (Port 25) for email transfer.  

---

## 5. Why are Ports Important?
Ports allow **multiple types of traffic** to flow simultaneously without confusion.

Example:  
- Bob sends Alice an MP3 via FTP (Port 21).  
- At the same time, Alice loads a website via HTTP (Port 80).  
- Even though both streams travel over the same Wi-Fi, the OS knows which application to send the data to.

---

## 6. OSI Model & Ports
The OSI model divides Internet communication into **7 layers**.

- **Ports are part of the Transport Layer (Layer 4)**.  
- Only transport protocols (TCP, UDP) define port numbers.  
- The **Network Layer (Layer 3, e.g., IP)** is unaware of ports (only handles IP addresses).

---

## 7. OSI Model Protocols

### 🔹 Layer 1: Physical Layer
Examples: USB, Ethernet, Wi-Fi PHY, DSL, ISDN, Bluetooth

### 🔹 Layer 2: Data Link Layer
Examples: Ethernet, PPP, VLAN, STP, MAC, LACP, HDLC

### 🔹 Layer 3: Network Layer
Examples: IPv4, IPv6, ICMP, IPSec, OSPF, MPLS, NAT, RIP, BGP

### 🔹 Layer 4: Transport Layer
Examples: TCP, UDP, SCTP, DCCP

### 🔹 Layer 5: Session Layer
Examples: PPTP, SMB, RPC, NFS, PAP

### 🔹 Layer 6: Presentation Layer
Examples: TLS, SSL, AFP

### 🔹 Layer 7: Application Layer
Examples: HTTP, HTTPS, DNS, FTP, SMTP, POP3, SSH, SNMP, Telnet, BitTorrent

---

## 8. Common Ports and Services

| Port | Protocol/Service | Description | Transport |
|------|-----------------|-------------|-----------|
| 20-21 | FTP | File Transfer Protocol | TCP |
| 22 | SSH | Secure Shell (remote login, file transfer, tunneling) | TCP |
| 23 | Telnet | Remote text communication (insecure) | TCP/UDP |
| 25 | SMTP | Email transfer between servers | TCP |
| 53 | DNS | Domain Name System (hostname ↔ IP) | TCP/UDP |
| 69 | TFTP | Trivial File Transfer Protocol | UDP |
| 80 | HTTP | Unencrypted web traffic | TCP |
| 110 | POP3 | Email retrieval from server | TCP/UDP |
| 123 | NTP | Network Time Protocol | UDP |
| 135 | DCE/RPC | Endpoint Mapper | TCP/UDP |
| 139 | NetBIOS | Session Service | TCP/UDP |
| 161 | SNMP | Network management protocol | TCP/UDP |
| 389 | LDAP | Directory Access Protocol | TCP/UDP |
| 443 | HTTPS | Encrypted web traffic | TCP/UDP |
| 445 | SMB | Microsoft Directory Services & file sharing | TCP/UDP |
| 465 | SMTP (Secure) | Secure mail submission | TCP |
| 514 | Syslog | Logging protocol | UDP |
| 587 | SMTP | Email submission | TCP |
| 636 | LDAPS | Secure LDAP over SSL | TCP/UDP |
| 993 | IMAP | Secure mail retrieval | TCP |
| 995 | POP3 (Secure) | Secure email download | TCP/UDP |
| 1433 | MSSQL | Microsoft SQL Server | TCP |
| 1521 | Oracle DB | Oracle Database | TCP |
| 3306 | MySQL | MySQL Database | TCP |
| 3389 | RDP | Remote Desktop Protocol | TCP |
| 5060 | SIP | Session Initiation Protocol (VoIP) | TCP/UDP |
| 6881–6999 | BitTorrent | Peer-to-peer sharing | TCP/UDP |

---

## 9. Security Notes on Ports
- Open ports can be **attack vectors** if not properly secured.  
- Use **firewalls** to restrict access.  
- Prefer **encrypted protocols** (e.g., HTTPS over HTTP, SFTP over FTP).  

---

## 10. Summary
- Protocols define communication rules.  
- Ports act as "doors" into a machine’s services.  
- OSI Model explains where protocols & ports operate.  
- Common services map to well-known ports (0–1023).  


### ***NOTE***
> ***TÀI LIỆU BUILD BY @TIẾN THIỆN*** [(truy cập chi tiết)](https://tienthien196.github.io/ecosys.portfolioBNJ/)