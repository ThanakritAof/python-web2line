from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')

def send(text):
    line_bot_api.push_message('userId', TextSendMessage(text=text))