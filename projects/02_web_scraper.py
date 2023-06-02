import requests
from bs4 import BeautifulSoup

# Prompt for the list of companies
company_list = input("Enter the list of companies (each on a new line):\n")

# Split the input into a list of company names
company_names = company_list.strip().split('\n')

# Initialize a dictionary to store the job positions for each company
job_positions = {}

# Iterate through each company name
for company_name in company_names:
    # Construct the search URL for the company's career page
    search_url = f'https://www.example.com/careers?q={company_name}'

    # Send a GET request to the search URL
    response = requests.get(search_url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the job links with IT positions
    job_links = soup.find_all('a', {'class': 'job-link', 'data-category': 'IT'})

    # Store the job positions in the dictionary
    job_positions[company_name] = [link['href'] for link in job_links]

# Save the job positions to a text file
output_file = 'job_positions.txt'
with open(output_file, 'w') as file:
    for company_name, positions in job_positions.items():
        file.write(f'{company_name}\n')
        for position in positions:
            file.write(f'- {position}\n')

print(f"Job positions saved to {output_file}.")
