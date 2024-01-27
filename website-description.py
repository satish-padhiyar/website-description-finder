import requests
from bs4 import BeautifulSoup

def get_website_description(url):
    try:
        # Send an HTTP GET request to the website
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the website
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the meta description tag if present
            meta_description = soup.find('meta', attrs={'name': 'description'})

            if meta_description:
                return meta_description.get('content')
            else:
                return "No meta description found on the website."

        else:
            return f"Failed to retrieve website content. Status code: {response.status_code}"

    except Exception as e:
        return f"An error occurred: {e}"

# Get user input for the website URL
user_input = input("Enter the URL of the website: ")

# Call the function with the user-provided URL
description = get_website_description(user_input)

# Print the result
print(f"Website Description: {description}")
