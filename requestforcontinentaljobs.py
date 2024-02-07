import requests
import json

payload = {
'tx_conjobs_api[filter][locationSuggestChecksums][]': '9239c9b9130658261ab51795372bd7aa',
'tx_conjobs_api[filter][searchTerm]':'Internship',
'tx_conjobs_api[itemsPerPage]':'100'
}
# Make the POST request to the API endpoint
url = "https://jobs.continental.com/ro/api/result-list/pagetype-jobs/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

response = requests.get(url,params=payload,headers=headers,verify=False)
json_data = response.json()

if "result" in json_data:
    # Extract the list of results
    job_list = json_data["result"]

    # Specify the file path to save the JSON file
    file_path = "jobs_data.json"

    # Save the JSON data to a file
    with open(file_path, "w") as json_file:
        json.dump(job_list, json_file, indent=4)

    print(f"JSON data saved successfully to {file_path}")
else:
    print("No list of results found in the JSON data.")

with open('jobs_data.json') as f:
    data = json.load(f)
with open('results.txt', 'w') as f:
    for item in data['list']:
        f.write(item['title']+'\n')
        f.write(item['publicationDate']+'\n')
        f.write('https://jobs.continental.com/en/detail-page/job-detail/'+str(item['url'])+'\n')
        f.write('\n')
        f.write('\n')
