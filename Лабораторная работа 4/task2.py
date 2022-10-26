def get_count_char(str_):
    dict = {}
    sstr_="".join(str_.split())
    lstr_ = sstr_.lower()
    count = 0
    for symbol in lstr_:
        bb = symbol.isalpha()
        if bb:
            count +=1
            if symbol in dict:
                dict[symbol]+=1
            else:
                dict[symbol] = 1
        else:
            pass

    return count, dict

def get_char(dict_, count_):
    for symbol in dict_:
        dict_[symbol] =round(dict_[symbol]/count_*100,2)

    return dict_

    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
Count, DD = get_count_char(main_str)
print(DD)
" в процентах "
print(get_char(DD,Count))