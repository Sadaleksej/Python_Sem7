def count_syllables (str):
    n = 0
    str = str.upper()    
    dicRu = ['А', 'Е', 'И', 'О', 'У', 'Ё', 'Я', 'Ы', 'Э', 'Ю']
    for i in dicRu:
        if i in str:
            n = n + str.count(i)
    return n

rhyme = input("Винни, вводи свою кричалку: ")
strings = []
strings = rhyme.split(" ")
print(strings)

if len(set(map(count_syllables, strings))) == 1:
    print("Парам пам-пам, Винни, ритм есть!")
else:
    print("Пам парам, чушь какая-то. Попробуй еще, Винни!")



    
    
    