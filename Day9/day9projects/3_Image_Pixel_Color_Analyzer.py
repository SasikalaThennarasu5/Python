# Project 3: Image Pixel Color Analyzer
pixels = [
    (255, 255, 255), (0, 0, 0), (255, 0, 0), (255, 0, 0),
    (0, 255, 0), (0, 0, 255), (255, 0, 0)
]

target_color = (255, 0, 0)
print("Target color count:", pixels.count(target_color))

subregion = pixels[2:6]
print("Subregion:", subregion)