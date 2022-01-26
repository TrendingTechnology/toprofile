from PIL import Image, ImageCms
import os, sys
from tqdm import tqdm

f = open(os.path.dirname(sys.argv[0]) + "/../paths.txt")
text = f.read().splitlines()
f.close()
if len(text) != 2:
    print("Error: Color profile paths file wrongly formatted. Use 'toprofile -config' to reconfigure.")
    exit()

img_path = sys.argv[1]
disp_prof = os.path.abspath(text[0])
img_prof = os.path.abspath(text[1])
file_types = {
    ".BMP",
    ".DDS",
    ".DIB",
    ".EPS",
    ".GIF",
    ".ICNS",
    ".ICO",
    ".IM",
    ".JPEG",
    ".MJ2",
    ".MJP2",
    ".MSP",
    ".PCX",
    ".PNG",
    ".PPM",
    ".SGI",
    ".SPIDER",
    ".TGA",
    ".TIFF",
    ".WEBP",
    ".XBM"
}

if os.path.isdir(img_path):
    transform_ready = False
    for name in tqdm(os.listdir(img_path)):
        f = os.path.join(img_path, name)
        if os.path.isfile(f) and os.path.splitext(f)[1].upper() in file_types:
            if transform_ready == False:
                transform = ImageCms.buildTransform(disp_prof, img_prof, "RGBA", "RGBA")
                transform_read = True
            img = Image.open(f)
            img = ImageCms.applyTransform(img, transform)
            img.save(f)
        else:
            tqdm.write("Not a compatible image: skipped child item {}".format(f))

elif os.path.isfile(img_path):
    img = Image.open(sys.argv[1])
    transform = ImageCms.buildTransform(disp_prof, img_prof, "RGBA", "RGBA")
    img = ImageCms.applyTransform(img, transform)
    img.save(sys.argv[1])
else:
    print("Error: Invalid path")
