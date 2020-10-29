import boto3
client = boto3.client('ecr', region_name='ap-northeast-2')
repo_create = client.create_repository(repositoryName="<your-repo-name")
responese = client.describe_repositories()
print(responese)