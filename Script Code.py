url = 'https://account.uipath.com/oauth/token'
json_data = '{"Content-Type": "application/json"}'
headers = json.loads(json_data)

json_data = '{"grant_type": "refresh_token","client_id": "<<Your client ID>>","refresh_token": "<<Your refresh token generated>>"}'
data = json.loads(json_data)
response = requests.post(url, headers=headers, json=data)
token = response.json().get("access_token")

url = 'https://cloud.uipath.com/erigertndokaj/DefaultTenant/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs'
json_data = '{"Content-Type": "application/json", "X-UIPATH-TenantName": "DefaultTenant", "X-UIPATH-OrganizationUnitId": "<<Your folder ID>>", "Authorization": "Bearer '+token+'"}'
headers = json.loads(json_data)
json_data = '{"startInfo": {"ReleaseKey": "<<Your release key>>","Strategy": "ModernJobsCount", "JobsCount": 1,"InputArguments": "{}"}}'
data = json.loads(json_data)
requests.post(url, headers=headers, json=data)
