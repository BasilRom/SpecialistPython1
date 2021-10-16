# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

# def log(text, file="log.txt"):
#     pass


# log("hello world")  # дописывает "hello world" в конец файла log.txt
# log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt

def log(text, file):
    f = open(file, 'a', encoding= 'utf-8')
    f.write(text)
    f.close()

log('\nРагнар должен быть убит', "seek.txt")
