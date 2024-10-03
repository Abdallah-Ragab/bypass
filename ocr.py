import easyocr

reader = easyocr.Reader(['en'], gpu = True)

def read_image(image_path):
    text_list = reader.readtext(image_path, detail=0)
    text = "\n".join(text_list)
    return text

def save_to_txt(text, path):
    with open(path, 'w') as f:
        f.write(text)

