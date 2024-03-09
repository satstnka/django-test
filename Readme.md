# Django サンプルプログラム
## 開発環境構築
1. 仮装環境を構築する。
```
python -m venv venv
```
2. 仮装環境を有効にする。
```
source venv/bin/activate
```
3. Django インストール
```
pip install django
```

## アプリケーション作成
1. プロジェクトを作成する。(今回は helloproject という名前のプロジェクトを作成する)
```
django-admin startproject helloproject
```
2. プロジェクトフォルダーに移動
```
cd helloproject
```
3. アプリケーション作成 (今回は helloapp という名前のアプリケーションを作成)
```
python manage.py startapp helloapp
```
4. helloproject/settings.py 修正

INSTALL_APPS に helloapp を追加する。
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'helloapp',
]
```

言語を日本語にする。
```
LANGUAGE_CODE = 'ja'
```

タイムゾーンを日本(東京)にする。
```
TIME_ZONE = 'Asia/Tokyo'
```
5. サーバー起動
```
python manage.py runserver
```
これで http://localhost:8000/ にアクセスするとページをみる事ができる。

## ページの表示
1. helloapp フォルダーに templates フォルダーを作成し、その中に hello.html を作成する。
```
mkdir helloapp/templates/
touch helloapp/templates/hello.html
```
2. helloapp.html の中にHTML を書く。
```
<!DOCTYPE html>
<html>
  <head>
    <title>Hello</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1>こんにちは</h1>
    <p>これはテストページです。</p>
  </body>
</html>
```
3. helloapp/views.py の中でビューの定義を追加する。
```
from django.views.generic import TemplateView

class HelloView(TemplateView):
    template_name = "hello.html"
```
4. helloproject/urls.py に URL 設定追加。
```
from helloapp import views

urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'),
]
```
5. サーバー起動
```
python manage.py runserver
```
これで http://localhost:8000/ にアクセスするとページをみる事ができる。

