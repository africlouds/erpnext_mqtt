# -*- coding: utf-8 -*-
# Copyright (c) 2015, Africlouds Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
import paho.mqtt.client as mqtt
from frappe import _
from frappe.utils.background_jobs import enqueue

class MQTTClient(Document):
	def autoname(self):
		self.name = make_autoname(self.ip+ ":" + self.port)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("SDC")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.topic == "SDC":
    	print(msg.topic+" "+str(msg.payload))

@frappe.whitelist()
def start_mqtt(ip, port):
	enqueue(listen, ip=ip, port=port)

def listen(ip, port):
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("192.168.56.1", 1883, 60)
	client.subscribe("SDC")
        client.loop_forever()

