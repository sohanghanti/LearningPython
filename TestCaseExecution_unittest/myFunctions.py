def change_to_captial(text):
    try:
        return text.capitalize()
    except TypeError:
        print('Type Error')
