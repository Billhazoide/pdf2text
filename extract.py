from asyncore import write
from pdf2image import convert_from_bytes, convert_from_path
from time import sleep
from PIL import Image
import pytesseract
import sys
import os

# Print things in "one single line"
def print_same_line(text):
  sys.stdout.write('\r')
  sys.stdout.flush()
  sys.stdout.write(text)
  sys.stdout.flush()

# Path to the pdf
path_files = r"/home/evil-twin/Projects/pdf2text/files/"
# List pdf files in folder
folder = os.listdir(path_files)

print("Capturando arquivos.")

# Converting pdf to image
for pdf in folder: 
  # Count the pages will be stracted later
  image_count = 1

  # Check only for pdf files
  if(pdf.endswith(".pdf")):
    # Temporary path to store the imgs
    temp_path_files = path_files + "temp/"

    # PDF file name without the ".pdf"
    pdf_splited_name = pdf[0:-4]
    
    print("Processando arquivo: \"{}\".\r".format(pdf_splited_name))

    sleep(1)

    # Check if already have folder with this file name
    folder_exist = os.path.exists(temp_path_files + pdf_splited_name)

    if(folder_exist == False):
      # Create temporary folder for this file
      os.mkdir(temp_path_files + pdf_splited_name)

    folder_empty = os.listdir(temp_path_files + pdf_splited_name)
    
    # If folder is not empty
    if(len(folder_empty) > 0):
      print("A pasta destino já contém arquivos, ao continuar os arquivos serão sobrescritos.")
      user_input = input("Deseja continuar? (s/n): ")
      
      if(user_input == "s" or user_input == "n"):
        
        if(user_input == "s"):
          print("Continuando com a conversão de \"{}\".".format(pdf_splited_name))
          pass
        
        else:
          print("O arquivo \"{}\" não será convertido".format(pdf_splited_name))
          continue
      
      else:
        print("Por favor responda com \"s\" para Sim ou \"n\" para Não.")
        user_input = input("Deseja continuar? (s/n): ")
        
    # Get PDF path for each file in folder "files"  
    pdf_path = path_files + pdf
    
    # Convert each PDF page to ppm
    pdf_convert = convert_from_path(pdf_path,size=800)

    # Loop to save img of each page and save in folder
    print_same_line("Convertendo pdf para imagem...\r")
    sleep(1)

    print("Salvando páginas como imagem...")

    for page in pdf_convert:
      # New generated img from pdf page
      file_name = pdf_splited_name + "-" + str(image_count) + ".jpg"
      
      # Saving imgs to "temp" folder
      page.save(temp_path_files + pdf_splited_name + "/" + file_name, "JPEG")
      
      image_count = image_count +1

sys.stdout.write("clear")
sys.stdout.flush()

print("\nConcluído!\r")