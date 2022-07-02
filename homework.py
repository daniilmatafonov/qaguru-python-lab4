# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__


def open_browser(name):
    print_name(open_browser, name)
    pass


def go_to_companyname_homepage(homepage):
    print_name(go_to_companyname_homepage, homepage)
    pass


def find_registration_button_on_login_page(page_url, button_text):
    print_name(find_registration_button_on_login_page, page_url, button_text)
    pass


def print_name(f_name, *args):
    print("Func name: ", f_name.__name__.replace('_', ' ').capitalize(), "args: ", *args)


open_browser('chrome')
go_to_companyname_homepage('https://demoqa.com/automation-practice-form')
find_registration_button_on_login_page('https://demoqa.com/automation-practice-form', 'Submit')
