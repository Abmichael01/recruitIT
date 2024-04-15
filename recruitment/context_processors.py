from .models import Notification

def notifications(request):
    # Retrieve notifications for the current user
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user)
    else:
        notifications = []
    
    return {'notifications': notifications}
