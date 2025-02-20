import requests

# Set the API endpoint and headers
url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjMWRhNTQyMTc0NTA0NDQ5OWMxMmE0NzU2NWY3NjYyZiIsIm5iZiI6MTczODM0NDAxOS4yNzAwMDAyLCJzdWIiOiI2NzlkMDY1MzI1YjZmMWIzMGRiZGZmZGEiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ynnqK7wMoE-KmzCBZp2aULUHHbXD66lM92hcX4wxp1c"
}

# Fetch data from TMDB
response = requests.get(url, headers=headers)
if response.status_code == 200:
    movies = response.json().get("results", [])[:10]  # Get only the first 10 results

    # Create a list to store the movie titles
    popular_titles = [movie["title"] for movie in movies]

    # Print the list of popular titles
    print(popular_titles)
else:
    print("Failed to fetch data:", response.status_code)
