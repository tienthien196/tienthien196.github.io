---
sidebar_position: 4
sidebar_label: Computer Architecture
---

# Computer Architecture

```
+---------------------+     +----------------------------+
|                     |     |                            |
|   Input Devices     |<--->|       I/O Controller       |
| (Keyboard, Mouse,   | Bus | (USB, SATA, PCIe, Network) |
|  Webcam, Scanner)   |<--->|                            |
|                     |     +-------------+--------------+
+---------------------+                   |
                                          |
                                          | System I/O Bus
                                          |
+---------------------+                   v                   +---------------------+
|                     |     +-----------------------------+   |                     |
|   Output Devices    |<--->|         GPU (Graphics       |<->|    Display /        |
| (Monitor, Printer,  | Bus |       Processing Unit)      |   |    Audio Devices    |
|  Speakers)          |<--->|                             |   |                     |
|                     |     +-----------------------------+   +---------------------+
+---------------------+                   |
                                          |
                                          | Front-Side Bus / DMI / PCIe
                                          v
                                +----------------------+
                                |       CPU            |
                                | +------------------+ |
                                | |   Control Unit   | |
                                | +------------------+ |
                                | |      ALU         | |
                                | +------------------+ |
                                | |   Registers      | |
                                | | (R0, R1, PC, SP) | |
                                | +------------------+ |
                                | |  L1 Cache (I + D)| |
                                | |  L2 Cache        | |
                                | |  L3 Cache (Shared)||
                                | +------------------+ |
                                +-----------+----------+
                                            |
                                            | CPU Memory Bus (High Speed)
                                            |
                                            v
                       +------------------------------------------+
                       |                Main Memory               |
                       | (RAM - DDR4/DDR5)                        |
                       | +------------+  +------------+           |
                       | |  Program   |  |   Data     |           |
                       | |   Code     |  |   Section  |           |
                       | +------------+  +------------+           |
                       +------------------------------------------+
                                            ^
                                            | Memory Bus
                                            |
                                            v
                     +---------------------------------------------+
                     |                Motherboard                  |
                     | +-----------------+  +--------------------+ |
                     | |   Chipset       |  |   Clock Generator  | |
                     | | (Northbridge +  |  |                    | |
                     | |  Southbridge or |  +--------------------+ |
                     | |   PCH)          |                         |
                     | |                 |                         |
                     | | - Memory Ctrl.  |                         |
                     | | - PCIe lanes    |                         |
                     | | - SATA/USB ctrl|                         |
                     | +-----------------+                         |
                     +---------------------------------------------+
                                            |
                  +------------+           | PCI Express / SATA / USB
                  |            |           |
                  |  Storage   |<----------+
                  | Devices    |
                  | (SSD, HDD, |<----------+ USB / Thunderbolt
                  |  Flash)    |
                  |            |
                  +------------+
                          
```


```
+==================================================================+
|                   CPU CORE HIỆN ĐẠI (1 nhân)                     |
|       (Dùng đồng thời tất cả kỹ thuật để đạt IPC > 3)            |
+==================================================================+

  +---------------------+
  |  Instruction Fetch  | ← Lấy lệnh từ L1i Cache
  +----------+----------+
             |
             v
  +---------------------+
  |  Instruction Decode | ← Giải mã lệnh (CISC → µops nếu cần)
  +----------+----------+
             |
             v
  +---------------------------+
  |  μop Cache / Scheduler    | ← Chuẩn bị lệnh cho pipeline
  |  (Out-of-Order Engine)    | ← Sắp xếp lại lệnh để tối ưu
  +-------------+-------------+
                |
        +-------v--------+     +-------------------------+
        |   PIPELINE     | --> |   EXECUTION UNITS (×N)  |
        | (IF → ID → EX) |     | - ALU × 4                |
        |                |     | - FPU × 2                |
        |                |     | - Load/Store Unit × 2    |
        |                |     | - Branch Unit            |
        +----------------+     +------------+------------+
                                            |
                                            v
                                 +----------------------+
                                 |    DATA CACHE (L1d)   |
                                 +-----------+-----------+
                                             |
                                             v
                                 +-----------------------+
                                 |       REGISTER FILE   |
                                 | (Rename, Bypass Logic)|
                                 +-----------------------+

                +-----------------------------------------+
                |       CÁC KỸ THUẬT CÙNG HOẠT ĐỘNG        |
                +-----------------------------------------+
                | • PIPELINE: Dây chuyền lệnh (5–14 stage)|
                | • SUPERSCALAR: 4–6 lệnh/chu kỳ          |
                | • OUT-OF-ORDER: Tối ưu thứ tự thực thi  |
                | • BRANCH PREDICTOR: Độ chính xác >95%   |
                | • SIMD (AVX/NEON): Xử lý vector         |
                | • REGISTER RENAMING: Tránh xung đột     |
                +-----------------------------------------+
```



```
+-------------------------------------------------------------+
|               ISA - Instruction Set Architecture            |
|   (Giao diện giữa phần mềm và phần cứng)                    |
+-------------------------------------------------------------+

+----------------+     +---------------------+     +-------------+
|                |     |                     |     |             |
|  Assembly Code | --> |   Machine Code      | --> |  Microcode  |
|  (ADD R1,R2,R3) |     |  (32-bit: 0x00234020)|     |  (Optional) |
|                |     |                     |     |             |
+----------------+     +----------+----------+     +-------------+
                                  |
                                  v
           +--------------------------------------------------+
           |               CPU EXECUTION FLOW                 |
           +--------------------------------------------------+
           | 1. FETCH: Lấy lệnh từ Memory → IR (Instruction Register) |
           |    [PC] → Address Bus → Memory → Data Bus → IR           |
           |                                                            |
           | 2. DECODE: Giải mã lệnh → xác định:                        |
           |    - Loại lệnh (R-type, I-type, J-type)                    |
           |    - Thanh ghi nguồn (Rs, Rt), đích (Rd)                   |
           |    - Opcode & Function field                               |
           |                                                            |
           | 3. EXECUTE: ALU thực hiện phép toán                       |
           |    Ví dụ: R1 = R2 + R3                                     |
           |                                                            |
           | 4. MEMORY ACCESS (nếu cần):                               |
           |    - LOAD: Đọc dữ liệu từ RAM                              |
           |    - STORE: Ghi dữ liệu vào RAM                            |
           |                                                            |
           | 5. WRITE BACK: Ghi kết quả vào thanh ghi (Rd)             |
           +------------------------------------------------------------+

+-----------------------------------------------------------------------+
|                        ISA COMPONENTS                                 |
+----------------------------+----------------------+---------------------+
|   R-TYPE (Register)        |   I-TYPE (Immediate) |   J-TYPE (Jump)     |
| Opcode | Rs | Rt | Rd |Sh|F| Opcode | Rs | Rt | Addr | Opcode | Target  |
| 6b     | 5b | 5b | 5b |5b|6b| 6b     | 5b | 5b | 16b    | 6b     | 26b     |
+----------------------------+----------------------+---------------------+
| EX: ADD R1,R2,R3           | EX: LW R1,4(R2)      | EX: J loop           |
| (Tính toán giữa thanh ghi) | (Tải từ bộ nhớ)      | (Nhảy đến nhãn)      |
+----------------------------+----------------------+---------------------+

+------------------------+     +-------------------------+
| Supported Data Types   |     | Addressing Modes        |
| - Byte (8-bit)         |     | - Immediate: #5         |
| - Halfword (16-bit)    |     | - Register: R1          |
| - Word (32-bit)        |     | - Base + Offset: 4(R2)  |
| - Single/Double Float  |     | - PC-relative: loop     |
+------------------------+     +-------------------------+

+-------------------------------------------------------------+
| Key Features of ISA                                         |
| - Tập lệnh (ADD, SUB, LW, SW, BEQ, J, ...)                  |
| - Số lượng thanh ghi (R0–R31)                                |
| - Định dạng lệnh (3 loại chính)                             |
| - Cách định địa chỉ (addressing modes)                      |
| - Hỗ trợ ngắt (interrupts) và ngoại lệ (exceptions)         |
| - Giao diện ABI (Application Binary Interface)              |
+-------------------------------------------------------------+
```
>[!note]
---
Computer architecture is a crucial concept in computer science. It involves designing and organizing computer systems at
the hardware level, encompassing the structure and functionality of computer components and how they interact to execute
instructions and perform tasks.

At its core, computer architecture defines the blueprint of a computer system, specifying the relationships between its
various components.
The computer's key parts include the Central Processing Unit (CPU), memory hierarchy, input/output systems, and the
interconnection structure.
The CPU confidently executes instructions that are stored in memory.
The memory hierarchy consists of different levels of storage, including registers, cache, RAM, and secondary storage,
each with varying access times and capacities.

The instruction set architecture (ISA) serves as the interface between hardware and software, defining the set of
instructions that a CPU can execute.
Having different ISAs can affect software compatibility and system performance, so it's important to consider this when
selecting a CPU.

Additionally, computer architecture incorporates parallelism and pipelining techniques to enhance processing speed.
Parallelism involves executing multiple instructions simultaneously, while pipelining divides instruction execution into
stages, enabling the concurrent processing of multiple instructions.

Interconnection structures such as buses and networks facilitate communication between components!
Input/output systems manage the interaction between the computer and external devices, ensuring seamless data transfer.

The evolution of computer architecture has seen the transition from single-core to multi-core processors, enabling
significantly improved performance through parallel processing.
The advancements in Reduced Instruction Set Computing (RISC) and Complex Instruction Set Computing (CISC) architectures
have revolutionized CPU design strategies.

As a foundational aspect of computer science, computer architecture plays a crucial role in determining how hardware
components collaborate to execute instructions and deliver computing capabilities.


