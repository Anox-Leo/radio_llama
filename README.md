# 🦙 Radio Llama

Radio Llama is an application that generates personalized audio content using generative AI. From AI-generated radio with your playlists to interactive storytelling, Radio Llama offers a unique and dynamic listening experience. This project was developed during the Shift - Generative AI hackathon
 
## 📸 Preview

### Landing page

![Landing page](https://github.com/Anox-Leo/radio_llama/blob/main/images/landing_page.png)

### Radio generation page

![Radio genereation page](https://github.com/Anox-Leo/radio_llama/blob/main/images/radio_generation_page.png)

## How to locally test

- Go to the folder `llamapy/utils_romain` and copy the `.env.dist` file to `.env`

- Get the required API key from Eleven Labs, Mistral and Spotify and fill the `.env` file with the correct values

- Install the dependencies with `pip install -r requirements.txt`

- Open the file `radio.py` and change the 'genre' variable at the start of the file to the genre you want to test

- Run the script with `python3 radio.py`
