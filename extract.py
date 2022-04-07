from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os
from time import sleep
import sys

def print_same_line(text):
  sys.stdout.write('\r')
  sys.stdout.flush()
  sys.stdout.write(text)
  # sys.stdout.flush()

class Main:

  # Converting pdf to image
  def convertDocuments():
    
    #### PATHS ####
    # Path to the pdf
    path_files = os.getcwd() + "/files/"

    # List pdf files in folder
    folder = os.listdir(path_files)

    # Temporary path to store the imgs
    temp_path_files = path_files + "temp/"
    #### PATHS ####

    for pdf in folder: 
      # Count the pages will be stracted later
      image_count = 1

      # Convert documents count
      converted_pdf_arr = []
      converted_pdf_arr.append(pdf)

      # Check only for pdf files
      if(pdf.endswith(".pdf")):
        print("Capturando arquivos.")

        # PDF file name without the ".pdf"
        pdf_splited_name = pdf[0:-4]
        
        print("Processando arquivo: \"{}\".\r".format(pdf_splited_name))

        # Check if already have folder with this file name
        folder_exist = os.path.exists(temp_path_files + pdf_splited_name)

        if(folder_exist == False):
          # Create temporary folder for this file
          os.mkdir(temp_path_files + pdf_splited_name)

        folder_empty = os.listdir(temp_path_files + pdf_splited_name)
        
        # If folder is not empty
        if(len(folder_empty) > 0):
          print("\nA pasta destino já contém arquivos do tipo PDF, ao continuar os arquivos serão sobrescritos.")
          user_input = input("Deseja continuar? (s/n): ")
          
          if(user_input == "s" or user_input == "n"):
            
            if(user_input == "s"):
              print("\nContinuando com a conversão de \"{}\".".format(pdf_splited_name))
              pass
            
            elif(user_input == "n"):
              print("\nO arquivo \"{}\" não será convertido".format(pdf_splited_name))
              continue
          
          else:
            print("Por favor responda com \"s\" para Sim ou \"n\" para Não.")
            user_input = input("Deseja continuar? (s/n): ")
        
        print("Convertendo pdf para imagem...")
            
        # Get PDF path for each file in folder "files"  
        pdf_path = path_files + pdf
        
        # Convert each PDF page to ppm
        # Put an large size to decrease the marge of text error
        pdf_convert = convert_from_path(pdf_path,size=2000)

        # Loop to save img of each page and save in folder
        print("Salvando páginas.")

        for page in pdf_convert:
          # New generated img from pdf page
          file_name = pdf_splited_name + "-" + str(image_count) + ".jpg"
          
          # Saving imgs to "temp" folder
          page.save(temp_path_files + pdf_splited_name + "/" + file_name, "JPEG")
          
          image_count = image_count +1

      else:
        return print("Nenhum arquivo cadidato a conversão,\ninsira um documento na pasta \"files\".\nVerificando em 30s.")
  
    # Remove all items from converted pdfs array
    # converted_pdf_arr.clear()
        
  ############# Starts extract text from images #############

  def extractText():
      
    #### PATHS ####
    # Path to the pdf
    path_files = os.getcwd() + "/files/"

    # Temporary path to store the imgs
    temp_path_files = path_files + "temp/"
    #### PATHS ####

    # List directory folder with the folders imgs
    imgs_folder = os.listdir(os.getcwd() + "/files/temp/")
    # Path for the directories with imgs
    imgs_path = os.getcwd() + "/files/temp/"
    # Removing extracted text folder from list
    imgs_folder.remove("extracted_text") 

    # Loop with the listed image files in each folder
    for content in imgs_folder:
      # Check if already have folder with this file name
      folder_exist = os.path.exists(imgs_path + "extracted_text/" + content )

      if(folder_exist == False):
        # Create temporary folder for this file
        os.mkdir(imgs_path + "extracted_text/" + content)

      # Checking if folder empty 
      folder_empty = os.listdir(temp_path_files + "extracted_text/" + content)
      
      # If folder is not empty
      if(len(folder_empty) > 0):
        print("\nA pasta destino já contém arquivos do tipo TXT, ao continuar os arquivos serão sobrescritos.")
        user_input = input("Deseja continuar? (s/n): ")
        
        if(user_input == "s" or user_input == "n"):
          
          if(user_input == "s"):
            print("\nContinuando com a extração de \"{}\".".format(content))
            # Check files .txt in folder and delete one by one, mantaining the folder.
            files_in = os.listdir(os.getcwd() + "/files/temp/extracted_text/" + content)
            for file in files_in:
              os.remove(imgs_path + "extracted_text/" + file[0:-6] + "/" + file)
            pass
          
          elif(user_input == "n"):
            print("\nO arquivo \"{}\" não será extraído".format(content))
            continue
        
        else:
          print("Por favor responda com \"s\" para Sim ou \"n\" para Não.")
          user_input = input("Deseja continuar? (s/n): ")

      print("Extraindo texto de \"{}\"...".format(content))

      # Path to each img inside the folder
      img_path = "{}{}/".format(imgs_path, content)
      # Listing imgs in folder
      imgsArray = os.listdir(img_path)
      
      total_page_converted = 0

      # Loop with each img element
      for img in imgsArray:
        # Read the text from image
        text = str(pytesseract.image_to_string(Image.open(img_path + img)))
        
        # Remove the ".jpg" from the name
        img_sliced_name = img[0:-4]

        # Giving a name for new txt file
        text_file_name = img_sliced_name + ".txt"
        total_page_converted = total_page_converted + 1

        # Formating terminal display name
        new_img_name = img_sliced_name.replace("-","  ")
        print_same_line("Página: {} / Total de páginas:{}".format(new_img_name[-3:], total_page_converted))

        # Path to seve new txt file
        text_file_path_save = imgs_path + "extracted_text/" + content + "/" + text_file_name
        
        # Creating and saving txt file
        with open(text_file_path_save, 'x') as new_file:
          new_file.write(text)

    # Remove pdf that already converted
    pdf_delete = os.getcwd() + "/files/"
    original_pdf_list = os.listdir(pdf_delete)
    
    for og_pdf in original_pdf_list:
      if(og_pdf.endswith(".pdf")):
        os.remove(pdf_delete + og_pdf)

    print("\nConcluído!\r")
      
if __name__ == "__main__":
  convert = Main

  while True:
    try:convert.convertDocuments()
    except Exception as e: print("Erro ao tentar converter documentos", e)
    
    try: convert.extractText()
    except Exception as e: print("Erro ao tentar extrair o texto das páginas.", e)

    # Wait 30sec
    sleep(30)
