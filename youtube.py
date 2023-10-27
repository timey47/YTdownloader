from pytube import YouTube

def convert_seconds(seconds):
    """Convert seconds to minutes and seconds."""
    minutes = seconds // 60
    seconds %= 60
    return f"{minutes} minutes, {seconds} seconds"

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)
    print("Duration:", convert_seconds(yt.length))
    print("\nDescription:\n", yt.description)

    # Ask the user for the download directory
    download_path = input("\nEnter the download directory (or press Enter to download in the current directory): ")
    
    if not download_path:
        download_path = "."

    # Select the highest resolution MP4 video stream
    yd = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
    
    print("\nStarting download...")

    # Download the video to the specified directory
    yd.download(output_path=download_path)
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))
