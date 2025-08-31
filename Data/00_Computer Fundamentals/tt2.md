# 🛠️ TẦNG 2: DEVELOPMENT CORE  
> *Ngôn ngữ lập trình: C++ (compiled) & Python (interpreted)*

---

## 🎯 Mục tiêu
- Hiểu cách **code được chuyển thành hành động của máy tính**
- Nắm rõ sự khác biệt giữa **compiled vs interpreted**
- Thành thạo **C++ và Python** ở mức sâu, không chỉ cú pháp
- Biết cách **kết hợp cả hai** để phát triển hệ thống hiệu quả

---

## 🔁 Tổng quan: Compiled vs Interpreted

| Đặc điểm | C++ (Compiled) | Python (Interpreted) |
|--------|----------------|----------------------|
| Cách thực thi | Biên dịch thành machine code trước khi chạy | Thông dịch từng dòng tại runtime |
| Tốc độ | Rất nhanh | Chậm hơn (do dynamic typing, GIL) |
| Memory control | Thủ công (con trỏ, new/delete) | Tự động (garbage collection) |
| Type system | Static, compile-time | Dynamic, runtime |
| Debugging | Khó hơn (segfault, memory leak) | Dễ hơn (lỗi rõ, exception) |
| Use cases | Hệ thống, game, embedded | Scripting, AI, web, automation |

> 💡 **Hiểu được sự khác biệt này → bạn biết khi nào dùng C++, khi nào dùng Python.**

---

## 1. C++ – NGÔN NGỮ BIÊN DỊCH (COMPILED)

### 1.1. Cơ chế biên dịch
- Preprocessing
  - `#include`, `#define`, `#ifdef`
- Compilation
  - Source code → Assembly → Object file (`.o`, `.obj`)
- Linking
  - Static linking vs Dynamic linking
  - Static library (`.a`, `.lib`) vs Shared library (`.so`, `.dll`)
- Executable generation
  - ELF (Linux), PE (Windows), Mach-O (macOS)

### 1.2. Cấu trúc chương trình
- `main()` function
- Header files (`.h`) vs Source files (`.cpp`)
- Include guards, `#pragma once`
- Namespaces (`std`, custom)
- Forward declaration

### 1.3. Kiểu dữ liệu & Biến
- Primitive types: `int`, `float`, `double`, `char`, `bool`
- Size of types (`sizeof`)
- `const`, `volatile`
- Type conversion: implicit vs explicit (`static_cast`, `dynamic_cast`, etc.)

### 1.4. Con trỏ & Quản lý bộ nhớ
- Con trỏ: `int*`, `void*`, `nullptr`
- Địa chỉ bộ nhớ: `&variable`
- Dereferencing: `*ptr`
- Mảng và con trỏ: `arr[i]` ≡ `*(arr + i)`
- Cấp phát động: `new` / `delete`, `new[]` / `delete[]`
- Memory leak, dangling pointer, double free
- Smart pointers (Modern C++)
  - `std::unique_ptr`
  - `std::shared_ptr`
  - `std::weak_ptr`

### 1.5. Lập trình hướng đối tượng (OOP)
- Class và Object
- Constructor / Destructor
- Copy constructor, Move constructor (C++11)
- Encapsulation: `public`, `private`, `protected`
- Inheritance
- Polymorphism
  - Virtual functions
  - Pure virtual functions / Abstract class
  - V-table
- Operator overloading

### 1.6. Template & Generic Programming
- Function templates
- Class templates
- STL (Standard Template Library)
  - Containers: `vector`, `list`, `map`, `set`, `unordered_map`
  - Iterators
  - Algorithms: `sort`, `find`, `transform`, `accumulate`
  - Function objects (functors), `std::function`, lambdas

### 1.7. C++ Modern (C++11/14/17/20)
- `auto` keyword
- Range-based `for` loop
- `nullptr` vs `NULL`
- Move semantics (`std::move`, rvalue references)
- `constexpr`
- `std::thread`, `std::async` (multithreading)
- RAII (Resource Acquisition Is Initialization)

### 1.8. Tương tác với hệ thống
- Inline Assembly (nếu cần)
- System calls (POSIX: `fork`, `exec`, `open`, `read`)
- Interfacing with C (extern "C")
- FFI (Foreign Function Interface)

---

## 2. PYTHON – NGÔN NGỮ THÔNG DỊCH (INTERPRETED)

### 2.1. Cơ chế thông dịch
- Source code → Bytecode (`.pyc`) → Python Virtual Machine (PVM)
- Interpreter: CPython (main), PyPy, Jython, IronPython
- Global Interpreter Lock (GIL)
  - Giới hạn multithreading thực sự
  - Giải pháp: multiprocessing, asyncio

### 2.2. Cấu trúc chương trình
- Module và Package
- `__name__ == "__main__"`
- Import system: `import`, `from ... import`, relative import
- `__init__.py`, `__all__`

### 2.3. Kiểu dữ liệu & Biến
- Dynamic typing
- Mutable vs Immutable: `list` vs `tuple`, `dict` vs `frozenset`
- Built-in types: `int`, `float`, `str`, `bool`, `None`
- Container types: `list`, `dict`, `tuple`, `set`
- Type hints (Python 3.5+): `: int`, `-> str`, `typing` module

### 2.4. Memory Management
- Reference counting
- Garbage collection (cyclic references)
- `id()`, `sys.getrefcount()`
- `del` statement
- Memory profiling: `tracemalloc`, `memory_profiler`

### 2.5. Lập trình hướng đối tượng (OOP)
- Class và Object
- `__init__`, `__str__`, `__repr__`
- Inheritance, MRO (Method Resolution Order)
- `super()`
- Encapsulation (ngầm, không private thật)
- Polymorphism (duck typing)
- Properties (`@property`, setters)
- Magic methods (`__add__`, `__len__`, `__getitem__`, v.v.)

### 2.6. Functional Programming
- First-class functions
- Lambda expressions
- `map`, `filter`, `reduce`
- Decorators (`@decorator`)
- Generators (`yield`)
- Context managers (`with` statement, `__enter__`, `__exit__`)

### 2.7. Module & Thư viện phổ biến
- `os`, `sys`, `subprocess` – hệ thống
- `json`, `pickle` – serialization
- `re` – regex
- `threading`, `multiprocessing`, `asyncio` – concurrency
- `requests` – HTTP
- `sqlite3` – database
- `argparse` – CLI arguments

### 2.8. Tối ưu & Debug
- `cProfile`, `timeit`
- `pdb` – debugger
- Logging (`logging` module)
- Virtual environments (`venv`, `virtualenv`)
- Packaging: `setup.py`, `pyproject.toml`, `pip`

---

## 🔗 MỐI LIÊN HỆ GIỮA C++ VÀ PYTHON

| Mục đích | Cách kết hợp |
|--------|-------------|
| **Tốc độ + Linh hoạt** | Viết core bằng C++ (nhanh), gọi từ Python (dễ dùng) |
| **AI/ML** | Model training (Python), inference engine (C++) |
| **Game** | Game logic (Python), rendering/physics (C++ trong Unreal) |
| **Hệ thống** | System calls, driver (C++), automation script (Python) |

### ✅ Cách tích hợp:
- **PyBind11** – Export C++ classes/functions to Python
- **Cython** – Viết Python như C, biên dịch thành C
- **ctypes / CFFI** – Gọi C/C++ từ Python
- **SWIG** – Tạo binding tự động

> 💡 Ví dụ:  
> - Viết thuật toán Dijkstra bằng C++ → biên dịch thành `.so` → gọi từ Python qua `ctypes`  
> - Dùng PyBind11 để expose class `NeuralNetwork` từ C++ sang Python

---

## 🧩 Nguyên lý thiết kế tầng 2

| Nguyên lý | Áp dụng |
|---------|--------|
| **Separation of Concerns** | C++ cho hiệu năng, Python cho logic điều khiển |
| **Leverage Strengths** | Dùng đúng công cụ cho đúng việc |
| **Understand the Stack** | Biết code của bạn đi qua biên dịch/thông dịch như thế nào |
| **Performance vs Productivity** | C++: performance; Python: productivity → chọn tùy bối cảnh |

---

## 🔚 Kết luận
Tầng 2 không phải là "học ngôn ngữ", mà là **hiểu cách con người giao tiếp với máy tính qua code**.

> ✅ Với **C++**, bạn **kiểm soát hoàn toàn phần cứng**.  
> ✅ Với **Python**, bạn **tập trung vào giải quyết vấn đề**.

Khi kết hợp cả hai:
- Bạn có thể **xây hệ thống hiệu quả**: phần lõi nhanh, phần giao tiếp linh hoạt
- Bạn có thể **làm AI, game, backend, systems** mà không bị giới hạn bởi ngôn ngữ

> 💡 Đây là nền tảng để bạn **chuyển lên Tầng 3 (Systems & Innovation)** với tư duy hệ thống thực sự.