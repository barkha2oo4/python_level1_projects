# 12 am("midnight")-->1 am->2 am->3 am-----------------11am->12am("midnight")
# 00("midnight")->1am----------12am->13am----->00("midnight")
'''07  05   45   PM
  hr  mins sec  meridian'''
hr,mins,sec = input().split(':')
sec,meridian =sec[:2], sec[2:]
if meridian == "PM":
    hr =str(int(hr)+12)
    if hr=='24':
        hr='12'
    print(hr+':'+mins+':'+sec)
else:
   if hr =='12':
    hr = '00'
print(hr+':'+mins+':'+sec)
