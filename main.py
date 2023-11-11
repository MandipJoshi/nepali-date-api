from fastapi import FastAPI
import datetime
import nepali_datetime
import pytz

app = FastAPI()

month_map={
    "01": "वैशाख",
    "02": "जेठ",
    "03": "असार",
    "04": "साउन",
    "05": "भदौ",
    "06": "असोज",
    "07": "कार्तिक",
    "08": "मंसिर",
    "09": "पुष",
    "10": "माघ",
    "11": "फागुन",
    "12": "चैत"
}

number_map={
    "0": "०",
    "1": "१",
    "2": "२",
    "3": "३",
    "4": "४",
    "5": "५",
    "6": "६",
    "7": "७",
    "8": "८",
    "9": "९"
}

weekday_map={
    "6": "आइतवार",
    "0": "सोमवार",
    "1": "मङ्गलवार",
    "2": "बुधवार",
    "3": "बिहिवार",
    "4": "शुक्रवार",
    "5": "शनिवार"
}

def get_nepali_date():
    today_date=str(nepali_datetime.date.today())
    date=today_date.split("-")
    
    temp_date_year="" #Declear to concatinate
    for x in list(date[0]):
        temp_date_year+=number_map[x]

    date[0]=temp_date_year

    temp_date="" #Declear to concatinate
    for x in list(date[2]):
        temp_date+=number_map[x]

    date[2]=temp_date
    
    return f"{date[0]} {month_map[date[1]]} {date[2]}"

def get_weekday():
    weekday=str(datetime.datetime.now().weekday())
    return weekday_map[weekday]

@app.get("/date")
def nepali_date():
    return get_nepali_date()

@app.get("/which_day")
def which_day():
    return get_weekday() 
