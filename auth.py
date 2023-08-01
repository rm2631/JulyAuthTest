CLIENT_ID = "<>" # Replace with your client ID
CLIENT_SECRET = "<>" # Replace with your client secret
TENANT_ID = "<>" # Replace with your tenant ID

import requests
import jwt
from azure.identity import InteractiveBrowserCredential

def get_valid_token():
    # Replace these variables with your actual values
    token_endpoint = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"  # Replace YOUR_TENANT_ID

    # Token request parameters
    token_data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "https://graph.microsoft.com/.default",  # Replace with the required scope
    }

    # Make a POST request to the token endpoint to obtain the token
    response = requests.post(token_endpoint, data=token_data)
    token_json = response.json()
    return token_json["access_token"]

def validate_token(token):   
    # Verify the token using the tenant's issuer URL and audience (your client ID)
    decoded_token = jwt.decode(
        token,
        options={"verify_signature": False},
        issuer=f"https://login.microsoftonline.com/{TENANT_ID}/v2.0",
        audience=CLIENT_ID,
    )
    
    print(decoded_token.get('app_displayname'))
    return decoded_token.get('appid') == CLIENT_ID
    
if __name__ == "__main__":
    token = get_valid_token()
    print("Valid token is valid: " + str(validate_token(token)))