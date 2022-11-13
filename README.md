# Panel-Power-Action
mass stopping and starting of servers hosted on panel

main.py <== script file that need to run

config.py <== configuration of server addresses

Prerequisite
------------

BARER TOKEN

# insert api token generated from panel USER account API ( Important: not application API token )
barer_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' <== replace with actual token

Click on panel username ( for Ptero Panel )

![image](https://user-images.githubusercontent.com/98382155/201522294-7fee57b0-70e4-4295-a828-bcfc5a734f76.png)

Go to Api Credentials

![image](https://user-images.githubusercontent.com/98382155/201522320-daee99e6-c767-47e7-9497-d403ce51d36a.png)

Create new API key and leave IP blank.
Copy API Key and insert into barer_token field in config.py
KEY must be admin's KEY

..........................................................................................

For server List in config.py


The last part of url is server identifier
make sure to follow the format when adding servers. Esp , the comma at the end. The last server doesn't require comma , <== important

![image](https://user-images.githubusercontent.com/98382155/201522464-86da2dc2-f5ba-4dc3-9d31-dc8c37236fb0.png)

    
Run with this command in server console "python main.py" or "python3 main.py"

