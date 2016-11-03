import heatmap
from PIL import Image

def heatmapper(UltraList,num):
    print ("Processing points...")
    print(UltraList)
    hm = heatmap.Heatmap()
    print("heatmapper loaded")
    img = hm.heatmap(UltraList)
    print("heatmap created")
    overlay = img
    background = Image.open('bk.jpg')

    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")


    Image.blend(background, overlay,0.4).save("result"+ str(num) +".png","PNG")
    print("overlay comepleted")
    print (UltraList)
