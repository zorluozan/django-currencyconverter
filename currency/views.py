from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    if request.method == "POST":
        firstCurrency = request.POST.get("firstCurrency")
        secondCurrency = request.POST.get("secondCurrency")
        amount = request.POST.get("amount")

        api_key = "<your_api_key>"
        url = "http://data.fixer.io/api/latest?access_key=" + api_key
        response = requests.get(url)

        infos = response.json()
        firstValue = infos["rates"][firstCurrency]
        secondValue = infos["rates"][secondCurrency]

        result = (secondValue / firstValue) * float(amount)

        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

    else:
        currencyInfo = {}
        return render(request,"index.html",{"currencyInfo": currencyInfo})

    return render(request,"index.html",{"currencyInfo": currencyInfo})