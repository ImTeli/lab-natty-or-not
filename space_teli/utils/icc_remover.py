from PIL import Image

image_path = "space_teli\\assets\\images\\milho.png"
image_path2 = "space_teli\\assets\\images\\nave.png"

def delete_iccfile(image_path):
    img = Image.open(image_path)
    img.info.pop('icc_profile', None)
    img.save(image_path)
    
delete_iccfile(image_path)
delete_iccfile(image_path2)
