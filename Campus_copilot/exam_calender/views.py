from django.shortcuts import render
from django.http import JsonResponse


def exam_calendar(request):
    return render(request, 'exam_calender/index_exam.html')

def send_email_notification(request):
    """
    Django view to handle email notifications.
    In a real implementation, this would integrate with Django's email system.
    """
    if request.method == 'POST':
        # Process email sending logic here
        pass
    return JsonResponse({'status': 'success'})
