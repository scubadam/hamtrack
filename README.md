# hamtrack
Hamster Wheel Tracking on Raspberry Pi with an optical disc encoder sensor.

How far does your hamster run?

#Wheel axel sensor fitting
![image](https://user-images.githubusercontent.com/21081296/119868356-da71aa00-bf16-11eb-84c2-a306e08bf5c1.png)

![image](https://user-images.githubusercontent.com/21081296/119868470-fa08d280-bf16-11eb-8462-267d0a0f3efd.png)

![image](https://user-images.githubusercontent.com/21081296/119868508-055bfe00-bf17-11eb-881d-6baded904672.png)

#Raspberry Pi GPIO for reading sensor and controlling lights and camera
![image](https://user-images.githubusercontent.com/21081296/119868588-2290cc80-bf17-11eb-89f8-cc43cde30ffb.png)

#Uses gpiozero and offers a callback param to receive your data.

#Demo testing done using a straw with the encoder disc on the end (no hamsters were harmed in the hacking of this project)
![image](https://user-images.githubusercontent.com/21081296/119869004-ab0f6d00-bf17-11eb-9533-24ec0e4ef497.png)

#Sample pushing data to to influxDb rendered in grafana - both running on the Raspberry Pi
![image](https://user-images.githubusercontent.com/21081296/119868782-671c6800-bf17-11eb-820d-bc7c3261b7fc.png)
