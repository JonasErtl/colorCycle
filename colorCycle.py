#imports
from time import sleep
import requests
import random 

#Home Assistant IP and Token
ha_url = "http://192.168.178.34:8123"
ha_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxNjdmYWQ3OTI5NTc0OTM0YWE2NTNiZTUxYWMwODVkNyIsImlhdCI6MTcwNzk1MTQ3NywiZXhwIjoyMDIzMzExNDc3fQ.nuIv6LYvRLFegm1kfvSIbJwxyzi9aLa_ILq-eONxKYg"
start_color = (255,255,255) #starting color 

while True:
    #A function to generate random colors 
    def ColorGen():
        colors = random.sample(range(0,255), 3)
        return colors


    headers = {
        "Authorization": f"Bearer {ha_token}",
        "content-type": "application/json",
        }

        # Homeassistent entity id of the desired light
    entity_id = "light.mobilt_ljus_light"

    
    end_color = ColorGen()

    #fade function
        
    def FadeColor(start_color, end_color, transition_time=10):
        """
        Fades the color from `start_color` to `end_color` over `transition_time` seconds.

        Args:
            start_color: The starting color tuple (R, G, B).
            end_color: The ending color tuple (R, G, B).
            transition_time: The duration of the transition in seconds.
        """

        step_size = transition_time / 10  # Adjust step size for desired smoothness
        for _ in range(10):
            new_color = tuple(int(start_color[i] + (end_color[i] - start_color[i]) * (_ / 10)) for i in range(3))
            # Apply the new color to your smart home light here
            print(type(new_color))
            data = {
            "entity_id": entity_id,
            "rgb_color": [new_color[0], new_color[1], new_color[2]],  # RGB values 
            "transition":  0,  # Transition time in seconds
            }

            response = requests.post(f"{ha_url}/api/services/light/turn_on", headers=headers, json=data)

            if response.status_code ==  200:
                print("Light turned on successfully.")
            else:
                print("Failed to turn on light.")

            print(new_color)
            sleep(step_size)
    FadeColor(start_color=start_color, end_color=end_color)
    start_color=end_color
    print(start_color)


