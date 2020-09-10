import os
from github import Github

token = os.environ.get('GITHUB_TOKEN')
g = Github(token)

repo = g.get_repo('bofavom/grayscale_bitcoin_shares')


def updateFile(filename):
    fileContent = None
    with open(filename, 'r') as f:
        fileContent = f.read()

    f.close()
    
    if fileContent is not None:
        contents = repo.get_contents(filename)
        commitMessage = 'New update'
        repo.update_file(contents.path, commitMessage, fileContent, contents.sha)