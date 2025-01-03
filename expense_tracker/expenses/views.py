from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Sum
from .models import Expense
from .forms import CustomUserCreationForm, CustomLoginForm
import json
from django import forms
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Expense, MonthlyLimit
 # Import the form from forms.py
from django.db.models.functions import TruncMonth



class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ['date']

# Form: Limit Form
class LimitForm(forms.Form):
    limit = forms.DecimalField(max_digits=10, decimal_places=2)

# Views
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Authenticate the user
            login(request, user)    # Log the user in
            messages.success(request, "You have logged in successfully.")
            return redirect('dashboard')  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomLoginForm()  # Empty form for GET request

    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    return render(request, 'index.html')

# views.py



@login_required
def dashboard_view(request):
    user = request.user
    expenses = Expense.objects.filter(user=user).order_by('-date')

    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    monthly_limit = MonthlyLimit.objects.filter(user=user).first()

    context = {
        'expenses': expenses,
        'total_expenses': total_expenses,
        'monthly_limit': monthly_limit,
    }
    
    return render(request, 'dashboard.html', context)


@login_required
def add_expense(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        category = request.POST['category']
        description = request.POST['description']
        date = request.POST['date']

        Expense.objects.create(
            user=request.user,
            amount=amount,
            category=category,
            description=description,
            date=date
        )
        return redirect('dashboard')

    return render(request, 'add_expense.html')

# views.py



@login_required
def view_expense(request):
    user = request.user
    expenses = Expense.objects.filter(user=user).order_by('-date')  # Display expenses in reverse date order

    # Get filter parameters from GET request
    category_filter = request.GET.get('category', '')
    date_filter = request.GET.get('date', '')

    # Apply category filter if provided
    if category_filter:
        expenses = expenses.filter(category__icontains=category_filter)
    
    # Apply date filter if provided
    if date_filter:
        expenses = expenses.filter(date=date_filter)

    context = {
        'expenses': expenses,
        'category_filter': category_filter,
        'date_filter': date_filter,
    }

    return render(request, 'view_expense.html', context)

from django.shortcuts import render, get_object_or_404, redirect


@login_required
def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)
    
    if request.method == 'POST':
        expense.category = request.POST.get('category')
        expense.amount = request.POST.get('amount')
        expense.description = request.POST.get('description')
        expense.date = request.POST.get('date')
        expense.save()
        return redirect('view_expense')  # Redirect after saving changes

    return render(request, 'edit_expense.html', {'expense': expense})
@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)
    
    if request.method == 'POST':
        expense.delete()  # Delete the expense from the database
        return redirect('view_expense')  # Redirect after deletion
    
    return redirect('view_expense')  # In case method isn't POST, still redirect
@login_required
def monthly_summary(request):
    # Ensure the user is logged in
    if not request.user.is_authenticated:
        return redirect('login')

    # Query to group expenses by month for the logged-in user
    expenses = (
        Expense.objects.filter(user=request.user)
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total_expense=Sum('amount'))
        .order_by('month')
    )

    # Extract month names and total expenses
    months = [expense['month'].strftime('%B %Y') for expense in expenses]
    total_expenses = [float(expense['total_expense']) for expense in expenses]  # Convert Decimal to float

    # Pass data to the template
    return render(request, 'monthly_summary.html', {
        'months': json.dumps(months),
        'total_expenses': json.dumps(total_expenses),
    })

@login_required
def category_summary(request):
    # Ensure the user is logged in
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to your login page if not logged in

    # Query to get expenses for the logged-in user grouped by category
    expenses = (
        Expense.objects.filter(user=request.user)
        .values('category')
        .annotate(total_expense=Sum('amount'))
    )

    # Extract category names and total expenses
    category_names = [expense['category'] for expense in expenses]
    total_expenses = [float(expense['total_expense']) for expense in expenses]

    # Pass data to the template
    return render(request, 'category_summary.html', {
        'category_names': json.dumps(category_names),
        'total_expenses': json.dumps(total_expenses),
    })
@login_required
def set_monthly_limit(request):
    if request.method == 'POST':
        limit = request.POST['limit']
        MonthlyLimit.objects.update_or_create(user=request.user, defaults={'limit': limit})
        return redirect('dashboard')

    return render(request, 'set_monthly_limit.html')