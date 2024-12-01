from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Event
import json

# 增加事件
@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event = Event.objects.create(
            child_event_id=data.get('child_event_id'),
            quadrant=data.get('quadrant'),
            category=data.get('category'),
            title=data.get('title'),
            description=data.get('description'),
            deadline=data.get('deadline')
        )
        return JsonResponse({'message': 'Event added', 'event_id': event.event_id})

# 查询所有事件
def get_events(request):
    if request.method == 'GET':
        events = list(Event.objects.values())
        return JsonResponse(events, safe=False)

# 查询单个事件
def get_event(request, event_id):
    if request.method == 'GET':
        event = get_object_or_404(Event, event_id=event_id)
        return JsonResponse({
            'event_id': event.event_id,
            'child_event_id': event.child_event_id,
            'quadrant': event.quadrant,
            'category': event.category,
            'title': event.title,
            'description': event.description,
            'deadline': event.deadline,
            'created_at': event.created_at,
            'updated_at': event.updated_at
        })

# 修改事件
@csrf_exempt
def update_event(request, event_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        event = get_object_or_404(Event, event_id=event_id)
        event.child_event_id = data.get('child_event_id', event.child_event_id)
        event.quadrant = data.get('quadrant', event.quadrant)
        event.category = data.get('category', event.category)
        event.title = data.get('title', event.title)
        event.description = data.get('description', event.description)
        event.deadline = data.get('deadline', event.deadline)
        event.save()
        return JsonResponse({'message': 'Event updated'})

# 删除事件
@csrf_exempt
def delete_event(request, event_id):
    if request.method == 'DELETE':
        event = get_object_or_404(Event, event_id=event_id)
        event.delete()
        return JsonResponse({'message': 'Event deleted'})
