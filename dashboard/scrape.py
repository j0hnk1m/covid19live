import requests
from .models import Country, Date
from datetime import datetime
from django.utils import timezone
from tqdm import tqdm
import pytz
from django.db.models import Q


def update_country(name_, code_, confirmed_, recovered_, deaths_, date_):
    try:
        c = Country.objects.get(name=name_, code=code_)
        c.confirmed = confirmed_
        c.recovered = recovered_
        c.deaths = deaths_
        c.last_updated = date_
        c.save(update_fields=['confirmed', 'recovered', 'deaths', 'last_updated'])
        return c
    except:
        if confirmed_ == 0:
            mortality_ = 0
        else:
            mortality_ = deaths_ / confirmed_
        
        return Country.objects.create(
            name=name_, 
            code=code_,
            confirmed=confirmed_,
            recovered=recovered_,
            deaths=deaths_,
            mortality=mortality_*100,
            last_updated=datetime.now().date()
        )


def update_dates(data, c):
    for i in data:
        date_ = datetime.strptime(i['Date'], '%Y-%m-%dT%H:%M:%SZ').date()
        try:
            Date.objects.get(date=date_, country=c)
            return
        except:
            Date.objects.create(
                date=date_,
                country=c,
                confirmed=i['Confirmed'],
                recovered=i['Recovered'],
                deaths=i['Deaths']
            )


def get_global():
    try:
        return Country.objects.get(name='Global')
    except:
        return


def get_countries():               
    return Country.objects.all()


def get_dates():
    return Date.objects.all()


def fetch_api_data():
    data = requests.get('https://api.covid19api.com/summary').json()

    # Global stats
    update_country(
        'Global', 
        '  ', 
        data['Global']['TotalConfirmed'], 
        data['Global']['TotalRecovered'], 
        data['Global']['TotalDeaths'], 
        datetime.strptime(data['Date'], '%Y-%m-%dT%H:%M:%SZ').date()
    )

    # Countries stats
    for i in data['Countries']:
        update_country(
            i['Country'], 
            i['CountryCode'], 
            i['TotalConfirmed'], 
            i['TotalRecovered'], 
            i['TotalDeaths'], 
            datetime.strptime(i['Date'], '%Y-%m-%dT%H:%M:%SZ').date()
        )
    
    print("*****************UPDATED DATABASE (COUNTRY)*****************")


def update_time_data():
    countries = requests.get('https://api.covid19api.com/countries').json()

    for country in tqdm(countries):    
        data = requests.get(f"https://api.covid19api.com/total/country/{country['Slug']}").json()
        if len(data) > 0:
            c = update_country(
                country['Country'], 
                country['ISO2'], 
                data[-1]['Confirmed'], 
                data[-1]['Recovered'], 
                data[-1]['Deaths'],
                datetime.strptime(data[-1]['Date'], '%Y-%m-%dT%H:%M:%SZ').date()
            )
            update_dates(data[:-1], c)
        
    print("*****************UPDATED DATABASE (TIME)*****************")

