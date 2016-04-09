"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from api.src.views import (
    create_account_view,
    login_view,
    tip_and_trick_view,
    rating_tip_and_trick_view,
    rating_user_view,
    rating_apply_view,
    category_view,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create-account', create_account_view.CreateAccountView.as_view()),
    url(r'^login', login_view.LoginView.as_view()),
    url(r'^category/?(?P<category_id>\w{1,50})?', category_view.CategoryView.as_view()),  # [0-9]+$ '?' is for optional
    url(r'^tip_and_trick/(?P<tip_and_trick_id>\d+)', tip_and_trick_view.TipAndTrickView.as_view()),  # [0-9]+$ '?' is for optional
    url(r'^tip_and_trick', tip_and_trick_view.TipAndTrickView.as_view()),  # [0-9]+$ '?' is for optional
    url(r'^rating/tip_and_trick/(?P<tip_and_trick_id>\d+)', rating_tip_and_trick_view.RatingTipAndTrickView.as_view()),  # [0-9]+$ '?' is for optional
    url(r'^rating/tip_and_trick', rating_tip_and_trick_view.RatingTipAndTrickView.as_view()),  # [0-9]+$ '?' is for optional
    url(r'^rating/user/(?P<user_id>\d+)', rating_user_view.RatingUserView.as_view()),  # [0-9]+$ '?' is for optional
    url(r'^rating/user', rating_user_view.RatingUserView.as_view()),  # [0-9]+$ '?' is for optional
    url(r'^rating_apply/(?P<rating_id>\d+)', rating_apply_view.RatingApplyView.as_view()),  # [0-9]+$ '?' is for optional
    url(r'^rating_apply', rating_apply_view.RatingApplyView.as_view()),  # [0-9]+$ '?' is for optional
]
