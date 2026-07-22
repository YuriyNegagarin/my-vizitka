[app]

# Название приложения (видно на телефоне под иконкой)
title = app

# Имя пакета — только латиница, без пробелов и цифр в начале
package.name = TestVizitka

# Домен пакета (можно оставить как есть)
package.domain = org.student

# Папка с исходным кодом (. = текущая папка)
source.dir = .

# Какие типы файлов включать в сборку
# ВАЖНО: kv — обязательно, иначе дизайн не попадёт в APK
# jpg/jpeg/png — для картинок
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf

# Версия приложения
version = 1.0

# ─── ГЛАВНАЯ СТРОКА: зависимости с ТОЧНЫМИ версиями ───
# Без точных версий сборка падает с ошибкой 'long' (старый pyjnius)
requirements = python3,kivy==2.3.0,pyjnius==1.6.1

# Ориентация экрана: portrait (вертикально) или landscape
orientation = portrait

# Заставка при запуске (необязательно)
# presplash.filename = %(source.dir)s/presplash.png

# Иконка приложения (необязательно)
# icon.filename = %(source.dir)s/icon.png

# ─── Android настройки ───
# Разрешения. INTERNET нужен для AsyncImage (картинки из сети)
android.permissions = INTERNET

# Версии Android API (проверенные значения)
android.api = 33
android.minapi = 21
android.ndk = 25b

# Автоматически принять лицензию SDK (без этого сборка спросит и упадёт)
android.accept_sdk_license = True

# Архитектура процессора (arm64-v8a — современные телефоны)
android.arch = arm64-v8a
p4a.branch = v2024.01.21


[buildozer]

# Уровень логов: 2 = подробно (удобно искать ошибки)
log_level = 2

# ─── ВАЖНО: убирает вопрос про root-пользователя ───
# В облаке (Colab/GitHub) некому ответить на этот вопрос — ставим 0
warn_on_root = 0
