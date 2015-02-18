__author__ = 'Research - Jose Rodriguez'

# Import statements
############################################
import socket
import kivy

kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.properties import StringProperty

# Network Settings
############################################
server_address = ('192.168.0.193', 55555)  # This computer's IP address and port
raspi_address = ('192.168.0.197', 55554)  # Raspberry Pi's address and port

socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # bind server (this computer) to receive packets
socket1.bind(server_address)  #

socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create another socket that points to the raspi

# Main Program
############################################


class TimeFetch(BoxLayout):
    def update_time(self, *args):
        print("Fetching time: ")
        comando = 20
        socket2.sendto(bytes(comando), raspi_address)
        data, addr = socket1.recvfrom(1024)
        label = self.ids.time_label
        label.text = str(data)


class RigMK2core(App):
    def build(self):
        return TimeFetch()


if __name__ == '__main__':
    RigMK2core().run()