"""This module provides a simple GUI to zip files. BONUS EXAMPLE 166"""

import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose file")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose folder")

compress_button = sg.Button("Compress")

layout = [
    [label1, input1, choose_button1],
    [label2, input2, choose_button2],
    [compress_button],
]

window = sg.Window(title="File compressor", layout=layout)
window.read()
window.close()
