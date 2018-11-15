# Renamer50

Yet another one batch renamer app, with simple and intuitive drag-and-drop interface and variety of renaming rules.
A graduation project for Harvard CS50x course

## Getting started

1. Install dependencies: `pip3 install -r requirements.txt`
2. Run the app: `python app.py`

## How to use
If you are video type: [Demo](https://youtu.be/cMsidcfVKwk)

The app has intuitive drag and drop interface. Renaming your files requires only few steps:

1. Drag your files inside the right part of the app - they will appear immediately. If you want to delete some files later, select the relative checkbox and press button "Delete"
2. Create a so-called block and add it to the "Block box". Block is just a part of new filename - see below detailed info on all available blocks. "Block box", or just blocks area is an area where all your blocks appear. Keeping them there lets you reuse the same block as many times as you want, and save some extra mouse moves.
3. Take a block from the Block are and add it to the new pattern area. You can add as much blocks as you want, and change their order. If at some point you feel you don't need one the blocks, just drop it on the trash bin area. It will disappear from your pattern area, but will be still available in the blocks are, in case you change your mind.
4. Whatever block you choose, it can also has additional options - see [Block options](#Block-options)
5. Check the previews of new filenames in the table - it is updated dynamically, when you change the pattern.
6. Once you feel ready, click "Rename"!
7. In case of name conflict, files will not be renamed, and the app will inform you about it. Change your pattern to resolve conflict.

## Blocks

As of current version, following blocks are available:

### Text blocks

* **Exact text**. Any exact text/character sequence will be inserted.  
 _Example:_ __Exact text: myVacation__  
  `C:/photos/IMG0225.jpg -> C:/photos/myVacation.jpg`

* **Date**. Select any date and choose desired formatting.  
 _Example:_ __date: 12/11/2018 yy-MM-dd__    
  `C:/photos/IMG0225.jpg -> C:/photos/18-11-12.jpg`

* **Directory name**. Name of parent directory.  
 _Example:_ __Directory name__  
  `C:/photos/IMG0225.jpg -> C:/photos/photos.jpg`

* **Original name**. Full original name of file. Won't make any changes if used alone but helpful in combination with other blocks.  
 _Example:_ __Original name__  
`C:/photos/IMG0225.jpg -> C:/photos/IMG0225.jpg`

* **Word in current name**. Takes 2 parameters: word number and separators. Separators are used to determine how the filename should be split. You can specify multiple separators, splitting them with "|", for example "\_| |\-". If none are specified, default separator is " "(one whitespace), but if any of separators are specified, whitespace is ignored (unless it is specially mentioned in the list of separators, as in example above)  
  _Example:_ **Word:2:_|-**  
  ```C:/photos/my-vacation_2005.jpg -> C:/photos/vacation.jpg```

### Number blocks

* **Counter**. A numbering block, each file within the list will get an incremented number. You may specify starting number and leading zeroes in front.  
 _Example:_ __Nr:0001__  
  `C:/photos/IMG0225.jpg -> C:/photos/0001.jpg`

* **Number of items in list**. Number of files in current list of files. This number is not changing. Can be used effective with the counter (see example)  
 _Example:_ __Nr:08-Nr:All__  
  `C:/photos/IMG0225.jpg -> C:/photos/08-17.jpg`

* **Number of files in folder**. Number of files in parent folder. Will be different for files, located in different folders.  
 _Example:_ __DirectoryName\_ OriginalName- Nr:01__  
  `C:/photos/IMG0225.jpg -> C:/photos/photos_IMG0225-01.jpg`

## Block options

Each block (with some obvious exceptions) can take 2 additional parameters:

* __Change case:__ _lowercase, uppercase, reversed_. The text case will be changed accordingly. Numbers and symbols won't be affected.
* __Include separators:__ add any separators to split the block. Each block can have it's individual separator, and it can include any sequence of characters or even text.  
   _Example:_ __Nr:Folder__  
  `C:/photos/IMG0225.jpg -> C:/photos/182.jpg`

## Built with

* [PyQt5](http://www.riverbankcomputing.com/software/pyqt/intro)
* [QT Designer](https://www.qt.io/qt-features-libraries-apis-tools-and-ide/)

## License

This project is licensed under the MIT License.

## Authors

* [**Irina Illustrova**](https://github.com/Illustrova)