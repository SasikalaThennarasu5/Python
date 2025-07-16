monday = {"#fun", "#code"}
tuesday = {"#code", "#python"}
wednesday = {"#fun", "#ai"}

weekly = set()
weekly.update(monday, tuesday, wednesday)
unique = monday ^ tuesday ^ wednesday

print("Weekly trending:", weekly)
print("Unique daily hashtags:", unique)