# coding=utf-8
from flask import jsonify, request, Blueprint
from flask.templating import render_template

utils_module = Blueprint('utils_module', __name__,
                        template_folder='templates')

try:
    
    @utils_module.route('/utils')
    def utils():
        return render_template('utils.html')

    def GetDatetime():  
        date_time = datetime.now().strftime("%A %B %Y %H:%M:%S")
        return date_time

    @utils_module.route('/utils/GetDatetime')
    def utilsGetDatetime():
        return jsonify(GetDatetime()), 200 

    @utils_module.route('/utils/GetMonths')
    def GetMonths():
        return jsonify(get_forward_month_list()), 200 

    @utils_module.route('/utils/GetMonthsFull')
    def GetMonthsFull():
        return jsonify(get_forward_month_list_short()), 200 


    @utils_module.route('/utils/get_day_name')
    def get_day_name():
        return jsonify(get_day_name()), 200 


    from datetime import datetime
    from calendar import month_abbr, month_name, day_name

    def get_forward_month_list():
        month = datetime.now().month  # current month number
        return [month_abbr[(month % 12 + i) or month] for i in range(12)]

    def get_forward_month_list_short():
        month = datetime.now().month # current month number
        return [month_name[(month % 12 + i) or month ] for i in range(12)]

    def get_day_name():
        return list(day_name)




    @utils_module.route('/utils/password_generator')
    def utils_password_generator():
        return jsonify(password_generator()), 200 

    @utils_module.route('/utils/password_generator_Letter_numbers')
    def utils_password_generator_Letter_numbers():
        return jsonify(password_generator_Letter_numbers()), 200 

    import string
    import random

    LETTERS = string.ascii_letters
    NUMBERS = string.digits  
    PUNCTUATION = string.punctuation    

    def password_generator(length=8):
        '''
        Generates a random password having the specified length
        :length -> length of password to be generated. Defaults to 8
            if nothing is specified.
        :returns string <class 'str'>
        '''
        # create alphanumerical from string constants
        printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

        # convert printable from string to list and shuffle
        printable = list(printable)
        random.shuffle(printable)

        # generate random password and convert to string
        random_password = random.choices(printable, k=length)
        random_password = ''.join(random_password)
        return random_password

    def password_generator_Letter_numbers(length=8):
        '''
        Generates a random password having the specified length
        :length -> length of password to be generated. Defaults to 8
            if nothing is specified.
        :returns string <class 'str'>
        '''
        # create alphanumerical from string constants
        printable = f'{LETTERS}{NUMBERS}'

        # convert printable from string to list and shuffle
        printable = list(printable)
        random.shuffle(printable)

        # generate random password and convert to string
        random_password = random.choices(printable, k=length)
        random_password = ''.join(random_password)
        return random_password

    def get_string(letters_count, digits_count):
        letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
        digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

        # Convert resultant string to list and shuffle it to mix letters and digits
        sample_list = list(letters + digits)
        random.shuffle(sample_list)
        # convert list to string
        final_string = ''.join(sample_list)
        print('Random string with', letters_count, 'letters', 'and', digits_count, 'digits', 'is:', final_string)

except Exception as exc:
    print(exc)
# log
 
    
