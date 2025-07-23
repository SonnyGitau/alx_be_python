


try :
    f = open("doggy_dog.py")
except FileNotFoundError as e:
   print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally..")