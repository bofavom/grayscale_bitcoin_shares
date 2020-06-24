from github import Github

g = Github('f713917873d849cda706e7c09fa3070801d6cc4a')

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