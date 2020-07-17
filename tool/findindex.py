str_1 = input('Please input the text')
str_1 = str_1.replace('  ',' ')
str_1 = str_1.replace("'",'')
while True:
    char_1=str(input('Please input the labeled name which you would like to predict:'))
    start=0
    index = 0
    while index != -1:
        index = str_1.find(char_1, start)
        start = index + 1
        end = index + len(char_1)
        print(index,end)
                
