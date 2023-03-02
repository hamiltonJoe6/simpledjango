from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Notification

def index(request):
        return HttpResponse('this is something')

def show_notification(request, notification_id):
	n = Notification.objects.get(id=notification_id)
	return render(request, 'approvals/notification.html', {'notification': n})

def delete_notification(request, notification_id):
	n = Notification.objects.get(id=notification_id)
	n.viewed = True
	n.save()

	return HttpResponse(request, 'ok')
