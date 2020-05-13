def message(text):
    text = '元智:' + text
    def print_message():
        print(text)
    return print_message

m = message('Hello')
m()
