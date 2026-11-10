import json
import os

with open('camData.json', 'r') as file:
    camData = json.load(file)['camData']

with open('contourData.json', 'r') as file:
    contourData = json.load(file)['contoursPts']

outputFolder = '3dTo2d'
os.makedirs(outputFolder, exist_ok=True)
Info = {}

for data in camData:
    name = data['name']

   
    if name not in Info:
        Info[name] = {
            'count': 0,
            'azimuth': [],
            'elevation': [],
            'contourPoints': []
        }

    
    Info[name]['count'] += 1
    Info[name]['azimuth'].append(data['azimuth'])
    Info[name]['elevation'].append(data['elevation'])
    Info[name]['contourPoints'].append(contourData[data['index']])
    

for name, i in Info.items(): 
    result={
        'name': name,
        'azimuthRange' : [round(min(i['azimuth']),2), round(max(i['azimuth']),2)],
        'elevationRange': [round(min(i['elevation']),2),round(max(i['elevation']),2)],
        'numOfContours': len(i['contourPoints']),
        'contours': i['contourPoints']
    } 
    filename= f'contours_{name}.json'

    filePath=os.path.join(outputFolder,filename)
    with open(filePath, 'w') as file:
        json.dump(result, file,indent=2)

    filePath=os.path.join(outputFolder,filename)
    
    
