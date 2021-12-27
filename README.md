# Declutter Your Downloads Folder

1. open up your terminal and follow these steps

    `git clone git@github.com:IAmPissed/downloads-declutterer.git`
  
2. navigate to the project folder and run this command

    `touch .env`
  
3. open up the .env filer and enter the following text

    `SOURCE_FOLDER_PATH="path/to/your/downloads/folder"`
  
4. within the project folder run this command to install dependencies

    `pip install -r requirements.txt`

5. now you can set up your downloads folder structure like this:

    * Downloads
      * Audio
      * Images
      * Documents
        * Word
        * Excel
        * PowerPoint
        * PDF
        * Text
      * Programs
      * Videos
      * Compressed
