import requests
import json
import xmltodict

def load_api_key(config_file):
    with open(config_file, 'r') as file:
        api_key = json.load(file)
    return api_key

def geolocate_callsigns(callsigns, config_file):
    api_key = load_api_key(config_file)
    base_url = "https://xmldata.qrz.com/xml/current/?"
    
    # Get session key
    try:
        session_response = requests.get(f"{base_url}username={api_key['username']};password={api_key['password']}")
        session_response.raise_for_status()
        
        # Parse XML response
        session_data = xmltodict.parse(session_response.content)
        session_key = session_data['QRZDatabase']['Session']['Key']
    except requests.exceptions.RequestException as e:
        print(f"Error obtaining session key: {e}")
        return []
    except KeyError:
        print("Invalid session response. Check your API credentials.")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

    results = []
    for callsign in callsigns:
        try:
            response = requests.get(f"{base_url}s={session_key};callsign={callsign}")
            response.raise_for_status()
            
            # Parse XML response
            data = xmltodict.parse(response.content)
            
            if 'Callsign' in data['QRZDatabase']:
                location = {
                    'callsign': callsign,
                    'lat': data['QRZDatabase']['Callsign']['lat'],
                    'lon': data['QRZDatabase']['Callsign']['lon'],
                    'grid': data['QRZDatabase']['Callsign']['grid']
                }
                results.append(location)
            else:
                print(f"Call sign {callsign} not found.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for call sign {callsign}: {e}")
        except KeyError:
            print(f"Invalid response format for call sign {callsign}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    return results

# Example usage
config_file = 'config.json'
callsigns = ['WA3MH','K3MLH','EA4T','W4KD','K2XE','K9NN','K4RGN','WD4OOZ','EA5ST','KL5NS','K4VHE','AD9AR']
locations = geolocate_callsigns(callsigns, config_file)
print(locations)
