import csv

def getColour(grp, step):
    if grp == 'A':
        #red 197, 30, 58
        colour = '#{:02x}{:02x}{:02x}'.format(197-20*step if 197-20*step >= 0 else 0, 30-20*step if 30-20*step >= 0 else 0, 58-20*step if 58-20*step >= 0 else 0)
    elif grp == 'B':
        #orange 255, 79, 0
        colour = '#{:02x}{:02x}{:02x}'.format(255-20*step if 255-20*step >= 0 else 0, 79-20*step if 79-20*step >= 0 else 0, 0-20*step if 0-20*step >= 0 else 0)
    elif grp == 'C':
        #yellow 255, 191, 0
        colour = '#{:02x}{:02x}{:02x}'.format(255-20*step if 255-20*step >= 0 else 0, 191-20*step if 191-20*step >= 0 else 0, 0-20*step if 0-20*step >= 0 else 0)
    elif grp == 'D':
        #green 86, 130, 3
        colour = '#{:02x}{:02x}{:02x}'.format(86-20*step if 86-20*step >= 0 else 0, 130-20*step if 130-20*step >= 0 else 0, 3-20*step if 3-20*step >= 0 else 0)
    elif grp == 'E':
        #blue 49, 140, 231
        colour = '#{:02x}{:02x}{:02x}'.format(49-20*step if 49-20*step >= 0 else 0, 140-20*step if 140-20*step >= 0 else 0, 231-20*step if 231-20*step >= 0 else 0)
    elif grp == 'F':
        #purple 138, 43, 226
        colour = '#{:02x}{:02x}{:02x}'.format(138-20*step if 138-20*step >= 0 else 0, 43-20*step if 43-20*step >= 0 else 0, 226-20*step if 226-20*step >= 0 else 0)
    elif grp == 'G':
        #pink 255, 145, 175
        colour = '#{:02x}{:02x}{:02x}'.format(255-20*step if 255-20*step >= 0 else 0, 145-20*step if 145-20*step >= 0 else 0, 175-20*step if 175-20*step >= 0 else 0)
    else: #'H'
        #grey 128, 128, 128
        colour = '#{:02x}{:02x}{:02x}'.format(128-20*step if 128-20*step >= 0 else 0, 128-20*step if 128-20*step >= 0 else 0, 128-20*step if 128-20*step >= 0 else 0)

    return colour


res = open("thesis-radar-chart/static/res.txt", "w")
res.write("export const data = {\n")

with open("thesis-radar-chart/static/radarcharts.csv", newline='') as radarcharts:
    data = list(csv.reader(radarcharts))
    
    # Get headers
    res.write("labels: [\n")
    for header in data[0][3:]:
        res.write("'"+header+"',\n")
    res.write("],\n")

    prev = ''
    step = 0
    res.write("datasets: [")
    for row in data[1:]:
        res.write("{\n")

        # label
        res.write("label: '"+str(row[2])+"',\n")

        # data
        res.write("data: "+str(row[3:])+",\n")

        # colour
        res.write("fill: true,\n")
        colour = getColour(row[0], step)
        res.write("backgroundColor: '"+colour+"20',\n")
        res.write("borderColor: '"+colour+"',\n")
        res.write("pointBackgroundColor: '"+colour+"',\n")
        res.write("pointBorderColor: '#FFF',\n")
        res.write("pointHoverBackgroundColor: '#FFF',\n")
        res.write("pointHoverBorderColor: '"+colour+"',\n")
        if prev != row[0]:
            prev = row[0]
            step = 0
        else:
            step += 1

        res.write("}, ")

    res.write("]\n")
    res.write("}\n")

res.close()