def func():
    print("func() in name_main.py")

print("TOP LEVEL ONE.PY")

if __name__== '__main__':
    print("name_main.py is being run dirrectly")
else:
    print("name_main has been imported")