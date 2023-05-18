"""
URL configuration for trainerconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from trainerapp.views import MainPage, AddExerciseView, ExerciseListView, AddTrainingView, TrainingListView, AddTrainingPlanView, TrainingPlanListView
from users.views import AppLoginView
from auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", MainPage.as_view(), name="main-page"),
    path("add_exercise/", AddExerciseView.as_view(), name="add-exercise"),
    path("exercise_list/", ExerciseListView.as_view(), name="exercise-list"),
    path("add_training/", AddTrainingView.as_view(), name="add-training"),
    path("training_list/", TrainingListView.as_view(), name="training-list"),
    path('add_training_plan/', AddTrainingPlanView.as_view(), name="add-training-plan"),
    path('training_plan_list/', TrainingPlanListView.as_view(), name="training-plan-list"),
    path("register/", views.register, name="register"),
    path('login/', AppLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
