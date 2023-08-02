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
from django.urls import path
from trainerapp.views import (
    MainPage,
    AddExerciseView,
    ExerciseListView,
    AddTrainingView,
    TrainingListView,
    AddTrainingPlanView,
    TrainingPlanListView,
    UpdateExerciseView,
    DeleteExerciseView,
    UpdateTrainingView,
    DeleteTrainingView,
    UpdateTrainingPlanView,
    DeleteTrainingPlanView,
    ExerciseDetailView,
    TrainingDetailView,
    TrainingPlanDetailView,
)
from users.views import AppLoginView, AppLogoutView, RegisterView
from chat.views import (
    ThreadListView,
    AddThreadView,
    AddMessageView,
    DeleteThreadView,
    DeleteMessageView,
    ThreadDetailView,
)
from calendar_schedule.views import CreateEventView, EventListView, UpdateEventView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", MainPage.as_view(), name="main-page"),
    path("add_exercise/", AddExerciseView.as_view(), name="add-exercise"),
    path("exercise_list/", ExerciseListView.as_view(), name="exercise-list"),
    path(
        "update_exercise/<int:pk>/",
        UpdateExerciseView.as_view(),
        name="update-exercise",
    ),
    path(
        "delete_exercise/<int:pk>/",
        DeleteExerciseView.as_view(),
        name="delete-exercise",
    ),
    path(
        "exercise_details/<int:pk>/",
        ExerciseDetailView.as_view(),
        name="exercise-details",
    ),
    path("add_training/", AddTrainingView.as_view(), name="add-training"),
    path("training_list/", TrainingListView.as_view(), name="training-list"),
    path(
        "delete_training/<int:pk>/",
        DeleteTrainingView.as_view(),
        name="delete-training",
    ),
    path(
        "update_training/<int:pk>/",
        UpdateTrainingView.as_view(),
        name="update-training",
    ),
    path(
        "training_details/<int:pk>/",
        TrainingDetailView.as_view(),
        name="training-details",
    ),
    path("add_training_plan/", AddTrainingPlanView.as_view(), name="add-training-plan"),
    path(
        "training_plan_list/", TrainingPlanListView.as_view(), name="training-plan-list"
    ),
    path(
        "training_plan_details/<int:pk>/",
        TrainingPlanDetailView.as_view(),
        name="training-plan-details",
    ),
    path(
        "update_training_plan/<int:pk>/",
        UpdateTrainingPlanView.as_view(),
        name="update-training-plan",
    ),
    path(
        "delete_training_plan/<int:pk>/",
        DeleteTrainingPlanView.as_view(),
        name="delete-training-plan",
    ),
    path(
        "login/",
        AppLoginView.as_view(template_name="registrations/login.html"),
        name="login",
    ),
    path("logout/", AppLogoutView.as_view(), name="logout"),
    path(
        "register/",
        RegisterView.as_view(template_name="registrations/register.html"),
        name="register",
    ),
    path(
        "change_password/",
        auth_views.PasswordChangeView.as_view(
            template_name="registrations/change_password.html",
            success_url="/",
        ),
        name="change_password",
    ),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="registrations/password_reset_form.html",
            email_template_name="registrations/password_reset_email.html",
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registrations/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registrations/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registrations/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
    path("thread_list/", ThreadListView.as_view(), name="thread-list"),
    path("add_thread/", AddThreadView.as_view(), name="add-thread"),
    path("add_message/", AddMessageView.as_view(), name="add-message"),
    path("thread/<int:pk>/", ThreadDetailView.as_view(), name="thread"),
    path("delete_thread/<int:pk>/", DeleteThreadView.as_view(), name="delete-thread"),
    path(
        "delete_message/<int:pk>/", DeleteMessageView.as_view(), name="delete-message"
    ),
    path('create_event/', CreateEventView.as_view(), name='create-event'),
    path('event_list/', EventListView.as_view(), name='event-list'),
    path('update_event/', UpdateEventView.as_view(), name="update-event"),
]
