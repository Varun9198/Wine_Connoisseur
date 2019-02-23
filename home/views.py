from django.shortcuts import render
from .models import *
# import pandas as pd
import csv
# count = 0



def mk_float(s):
    s = s.strip()
    return float(s) if s else 0

def read():
    Wine.objects.all().delete()
    with open(r'C:\Users\dell\Desktop\WineConnoisseur\home\wines_data.csv', mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        id = 0
        for row in csv_reader:
            line_count += 1
            
            # if line_count != 0:
            if True:
                # if id == 10:
                    # break
                # x = None
                # if row['price'] == None:
                #     x = 'lolwa'
                # else:
                #     x = row['price']
                x = int(mk_float(row['price']))
                y = int(mk_float(row['points']))

                w = Wine(ID = id,
                        COUNTRY=row['country'] if row['country'] != None else ' ',
                        DESCRIPTION=row['description'] if row['description'] != None else ' ',
                        DESIGNATION=row['designation'] if row['designation'] != None else ' ',
                        POINTS=y,
                        PRICE=x,
                        PROVINCE=row['province'] if row['province'] != None else ' ',
                        REGION_1=row['region_1'] if row['region_1'] != None else ' ',
                        REGION_2=row['region_2'] if row['region_2'] != None else ' ',
                        VARIETY=row['variety'] if row['variety'] != None else ' ',
                        WINERY=row['winery'] if row['winery'] != None else ' ')
                w.save()
                id += 1

# Create your views here.
def index(request):
    # read()
    wines = Wine.objects.all()
    return render(request, 'show_data.html', {'wines' : wines})

def sorted_data(request):
    wines = Wine.objects.order_by('PRICE')
    return render(request, 'show_data.html', {'wines' : wines})

def filter(request):
    country = request.POST.get('country')
    province = request.POST.get('post')
    # region_1 = request.POST.get('region_1')
    # region_2 = request.POST.get('region_2')
    wines = None
    if country != None:
        if province != None:
            wines = Wine.objects.filter(COUNTRY=country, PROVINCE=province)
        else:
            wines = Wine.objects.filter(COUNTRY=country)
    else:
        if province != None:
            wines = Wine.objects.filter(PROVINCE=province)
        else:
            wines = Wine.objects.all()

    # if country != None:
    #     wines = wines.objects.filter(COUNTRY=country)
    # if province != None:
    #     wines = wines.objects.filter(PROVINCE=province)
    # print(wines != None)
    return render(request, 'show_data.html', {'wines' : wines})
