import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"
SPOTIFY_CLIENT_ID = "cc2e23f16916454db2b6763b6bb64b42"
SPOTIFY_CLIENT_SECRET = "6048ca3e35984b069dfb0e08d621b47f"
SPOTIFY_REDIRECT_URI = "https://example.com/callback"

user_input_date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")

billboard_url = f"{BILLBOARD_BASE_URL}/{user_input_date}"

billboard_response = requests.get(billboard_url,
                                  headers={"User-Agent": "Chrome/136.0.0.0"})
billboard_response.raise_for_status()
billboard_html_content = billboard_response.text

soup = BeautifulSoup(billboard_html_content, "html.parser")

h3_tags = soup.find_all("h3", id="title-of-a-story", class_="a-no-trucate")

song_title = [h3_tag.get_text().strip() for h3_tag in h3_tags]
# print(song_title)
list_of_scope = ['user-read-email','user-follow-read', 'playlist-read-private',
                 'playlist-read-collaborative', 'playlist-modify-private',
                 'playlist-modify-public']
SPOTIFY_SCOPES = ' '.join(list_of_scope)

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               scope=SPOTIFY_SCOPES,
                                             redirect_uri=SPOTIFY_REDIRECT_URI))

year = user_input_date.split("-")[0]

# Searching spotify to find the song by title
song_uris = []
for title in song_title:
    searched_result = sp.search(q=f"track: {title} year: {year}", type="track")
    try:
        uri = searched_result['tracks']['items'][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")


user_id = sp.current_user()['id']
# Creating a private playlist in spotify
playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{user_input_date} Billboard 100",
                                   public=False,
                                   collaborative=False)

playlist_id = playlist['id']
# Add song to the playlist
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
print('Tracks added successfully')



