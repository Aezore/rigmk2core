__author__ = 'Research - Jose Rodriguez'
import socket

import kivy


kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.properties import StringProperty

server_address = ('192.168.0.193', 55555)
raspi_address = ('192.168.0.197', 55554)

socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # bind server
socket1.bind(server_address)

socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create raspi send command bind


# data, addr = socket1.recvfrom(1024)
#strvalue = data.decode('utf-8')


class TimeFetch(BoxLayout):

    #text_label = StringProperty("Tiempo:")

    # def __init__(self, **kwargs):
    #     super(TimeFetch, self).__init__(**kwargs)
    #
    #     self.cols = 2
    #
    #     tiempo = Label(text=text_label)
    #     self.add_widget(tiempo)
    #
    #     boton = Button(text="Fetch!")
    #     boton.bind(on_press=self.on_event)
    #     self.add_widget(boton)

    def on_event(self, *args):
        print("Fetching time: ")
        comando = 20
        socket2.sendto(bytes(comando), raspi_address)
        data, addr = socket1.recvfrom(1024)
        label = self.ids.time_label
        label.text = str(data)


class RigMK2core(App):
    def build(self):
        return TimeFetch()
        #tiempo = TimeFetch()
        #return tiempo


if __name__ == '__main__':
    RigMK2core().run()







# Old code
#-----------------------
# while True:
# data, addr = socket1.recvfrom(1024)
#    # button1 = Button(size_hint=(None, None), text='plop')
#    strvalue = data.decode('utf-8')
#    print("Received: ", strvalue)
