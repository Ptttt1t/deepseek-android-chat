import os
import threading
import json
import requests

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.clock import mainthread
from kivy.uix.label import Label

KV = '''
<ChatLabel@Label>:
    markup: True

<ChatLayout>:
    orientation: 'vertical'
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        BoxLayout:
            id: history_box
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            Label:
                id: chat_history
                text: root.chat_history
                markup: True
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
    BoxLayout:
        size_hint_y: None
        height: '50dp'
        TextInput:
            id: user_input
            multiline: False
            hint_text: 'Type your message'
            on_text_validate: root.on_send()
        Button:
            text: 'Send'
            size_hint_x: None
            width: '80dp'
            on_release: root.on_send()
'''

class ChatLayout(BoxLayout):
    chat_history = StringProperty('')

    def append_message(self, role, content):
        self.chat_history += f"[b]{role}: [/b]{content}\n\n"

    def on_send(self):
        user_msg = self.ids.user_input.text.strip()
        if not user_msg:
            return
        self.ids.user_input.text = ''
        self.append_message('User', user_msg)
        threading.Thread(target=self.call_api, args=(user_msg,), daemon=True).start()

    def call_api(self, message):
        api_key = os.environ.get('DEEPSEEK_API_KEY', 'YOUR_DEEPSEEK_API_KEY')
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}',
        }
        data = {
            'model': 'deepseek-chat',
            'messages': [
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': message},
            ],
            'stream': False,
        }
        try:
            response = requests.post('https://api.deepseek.com/chat/completions',
                                     headers=headers, data=json.dumps(data))
            response.raise_for_status()
            result = response.json()
            content = result['choices'][0]['message']['content']
        except Exception as e:
            content = f'Error: {e}'
        self.update_response(content)

    @mainthread
    def update_response(self, content):
        self.append_message('Assistant', content)

class DeepSeekChatApp(App):
    def build(self):
        Builder.load_string(KV)
        return ChatLayout()

if __name__ == '__main__':
    DeepSeekChatApp().run()
