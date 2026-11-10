import json
import numpy as np
import os

with open('camData.json', 'r') as file:
    camData = json.load(file)['camData']

with open('contourData.json', 'r') as file:
    contourData = json.load(file)['contoursPts']

outputFolder = '3dTo2d'
Info = {}

for data in camData:
    name = data['name']

    # New name: create an empty record for it
    if name not in Info:
        Info[name] = {
            'count': 0,
            'azimuth': [],
            'elevation': [],
            'contourPoints': []
        }

    # Save this shape's data under its name
    Info[name]['count'] += 1
    Info[name]['azimuth'].append(data['azimuth'])
    Info[name]['elevation'].append(data['elevation'])
    Info[name]['contourPoints'].append(contourData[data['index']])
for name in Info:
    minAz=min(Info[name]['azimuth'])
    maxAz=max(Info[name]['azimuth'])
    minElv=min(Info[name]['elevation'])
    maxElv=max(Info[name]['elevation'])
    del Info[name]['elevation']
    del Info[name]['azimuth']
    Info[name]['Elevation_Range']=f'{minElv}-{maxElv}'
    Info[name]['Azimuth_Range']= f'{minAz}-{maxAz}'
    

# Check the result
for name in Info:  
    filename= f'contours_{name}.json'
    with open(filePath, 'w') as file:
        json.dump(Info[name], file)

    filePath=os.path.join(outputFolder,filename)
    
    
