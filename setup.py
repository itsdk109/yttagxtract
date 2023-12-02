# Import the necessary modules
import os
#The build function is commonly used to create an API client for a specific Google API.
from googleapiclient.discovery import build

# Set your API key here (You should replace this with your actual API key)
API_KEY = 'Your_API_Key_Here'

# Create a YouTube Data API service using the API key
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Define a function to get video details given a YouTube video URL
def get_video_details(video_url):
    try:
        # Extract the video ID from the URL
        video_id = video_url.split('?v=')[1]
        
        # Use the YouTube Data API to fetch video details, specifically the snippet part
        response = youtube.videos().list(part='snippet', id=video_id).execute()
        
        # Extract information from the API response
        video_info = response['items'][0]['snippet']
        title = video_info['title']
        tags = video_info.get('tags', [])  # Get video tags if available, or an empty list if not
        keywords = video_info.get('description', '').split()  # Get keywords from the video description
        
        # Return the extracted video details as a dictionary
        return {
            'video_id': video_id,
            'title': title,
            'tags': tags,
            'keywords': keywords
        }
    except IndexError:
        # Handle the case where the URL is not in the expected format
        print("Error: Invalid YouTube video URL format. Please provide a valid URL.")
        return None

# The following code will only run if this script is executed directly (not imported as a module)
if __name__ == '__main__':
    # Prompt the user to input a YouTube video URL
    video_url = input("Enter YouTube video URL: ")
    print(" ")
    
    # Call the get_video_details function to retrieve video information
    video_details = get_video_details(video_url)
    
    # Check if video_details is None (indicating an error)
    if video_details is not None:
        # Print the retrieved video details
        print("Video ID:", video_details['video_id'])
        print(" ")
        print("Title:", video_details['title'])
        print(" ")
        # Print tags in a readable format
        if video_details['tags']:
            tags_sentence = ', '.join(video_details['tags'])
            print("Tags:\n", tags_sentence)
        else:
            print("Tags: No tags available")
            
        print(" ")

        # Print keywords in a readable format with a period at the end
        if video_details['keywords']:
            keyword_sentence = ' '.join(video_details['keywords']) + '.'
            print("Keywords:\n", keyword_sentence)
        else:
            print("Keywords: No keywords available")
