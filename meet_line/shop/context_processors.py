from datetime import datetime
from .models import ShopRequest

def notification_processor(request):
    card_id = request.session.session_key
    request = ShopRequest.objects.filter(card_id = card_id)
    if not request.exists():
        return {
            'notification' : False
        }
    current_time = datetime.now()
    request_time = request.get(card_id=card_id).request_date
    delta = current_time - request_time
    if delta.total_seconds() < 300:  # 10 minutes
        return {
            'notification' : True
        }
    else:
        return {
            'notification' : False
        }
     