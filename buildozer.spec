[app]

# نام برنامه
title = My Calculator

# نام پکیج
package.name = mycalculator

# دامنه پکیج
package.domain = org.mycalculator

# پوشه اصلی برنامه
source.dir = .

# فایل‌هایی که وارد APK می‌شوند
source.include_exts = py,kv,png,jpg,jpeg,atlas

# نسخه برنامه
version = 1.0.0

# کتابخانه‌های مورد نیاز
requirements = python3,kivy==2.3.1

# جهت صفحه
orientation = portrait

# تمام صفحه نباشد
fullscreen = 0

# فقط معماری 64 بیتی
android.archs = arm64-v8a

# Android API
android.api = 34

# حداقل Android API
android.minapi = 24

# NDK
android.ndk = 28c

# API مورد استفاده NDK
android.ndk_api = 24

# Activity استاندارد Kivy
android.entrypoint = org.kivy.android.PythonActivity

# مجوز اینترنت لازم نیست
android.permissions =

# AndroidX
android.enable_androidx = True

# قبول خودکار مجوزهای SDK
android.accept_sdk_license = True

# ذخیره‌سازی خصوصی
android.private_storage = True

# لاگ
log_level = 2


[buildozer]

# سطح لاگ
log_level = 2

# هشدار اجرای root
warn_on_root = 0
