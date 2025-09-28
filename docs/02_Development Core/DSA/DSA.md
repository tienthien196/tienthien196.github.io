```

GIẢI THUẬT 
│
├── 1. [PARADIGM] ĐỆ QUY (Recursion)
│   ├── 1.1. Tính khi quay lui (Compute on return)
│   ├── 1.2. Đệ quy đuôi (Tail Recursion)
│   ├── 1.3. Phân nhánh (Binary / Multiple Recursion)
│   ├── 1.4. Làm việc khi đi xuống (Action before call)
│   ├── 1.5. Làm việc khi quay lên (Action after call)
│   ├── 1.6. Đệ quy có điều kiện chọn hướng (Conditional branching)
│   ├── 1.7. Đệ quy tăng dần (Forward recursion)
│   ├── 1.8. Đa điều kiện dừng (Multiple base cases)
│   ├── 1.9. Đệ quy lồng (Nested recursion)
│   └── 1.10. Đệ quy gọi chéo (Mutual recursion)
│
├── 2. [PARADIGM] CHIA ĐỂ TRỊ (Divide and Conquer)
│   ├── 2.1. Chia đôi – Gọi hai nửa – Gộp sau (Merge Sort, Max/Min)
│   ├── 2.2. Chia theo tính chất toán học (Lũy thừa nhanh, Binary GCD)
│   ├── 2.3. Chia – Chọn một – Không gộp (Binary Search, Peak Finding)
│   └── 2.4. Chia – Trị – Gộp với biến tích lũy (Đếm phép so sánh, đo độ sâu)
│
├── 3. [PARADIGM] THAM LAM (Greedy)
│   ├── 3.1. Sắp xếp + Chọn theo thứ tự (Activity Selection, Job Scheduling)
│   ├── 3.2. Chọn cực trị tại mỗi bước (Đổi tiền hệ chuẩn, Fractional Knapsack)
│   ├── 3.3. Duy trì ứng viên tốt nhất (Max profit 1 giao dịch)
│   └── 3.4. Tham lam ngược (Greedy from the end – Jump Game II)
│
├── 4. [PARADIGM] QUY HOẠCH ĐỘNG (Dynamic Programming)
│   ├── 4.1. Đệ quy + Memoization (Top-down)
│   ├── 4.2. Lặp + Bảng 1D (Bottom-up)
│   ├── 4.3. Tối ưu không gian (→ O(1))
│   ├── 4.4. Bảng 2D (Bottom-up cho bài 2 chiều)
│   ├── 4.5. Truy vết lời giải (Path Reconstruction)
│   ├── 4.6. DP trên cây (Tree DP)
│   ├── 4.7. DP trạng thái (State Machine DP)
│   └── 4.8. Bitmask DP (biểu diễn trạng thái bằng bit)
│
├── 5. [PARADIGM] DUYỆT & KHÁM PHÁ (Graph & State Space)
│   ├── 5.1. DFS (Depth-First Search)
│   ├── 5.2. BFS (Breadth-First Search)
│   ├── 5.3. Duyệt theo mức (Level-order)
│   ├── 5.4. Duyệt có nhớ (Memoized DFS cho trạng thái)
│   └── 5.5. Duyệt toàn bộ không gian (State-space search)
│
├── 6. [PARADIGM] BACKTRACKING CÓ CẤU TRÚC (Structured Backtracking)
│   ├── 6.1. Constraint Propagation (lan truyền ràng buộc)
│   ├── 6.2. Forward Checking (kiểm tra trước khi gọi)
│   ├── 6.3. Backjumping (quay lui nhảy có chọn lọc)
│   └── 6.4. Conflict-Directed Backjumping (dùng trong SAT solvers)
│
├── 7. [PARADIGM] THUẬT TOÁN NGẪU NHIÊN (Randomized Algorithms)
│   ├── 7.1. Las Vegas (luôn đúng, thời gian ngẫu nhiên)
│   ├── 7.2. Monte Carlo (nhanh, có xác suất sai)
│   ├── 7.3. Reservoir Sampling (lấy mẫu từ stream)
│   └── 7.4. Randomized Incremental Construction (Convex Hull, v.v.)
│
├── 8. [PARADIGM] TƯ DUY HÌNH HỌC & TOPO (Geometric & Topological)
│   ├── 8.1. Sweep Line (quét đường – tìm giao đoạn)
│   ├── 8.2. Rotating Calipers (đường kính tập lồi)
│   ├── 8.3. Plane Sweep + Event Queue
│   └── 8.4. Topological Ordering (task scheduling, build system)
│
├── 9. [PARADIGM] THUẬT TOÁN TRỰC TUYẾN (Streaming / Online)
│   ├── 9.1. Sliding Window nâng cao (median, mode – heap + hash)
│   ├── 9.2. Count-Min Sketch / Bloom Filter (xấp xỉ tập hợp)
│   ├── 9.3. Heavy Hitters (Misra-Gries – tìm phần tử phổ biến)
│   └── 9.4. Time-decayed aggregates (ưu tiên dữ liệu mới)
│
└── 10. [PARADIGM] TƯ DUY TRÒ CHƠI & ĐỐI KHÁNG (Adversarial)
    ├── 10.1. Minimax + Alpha-Beta Pruning
    ├── 10.2. Nash Equilibrium trong trò chơi rời rạc
    ├── 10.3. Zero-sum game trên đồ thị
    └── 10.4. Adversarial robustness (mở rộng sang AI/ML)

[HỖ TRỢ] KỸ THUẬT CÀI ĐẶT & TỐI ƯU
│
├── 6.1. Tiền xử lý (Preprocessing)
│   ├── Mảng tiền tố (Prefix Sum / XOR / Min / Max)
│   ├── Mảng hiệu (Difference Array)
│   └── Bảng băm tiền xử lý (Precomputed hash)
│
├── 6.2. Kỹ thuật con trỏ & cửa sổ
│   ├── Hai con trỏ (Two Pointers)
│   ├── Cửa sổ trượt (Sliding Window)
│   └── Lính canh (Sentinel – tránh kiểm tra biên)
│
├── 6.3. Quản lý trạng thái
│   ├── Cờ hiệu (Flag / Boolean marker)
│   ├── Mảng đánh dấu (visited[], used[])
│   └── Bitmask (biểu diễn tập hợp bằng bit)
│
├── 6.4. Xử lý dữ liệu đặc biệt
│   ├── Số lớn (Big Integer – cộng/trừ/nhân)
│   ├── Chuỗi lớn (so sánh, xử lý)
│   └── Phân số / Số thực an toàn (tránh lỗi làm tròn)
│
├── 6.5. An toàn & Kiểm thử
│   ├── Lập trình phòng thủ (Defensive Programming)
│   ├── Kiểm tra trường hợp biên (n=0, rỗng, âm…)
│   └── Tránh lỗi phổ biến (off-by-one, tràn số, chia 0…)
│
├── 6.6. Tối ưu phần cứng & hiệu năng
│   ├── Cache-aware / Cache-oblivious algorithms
│   ├── SIMD vectorization (AVX2/NEON)
│   ├── Branch prediction optimization
│   └── Memory pool / Arena allocation
│
├── 6.7. Xử lý dữ liệu khổng lồ
│   ├── External Sorting
│   ├── Map-Reduce pattern
│   └── Sketching & Sampling (ước lượng thay vì chính xác)
│
└── 6.8. Đảm bảo chất lượng & an toàn
    ├── Invariant checking (assert loop/đệ quy invariant)
    ├── Fuzz testing for algorithms
    └── Formal verification hints (chứng minh đúng bằng bất biến)
```