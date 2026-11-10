from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.db.models import Count
import json
from .models import Event
from .forms import EventForm

# --- PUBLIC / USER VIEWS ---

def home(request):
    events = Event.objects.filter(is_approved=True).order_by('-event_date')
    return render(request, 'home.html', {'events': events})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})

@login_required
def my_events(request):
    user_events = Event.objects.filter(user=request.user).order_by('-event_date')
    return render(request, 'my_events.html', {'events': user_events})

# --- FULL ADMIN DASHBOARD VIEWS ---

@staff_member_required
def admin_dashboard(request):
    # Show everything so admin can manage existing events too
    all_events = Event.objects.all().order_by('-created_at')
    pending_count = Event.objects.filter(is_approved=False).count()
    return render(request, 'admin_dashboard.html', {
        'events': all_events,
        'pending_count': pending_count
    })

@staff_member_required
def approve_event(request, event_id):
    if request.method == "POST":
        event = get_object_or_404(Event, id=event_id)
        event.is_approved = True
        event.save()
    return redirect('admin_dashboard')

@staff_member_required
def reject_event(request, event_id):
    if request.method == "POST":
        event = get_object_or_404(Event, id=event_id)
        event.delete() # Deletes the pending request
    return redirect('admin_dashboard')

@staff_member_required
def toggle_featured(request, event_id):
    if request.method == "POST":
        event = get_object_or_404(Event, id=event_id)
        event.is_featured = not event.is_featured
        event.save()
    return redirect('admin_dashboard')

@staff_member_required
def edit_event_admin(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form, 'event': event})

@staff_member_required
def delete_event_admin(request, event_id):
    if request.method == "POST":
        event = get_object_or_404(Event, id=event_id)
        event.delete()
    return redirect('admin_dashboard')

@staff_member_required
def analytics_dashboard(request):
    total_events = Event.objects.count()
    approved_events = Event.objects.filter(is_approved=True).count()
    pending_events = Event.objects.filter(is_approved=False).count()
    
    # Event types distribution
    event_types_data = Event.objects.values('event_type').annotate(count=Count('id'))
    types_labels = [item['event_type'] for item in event_types_data]
    types_values = [item['count'] for item in event_types_data]

    # Events over time (by month/date)
    # Grouping by event_date (or created_at)
    # For simplicity, we can format the date to string in python to group them
    events = Event.objects.all().order_by('created_at')
    date_counts = {}
    for event in events:
        date_str = event.created_at.strftime('%Y-%m-%d')
        date_counts[date_str] = date_counts.get(date_str, 0) + 1
    
    dates_labels = list(date_counts.keys())
    dates_values = list(date_counts.values())

    latest_events = Event.objects.all().order_by('-created_at')[:10]

    context = {
        'total_events': total_events,
        'approved_events': approved_events,
        'pending_events': pending_events,
        'types_labels_json': json.dumps(types_labels),
        'types_values_json': json.dumps(types_values),
        'dates_labels_json': json.dumps(dates_labels),
        'dates_values_json': json.dumps(dates_values),
        'latest_events': latest_events,
    }
    return render(request, 'analytics_dashboard.html', context)

# --- AUTHENTICATION VIEWS ---

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'auth_login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login after creation
            login(request, user)
            messages.success(request, f"Account created successfully! Welcome, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
        
    return render(request, 'auth_register.html', {'form': form})