from django.contrib import admin
from django.urls import path, include
from ide_editor import views


urlpatterns = [
    path("", view=views.login_signup, name=""),
    path("home", view=views.home, name="home"),
    path("editor", view=views.editor, name="editor"),
    path("login", view=views.login, name="login"),
    path("runcode", view=views.runCode, name="runcode"),
    path("signup", view=views.signup, name="signup"),
    path("problemset", view=views.problemSet, name="problemset")
]
