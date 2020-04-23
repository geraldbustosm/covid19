import requests
from ast import literal_eval

# Setup
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
url = 'https://e.infogram.com/d9e30e4b-e63c-4e02-a72a-eca4653f3283'
headers = {'User-agent' : user_agent}

# Make request
res = requests.get(url, headers=headers)
src = res.text

# Get the array like raw string
begin = src.find('[[') + 1
end = src.find(']]') + 2
string_array = src[begin : end]

# Convert string list into array
array = literal_eval(string_array)