def cal_rectangle(lenght,width):
        area = lenght*width
        peremeter =2*(lenght + width)

        return (area,peremeter)
lenth=float(input("enter the lenght of rectangle"))
width=float(input("enter tnhe lenght of the rectangle"))
area,peremeter =cal_rectangle(lenth,width)
print("area:",area,"parameter:",peremeter)