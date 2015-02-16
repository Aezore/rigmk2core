__author__ = 'Research - Jose Rodriguez'
import socket

import kivy


kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
server_address = ('192.168.0.196', 55555)

socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket1.bind(server_address)
data, addr = socket1.recvfrom(1024)
strvalue = data.decode('utf-8')


class TimeFetch(GridLayout):

    def etiqueta(self, **kwargs):
        super(TimeFetch, self).__init__(**kwargs)
        self.cols = 1
        self.tiempo = Label(text='tiempo ' + strvalue)
        self.add_widget(self.tiempo)


class RigMK2core(App):

    def recv_mesg(self):
        TimeFetch.tiempo.text += 'tiempo ' + strvalue

    def build(self):
        tiempo = TimeFetch()
        Clock.schedule_interval(tiempo.etiqueta, 1.0 / 60.0)
        return tiempo


if __name__ == '__main__':
    RigMK2core().run()







# Old code
#-----------------------
# while True:
# data, addr = socket1.recvfrom(1024)
#    # button1 = Button(size_hint=(None, None), text='plop')
#    strvalue = data.decode('utf-8')
#    print("Received: ", strvalue)
