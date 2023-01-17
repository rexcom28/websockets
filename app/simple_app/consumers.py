from django.template.loader import render_to_string
from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer
from datetime import datetime
import time 
import threading
from random import randint

class BMIConsumer(JsonWebsocketConsumer):
    '''Consumer'''
    def connect(self):
        '''Connect'''
        self.accept()

    def disconnect(self, close_code):
        '''disconnect'''
        pass

    def receive_json(self,data):
        '''event when data is received'''
        height = data['height']/100
        weight =data['weight']
        bmi = round(weight/ (height ** 2),1 )
        print('aaaaa')
        self.send_json(
            content={
                
                "action":"BMI result",
                "html":render_to_string(
                    "components/_bmi_result.html",
                    {"height":height, "weight":weight,"bmi":bmi}
                )
            }
        )


class EchoConsumer(WebsocketConsumer):
    '''class docstring'''

    def connect(self):
        '''Event when client connects'''
        #informs cliente of successful connection

        self.accept()

        #send message to client
        self.send(text_data="You are connected by WebSockets!")

        def send_time(self):
            while True:
                self.send(text_data=str(datetime.now().strftime("%H:%M:%S")))
                time.sleep(1)
        threading.Thread(target=send_time, args=(self,)).start()

    def disconnect(self,close_code):
        """Event when client disconnects"""
        pass

    def recive(self, text_data):
        """event when data is recived"""
        pass


class BingoConsumer(JsonWebsocketConsumer):
    '''asdasd'''

    def connect(self):
        '''connect'''
        self.accept()
        # Send numbers to client
        # generates numbers 5 randos number, approximately between 1 and 10
        random_numbers = list(set([randint(1,10) for _ in range(5)]))
        message = {
            'action':'New ticket',
            'ticket':random_numbers
        }
        self.send_json(content=message)

        def send_ball(self):
            while True:
                random_ball = randint(1,10)
                message = {
                    'action': 'New ball',
                    'ball': random_ball
                }
                self.send_json(content=message)
                time.sleep(1)
        threading.Thread(target=send_ball, args=(self,)).start()

    def disconnect(self, close_code):
        '''Event when client diconnects'''
        pass

    def recive_json(self, data):
        '''Event when data is recived'''
        pass
