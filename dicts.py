dict_lesson1 = {
    'city': "Москва",
    'temperature': 20
}
print (dict_lesson1['city'])
dict_lesson1['temperature'] = dict_lesson1['temperature'] - 5
print (dict_lesson1)
print (dict_lesson1.get('country'))
print (dict_lesson1.get('country', 'Россия'))
dict_lesson1['date'] = '27.05.2019'
print (len(dict_lesson1))