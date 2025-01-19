import folium

def create_folium_map(locations, origin=None, output_file='map.html'):
    # Determine map center
    if origin:
        m = folium.Map(location=[origin['lat'], origin['lon']], zoom_start=5)
    else:
        avg_lat = sum(loc['lat'] for loc in locations) / len(locations)
        avg_lon = sum(loc['lon'] for loc in locations) / len(locations)
        m = folium.Map(location=[avg_lat, avg_lon], zoom_start=5)
    
    # Add origin marker if provided
    if origin:
        folium.Marker(
            location=[origin['lat'], origin['lon']],
            popup=f"Origin: {origin['name']}",
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
    
    # Add markers for each location
    for loc in locations:
        folium.Marker(
            location=[loc['lat'], loc['lon']],
            popup=f"{loc['callsign']} ({loc['grid']})",
            tooltip=loc['callsign']
        ).add_to(m)
    
    # Save the map to an HTML file
    m.save(output_file)
    print(f"Map has been saved to {output_file}")

if __name__ == "__main__":
    # Example usage
    locations = [
    {'callsign': 'K1ABC', 'lat': 45.0, 'lon': -93.0, 'grid': 'EN34'},
    {'callsign': 'N1XYZ', 'lat': 42.0, 'lon': -88.0, 'grid': 'EN62'},
    {'callsign': 'W1ZZZ', 'lat': 40.0, 'lon': -75.0, 'grid': 'FN20'}
    ]

    origin = {'name': 'Saint Joseph', 'lat': 44.0, 'lon': -92.5}

    create_folium_map(locations, origin)
