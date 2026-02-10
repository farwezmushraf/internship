import os
try:
    with open("image.jpg","rb")as f:
     image = f.read()
     print(image)

except Exception as e:
   print(f"Error :{e}")

finally:
   print("Oops! That file doesn't exist yet" )


   

