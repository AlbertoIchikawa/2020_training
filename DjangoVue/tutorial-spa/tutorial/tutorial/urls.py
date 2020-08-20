"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from polls.api_urls import question_router
from polls import api_views as poll_views  # 追加
from rest_framework_jwt.views import obtain_jwt_token  # 追加
from rest_framework_jwt.views import verify_jwt_token  # <--- 追加




api_urlpatterns = [  # apiのURL一覧 (まだquestionだけ)
    path('auth/', obtain_jwt_token),  # 追加
    path('auth/verify/', verify_jwt_token),  # <--- 追加
    path('questions/', include(question_router.urls)),  # 慣例として複数形にする
    path('choices/<int:choice_id>/vote/', poll_views.VoteView.as_view()),  # 追加
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1.0/', include(api_urlpatterns)),  # api/1.0/としてapi一覧を登録
]
