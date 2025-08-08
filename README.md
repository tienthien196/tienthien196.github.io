# Ecosystem Support and Build by Me !!

> Project được build bởi **@author** với mục đích lưu trữ toàn bộ checklist từ **BNJ**.

---

## Mục Lục

- [HomePage](/www/ecosystem.html)
- HardWare (Update soon)
- Computer Science
  - 1\. [Computer Architecture](/CSLIist/Architecture/ComputerArchitecture.md)
  - 2\. [Computer Network](/CSLIist/Network/ComputerNetwork.md)
  - 3\. Software
    - [System Software](/CSLIist/Software/SysTem/SystemSoftware.md)
      - 1\. [OperatorSystem](/CSLIist/Software/SysTem/OperatorSystem.md)
      - 2\. [Compiler](/CSLIist/Software/SysTem/Compiler.md)
      - 3\. [Devices IO Driver](/CSLIist/Software/SysTem/Devices%20IO%20Driver.md)
    - [Application Software](/CSLIist/Software/App/ApplicationSoftware.md)
      - 1\. Build Source
        - AI Agent
            1. [AI](/CSLIist/Software/App/BuildSource/AI_Agent/AI-Guide.md)
            2. [Agent](/CSLIist/Software/App/BuildSource/AI_Agent/AI-Agent-Guide.md)
        - [Client](/CSLIist/Software/App/BuildSource/Client/Client.md)
        - [Server](CSLIist/Software/App/BuildSourceServer/Server.md)
        - [WWW](CSLIist/Software/App/BuildSource/WWW/Web3-Guide.md)
        - Tools
      - 2\. [Cyber Security](/CSLIist/Software/App/CyberSecurity.md)

---

## HardWare

*Đang được cập nhật...*

---

## Computer Science

### 1. Computer Architecture

- **Mô tả**: Lý thuyết trừu tượng về cách tổ chức và hoạt động của phần cứng máy tính, bao gồm CPU, bộ nhớ, và các thành phần liên quan.
- **Checklist**:
  - [ ] Hiểu về các thành phần chính: CPU, RAM, Cache, Bus.

  - [ ] Tìm hiểu các mô hình kiến trúc: Von Neumann, Harvard.

  - [ ] Nghiên cứu về pipeline, superscalar, và parallel processing.

  - [ ] Tài liệu tham khảo: Sách *Computer Organization and Design* của Patterson & Hennessy.
- **Công cụ đề xuất**:
  - Logisim: Phần mềm mô phỏng mạch logic.
  - Simulators: RISC-V, MIPS simulators.
- **Kinh nghiệm**:
  - Thực hành thiết kế mạch đơn giản để hiểu cách hoạt động của CPU.
  - Tìm hiểu cách tối ưu hóa hiệu suất qua các kỹ thuật như branch prediction.

### 2. Computer Network

- **Mô tả**: Lý thuyết trừu tượng về mạng máy tính, giao thức, và cách các thiết bị kết nối, truyền thông.
- **Checklist**:
  - [ ] Nắm vững mô hình OSI và TCP/IP.

  - [ ] Tìm hiểu các giao thức: HTTP, DNS, FTP, TCP, UDP.

  - [ ] Hiểu về cấu trúc mạng: LAN, WAN, VPN.

  - [ ] Tài liệu tham khảo: Sách *Computer Networking: A Top-Down Approach* của Kurose & Ross.
- **Công cụ đề xuất**:
  - Wireshark: Phân tích gói tin mạng.
  - Cisco Packet Tracer: Mô phỏng mạng.
- **Kinh nghiệm**:
  - Thực hành thiết lập mạng nội bộ (LAN) nhỏ.
  - Phân tích lưu lượng mạng để hiểu cách các giao thức hoạt động.

### 3. Software

#### System Software

- **Mô tả**: Phần mềm hệ thống cung cấp nền tảng cho hoạt động của máy tính, bao gồm hệ điều hành, trình biên dịch, và driver.

##### 1. OS

- **Mô tả**: Hệ điều hành quản lý tài nguyên phần cứng và cung cấp giao diện cho phần mềm ứng dụng.
- **Checklist**:
  - [ ] Tìm hiểu các thành phần: Kernel, File System, Process Management.

  - [ ] Nghiên cứu các hệ điều hành: Linux, Windows, macOS.

  - [ ] Tài liệu tham khảo: Sách *Operating System Concepts* của Silberschatz.
- **Công cụ đề xuất**:
  - VirtualBox: Mô phỏng và thử nghiệm các hệ điều hành.
  - Linux distributions (Ubuntu, Fedora): Thực hành quản trị hệ thống.
- **Kinh nghiệm**:
  - Cài đặt và cấu hình Linux trên máy ảo.
  - Tìm hiểu cách viết shell script để tự động hóa tác vụ.

##### 2. Compiler

- **Mô tả**: Trình biên dịch chuyển đổi mã nguồn thành mã máy tính có thể thực thi.
- **Checklist**:
  - [ ] Hiểu về các giai đoạn biên dịch: Lexical Analysis, Syntax Analysis, Code Generation.

  - [ ] Tìm hiểu các trình biên dịch: GCC, Clang.

  - [ ] Tài liệu tham khảo: Sách *Compilers: Principles, Techniques, and Tools* của Aho.
- **Công cụ đề xuất**:
  - GCC: Biên dịch C/C++.
  - LLVM: Nghiên cứu tối ưu hóa mã.
- **Kinh nghiệm**:
  - Thử viết một trình biên dịch đơn giản cho ngôn ngữ mini.
  - Tìm hiểu cách tối ưu hóa mã máy.

##### 3. Devices IO Driver

- **Mô tả**: Driver điều khiển giao tiếp giữa phần cứng và hệ điều hành.
- **Checklist**:
  - [ ] Hiểu về driver: Kernel modules, User-space drivers.

  - [ ] Tìm hiểu cách viết driver cho Linux.

  - [ ] Tài liệu tham khảo: *Linux Device Drivers* của Corbet.
- **Công cụ đề xuất**:
  - Linux Kernel Module Programming.
  - QEMU: Mô phỏng thiết bị phần cứng.
- **Kinh nghiệm**:
  - Thực hành viết module kernel đơn giản.
  - Tìm hiểu cách debug driver.

#### Application Software

- **Mô tả**: Phần mềm ứng dụng phục vụ người dùng cuối, bao gồm AI, client, server, web, và các công cụ.

##### 1. Build Source

###### AI Agent

- **Mô tả**: Các agent AI tự động hóa tác vụ hoặc hỗ trợ ra quyết định.
- **Checklist**:
  - [ ] Tìm hiểu các framework: TensorFlow, PyTorch.

  - [ ] Hiểu về các thuật toán: Neural Networks, Reinforcement Learning.

  - [ ] Tài liệu tham khảo: *Deep Learning* của Goodfellow.
- **Công cụ đề xuất**:
  - Jupyter Notebook: Thực hành AI/ML.
  - Google Colab: Hỗ trợ GPU miễn phí.
- **Kinh nghiệm**:
  - Xây dựng một mô hình AI đơn giản (ví dụ: phân loại ảnh).
  - Tìm hiểu cách triển khai AI agent trên cloud.

###### Client

- **Mô tả**: Chủ yếu tập trung vào phát triển game và ứng dụng client-side.
- **Checklist**:
  - [ ] Tìm hiểu các engine game: Unity, Unreal Engine.

  - [ ] Hiểu về giao diện người dùng: SDL, OpenGL.

  - [ ] Tài liệu tham khảo: *Game Programming Patterns* của Robert Nystrom.
- **Công cụ đề xuất**:
  - Unity: Phát triển game 2D/3D.
  - Godot: Engine mã nguồn mở.
- **Kinh nghiệm**:
  - Thực hành xây dựng game đơn giản (ví dụ: Flappy Bird clone).
  - Tìm hiểu về optimal rendering techniques.

###### Server

- **Mô tả**: Xây dựng và quản lý backend server.
- **Checklist**:
  - [ ] Tìm hiểu các framework: Node.js, Django, Spring.

  - [ ] Hiểu về API: REST, GraphQL.

  - [ ] Tài liệu tham khảo: *Designing Data-Intensive Applications* của Kleppmann.
- **Công cụ đề xuất**:
  - Postman: Kiểm tra API.
  - Docker: Triển khai containerized server.
- **Kinh nghiệm**:
  - Xây dựng một REST API đơn giản.
  - Tìm hiểu cách scale server với load balancer.

###### WWW

- **Mô tả**: Nghiên cứu đặc biệt về Web 3, blockchain, và các công nghệ web hiện đại.
- **Checklist**:
  - [ ] Tìm hiểu về Web 3: Ethereum, IPFS, Smart Contracts.

  - [ ] Hiểu về frontend: React, Vue.js.

  - [ ] Tài liệu tham khảo: *Mastering Blockchain* của Imran Bashir.
- **Công cụ đề xuất**:
  - Hardhat: Phát triển smart contract.
  - IPFS: Lưu trữ phi tập trung.
- **Kinh nghiệm**:
  - Xây dựng một DApp đơn giản trên Ethereum.
  - Tìm hiểu về decentralized identity.

###### Tools

- **Mô tả**: Các công cụ hỗ trợ phát triển và quản lý dự án.
- **Checklist**:
  - [ ] Tìm hiểu về version control: Git, GitHub.

  - [ ] Hiểu về CI/CD: Jenkins, GitHub Actions.
- **Công cụ đề xuất**:
  - VS Code: IDE mạnh mẽ.
  - Jira: Quản lý dự án.
- **Kinh nghiệm**:
  - Thiết lập pipeline CI/CD cho dự án.
  - Tìm hiểu cách sử dụng Git hiệu quả.

##### 2. Cyber Security

- **Mô tả**: Bảo mật hệ thống và ứng dụng, phòng chống tấn công mạng.
- **Checklist**:
  - [ ] Tìm hiểu các khái niệm: Encryption, Authentication, Penetration Testing.

  - [ ] Hiểu về các công cụ: Metasploit, Burp Suite.

  - [ ] Tài liệu tham khảo: *Hacking: The Art of Exploitation* của Jon Erickson.
- **Công cụ đề xuất**:
  - Kali Linux: Hệ điều hành cho pentesting.
  - Nmap: Quét mạng.
- **Kinh nghiệm**:
  - Thực hành pentesting trên môi trường thử nghiệm (như Hack The Box).
  - Tìm hiểu cách phát hiện và vá lỗ hổng XSS, SQL Injection.