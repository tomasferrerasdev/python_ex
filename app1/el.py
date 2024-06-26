import glob


myfiles = glob.glob("Files/*.txt")
myfiles = [filepath.replace("\\", "/") for filepath in myfiles]

print(myfiles)
