from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
path('login/', views.login_view, name='login'),
path('dashboard/', views.dashboard_view, name='dashboard'),
    path('', views.index, name='index'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('add_expense/', views.add_expense, name='add_expense'),
    path('view_expense/', views.view_expense, name='view_expense'),
     path('edit/<int:id>/', views.edit_expense, name='edit_expense'),
 path('delete/<int:id>/', views.delete_expense, name='delete_expense'),

    path('monthly_summary/', views.monthly_summary, name='monthly_summary'),
    path('category_summary/', views.category_summary, name='category_summary'),  # Category-wise summary
    path('set_monthly_limit/', views.set_monthly_limit, name='set_monthly_limit'),  # Set monthly expense limit
]