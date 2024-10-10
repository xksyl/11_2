import requests


r = requests.get('https://api.github.com/events')
data = r.json()


print('Данные JSON:', data)
print("Заголовки:", r.headers)

















