Hiểu từ khi bật nguồn → hệ điều hành chạy → dữ liệu đi qua mạng → chương trình thực thi 
# 🧱 TẦNG 1: HIỂU BẢN CHẤT MÁY TÍNH  
> *Computer Architecture & Computer Networks – Bản đồ khái niệm từ tổng quát đến chi tiết*

---

## 1. COMPUTER ARCHITECTURE  
*Thiết kế và hoạt động bên trong của máy tính*

### 1.1. Digital Logic (Lô-gic số)
- Boolean Algebra
  - AND, OR, NOT, XOR
  - NAND, NOR (universal gates)
  - Truth tables
  - Boolean expressions
  - De Morgan's Laws
- Logic Gates
  - Transistor as switch
  - CMOS technology
  - Gate delay, fan-out
- Combinational Circuits
  - Multiplexer (MUX)
  - Demultiplexer (DEMUX)
  - Decoder
  - Encoder
  - Adder (Half Adder, Full Adder)
  - Arithmetic Logic Unit (ALU) – basic design
- Sequential Circuits
  - Latch (SR Latch)
  - Flip-Flop (D Flip-Flop, JK Flip-Flop)
  - Clock signal
  - Synchronous vs Asynchronous circuits
  - Register
  - Shift Register
  - Counter (Binary Counter, Ring Counter)

### 1.2. Processor Design (Thiết kế bộ xử lý)
- Central Processing Unit (CPU)
  - Control Unit (CU)
  - Arithmetic Logic Unit (ALU)
  - Registers (General-purpose, PC, IR, ACC, SP)
- Datapath
  - Instruction fetch, decode, execute
  - Bus system (data bus, address bus, control bus)
- Instruction Set Architecture (ISA)
  - RISC vs CISC
  - x86, ARM, RISC-V
  - Instruction formats (opcode, operands)
  - Addressing modes (immediate, direct, indirect, indexed)
  - Assembly language
    - Mnemonics
    - Labels, directives
    - Assembler (two-pass)
- Control Unit Design
  - Hardwired control
  - Microprogrammed control
  - Microcode

### 1.3. Memory Hierarchy
- Memory types
  - Volatile vs Non-volatile
  - RAM (DRAM, SRAM)
  - ROM (PROM, EPROM, EEPROM, Flash)
- Memory Organization
  - Address space
  - Byte addressing
  - Endianness (Little-endian, Big-endian)
  - Memory-mapped I/O
- Cache Memory
  - Cache hit / miss
  - Hit rate, miss penalty
  - Cache mapping (Direct-mapped, Fully associative, Set-associative)
  - Replacement policies (LRU, FIFO, Random)
  - Write policies (Write-through, Write-back)
  - Cache coherence (in multi-core)
- Virtual Memory
  - Page, Frame
  - Page table
  - TLB (Translation Lookaside Buffer)
  - Paging, segmentation
  - Page fault
  - Demand paging
  - Working set model

### 1.4. Storage Systems
- Secondary storage
  - Hard Disk Drive (HDD)
    - Platter, track, sector
    - Seek time, rotational latency, transfer time
  - Solid State Drive (SSD)
    - NAND flash
    - Wear leveling
    - TRIM command
- Tertiary storage
  - Magnetic tape
  - Optical storage (CD, DVD, Blu-ray)

### 1.5. Input/Output (I/O) Systems
- I/O interfaces
  - Programmed I/O
  - Interrupt-driven I/O
  - Direct Memory Access (DMA)
- I/O controllers
- Buses
  - System bus
  - Expansion buses (PCI, PCIe, USB)
- Interrupts
  - Interrupt vector table
  - Interrupt service routine (ISR)
  - Maskable vs Non-maskable interrupts

### 1.6. Performance & Parallelism
- CPU Performance
  - Clock cycle, clock rate
  - CPI (Cycles Per Instruction)
  - MIPS, FLOPS
  - Amdahl's Law
- Pipelining
  - Pipeline stages (IF, ID, EX, MEM, WB)
  - Pipeline hazards
    - Structural hazard
    - Data hazard (forwarding, stalling)
    - Control hazard (branch prediction)
- Parallel Architectures
  - Multi-core processors
  - SIMD (Single Instruction, Multiple Data)
  - Superscalar, Out-of-order execution
  - SISD, SIMD, MISD, MIMD (Flynn's Taxonomy)

---

## 2. COMPUTER NETWORKS  
*Hệ thống truyền thông giữa các máy tính*

### 2.1. Network Models
- OSI Model (7 layers)
  1. Physical Layer
  2. Data Link Layer
  3. Network Layer
  4. Transport Layer
  5. Session Layer
  6. Presentation Layer
  7. Application Layer
- TCP/IP Model (4 layers)
  1. Link Layer
  2. Internet Layer
  3. Transport Layer
  4. Application Layer
- Encapsulation / Decapsulation
- Protocol data unit (PDU) per layer

### 2.2. Physical Layer
- Transmission media
  - Twisted pair (UTP, STP)
  - Coaxial cable
  - Fiber optic (single-mode, multi-mode)
  - Wireless (radio, microwave, infrared)
- Signal encoding
  - Analog vs Digital signals
  - Modulation (AM, FM, PM)
  - Line coding (NRZ, Manchester, etc.)
- Bandwidth, throughput, latency
- Multiplexing
  - FDM, TDM, WDM

### 2.3. Data Link Layer
- Framing
  - Byte stuffing, bit stuffing
- Error detection
  - Parity check
  - Checksum
  - CRC (Cyclic Redundancy Check)
- Error correction
  - Hamming code
- Flow control
  - Stop-and-Wait
  - Sliding Window (Go-Back-N, Selective Repeat)
- Medium Access Control (MAC)
  - CSMA/CD (Ethernet)
  - CSMA/CA (Wi-Fi)
  - Token Ring
- LAN technologies
  - Ethernet (IEEE 802.3)
  - MAC address
  - Switch vs Hub
  - VLAN

### 2.4. Network Layer
- IP (Internet Protocol)
  - IPv4 vs IPv6
  - IP address (classful, CIDR)
  - Subnetting, supernetting
  - Private IP, public IP
  - NAT (Network Address Translation)
- Routing
  - Forwarding vs Routing
  - Routing tables
  - Static vs Dynamic routing
  - Distance Vector (RIP)
  - Link State (OSPF)
  - Path Vector (BGP)
- ICMP (Internet Control Message Protocol)
  - Ping, Traceroute
- ARP (Address Resolution Protocol)
  - MAC-to-IP mapping
- DHCP (Dynamic Host Configuration Protocol)
  - IP assignment process

### 2.5. Transport Layer
- End-to-end communication
- UDP (User Datagram Protocol)
  - Connectionless
  - No reliability
  - Use cases: DNS, VoIP, video streaming
- TCP (Transmission Control Protocol)
  - Connection-oriented
  - Three-way handshake (SYN, SYN-ACK, ACK)
  - Sequence numbers, acknowledgment
  - Flow control (sliding window)
  - Congestion control
    - Slow start
    - Congestion avoidance
    - Fast retransmit, fast recovery
  - Retransmission, timeout
- Port numbers
  - Well-known ports (HTTP:80, HTTPS:443, etc.)
  - Ephemeral ports
- Socket programming
  - Client-server model
  - `socket()`, `bind()`, `listen()`, `accept()`, `connect()`, `send()`, `recv()`

### 2.6. Application Layer
- DNS (Domain Name System)
  - Hierarchical structure (root, TLD, authoritative)
  - DNS record types (A, AAAA, CNAME, MX, TXT)
  - Recursive vs Iterative queries
  - DNS caching
- HTTP / HTTPS
  - Request methods (GET, POST, PUT, DELETE)
  - Status codes (200, 404, 500, etc.)
  - Headers, body
  - Persistent vs non-persistent connections
  - Cookies, sessions
  - TLS/SSL handshake
- Email protocols
  - SMTP (Simple Mail Transfer Protocol)
  - POP3, IMAP
- WebSockets
  - Full-duplex communication
  - Use in real-time apps (chat, games)
- APIs (REST, gRPC)

### 2.7. Network Security (Basic)
- Encryption
  - Symmetric (AES)
  - Asymmetric (RSA)
  - TLS/SSL
- Firewalls
  - Packet filtering
  - Stateful inspection
- VPN (Virtual Private Network)
- DDoS attacks, phishing, malware

### 2.8. Advanced Concepts
- Quality of Service (QoS)
- Software-Defined Networking (SDN)
- Network Function Virtualization (NFV)
- Content Delivery Networks (CDN)
- Peer-to-Peer (P2P) networks
- Cloud networking (VPC, load balancer, NAT gateway)

---

## 🧩 Mối liên hệ giữa 2 lĩnh vực

| Computer Architecture | ↔ | Computer Networks |
|------------------------|---|-------------------|
| CPU performance affects packet processing | ←→ | Network speed affects system responsiveness |
| Cache efficiency impacts network stack | ←→ | Latency affects real-time computation |
| DMA reduces CPU load for I/O | ←→ | High-throughput networks require fast memory access |
| Multi-core systems handle concurrent connections | ←→ | Parallelism in networking (e.g., HTTP/2, QUIC) |

> ✅ **Hiểu cả hai → bạn có thể thiết kế hệ thống hiệu quả, tối ưu từ phần cứng đến phần mềm.**

---

## 🔚 Kết luận
Tầng 1 không phải là "môn học", mà là **bản chất của mọi hệ thống số**.  
Nắm vững các khái niệm trên → bạn có thể:
- Đọc hiểu bất kỳ hệ thống nào (AI, blockchain, game engine)
- Tối ưu hiệu năng
- Debug sâu (từ segfault đến network timeout)
- Tự xây dựng hệ thống từ đầu (như OS, CPU giả, network stack)

> 💡 Đây là nền tảng để bạn **không bị giới hạn bởi công nghệ mới**, vì bạn luôn hiểu **nó hoạt động vì sao**.