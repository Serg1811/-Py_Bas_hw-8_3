import os

#Каталог из которого будем брать изображения
directory = 'files/'

#Получаем список файлов в переменную files
files = os.listdir(directory)
print(files)
#Фильтруем список
name_txt_files = filter(lambda x: x.endswith('.txt'), files)
length_name_content = []
for name_txt in name_txt_files:
   with open(directory + name_txt, encoding='utf-8') as f:
      text = f.readlines()
      length = str(len(text))
      length_name_content += [[length, name_txt, ''.join(text)]]
      # print(length, text)
length_name_content.sort(reverse=True)
print(length_name_content)
with open('new_text.txt', 'w+', encoding='utf-8') as f:
   for text in length_name_content:
      print(text)
      f.write(text[1] + '\n' + text[0] + '\n' + text[2]+'\n')

# s = [[1, 3], [2, 2], [3, 1]]
# s.sort()
# print(s)
