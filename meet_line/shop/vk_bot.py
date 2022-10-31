import os

from dotenv import load_dotenv
import vk_api

load_dotenv()

VK_KEY = str(os.getenv('VK_KEY'))
ADMIN_VK_ID = int(os.getenv('ADMIN_VK_ID'))

def send_vk_message(form_data, items_data):
    """Send a notification to admin via vk."""
    message = 'Новая заявка на покупку\n'
    for data in form_data.values():
        message += str(data)+'\n'
    bot = vk_api.VkApi(token = VK_KEY)
    vk = bot.get_api()
    vk.messages.send(
        user_id=ADMIN_VK_ID,
        random_id=0,
        message=message
    )
