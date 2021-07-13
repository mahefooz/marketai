from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def banknifty(request):
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY"
    headers = {
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41"
    }
    r = requests.Session()
    res = r.get(url, headers=headers)

    if res.status_code != 200:
        return HttpResponse(status=res.status_code)
    else:
        return HttpResponse(res.content)

def nifty(request):
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    headers = {
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41"
    }
    r = requests.Session()
    res = r.get(url, headers=headers)

    if res.status_code != 200:
        return HttpResponse(status=res.status_code)
    else:
        return HttpResponse(res.content)

def stock(request, name):
    url = "https://www.nseindia.com/api/option-chain-equities?symbol=" + name
    headers = {
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41"
    }
    r = requests.Session()
    res = r.get(url, headers=headers)

    if res.status_code != 200:
        return HttpResponse(status=res.status_code)
    else:
        return HttpResponse(res.content)