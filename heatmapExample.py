import heatmap

def heatmapper(UltraList):
    print ("Processing points...")
    print(UltraList)
    hm = heatmap.Heatmap()
    img = hm.heatmap(UltraList).save("classic.png")
    print (UltraList)
