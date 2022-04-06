# pdf2text

#### ~~Still doesn't convert to text but this is the idea~~

### **Now it does convert!**

#### Convert pdf into text document (.txt) using OCR.
Put your PDF files inside the "files/" folder, execute the script and everything will be
done by itself, with exception of exclusion of the images converted (files/temp/YOUR_FOLDER_PDF/), the text files (files/temp/extracted_text/YOUR_FOLDER_TXT/) and the original PDF files (files/).

### How to use:
Have pip3 installed in your machine, in the main folder, where is the file "requirements.txt",
use the command **"sudo pip3 install -r requirements.txt"** to install the necessary libraries to can you
use this script, after installed you can run normaly with *"python3 extract.py"*, may be one good
advice to always check up on the folders to don't ocupie space with non used files.

All logs appear in terminal so you can see what is happening, the language of the logs is PT-BR.

#### A few updates incoming like:
- Delete pdf document after all the process.
- Adition of error handlers.
- Savin files outside the project.
- Self text corrector, depending on the quality of the pdf, we get lot of wrong words.
- Maybe an web application where stays up all night so we can convert files any time during the day or night.
- Few malfunction errors on option to not overwrite the images, checking.
- Self translater to any language.
- Detect if page have any text.
