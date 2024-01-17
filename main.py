from gtts import gTTS

# Inputs

filename = input("Название файла/file name ") + ".mp3"
text = input("Введите текст/text ")

# Save

audio = gTTS(text=text,
             lang="ru",
             slow=False)

audio.save(filename)
