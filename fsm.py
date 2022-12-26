from transitions.extensions import GraphMachine

from utils import send_text_message

from utils import send_text_of_handsome


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
#美女state
    def is_going_to_pretty(self,event):
        print("is going to 美女")
        text = event.message.text
        return text.lower() == "美女"
    def on_enter_pretty(self, event):
        print("is entering to 美女")
        reply_token = event.reply_token
        send_text_message(reply_token, "美女")
#抽美女state
    def is_going_to_rand_pretty(self, event):
        print("is going to 抽美女")
        text = event.message.text
        return text.lower() == "抽"
    def on_enter_rand_pretty(self, event):
        print("is entering 抽美女")
        reply_token = event.reply_token
        send_text_message(reply_token, "抽")
        self.is_going_to_pretty(event)
#帥哥state
    def is_going_to_handsome(self,event):
        print("is going to 帥哥")
        text = event.message.text
        return text.lower() == "帥哥"
    def on_enter_handsome(self, event):
        print("is entering to 帥哥")
        reply_token = event.reply_token
        send_text_of_handsome(reply_token, "帥哥")

#抽帥哥state
    def is_going_to_rand_handsome(self, event):
        print("is going to 抽帥哥")
        text = event.message.text
        return text.lower() == "抽"
    def on_enter_rand_handsome(self, event):
        print("is entering 抽帥哥")
        reply_token = event.reply_token
        send_text_of_handsome(reply_token, "抽")
        self.is_going_to_handsome(event)


#回去state#user state
    def is_going_to_back(self, event):
        print("is going to back")
        text = event.message.text
        return text.lower() == "重新選擇"

    def on_enter_user(self,event):
        print("I'm entering 回去")
        reply_token = event.reply_token
        send_text_message(reply_token, "回去")
        self.go_back()
        print("iam user")


