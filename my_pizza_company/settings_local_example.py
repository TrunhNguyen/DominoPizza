# settings_local.example.py
# Copy file này thành settings_local.py và điền giá trị thật

SECRET_KEY = "your-secret-key-here"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "your_db_name",      # tên database
        "USER": "your_db_user",      # user PostgreSQL
        "PASSWORD": "your_db_pass",  # mật khẩu user PostgreSQL
        "HOST": "localhost",         # hoặc IP của server DB
        "PORT": "5432",               # cổng PostgreSQL mặc định
    }
}

DEBUG = True  # Đặt False khi chạy production