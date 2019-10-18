# this will download parking location at city level from git repository URL as geojson 

import urllib2

print('Beginning file download with urllib2...')


data_url = urllib2.urlopen('https://apps.dresden.de/ords/f?p=1110') # input of city name should get access to dat

datatowrite = data_url.read() # reading form url

#save in a workspace directory

with open('/Users/user/Downloads/', 'wb') as f:
    f.write(datatowrite)
