from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Announcement, Category
from .forms import AnnouncementForm

def index(request):
    search_query = request.GET.get('search', '')
    announcements = Announcement.objects.all()
    
    if search_query:
        announcements = announcements.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query) |
            Q(category__icontains=search_query) |
            Q(author__icontains=search_query)
        )
        
    context = {
        'announcements': announcements,
        'search_query': search_query,
    }
    return render(request, 'announcements/index.html', context)

def view_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    return render(request, 'announcements/view_announcement.html', {'announcement': announcement})

@login_required
def admin_dashboard(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements/admin_dashboard.html', {'announcements': announcements})

@login_required
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = AnnouncementForm()
    
    return render(request, 'announcements/announcement_form.html', {'form': form, 'is_creating': True})

@login_required
def edit_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = AnnouncementForm(instance=announcement)
    
    return render(request, 'announcements/announcement_form.html', {'form': form, 'announcement': announcement, 'is_creating': False})

@login_required
def delete_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    
    if request.method == 'POST':
        announcement.delete()
        return redirect('admin_dashboard')
        
    return render(request, 'announcements/delete_confirmation.html', {'announcement': announcement})