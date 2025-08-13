
# Dự án cửa hàng pizza Domino

## Giới thiệu

Đây là ứng dụng web giúp khách hàng xem danh sách pizza, thêm vào giỏ hàng, và xem tổng giá tiền.

## Cách chạy dự án (vào terminal)

1. Tạo môi trường ảo:

python -m venv venv

2. Kích hoạt môi trường:

- Windows:

venv\Scripts\activate

- macOS/Linux:

source venv/bin/activate

3. Truy cập vào project:

cd venv
cd DominoPizza

4. Cài đặt thư viện:

pip install -r requirement.txt

5. Import Database:

- CREATE DATABASE mydb
- psql -U postgres mydb < backup.sql
- cp settings_local.example.py settings_local.py
- mở settings_local.py và thay thông tin của mình vào

6. Chạy server:

python manage.py runserver


7. Mở trình duyệt vào địa chỉ: 

http://127.0.0.1:8000/

