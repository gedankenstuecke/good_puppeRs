import os
import urllib

for i in ["pictures","pictures/doggo_less8","pictures/doggo_8","pictures/doggo_9","pictures/doggo_10","pictures/doggo_11","pictures/doggo_12","pictures/doggo_13","pictures/doggo_14"]:
    if not os.path.exists(i):
        os.makedirs(i)

for i,line in enumerate(open("dog_ratings.csv")):
    if i > 0:
        lline = line.replace("\n","").split("\t")
        if lline[-1] != "":
            if lline[-1].find("video") == -1:
                try:
                    rating = int(lline[1])
                    print rating
                    if rating < 9:
                        urllib.urlretrieve(lline[-1],"pictures/doggo_less8/"+lline[-1].split("/")[-1])
                    elif rating > 13:
                        next
                    else:
                        urllib.urlretrieve(lline[-1],"pictures/doggo_"+str(rating)+"/"+lline[-1].split("/")[-1])
                except:
                    pass
