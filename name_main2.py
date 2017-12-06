import name_main
print("TOP LEVEL TWO.PY")
name_main.func()

if __name__ == '__main__':
    print("name_main2.py is being run dirrectly")
else:
    print("name_main2 has been imported")
