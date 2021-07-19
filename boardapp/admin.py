from django.contrib import admin
from .models import BoardModel

# Register your models here.

# Djangoのadmin（管理機能）にアプリ（モデル）を追加
admin.site.register(BoardModel)