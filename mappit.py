import json
from geolocate_callsigns import geolocate_callsigns
from map_callsigns import create_folium_map

def generate_ham_radio_map(callsigns, origin, config_file, output_file='map.html'):
    # Geolocate the call signs
    locations = geolocate_callsigns(callsigns, config_file)
    
    # Check if any locations were found
    if not locations:
        print("No locations found for the provided call signs.")
        return
    
    # Create the map with the geolocated call signs and origin
    create_folium_map(locations, origin, output_file)
    print(f"Ham radio map created and saved to {output_file}")

# Example usage
callsigns = ['WA3MH','K3MLH','EA4T','W4KD','K2XE','K9NN','K4RGN','WD4OOZ','EA5ST','KL5NS','K4VHE','AD9AR']
origin = {'name': 'US-8375', 'lat': 27.9824 , 'lon': -80.7549}
config_file = 'config.json'
output_file = 'ham_radio_map.html'

generate_ham_radio_map(callsigns, origin, config_file, output_file)
