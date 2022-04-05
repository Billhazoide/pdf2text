from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os

# Path to the pdf
path_files = r"/home/evil-twin/Projects/pdf2text/files/"
# List pdf files in folder
folder = os.listdir(path_files)

# Converting pdf to image
print("Capturando arquivos.")

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
    
    print("Convertendo pdf para imagem...\r")
        
    # Get PDF path for each file in folder "files"  
    pdf_path = path_files + pdf
    
    # Convert each PDF page to ppm
    # Put an large size to increase the marge of text error
    pdf_convert = convert_from_path(pdf_path,size=1200)

    # Loop to save img of each page and save in folder
    print("Salvando páginas como imagem...")

    for page in pdf_convert:
      # New generated img from pdf page
      file_name = pdf_splited_name + "-" + str(image_count) + ".jpg"
      
      # Saving imgs to "temp" folder
      page.save(temp_path_files + pdf_splited_name + "/" + file_name, "JPEG")
      
      image_count = image_count +1

############# Starts extract text from images #############


# List directory folder with the folders imgs
imgs_folder = os.listdir("/home/evil-twin/Projects/pdf2text/files/temp/")
# Path for the directories with imgs
imgs_path = "/home/evil-twin/Projects/pdf2text/files/temp/"
# Removing extracted text folder from list
imgs_folder.remove("extracted_text") 

# Loop with the listed image files in each folder
for content in imgs_folder:
  print("Extraindo texto de {}...".format(content))
  
  # Path to each img inside the folder
  img_path = "{}{}/".format(imgs_path, content)
  # Listing imgs in folder
  imgsArray = os.listdir(img_path)
  
  # Loop with each img element
  for img in imgsArray:
    # Read the text from image
    text = str(pytesseract.image_to_string(Image.open(img_path + img)))
    
    # Giving a name for new txt file
    text_file_name = img + ".txt"

    # Check if already have folder with this file name
    folder_exist = os.path.exists(imgs_path + "extracted_text/" + content )

    if(folder_exist == False):
      # Create temporary folder for this file
      os.mkdir(imgs_path + "extracted_text/" + content)

    # Path to seve new txt file
    text_file_path_save = imgs_path + "extracted_text/" + content + "/" + text_file_name
    
    # Creating and saving txt file
    with open(text_file_path_save, 'x') as new_file:
      new_file.write(text)

print("\nConcluído!\r")