"""In task 1 we are going to answer some questions"""


# Как удалить дубли строк из файла?
# We may use a set (also good to use OrderedDict for complicated solutions)
def unique_lines():
    file_path = "./file.txt"
    file = open(file_path, "r", encoding='utf-8')
    lines = set(file.readlines())

    print(lines)
    with open("uniques.txt", "w") as uni_file:
        uni_file.write(' '.join(lines))

    uni_file.close()
    file.close()


unique_lines()


# Как дописать содержимое одного текстового файла в конец второго?
# in console $ cat second.txt >> first.txt


# Как разбить текстовый файл на несколько по 100 строк в каждом?
# in console $ split -l 100 ~/folder/filename ~/target_folder/divided_file_


# Как вывести на экран первые 30 строк файла?
# in console $ head -n 30 file.txt

# Как вывести на экран последние 30 строк файла?
# in console $ tail -n -30 file.txt


# Как вывести на экран строки текстового файла /tmp/file.txt начинающиеся со слова ‘START’?
def special_lines():
    import re
    file_path = "./tmp/file.txt"
    lines = open(file_path, "r", encoding='utf-8').readlines()
    for line in lines:
        if re.match(r"^START*", line) is not None:
            print(line)


special_lines()

# Как среди нескольких файлов в директории найти те, которые содержат слово ‘test’?
# in console $ grep -rnw '/PATH/TO/DIR' -e 'test'
