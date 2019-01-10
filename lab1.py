import requests
print(requests.__version__)
#r = requests.get("http://google.com")
#print(r.status_code)
#print(r.text)
#print(dir(r))

r = requests.get("https://raw.githubusercontent.com/zhangyi921/cmput404_lab1/master/lab1.py")
print(r.text)