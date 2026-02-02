from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
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