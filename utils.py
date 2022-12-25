import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models.send_messages import ImageSendMessage
import random


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

#抽美女
def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    if text == "美女":
        line_bot_api.reply_message(reply_token, TextSendMessage(text = "請輸入「抽」"))
    elif text == "抽":
        rnd = random.randrange(10)
        #print(random.randrange(10))
        print(rnd)
        if rnd > 5:
            image_message = ImageSendMessage(
            original_content_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/%E6%AF%8D%E8%83%8E%E5%A5%B3%E6%98%9F-1642061819.jpg?crop=0.510xw:1.00xh;0,0&resize=640:*',
            preview_image_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/%E6%AF%8D%E8%83%8E%E5%A5%B3%E6%98%9F-1642061819.jpg?crop=0.510xw:1.00xh;0,0&resize=640:*'
        )
        else:
            image_message = ImageSendMessage(
            original_content_url='https://images.chinatimes.com/newsphoto/2020-06-04/656/20200604002777.jpg',
            preview_image_url='https://images.chinatimes.com/newsphoto/2020-06-04/656/20200604002777.jpg'
        )
        line_bot_api.reply_message(reply_token, image_message)
    elif text == "回去":
        line_bot_api.reply_message(reply_token, TextSendMessage(text = "請輸入「美女」或「帥哥」"))
    else:
        line_bot_api.reply_message(reply_token, TextSendMessage(text = "打錯了啦"))
    return "OK"
#抽帥哥
def send_text_of_handsome(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    if text == "抽":
        image_message = ImageSendMessage(
            original_content_url='https://s.yimg.com/ny/api/res/1.2/nebeV8qpySHVxVO9ZR99Nw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTU3MA--/https://66.media.tumblr.com/905eae4db62fba8adbffd193403c258d/tumblr_inline_oe9jfsqLGx1tvmbsr_1280.jpg',
            preview_image_url='https://s.yimg.com/ny/api/res/1.2/nebeV8qpySHVxVO9ZR99Nw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTU3MA--/https://66.media.tumblr.com/905eae4db62fba8adbffd193403c258d/tumblr_inline_oe9jfsqLGx1tvmbsr_1280.jpg'
        )
        line_bot_api.reply_message(reply_token, image_message)
    elif text == "帥哥":
        line_bot_api.reply_message(reply_token, TextSendMessage(text = "請輸入「抽帥率」"))
    elif text == "回去":
        line_bot_api.reply_message(reply_token, TextSendMessage(text = "請輸入「美女」或「帥哥」"))
    else:
        line_bot_api.reply_message(reply_token, TextSendMessage(text = "打錯了啦帥哥"))
    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
