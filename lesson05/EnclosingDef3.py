def message(text):
    text = '元智:' + text
    def print_message():
        print(text)
    return print_message()  # 有括號直接執行，不需再輸入m()

m = message('Hello')
