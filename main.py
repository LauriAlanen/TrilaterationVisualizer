import os
import matplotlib.pyplot as plt



def trilaterate(circles):
    a = -2 * circles[0][0] + 2 * circles[1][0]
    b = -2 * circles[0][1] + 2 * circles[1][1]
    c = circles[0][2]**2 - circles[1][2]**2 - circles[0][0]**2 + circles[1][0]**2 - circles[0][1]**2 + circles[1][1]**2
    d = -2 * circles[1][0] + 2 * circles[2][0]
    e = -2 * circles[1][1] + 2 * circles[2][1]
    f = circles[1][2]**2 - circles[2][2]**2 - circles[1][0]**2 + circles[2][0]**2 - circles[1][1]**2 + circles[2][1]**2
    
    x_coordinates = (c*e - f*b)/(e*a - b*d)
    y_coordinates = (c*d - a*f)/(b*d - a*e)
    return (round(x_coordinates, 2), round(y_coordinates, 2))



def plotTrilateration(circles, x, y):
    figure, axes = plt.subplots()
    colors = ["r", "g", "b"]
    for index, circle in enumerate(circles):
        plot = plt.Circle((circle[0], circle[1]), circle[2], color=colors[index], fill=False, label=f"(x-{circle[0]})^2 + (y-{circle[1]})^2 = {circle[2]}^2")
        print(f"Plotted circle with {circle[0]}, {circle[1]}, {circle[2]} ")
        axes.plot([circle[0], x], [circle[1], y], "ro--")
        axes.add_patch(plot)
    axes.legend()
    plt.title(f"Intersection point is at {x,y}")
    plt.grid(color="white", linestyle="solid")
    plt.show()



if __name__ == "__main__":
    plt.style.use('dark_background')
    circles = []

    for i in range(1, 4):
        os.system("cls")
        print(f"Give the circle {i}'s equation in the following format ---> (x-h)^2 + (y-k)^2 = r^2")
        while True:
            try:
                values = ((float(input("h = ")), float(input("k = ")), float(input("r = "))))
                break
            except ValueError:
                print("Values can be only numbers!!!")
        circles.append((values[0], values[1], values[2]))
    
    points = trilaterate(circles)
    plotTrilateration(circles, points[0], points[1])
