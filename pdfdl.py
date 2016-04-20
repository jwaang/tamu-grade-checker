# Downloads PDFs from TAMU directory
# Convert PDFs into TXT with Zamzar
import requests

YEARS = ['2010', '2011', '2012', '2013', '2014', '2015', '2016']
SEASON = ['1', '2', '3']
SCHOOL = ['EN', 'BA']

for y in YEARS:
    for s in SEASON:
        for sch in SCHOOL:
            url = "http://web-as.tamu.edu/gradereport/PDFReports/"+y+s+"/grd"+y+s+sch+".pdf"
            name = "grd"+y+s+sch+".pdf"
            r = requests.get(url)
            with open(name, "wb") as code:
                code.write(r.content)