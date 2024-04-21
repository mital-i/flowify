## flowify

# Inspiration
From our experience, it is difficult to curate a playlist for an event or a gathering on the spot. For example, if we are going to the beach or a party, we would rather spend time enjoying the event than developing the perfect playlist. Additionally, we want to discover new music that fits the surrounding atmosphere. We realized that it would be better for AI to make these decisions as it already has a lot of knowledge on human behavior and preferences, thus making it the perfect thing to put to this task. Lastly, we wanted a name that would emphasize our desire to encourage our users to live in the moment (i.e. touch grass) and go with the flow rather than sweat the small things: Flowify, let the music take you outside.

# What it does
Navigating to our website, users log into their spotify account and are prompted to authenticate our account so flowify can make playlists through their account. Next, they are prompted to upload a picture of something near them, like a beach, or a nightclub, a birthday party, etc. The Gemini API suggests songs based on the parameters of the image. The Spotify API creates a playlist on the user’s account from the suggested songs, ready to play in app or on Spotify.

# How we built it
For our frontend we used the Python library called frontend, and for backend we used Fast API. Additionally, we used the Spotify API to create custom playlists for a given user (each user has to authenticate their Spotify account before being able to use the generator) and the Gemini API to find songs that match the vibe of the image that's parsed in.

# Challenges we ran into
Initially when we tried to activate authentication of Spotify accounts, the access token for the authentication request was missing. We spent a long time debugging to realize that the access code was set to None which was exchanged for the token and that's why we didn’t have an access token. To fix this we added a check to ensure the access code was not set to None. We also ran into issues with using a virtual environment. We temporarily solved the problem by pair programming but eventually changed to using default environments.

# What's next for flowify
In the future we want to continue improving the app and adding more features. We would like to add a way for users to take a picture on the app instead of having to upload a file every time as that may be inconvenient. Additionally, we want to make it possible for users to add multiple images to make an assorted playlist. We would like to add a way for users to add collaborators who can also upload images to the playlist. Last but not least we would like to be able to create a playback option on the mobile app.

# Built With
gemini
python
spotify
# Try it out
