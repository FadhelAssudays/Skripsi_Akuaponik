import paho.mqtt.client as mqtt 
import csv
import os
from datetime import datetime

csv_file = "file_name.csv"
# Callback saat terhubung ke broker
def on_connect(client, userdata, flags, rc):
    print("Terhubung ke MQTT dengan kode:", str(rc))
    client.subscribe("broker_topic")

# Callback saat menerima pesan
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print("Data diterima:", payload)
    data = payload.split(",")
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker_server", 1883, 60)  # Ganti jika broker di komputer lain

print("Menunggu data dari ESP32... Tekan Ctrl+C untuk berhenti.")
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nBerhenti.")
