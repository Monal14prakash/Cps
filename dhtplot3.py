import time
import board
import matplotlib.pyplot as plt
import adafruit_dht
sensor=adafruit_dht.DHT11(board.D4)
temp=[]
humi=[]
a=10
while (a>0):
    t=sensor.temperature
    h=sensor.humidity
    temp.append(t)
    humi.append(h)
    time.sleep(2)
    a=a-1

print("humi: ",h,"temp: ",t)

plt.plot(temp,r)
plt.xlabel("No of iterations")
plt.ylabel("temperature")
plt.title("Temp graph")
plt.show()

plt.bar(range(len(humi)),humi)
plt.xlabel