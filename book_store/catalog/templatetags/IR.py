from django import template

register = template.Library()


@register.filter(name='persian_int')
def persian_int(english_int):
    devanagari_nums = ('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    number = str(english_int)
    return ''.join(devanagari_nums[int(digit)] for digit in number)


@register.filter(name='persian_date')
def persian_date(english_date):
    devanagari_nums = ('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    date = ''
    for i in english_date:
        if i == '/':
            date += '/'
        else:
            date += devanagari_nums[int(i)]
    return date


@register.filter(name='persian_time')
def persian_date(english_time):
    devanagari_nums = ('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    time = ''
    for i in english_time:
        if i == ':':
            time += ':'
        else:
            time += devanagari_nums[int(i)]
    return time

@register.filter(name='price')
def price(input_int):
    devanagari_nums = ('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    persian_price = ''
    for i in f'{int(input_int):,d}':
        if i == ',':
            persian_price += ','
        else:
            persian_price += devanagari_nums[int(i)]
    return persian_price
