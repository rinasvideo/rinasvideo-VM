@echo off
pyinstaller rinasvideo.py -F -i NotePC.ico --exclude tkinter --exclude xml
pause