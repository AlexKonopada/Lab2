import twitter2
import json
import pandas as pd
from geopy.geocoders import Nominatim
import folium

data = twitter2.data_from_twitter2()
with open('friends.json', 'w') as f:
    json.dump(data, f, indent=2)

def getting_friends_locations(data):
    '''
    return dictionary with friends of twitter user and info about their location 
    '''
    d = {}
    for friend in data['users']:
        d[friend['screen_name']] = friend['location']
    return d
def to_pandas(info):
    '''
    return converted pandas dataframe of dictionary
    '''
    friends = pd.DataFrame(info.items(), columns=['Friends', 'Location'])
    return friends

def latitude_longitude(country):
    '''
    return tuple of latitude and longitude by given location
    '''
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(country)
    if location:
        lat = location.latitude
        lon = location.longitude
    else:
        lat = 0
        lon = 0 
    return lat, lon

def adding_coordinates(dataframe):
    '''
    return the dataframe with added coordinates of every location in previous data frame
    '''
    df = dataframe
    df['latitude_longitude'] = df.apply(lambda x: latitude_longitude(x['Location']), axis = 1)     
    df.drop(df.index[df['latitude_longitude'] == (0, 0)], inplace = True)       
    df[['latitude', 'longitude']] = pd.DataFrame(df['latitude_longitude'].tolist(), index=df.index)
    df.drop('latitude_longitude', axis='columns', inplace=True)
    return df
def creating_map(dataframe):
    '''
    return created map(html) with given dataframe
    '''
    df = dataframe
    lat = df['latitude']
    lon = df['longitude']
    friends = df['Friends']
    map = folium.Map()
    fg = folium.FeatureGroup(name='Films')
    for lt, ln, f in zip(lat, lon, friends):
        fg.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=f))
    map.add_child(fg)
    map.save('tavarischi.html')
    return df
info = getting_friends_locations(data)
final_data = adding_coordinates(to_pandas(info))
print(creating_map(final_data))






# print(getting_friends_locations(data))