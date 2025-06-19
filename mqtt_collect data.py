import paho.mqtt.client as mqtt 
import csv
import os
from datetime import datetime

csv_file = "data_mqtt_lagi.csv"
# Callback saat terhubung ke broker
def on_connect(client, userdata, flags, rc):
    print("Terhubung ke MQTT dengan kode:", str(rc))
    client.subscribe("bot/stasiun_cuaca")

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

client.connect("iot.digitalasistensi.com", 1883, 60)  # Ganti jika broker di komputer lain

print("Menunggu data dari ESP32... Tekan Ctrl+C untuk berhenti.")
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nBerhenti.")
