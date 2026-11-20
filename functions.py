import json


def loadproducts():
    file = open("products.json", "r", encoding="utf-8")
    products = json.load(file)
    file.close()
    return products


def showproducts():
    products = loadproducts()
    for p in products:
        print(p["id"],  p["name"],  p["price"], "m")


def sortbypriceasc():
    products = loadproducts()
    sortedproducts = sorted(products, key=lambda p: p["price"])
    for p in sortedproducts:
        print(p["id"], "-", p["name"], "-", p["price"], "m")


def sortbypricedesc():
    products = loadproducts()
    sortedproducts = sorted(products, key=lambda p: p["price"], reverse=True)
    for p in sortedproducts:
        print(p["id"], "-", p["name"], "-", p["price"], "m")

def searchbyname():
    products = loadproducts()
    name = input("Mehsulun adi:").lower()
    found = False
    for p in products:
        if name in p["name"].lower():
            print(p["id"], "-", p["name"], "-", p["price"], "m")
            found = True
    if found == False:
        print("Mehsul tapilmadi")


def searchbyid():
    products = loadproducts()
    try:
        id = int(input("Mehsul ID: "))
    except ValueError:
        print("ID yalniz reqem")
        return
    for p in products:
        if p["id"] == id:
            print(p["id"], "-", p["name"], "-", p["price"], "m")
            return
    print("mehsul tapimadi")


def getcheapestproduct():
    products = loadproducts()
    cheapest = products[0]
    for p in products:
        if p["price"] < cheapest["price"]:
            cheapest = p
    print("ucuz məhsul")
    print(cheapest["id"], "-", cheapest["name"], "-", cheapest["price"], "m")


def getexpensiveproduct():
    products = loadproducts()
    expensive = products[0]
    for p in products:
        if p["price"] > expensive["price"]:
            expensive = p
    print("bahali mehsul")
    print(expensive["id"], "-", expensive["name"], "-", expensive["price"], "m")