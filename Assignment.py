base=float(input("base:"))
height=float(input("height:"))
area=0.5*base*height 
print("area:",area)

radius=float(input("enter the radius of the circle"))
area=3.14*radius*radius 
print("area of circle is:",area)

celcius=float(input("enter the temperature in celsius:"))
fahrenheit=(celcius*1.8)+32
print(" %.2f C= %.2f f" %(celcius,fahrenheit))

fahrenheit=float(input("temperature(F):"))
celcius=(fahrenheit-32)/1.8
print("temperature(C):",celcius)
