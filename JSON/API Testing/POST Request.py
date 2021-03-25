def outer():
    try:
        x = 5
        def inner():
            print(x)
            x += 1
            print(x)
        inner()
    except:

outer()
