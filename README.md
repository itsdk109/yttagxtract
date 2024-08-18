# YouTube Video Tags & Description Extractor

This Python script allows users to retrieve details of a YouTube video by providing its URL. The script utilizes the YouTube Data API to fetch information such as video title, tags, and keywords from the video description.

## Prerequisites
Before using the script, ensure that you have the necessary modules installed:

### For Windows Users
```bash
pip install google-api-python-client
```

### For Linux Users
```bash
pip3 install google-api-python-client
```

## API Key Setup
To use the YouTube Data API, you need to set up an API key. Replace the placeholder in the script with your actual API key. if you do not know how to generate google API [Instruction](https://github.com/itsdk109/YouTube_Video_Tags_and_Description_Extractor/blob/main/google_api_create_instruction) or [Official_Site](https://cloud.google.com/api-gateway/docs/creating-api).

```python
# Set your API key here (You should replace this with your actual API key)
API_KEY = 'Your_API_Key_Here'
```

## Usage

### For Windows Users
1. Open a command prompt.
2. Navigate to the directory containing the script.
3. Run the script by entering the following command:
   ```bash
   python setup.py
   ```

### For Linux Users
1. Open a terminal.
2. Navigate to the directory containing the script.
3. Firstly give the executable permision and Run the script by entering the following command:
   ```bash
     chmod +x setup.py
   ```
   ```bash
   python3 setup.py
   ```

## Input
Enter a valid YouTube video URL when prompted.

![Project ScreenShot](https://github.com/itsdk109/yttagxtract/blob/main/yttagxtract.jpg)



## Output
The script will display the following details of the provided YouTube video:
- Video ID
- Title
- Tags (if available)
- Keywords extracted from the video description (if available)

Note: In case of an invalid YouTube video URL format, an error message will be displayed.

Feel free to use this script to quickly gather information about your favorite YouTube videos!

# Disclaimer: 
+ Do not use this tool for illegal or unethical purposes.
+ This script is intended for educational and legitimate purposes only.
+ Ensure compliance with YouTube's terms of service and policies while using this tool.
+ The developers of this script are not responsible for any misuse or violation of terms.
