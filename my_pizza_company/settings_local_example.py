# settings_local.example.py
# Copy file này thành settings_local.py và điền giá trị thật

SECRET_KEY = "your-secret-key-here"    #điền secret key được nhận

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydb",      #tên db sẽ tạo
        "USER": "postgres",  #tên user mặc định   
        "PASSWORD": "your_db_pass",   #thay cái này
        "HOST": "localhost",         
        "PORT": "5432",              
    }
}

DEBUG = True  