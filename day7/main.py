'''
file=open("sample3.txt","a")
file.write("\njidesh")'''
import os
try:
    with open("image.jpg","rb")as f:
     image = f.read()
     print(image)

except Exception as e:
   print(f"Error :{e}")

finally:
   if  os.path.exists("image.jpg"):
      print("id undu")
   else: 
      print("illa")


   


