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
        if rnd == 0:
            image_message = ImageSendMessage(
            original_content_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/%E6%AF%8D%E8%83%8E%E5%A5%B3%E6%98%9F-1642061819.jpg?crop=0.510xw:1.00xh;0,0&resize=640:*',
            preview_image_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/%E6%AF%8D%E8%83%8E%E5%A5%B3%E6%98%9F-1642061819.jpg?crop=0.510xw:1.00xh;0,0&resize=640:*'
            )
        elif rnd == 1:
            image_message = ImageSendMessage(
            original_content_url='https://images.chinatimes.com/newsphoto/2020-06-04/656/20200604002777.jpg',
            preview_image_url='https://images.chinatimes.com/newsphoto/2020-06-04/656/20200604002777.jpg'
            )
        elif rnd == 2:
            image_message = ImageSendMessage(
            original_content_url='https://www.upmedia.mg/upload/article/20221104182839308901.png',
            preview_image_url='https://www.upmedia.mg/upload/article/20221104182839308901.png'
            )
        elif rnd == 3:
            image_message = ImageSendMessage(
                original_content_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2q9ErxUXnpcHf6ktWVFcOKxmy_ASK6tL6_g&usqp=CAU',
                preview_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2q9ErxUXnpcHf6ktWVFcOKxmy_ASK6tL6_g&usqp=CAU'
            )
        elif rnd == 4:
            image_message = ImageSendMessage(
            original_content_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPcfDgTTRox0fjIiW7DKiQfAHrBnxG792p8w&usqp=CAU',
            preview_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPcfDgTTRox0fjIiW7DKiQfAHrBnxG792p8w&usqp=CAU'
            )
        elif rnd == 5:
            image_message = ImageSendMessage(
            original_content_url='https://cdn.hk01.com/di/media/images/dw/20220611/612271731398152192163405.jpeg/5QonZ96gqitCngn0yoj4YX5WBsRwPW1w-kAZVvpAGVY?v=w1920',
            preview_image_url='https://cdn.hk01.com/di/media/images/dw/20220611/612271731398152192163405.jpeg/5QonZ96gqitCngn0yoj4YX5WBsRwPW1w-kAZVvpAGVY?v=w1920'
            )
        elif rnd == 6:
            image_message = ImageSendMessage(
            original_content_url='https://cdn2.ettoday.net/images/5025/d5025953.jpg',
            preview_image_url='https://cdn2.ettoday.net/images/5025/d5025953.jpg'
            )
        elif rnd == 7:
            image_message = ImageSendMessage(
            original_content_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaadv1AUDWxnSyc4c764f-hYz7w8i1cI7bylPRTjgTnj38uWgzxmGZIHF7a7aFX4XeQO8&usqp=CAU',
            preview_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaadv1AUDWxnSyc4c764f-hYz7w8i1cI7bylPRTjgTnj38uWgzxmGZIHF7a7aFX4XeQO8&usqp=CAU'
            )
        elif rnd == 8:
            image_message = ImageSendMessage(
            original_content_url='https://media.zenfs.com/en/nownews.hk/2e4696b3c40cfc26a0bcf83b60306c67',
            preview_image_url='https://media.zenfs.com/en/nownews.hk/2e4696b3c40cfc26a0bcf83b60306c67'
            )
        elif rnd == 9:
            image_message = ImageSendMessage(
            original_content_url='https://images.chinatimes.com/newsphoto/2021-02-07/656/20210207003198.jpg',
            preview_image_url='https://images.chinatimes.com/newsphoto/2021-02-07/656/20210207003198.jpg'
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
        rnd = random.randrange(10)
        if rnd == 0:
            image_message = ImageSendMessage(
                original_content_url='https://s.yimg.com/ny/api/res/1.2/nebeV8qpySHVxVO9ZR99Nw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTU3MA--/https://66.media.tumblr.com/905eae4db62fba8adbffd193403c258d/tumblr_inline_oe9jfsqLGx1tvmbsr_1280.jpg',
                preview_image_url='https://s.yimg.com/ny/api/res/1.2/nebeV8qpySHVxVO9ZR99Nw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTU3MA--/https://66.media.tumblr.com/905eae4db62fba8adbffd193403c258d/tumblr_inline_oe9jfsqLGx1tvmbsr_1280.jpg'
            )
        elif rnd == 1:
            image_message = ImageSendMessage(
            original_content_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6E_7d-uisr2DYgd1xltbmcARke3fp_lZ4yw&usqp=CAU',
            preview_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6E_7d-uisr2DYgd1xltbmcARke3fp_lZ4yw&usqp=CAU'
            )
        elif rnd == 2:
            image_message = ImageSendMessage(
            original_content_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWPBYBRa9zZCJdfHeiWQ_LwPmr_XVPs-sROQ&usqp=CAU',
            preview_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWPBYBRa9zZCJdfHeiWQ_LwPmr_XVPs-sROQ&usqp=CAU'
            )
        elif rnd == 3:
            image_message = ImageSendMessage(
            original_content_url='https://inews.gtimg.com/newsapp_bt/0/13572251597/1000',
            preview_image_url='https://inews.gtimg.com/newsapp_bt/0/13572251597/1000'
            )
        elif rnd == 4:
            image_message = ImageSendMessage(
            original_content_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeBFU3s-e3RDTCBzmB-kvP4q9H8_Yv8xpqrQ&usqp=CAU',
            preview_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeBFU3s-e3RDTCBzmB-kvP4q9H8_Yv8xpqrQ&usqp=CAU'
            )
        elif rnd == 5:
            image_message = ImageSendMessage(
            original_content_url='https://dvblobcdnjp.azureedge.net//Content/Upload/Popular/Images/2019-03/afd65767-4fc4-4f2a-8c38-f9b90d6076e1_m.jpg',
            preview_image_url='https://dvblobcdnjp.azureedge.net//Content/Upload/Popular/Images/2019-03/afd65767-4fc4-4f2a-8c38-f9b90d6076e1_m.jpg'
            )
        elif rnd == 6:
            image_message = ImageSendMessage(
            original_content_url='https://imgur.dcard.tw/WFkzN2zh.jpg',
            preview_image_url='https://imgur.dcard.tw/WFkzN2zh.jpg'
            )
        elif rnd == 7:
            image_message = ImageSendMessage(
            original_content_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRaxuqrlwY6Aefqu4GlFSigY8ghNhkcrfgt3g&usqp=CAU',
            preview_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRaxuqrlwY6Aefqu4GlFSigY8ghNhkcrfgt3g&usqp=CAU'
            )
        elif rnd == 8:
            image_message = ImageSendMessage(
            original_content_url='https://i0.wp.com/pinkupost.com/wp-content/uploads/2018/05/ananweb.jpg?ssl=1',
            preview_image_url='https://i0.wp.com/pinkupost.com/wp-content/uploads/2018/05/ananweb.jpg?ssl=1'
            )
        elif rnd == 9:
            image_message = ImageSendMessage(
            original_content_url='https://storage.googleapis.com/www-cw-com-tw/article/202109/article-6141ac636f839.jpg',
            preview_image_url='https://storage.googleapis.com/www-cw-com-tw/article/202109/article-6141ac636f839.jpg'
            )
        line_bot_api.reply_message(reply_token, image_message)
    elif text == "帥哥":
        line_bot_api.reply_message(reply_token, TextSendMessage(text = "請輸入「抽」"))
    elif text == "回去":
        line_bot_api.reply_message(reply_token, TextSendMessage(text = "請輸入「美女」或「帥哥」"))
    else:
        line_bot_api.reply_message(reply_token, TextSendMessage(text = "打錯了啦"))
    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
