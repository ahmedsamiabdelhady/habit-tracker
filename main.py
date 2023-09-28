import requests
from datetime import datetime

USERNAME= "CREATE_YOUR_OWN_USERNAME"
TOKEN= "CREATE_YOUR_OWN_TOKEN"
GRAPHID= "CREATE_YOUR_OWN_ID"

pixela_endpoint= "https://pixe.la/v1/users"
pixela_params= {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response= requests.post(pixela_endpoint, json=pixela_params)
# print(response.text)

graph_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs"
header= {
    "X-USER-TOKEN": TOKEN
}

body= {
    "id": f"{GRAPHID}",
    "name": "TITLE_OF_GRAPH",
    "unit": "EX, KILOMETER, COMMIT, CALORY",
    "type": "INT OR FLOAT ONLY",
    "color": "ADD COLOR OF PIXELS: 'shibafu' (green), 'momiji' (red), 'sora' (blue), 'ichou' (yellow), 'ajisai' (purple) and 'kuro' (black)"
}

# response= requests.post(url=graph_endpoint, json=body, headers=header)
# print(response.text)

today= datetime.now()
today_formatted= today.strftime("%Y%m%d")

#HOW TO ADD PIXELS
add_pixel_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

body= {
    "date": today_formatted,
    "quantity": "3"
}

# response= requests.post(url=add_pixel_endpoint, json= body, headers= header)
# print(response.text)


#HOW TO UPDATE THE PIXELS
update_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today_formatted}"

body={
    "quantity": "10"
}

# response= requests.put(url= update_endpoint, json= body, headers= header)
# print(response.text)

#HOW TO DELETE THE PIXELS

delete_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today_formatted}"

# response= requests.delete(url= delete_endpoint, headers= header)
# print(response.text)