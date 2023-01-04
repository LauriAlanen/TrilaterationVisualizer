# Visualize trilateration using matplotlib.
## Trilateration Theory
### Read everything with a grain of salt because im no expert in mathematics.
#### Requirement's for trilateration.
- 1. Three reference points of which (x,y) coordinates are known at all times.
- 2. Distances between the reference point and the unknown point that you want to find out.
#### First we need three known reference points and their (x,y) coordinates, let's call them R1,R2,R3. Point U1 is the unknown point.
![image](https://user-images.githubusercontent.com/80245457/210521723-2ca14822-e557-4528-9303-ca6dd1510c78.png)
#### Then we need the distances between R1-U1, R2-U1, R3-U1.
![image](https://user-images.githubusercontent.com/80245457/210522285-9e5a4aa1-85d0-4685-b51b-a52fcac844d4.png)
#### So now we can make all the reference points circles (C1, C2, C3) with radii == D1-D3
![image](https://user-images.githubusercontent.com/80245457/210522571-8d6226b0-6829-4d7c-bac9-a6d50df70a56.png)



### The plot should look something like this. Ofcourse depending on the input.
![image](https://user-images.githubusercontent.com/80245457/210432809-c6e4aafc-ff9f-417b-9a02-6baf9eee45a1.png)

### Trilateration Use cases
#### Trilateration is used in many real world applications that need positioning including GPS. One project idea i got while working on this project is to track the position where a ping pong ball hits the plate using 3-4 microphones.
