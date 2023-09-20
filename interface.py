import tkinter as tk
from tkinter import filedialog as fd
import main


window = tk.Tk()
window.title('Text Analyser')
window.geometry('1920x1080')


# назначение функций
def create_checkbutton(parts_of_speech: list, grammemes: list) -> dict:
    for_parts_of_speech = {}
    for num in range(len(parts_of_speech)):
        for_parts_of_speech[parts_of_speech[num]] = tk.StringVar()
        packs[parts_of_speech[num]] = tk.Checkbutton(text=parts_of_speech[num], variable=for_parts_of_speech[parts_of_speech[num]], onvalue=grammemes[num], offvalue='')
    return for_parts_of_speech


def checkbutton_morphy() -> list:
    parts_of_speech_checkbuttom = []
    for key in for_parts_of_speech.keys():
        if for_parts_of_speech[key].get():
            parts_of_speech_checkbuttom.append(for_parts_of_speech[key].get())
    return parts_of_speech_checkbuttom


def path_to_file():
    grammenes = checkbutton_morphy()
    text_analyser = main.TextAnalyser(source_file=packs['file_name']['text'], parts_of_speech=grammenes)
    packs['word_count'] = tk.Label(text=f'Количество слов в этом тексте: {len(text_analyser.words)}', font=("Arial", 12))
    packs['word_pos'] = tk.Label(text=f'Количество слов выбранных частей речи: {len(text_analyser.pos_words)}', font=("Arial", 12))
    word_cloud = tk.PhotoImage(file='./wordcloud.png')
    lable_worldcloud = tk.Label(image=word_cloud)
    for item in packs.items():
        item[1].pack(anchor='nw', padx=5, pady=2)
    lable_worldcloud.pack(anchor='center')


def select_file():
    filename = fd.askopenfilename()
    if filename != '':
        packs['file_name']['text'] = filename


packs = {}
# ввод пути к файлу
packs['path_to_file_lable'] = tk.Button(text='Выберете файл с текстом', command=select_file, font=("Arial", 12))
packs['text_file_name'] = tk.Label(text='Путь к файлу:', font=("Arial", 12))
packs['file_name'] = tk.Label(text='Не указан')


# выбор частей речи

packs['morphy_lable'] = tk.Label(text='Выберите части речи:', font=("Arial", 12))
for_parts_of_speech = create_checkbutton([
    'Существительные',
    'Прилагательные(полное)',
    'Прилагательные(краткое)',
    'Компаративы',
    'Глаголы(личная форма)',
    'Глаголы(инфинитив)',
    'Причастия(полное)',
    'Причастия(кратко)',
    'Деепричастия',
    'Числительные',
    'Наречия',
    'Местоимения',
    'Предактивы',
    'Предлоги',
    'Союзы',
    'Частицы',
    'Междометия'
], [
    'NOUN',
    'ADJF',
    'ADJS',
    'COMP',
    'VERB',
    'INFN',
    'PRTF',
    'PRTS',
    'GRND',
    'NUMR',
    'ADVB',
    'NPRO',
    'PRED',
    'PREP',
    'CONJ',
    'PRCL',
    'INTJ'
])

packs['path_to_file_buttom'] = tk.Button(text='Провести анализ текста', command=path_to_file)

for item in packs.items():
    item[1].pack(anchor='nw', padx=5, pady=2)




window.mainloop()