filenames = ["doc.txt", "report.txt", "presentation.txt"]

for filename in filenames:
    file = open(filename, "w", encoding="utf-8")
    file.write("Hello")
    file.close()
