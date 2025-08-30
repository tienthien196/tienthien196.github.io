# app.py
from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

# Dữ liệu mẫu sách (có thể thay bằng file JSON hoặc database)
books = [
    {
        "id": 1,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "year": 1960,
        "isbn": "978-0-06-112008-4",
        "pages": 281,
        "status": "Available",
        "cover": "https://placehold.co/120x180/4f46e5/ffffff?text=TKAM",
        "addedDate": "2023-01-15"
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian Fiction",
        "year": 1949,
        "isbn": "978-0-452-28423-4",
        "pages": 328,
        "status": "Checked Out",
        "cover": "https://placehold.co/120x180/059669/ffffff?text=1984",
        "addedDate": "2023-02-20"
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic Literature",
        "year": 1925,
        "isbn": "978-0-7432-7356-5",
        "pages": 180,
        "status": "Available",
        "cover": "https://placehold.co/120x180/dc2626/ffffff?text=Gatsby",
        "addedDate": "2023-03-10"
    },
    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "year": 1813,
        "isbn": "978-0-14-143951-8",
        "pages": 432,
        "status": "Available",
        "cover": "https://placehold.co/120x180/7c3aed/ffffff?text=P&P",
        "addedDate": "2023-04-05"
    },
    {
        "id": 5,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Fiction",
        "year": 1951,
        "isbn": "978-0-316-76948-0",
        "pages": 277,
        "status": "Reserved",
        "cover": "https://placehold.co/120x180/ea580c/ffffff?text=Catcher",
        "addedDate": "2023-05-12"
    }
]

def admin_page():
    return '''
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quản Lý Sách</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    body {
      font-family: 'Inter', sans-serif;
    }
    .fade-in {
      animation: fadeIn 0.5s ease-in;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .book-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
    }
    .status-available {
      background-color: #dcfce7;
      color: #166534;
    }
    .status-checked-out {
      background-color: #fee2e2;
      color: #991b1b;
    }
    .status-reserved {
      background-color: #fef3c7;
      color: #92400e;
    }
  </style>
</head>
<body class="bg-gray-50 min-h-screen">
  <div class="container mx-auto px-4 py-8">
    <!-- Header -->
    <div class="bg-white rounded-lg shadow-lg p-6 mb-8">
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 class="text-3xl font-bold text-gray-800 flex items-center gap-3">
            <i class="fas fa-book-open text-blue-600"></i>
            Quản Lý Thư Viện (Admin)
          </h1>
          <p class="text-gray-600 mt-1">Quản lý và theo dõi tất cả sách trong hệ thống</p>
        </div>
        <button onclick="openModal()" class="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-3 rounded-lg transition duration-200 flex items-center gap-2 shadow-md hover:shadow-lg">
          <i class="fas fa-plus"></i>
          Thêm Sách Mới
        </button>
      </div>
    </div>

    <!-- Search and Filters -->
    <div class="bg-white rounded-lg shadow-lg p-6 mb-8">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div class="relative">
          <i class="fas fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
          <input type="text" id="searchInput" oninput="filterBooks()" placeholder="Tìm kiếm sách..." 
                 class="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
        </div>
        
        <select id="genreFilter" onchange="filterBooks()" class="px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
          <option value="Tất cả">Tất cả thể loại</option>
          <option value="Fiction">Tiểu thuyết</option>
          <option value="Classic Literature">Văn học kinh điển</option>
          <option value="Dystopian Fiction">Tiểu thuyết phản utopia</option>
          <option value="Romance">Lãng mạn</option>
          <option value="Science Fiction">Khoa học viễn tưởng</option>
        </select>
        
        <select id="statusFilter" onchange="filterBooks()" class="px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
          <option value="Tất cả">Tất cả trạng thái</option>
          <option value="Available">Có sẵn</option>
          <option value="Checked Out">Đã mượn</option>
          <option value="Reserved">Đã đặt</option>
        </select>
        
        <div class="flex gap-2">
          <button onclick="exportData()" class="flex-1 bg-green-600 hover:bg-green-700 text-white px-4 py-3 rounded-lg transition duration-200 flex items-center justify-center gap-2">
            <i class="fas fa-download"></i>
            Xuất
          </button>
          <button onclick="importData()" class="flex-1 bg-purple-600 hover:bg-purple-700 text-white px-4 py-3 rounded-lg transition duration-200 flex items-center justify-center gap-2">
            <i class="fas fa-upload"></i>
            Nhập
          </button>
        </div>
      </div>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
      <div class="bg-white rounded-lg shadow-lg p-6 fade-in">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Tổng số sách</p>
            <p id="totalBooks" class="text-3xl font-bold text-gray-800">0</p>
          </div>
          <div class="bg-blue-100 p-3 rounded-full">
            <i class="fas fa-book text-blue-600 text-2xl"></i>
          </div>
        </div>
      </div>
      
      <div class="bg-white rounded-lg shadow-lg p-6 fade-in">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Có sẵn</p>
            <p id="availableBooks" class="text-3xl font-bold text-green-600">0</p>
          </div>
          <div class="bg-green-100 p-3 rounded-full">
            <i class="fas fa-check-circle text-green-600 text-2xl"></i>
          </div>
        </div>
      </div>
      
      <div class="bg-white rounded-lg shadow-lg p-6 fade-in">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Đang mượn</p>
            <p id="checkedOutBooks" class="text-3xl font-bold text-red-600">0</p>
          </div>
          <div class="bg-red-100 p-3 rounded-full">
            <i class="fas fa-exchange-alt text-red-600 text-2xl"></i>
          </div>
        </div>
      </div>
      
      <div class="bg-white rounded-lg shadow-lg p-6 fade-in">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Đã đặt</p>
            <p id="reservedBooks" class="text-3xl font-bold text-yellow-600">0</p>
          </div>
          <div class="bg-yellow-100 p-3 rounded-full">
            <i class="fas fa-clock text-yellow-600 text-2xl"></i>
          </div>
        </div>
      </div>
    </div>

    <!-- Books Grid -->
    <div id="booksContainer" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
      <!-- Books will be inserted here by JavaScript -->
    </div>

    <!-- Empty State -->
    <div id="emptyState" class="hidden text-center py-16">
      <i class="fas fa-book-open text-gray-300 text-6xl mb-4"></i>
      <h3 class="text-xl font-semibold text-gray-500 mb-2">Không tìm thấy sách</h3>
      <p class="text-gray-400">Hãy thử thay đổi bộ lọc hoặc thêm sách mới</p>
    </div>
  </div>

  <!-- Add/Edit Book Modal -->
  <div id="bookModal" class="fixed inset-0 bg-black bg-opacity-50 hidden flex items-center justify-center p-4 z-50">
    <div class="bg-white rounded-lg shadow-xl max-w-2xl w-full max-h-screen overflow-y-auto">
      <div class="p-6 border-b border-gray-200">
        <div class="flex justify-between items-center">
          <h2 id="modalTitle" class="text-2xl font-bold text-gray-800">Thêm Sách Mới</h2>
          <button onclick="closeModal()" class="text-gray-500 hover:text-gray-700 text-2xl">&times;</button>
        </div>
      </div>
      
      <form id="bookForm" class="p-6">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Tiêu đề *</label>
              <input type="text" id="title" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Tác giả *</label>
              <input type="text" id="author" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Thể loại *</label>
              <select id="genre" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
                <option value="">Chọn thể loại</option>
                <option value="Fiction">Tiểu thuyết</option>
                <option value="Classic Literature">Văn học kinh điển</option>
                <option value="Dystopian Fiction">Tiểu thuyết phản utopia</option>
                <option value="Romance">Lãng mạn</option>
                <option value="Science Fiction">Khoa học viễn tưởng</option>
              </select>
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Năm xuất bản *</label>
              <input type="number" id="year" required min="1000" max="2024" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
            </div>
          </div>
          
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">ISBN</label>
              <input type="text" id="isbn" placeholder="978-0-00-000000-0" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Số trang</label>
              <input type="number" id="pages" min="1" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Trạng thái</label>
              <select id="status" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
                <option value="Available">Có sẵn</option>
                <option value="Checked Out">Đã mượn</option>
                <option value="Reserved">Đã đặt</option>
              </select>
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">URL Ảnh bìa</label>
              <input type="url" id="cover" placeholder="https://example.com/book-cover.jpg" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
            </div>
          </div>
        </div>
        
        <div class="mt-8 flex justify-end gap-3">
          <button type="button" onclick="closeModal()" class="px-6 py-3 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition duration-200">
            Hủy
          </button>
          <button type="submit" class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-200">
            Lưu Sách
          </button>
        </div>
      </form>
    </div>
  </div>

  <script>
    let books = ''' + json.dumps(books) + ''';
    let currentBookId = null;

    document.addEventListener('DOMContentLoaded', function() {
      renderBooks();
      updateStats();
    });

    async function fetchBooks() {
      const res = await fetch('/api/books');
      books = await res.json();
      renderBooks();
    }

    async function saveBook(bookData) {
      const res = await fetch('/api/books', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(bookData)
      });
      if (res.ok) {
        fetchBooks();
      }
    }

    async function deleteBook(id) {
      if (confirm('Bạn có chắc chắn muốn xóa sách này?')) {
        await fetch(`/api/books/${id}`, { method: 'DELETE' });
        fetchBooks();
      }
    }

    function renderBooks() {
      const container = document.getElementById('booksContainer');
      const emptyState = document.getElementById('emptyState');
      
      const searchTerm = document.getElementById('searchInput').value.toLowerCase();
      const genreFilter = document.getElementById('genreFilter').value;
      const statusFilter = document.getElementById('statusFilter').value;
      
      const filteredBooks = books.filter(book => {
        const matchesSearch = book.title.toLowerCase().includes(searchTerm) || 
                             book.author.toLowerCase().includes(searchTerm) ||
                             book.isbn.includes(searchTerm);
        const matchesGenre = genreFilter === 'Tất cả' || book.genre === genreFilter;
        const matchesStatus = statusFilter === 'Tất cả' || book.status === statusFilter;
        
        return matchesSearch && matchesGenre && matchesStatus;
      });
      
      container.innerHTML = '';
      
      if (filteredBooks.length === 0) {
        emptyState.classList.remove('hidden');
        container.classList.add('hidden');
      } else {
        emptyState.classList.add('hidden');
        container.classList.remove('hidden');
        
        filteredBooks.forEach(book => {
          const bookCard = document.createElement('div');
          bookCard.className = 'bg-white rounded-lg shadow-lg overflow-hidden book-card transition-all duration-300';
          bookCard.innerHTML = `
            <div class="flex">
              <img src="${book.cover || 'https://placehold.co/120x180/e5e7eb/6b7280?text=No+Image'}" 
                   alt="${book.title}" class="w-20 h-28 object-cover">
              <div class="p-4 flex-1">
                <h3 class="font-semibold text-gray-800 text-sm line-clamp-2">${book.title}</h3>
                <p class="text-gray-600 text-xs mt-1">${book.author}</p>
                <div class="flex gap-2 mt-2">
                  <span class="px-2 py-1 text-xs rounded-full ${
                    book.status === 'Available' ? 'status-available' : 
                    book.status === 'Checked Out' ? 'status-checked-out' : 'status-reserved'
                  }">${book.status}</span>
                  <span class="px-2 py-1 text-xs rounded-full bg-gray-100 text-gray-700">${book.genre}</span>
                </div>
              </div>
            </div>
            <div class="px-4 pb-4 pt-2">
              <div class="flex justify-between text-xs text-gray-500">
                <span>Năm: ${book.year}</span>
                <span>${book.pages || 'N/A'} trang</span>
              </div>
            </div>
            <div class="px-4 pb-4">
              <div class="flex gap-2">
                <button onclick="editBook(${book.id})" class="flex-1 bg-gray-100 hover:bg-gray-200 text-gray-700 py-2 px-3 rounded text-sm transition duration-200 flex items-center justify-center gap-1">
                  <i class="fas fa-edit"></i>
                  Sửa
                </button>
                <button onclick="deleteBook(${book.id})" class="flex-1 bg-red-100 hover:bg-red-200 text-red-700 py-2 px-3 rounded text-sm transition duration-200 flex items-center justify-center gap-1">
                  <i class="fas fa-trash"></i>
                  Xóa
                </button>
              </div>
            </div>
          `;
          container.appendChild(bookCard);
        });
      }
      
      updateStats();
    }

    function filterBooks() {
      renderBooks();
    }

    function openModal(bookData = null) {
      const modal = document.getElementById('bookModal');
      const form = document.getElementById('bookForm');
      const modalTitle = document.getElementById('modalTitle');
      
      form.reset();
      
      if (bookData) {
        currentBookId = bookData.id;
        modalTitle.textContent = 'Chỉnh Sửa Sách';
        
        document.getElementById('title').value = bookData.title;
        document.getElementById('author').value = bookData.author;
        document.getElementById('genre').value = bookData.genre;
        document.getElementById('year').value = bookData.year;
        document.getElementById('isbn').value = bookData.isbn || '';
        document.getElementById('pages').value = bookData.pages || '';
        document.getElementById('status').value = bookData.status;
        document.getElementById('cover').value = bookData.cover || '';
      } else {
        currentBookId = null;
        modalTitle.textContent = 'Thêm Sách Mới';
      }
      
      modal.classList.remove('hidden');
    }

    function closeModal() {
      document.getElementById('bookModal').classList.add('hidden');
    }

    document.getElementById('bookForm').addEventListener('submit', async function(e) {
      e.preventDefault();
      
      const formData = {
        id: currentBookId,
        title: document.getElementById('title').value,
        author: document.getElementById('author').value,
        genre: document.getElementById('genre').value,
        year: parseInt(document.getElementById('year').value),
        isbn: document.getElementById('isbn').value,
        pages: document.getElementById('pages').value ? parseInt(document.getElementById('pages').value) : null,
        status: document.getElementById('status').value,
        cover: document.getElementById('cover').value
      };
      
      await saveBook(formData);
      closeModal();
    });

    function editBook(id) {
      const book = books.find(b => b.id === id);
      if (book) openModal(book);
    }

    async function exportData() {
      const res = await fetch('/api/export');
      const data = await res.json();
      const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(data, null, 2));
      const a = document.createElement('a');
      a.href = dataStr;
      a.download = 'library-data.json';
      a.click();
    }

    async function importData() {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = '.json';
      input.onchange = async (e) => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.onload = async (event) => {
          try {
            const imported = JSON.parse(event.target.result);
            if (Array.isArray(imported)) {
              const res = await fetch('/api/import', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(imported)
              });
              if (res.ok) {
                alert('Nhập thành công!');
                fetchBooks();
              }
            }
          } catch (err) {
            alert('Lỗi: ' + err.message);
          }
        };
        reader.readAsText(file);
      };
      input.click();
    }

    function updateStats() {
      const total = books.length;
      const available = books.filter(b => b.status === 'Available').length;
      const checkedOut = books.filter(b => b.status === 'Checked Out').length;
      const reserved = books.filter(b => b.status === 'Reserved').length;
      
      document.getElementById('totalBooks').textContent = total;
      document.getElementById('availableBooks').textContent = available;
      document.getElementById('checkedOutBooks').textContent = checkedOut;
      document.getElementById('reservedBooks').textContent = reserved;
    }

    document.getElementById('bookModal').addEventListener('click', function(e) {
      if (e.target === this) closeModal();
    });

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') closeModal();
    });
  </script>
</body>
</html>
'''

def client_page():
    return '''
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Thư Viện Công Cộng</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
  <style>
    body { font-family: 'Inter', sans-serif; }
    .book-card:hover { transform: translateY(-2px); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
    .status-available { background-color: #dcfce7; color: #166534; }
    .status-checked-out { background-color: #fee2e2; color: #991b1b; }
  </style>
</head>
<body class="bg-gray-50 min-h-screen">
  <div class="container mx-auto px-4 py-8">
    <div class="bg-white rounded-lg shadow-lg p-6 mb-8 text-center">
      <h1 class="text-3xl font-bold text-gray-800"><i class="fas fa-book-open text-blue-600"></i> Thư Viện Công Cộng</h1>
      <p class="text-gray-600">Khám phá bộ sưu tập sách của chúng tôi</p>
    </div>

    <div id="booksContainer" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
      <!-- Sách sẽ được chèn bằng JS -->
    </div>
  </div>

  <script>
    fetch('/api/books')
      .then(res => res.json())
      .then(books => {
        const container = document.getElementById('booksContainer');
        books.forEach(book => {
          const card = document.createElement('div');
          card.className = 'bg-white rounded-lg shadow p-4 book-card transition';
          card.innerHTML = `
            <img src="${book.cover}" alt="${book.title}" class="w-full h-40 object-cover rounded mb-3">
            <h3 class="font-semibold text-gray-800">${book.title}</h3>
            <p class="text-gray-600 text-sm">${book.author}</p>
            <div class="mt-2">
              <span class="px-2 py-1 text-xs rounded-full ${book.status === 'Available' ? 'status-available' : 'status-checked-out'}">${book.status}</span>
            </div>
          `;
          container.appendChild(card);
        });
      });
  </script>
</body>
</html>
'''

# Lấy ID mới
def get_next_id():
    return max([book["id"] for book in books]) + 1 if books else 1

# Trang admin - quản lý sách
@app.route('/admin')
def admin():
    return render_template('admin.html', books=json.dumps(books))

# Trang client - xem sách
@app.route('/')
def client():
    return render_template('client.html', books=json.dumps(books))

# API: Lấy danh sách sách
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# API: Thêm hoặc cập nhật sách
@app.route('/api/books', methods=['POST'])
def add_or_update_book():
    data = request.get_json()
    data['id'] = int(data['id']) if data.get('id') else get_next_id()
    data['year'] = int(data['year'])
    data['pages'] = int(data['pages']) if data.get('pages') else None
    data['addedDate'] = data.get('addedDate', datetime.now().strftime('%Y-%m-%d'))

    # Nếu là chỉnh sửa
    if any(book['id'] == data['id'] for book in books):
        index = next(i for i, b in enumerate(books) if b['id'] == data['id'])
        books[index] = data
    else:
        books.append(data)

    return jsonify({"success": True, "books": books})

# API: Xóa sách
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({"success": True})

# API: Xuất dữ liệu JSON
@app.route('/api/export', methods=['GET'])
def export_data():
    return jsonify(books)

# API: Nhập dữ liệu JSON
@app.route('/api/import', methods=['POST'])
def import_data():
    global books
    data = request.get_json()
    if isinstance(data, list):
        books = [{**book, "id": book.get("id", get_next_id())} for book in data]
        return jsonify({"success": True, "count": len(books)})
    return jsonify({"success": False, "error": "Invalid data"}), 400

if __name__ == '__main__':
    # Tạo thư mục templates nếu chưa có
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)

    # Tạo file admin.html
    with open(r'./templates/admin.html', 'w', encoding='utf-8') as f:
        f.write(admin_page())
        print("Admin page created.")

    # Tạo file client.html (phiên bản rút gọn cho người dùng)
    with open(r'./templates/client.html', 'w', encoding='utf-8') as f:
        f.write(client_page())  
        print("Client page created.")

    print("🚀 Server đang chạy tại http://localhost:5000")
    print("👉 Truy cập /admin để quản lý")
    print("👉 Truy cập / để xem trang khách")
    app.run(debug=True)