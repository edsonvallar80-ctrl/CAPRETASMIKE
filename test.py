import PyPDF2
import pyttsx3

path = open("C:/Users/LENOVO/Downloads/Practica 1 plc.pdf", "rb")

pdfReader = PyPDF2.PdfReader(path)

speak = pyttsx3.init()

for page_num in range(len(pdfReader.pages)):
   
    text = pdfReader.pages[page_num].extract_text()
    
    if text:  
        speak.say(text)


speak.runAndWait()
speak.stop()
