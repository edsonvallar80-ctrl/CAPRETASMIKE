# Importar módulos
import PyPDF2
import pyttsx3

# Abrir el archivo PDF en modo lectura binaria
# Abrir el archivo PDF en modo lectura binaria
path = open("C:/Users/LENOVO/Downloads/Practica 1 plc.pdf", "rb")


# Crear un objeto PdfReader (PyPDF2 actualizado usa PdfReader en lugar de PdfFileReader)
pdfReader = PyPDF2.PdfReader(path)

# Inicializar el motor de texto a voz
speak = pyttsx3.init()

# Recorrer todas las páginas del PDF
for page_num in range(len(pdfReader.pages)):
    # Extraer texto de la página
    text = pdfReader.pages[page_num].extract_text()
    
    if text:  # Verifica que haya texto
        speak.say(text)

# Reproducir todo el texto
speak.runAndWait()
speak.stop()
