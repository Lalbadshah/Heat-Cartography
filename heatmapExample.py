import heatmap

def heatmapper(points):
    print "Processing %d points..." % len(points)
    print(points)
    hm = heatmap.Heatmap()
    img = hm.heatmap(points).save("classic.png")
