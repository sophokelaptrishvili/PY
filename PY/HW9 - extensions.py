

#input
fileName = input("write your file name:").lower()

#.gif
if ".gif" in fileName:
    print("image/gif")

# .jpg # .jpeg
elif ".jpeg" in fileName:
    print("image/jpeg")
elif ".jpg" in fileName:
    print("image/jpeg")

# .png
elif ".png" in fileName:
    print("image/png")
# .pdf
elif ".pdf" in fileName:
    print("application/pdf")
# .txt
elif ".txt" in fileName:
    print("text/plain")
# .zip
elif ".zip" in fileName:
    print("application/zip")

else:
    print("application/octet-stream")
