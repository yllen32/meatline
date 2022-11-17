import os
import vk_api

from dotenv import load_dotenv

from .views import logger


load_dotenv()

VK_KEY = str(os.getenv('VK_KEY'))
ADMIN_VK_ID = int(os.getenv('ADMIN_VK_ID'))
OWNER_VK_ID = int(os.getenv('OWNER_VK_ID'))

def prepare_messages(request_data, items_data):
    """Return a turple with the two stings preapred from form and queryset."""
    request_id = request_data.pk
    consumer_info = f'Новая заявка на покупку: № {request_id}\n'
    request_info = f'Подробности заявки № {request_id}:\n\n'
    consumer_info += str(request_data) + '\n'
    for item in items_data:
        request_info += str(item) + '\n'
    return consumer_info, request_info
    

def send_vk_message(request_data, items_data):
    """Send a notification to admin via vk."""
    messages = prepare_messages(request_data, items_data)
    bot = vk_api.VkApi(token = VK_KEY)
    vk = bot.get_api()
    try:
        for message in messages:
            vk.messages.send(user_id=ADMIN_VK_ID, random_id=0, message=message)
            vk.messages.send(user_id=OWNER_VK_ID, random_id=1, message=message)
    except Exception as err:
        logger.exception("Error during vk message sending")
