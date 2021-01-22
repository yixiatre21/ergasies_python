import urllib.request
import json
import datetime

def getUrl():
    for day in range(1, thisDay + 1):
        if day < 10:
            url = "https://api.opap.gr/draws/v3.0/1100/draw-date/" + thisMonth + "-0" + str(day) + "/" + thisMonth + "-0" + str(day)
        else:
            url = "https://api.opap.gr/draws/v3.0/1100/draw-date/" + thisMonth + "-" + str(day) + "/" + thisMonth + "-" + str(day)

        FinederFrequentNumber(url, day)


def FinederFrequentNumber(url, day):
    counter = []
    for i in range(81):
        counter.append(0)

    r = urllib.request.urlopen(url)
    html = r.read()
    html = html.decode()
    data = json.loads(html, strict=False)

    for draw in data["content"]:
        t = draw["winningNumbers"]["list"]
        for indice in t:
            counter[indice] += 1
    
    max = counter[0]
    maxNum = 0

    for num in range(81):
        if max < counter[num]:
            max = counter[num]
            maxNum = num

    print("The most frequent number(s) of %s-%s is(are):" % (thisMonth, day), end=" ")

    for num in range(maxNum, 81):
        if counter[num] == max:
            print("%s" % (num), end=' ')

    print("\n")


thisMonth = datetime.date.today().strftime("%Y-%m")

thisDay = datetime.date.today().day

getUrl()