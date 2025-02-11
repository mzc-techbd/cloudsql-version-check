import os
from google.cloud.resourcemanager import ProjectsClient, FoldersClient
from google.cloud import asset_v1
from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

instance_versions = ["MYSQL_5_6", "MYSQL_5_7", "POSTGRES_9_6", "POSTGRES_10", "POSTGRES_11", "POSTGRES_12"]

def get_project_num(org_id):
    client = asset_v1.AssetServiceClient()
    scope = f"organizations/{org_id}"
    query = f"sqladmin.googleapis.com AND state:enabled"

    request = asset_v1.SearchAllResourcesRequest(
        scope=scope,
        query=query,
    )

    for response in client.search_all_resources(request=request):
        get_cloudsql_version(project_name_split(response.project))

def project_name_split(project):
    return project.split('/',1)[1] # project/12345678 to 12345678

def get_cloudsql_version(project_id):
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('sqladmin', 'v1beta4', credentials=credentials)
    project = project_id 
    request = service.instances().list(project=project)
    results = []
    
    while request is not None:
        response = request.execute()

        if len(response) == 0:
            break

        for database_instance in response['items']:
            # TODO: Change code below to process each `database_instance` resource:
            for instance_version in instance_versions:
                if database_instance["databaseVersion"] == instance_version:
                    result = {
                        "project_num": project,
                        "project": database_instance["project"],
                        "displayName": database_instance["name"],
                        "databaseVersion": database_instance["databaseVersion"],
                        "gceZone": database_instance["gceZone"]
                    }
                    results.append(result)
        request = service.instances().list_next(previous_request=request, previous_response=response)

    if len(results) != 0:
        pprint(results)

def main():
    ORGANIZATION_ID = '' # 0123456789
    
    get_project_num(ORGANIZATION_ID)
    
if __name__=="__main__":
    main()
