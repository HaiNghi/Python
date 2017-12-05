try:
    f=open('simple.txt','r')
    f.write("Hello")
except IOError:
    print("Can not find this file")
finally:
    print("Whatever!")
# else:
#     print("success")
#     f.close()