from django.shortcuts import render

def exam_calendar(request):
    return render(request, 'exam_calender/index_exam.html')
