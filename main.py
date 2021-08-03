import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

numMonth = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

if __name__ == '__main__':
    with open('birthdays.json', 'r') as f:
        data = json.load(f)

    months = []

    for name, birthdaystr in data.items():
        month = birthdaystr.split('/')[0]
        months.append(numMonth[month])

    c = Counter(months)

    cat = []
    for id, name  in numMonth.items():
        cat.append(name)
    print(cat)

    monthstocount = []
    count = []
    for key, counter in c.items():
        monthstocount.append(key)
        count.append(counter)

    print(monthstocount)
    print(count)

    output_file("plot.html")
    p = figure(x_range=cat)
    p.vbar(x=monthstocount, top=count, width=0.5)
    show(p)