import requests
import json
import datetime

# Get time to fetch current csv
date = datetime.datetime.now()

res = requests.get('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto4/' + date.strftime("%Y-%m-%d") + '-CasosConfirmados-totalRegional.csv')
csv = res.text

# Initial variables
text = ""
data = []
subdata = []
i = 0

# Convert csv into array
while(i < len(csv)):
    if(i < len(csv) - 1 and csv[i] == ' ' and csv[i+1] == ' '):
        i = i + 1
    if(csv[i] != ',' and csv[i] != '\n' and csv[i] != '\r'):
        text = text + csv[i]
    if(csv[i] == ',' or csv[i] == '\n' or i == len(csv)-1):
        subdata.append(text)
        text = ""
    if(csv[i] == '\n' or i == len(csv)-1):
        data.append(subdata.copy())
        subdata.clear()
    i = i + 1

#Convert list into json
json = json.dumps(data)

# Make POST request to the API
res = requests.post('http://domain.com/api.php', data=json, headers={'PASSWORD' :'YOURPASSWORD'})

print(res.status_code)