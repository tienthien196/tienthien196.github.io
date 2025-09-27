```
DỮ LIỆU (DATA)
│
├── 1. DỮ LIỆU NGUYÊN THỦY (Primitive / Scalar Types)
│   │   → Không thể chia nhỏ hơn trong ngữ cảnh ngôn ngữ; thường được hỗ trợ bởi phần cứng hoặc runtime
│   │
│   ├── Số học:
│   │   ├── Số nguyên: int, byte, short, long, uint, bigint
│   │   ├── Số thực: float, double, half (IEEE 754)
│   │   └── Số thập phân chính xác: decimal, BigDecimal (dùng trong tài chính)
│   │
│   ├── Ký tự & văn bản:
│   │   ├── Ký tự đơn: char, code point (Unicode)
│   │   └── Chuỗi: string (immutable, first-class)
│   │
│   ├── Logic: boolean (true/false)
│   │
│   ├── Thời gian: date, time, datetime, timestamp, duration
│   │
│   ├── Giá trị đặc biệt: null, undefined, none, void
│   │
│   └── Tham chiếu: pointer, reference, handle (địa chỉ bộ nhớ hoặc đối tượng)
│
│
├── 2. CẤU TRÚC HỢP CHẤT CƠ BẢN (Built-in Composite Types)
│   │   → Được ngôn ngữ hỗ trợ trực tiếp như “nguyên thủy bậc cao”; không cần cài đặt thủ công
│   │
│   ├── Tuple: (x, y, "name") — dãy cố định, thứ tự, đa kiểu (heterogeneous)
│   ├── Record / Struct: {name: "A", age: 30} — tập hợp trường có tên (homogeneous/heterogeneous)
│   ├── Array / List: [1, 2, 3] — dãy động hoặc tĩnh, cùng kiểu (homogeneous)
│   ├── Set: {1, 2, 3} — tập hợp không trùng lặp, không thứ tự
│   └── Map / Dict / Hash: {"key": value} — ánh xạ khóa → giá trị
│
│
├── 3. CẤU TRÚC DỮ LIỆU THUẬT TOÁN (Algorithmic Data Structures)
│   │   → Dựa trên các kiểu trên, được thiết kế để tối ưu thao tác (thêm, xóa, tìm kiếm…)
│   │
│   ├── Danh sách liên kết (Linked List)
│   ├── Ngăn xếp (Stack) & Hàng đợi (Queue / Deque)
│   ├── Cây (Tree):
│   │   ├── Binary Tree, BST
│   │   ├── Trie (cây tiền tố)
│   │   ├── Heap (min/max)
│   │   └── Cây cân bằng (AVL, Red-Black, B-Tree)
│   ├── Đồ thị (Graph): có hướng / vô hướng, có trọng số
│   └── Bảng băm (Hash Table) — nền tảng cho Set/Map
│
│
├── 4. MÔ HÌNH DỮ LIỆU HƯỚNG HÀNH VI & TRỪU TƯỢNG
│   │
│   ├── Lập trình hướng đối tượng (OOP):
│   │   ├── Class / Object
│   │   ├── Encapsulation, Inheritance, Polymorphism
│   │   └── Interface / Abstract Type
│   │
│   ├── Kiểu trừu tượng (Abstract Data Type - ADT):
│   │   └── Định nghĩa qua hành vi (API), không phụ thuộc cài đặt (vd: Stack là ADT, có thể cài bằng array hoặc linked list)
│   │
│   └── Mô hình tác tử (Actor Model):
│       └── Dữ liệu sống trong các thực thể độc lập, giao tiếp qua tin nhắn (Erlang, Akka)
│
│
├── 5. MÔ HÌNH DỮ LIỆU QUAN HỆ & NGỮ NGHĨA
│   │
│   ├── Quan hệ (Relational Model):
│   │   ├── Bảng (Table), hàng (Tuple), cột (Attribute)
│   │   ├── Khóa chính, khóa ngoại
│   │   └── Phép toán quan hệ (SELECT, JOIN…)
│   │
│   ├── Mô hình thực thể-mối quan hệ (ER Model)
│   │
│   └── Dữ liệu ngữ nghĩa (Semantic Data):
│       ├── Triple: (chủ thể, vị từ, đối tượng) — RDF
│       ├── Ontology: mô tả khái niệm & quan hệ (OWL)
│       └── Knowledge Graph (Google, Wikidata)
│
│
├── 6. DỮ LIỆU HƯỚNG LUỒNG & SỰ KIỆN
│   │
│   ├── Luồng (Stream): dữ liệu liên tục theo thời gian (sensor, log, video)
│   ├── Sự kiện (Event): hành động có thời điểm (click, transaction)
│   ├── Log (immutable append-only sequence) — nền tảng của hệ thống phân tán
│   └── Kiến trúc: Event Sourcing, CQRS, Reactive Streams
│
│
├── 7. DỮ LIỆU TỰ MÔ TẢ & MANG NGỮ CẢNH
│   │
│   ├── Schema kèm dữ liệu: JSON Schema, Protocol Buffers, Avro, Parquet
│   ├── Dữ liệu có nguồn gốc (Provenance): ai tạo? khi nào? từ đâu?
│   ├── Dữ liệu mang chính sách: quyền truy cập, GDPR compliance
│   └── Capability-based data: dữ liệu đi kèm khả năng hành động
│
│
└── 8. DỮ LIỆU TRONG HỆ THỐNG THÔNG MINH & TƯƠNG LAI
    │
    ├── Vector / Embedding: biểu diễn ngữ nghĩa (word2vec, CLIP)
    ├── Tensor: mảng đa chiều (PyTorch, TensorFlow)
    ├── Biểu diễn xác suất: phân phối, Bayesian networks
    ├── Biểu diễn lai (Neuro-symbolic): kết hợp mạng neural + logic
    ├── Qubit: đơn vị thông tin lượng tử (superposition, entanglement)
    └── Dữ liệu trong hệ đa tác tử (Multi-agent systems): dữ liệu → tri thức → hành động tự trị
```