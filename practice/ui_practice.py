import requests

# Base URL with placeholder for the image number
base_url = "https://vishal-dcode.github.io/Cyberfiction-Clone/assets/images/bg_male/male{:04d}.png"

# Directory to save downloaded images
save_dir = "images/"

# Start and end numbers for the images
start = 1  # Start from image 0001
end = 300  # End at image 0300

# Loop through the range and download each image
for i in range(start, end + 1):
    # Format the URL
    image_url = base_url.format(i)
    try:
        # Send a request to the URL
        response = requests.get(image_url)
        response.raise_for_status()  # Check for HTTP errors

        # Save the image
        with open(f"{save_dir}male{i:04d}.png", "wb") as file:
            file.write(response.content)

        print(f"Downloaded: male{i:04d}.png")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {image_url}: {e}")
