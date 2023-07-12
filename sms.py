
import logging
import requests


# Set up the URL and message content
base_url = "http://{}/cgi/WebCGI?1500101=account=apiuser&password=apipass&port={}&destination={}&content={}"
ip="172.168.1.210" # ip of the GSM gateway
port=1 # port of the gateway ( depends on gateways vendors )
message = "[MSG]"  # Replace with your actual message or can be used with other Apis to get them
phone_numbers="00213791295922" #Replace with actual phone number or can be used with other Apis to get them


url = base_url.format(ip,port,phone_numbers, message)

# Send the SMS
response = requests.get(url)

    # Check the response status
if response.status_code == 200:
        print(f"SMS sent successfully to {phone_numbers}")
        print("Response code:", response.status_code)
        print(response.content)
        
else:
        print(f"Failed to send SMS to {phone_numbers}")
        print("Response code:", response.status_code)


