import requests
from bs4 import BeautifulSoup

# URL of Connect Housing
url = "https://www.rightmove.co.uk/estate-agents/profile/Connect-Housing/Re-Lets-176360.html"

# Parse the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the webpage content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the part you want to monitor (modify the selector accordingly)
    monitored_content_element = soup.find('div', class_='propertyList_noPropertiesMessageContainer__dvAkz')

    # Check if the element was found
    if monitored_content_element:
        monitored_content = monitored_content_element.text.strip()

        # Save the monitored content to a file
        with open('previous_content.txt', 'w') as f:
            f.write(monitored_content)

        print("Initial content saved.")

        # Load previous content
        with open('previous_content.txt', 'r') as f:
            previous_content = f.read()

        # Fetch the current content again
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            current_content_element = soup.find('div', class_='propertyList_noPropertiesMessageContainer__dvAkz')

            if current_content_element:
                current_content = current_content_element.text.strip()

                # Compare the current and previous content
                if current_content != previous_content:
                    print("Change detected!")

                    # Update the stored content
                    with open('previous_content.txt', 'w') as f:
                        f.write(current_content)
                else:
                    print("No change.")
            else:
                print("Current content element not found.")
        else:
            print("Failed to retrieve current content.")
    else:
        print("Monitored content element not found.")
else:
    print("Failed to retrieve webpage.")
    
