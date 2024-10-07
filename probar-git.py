from github import Github

g = Github("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")

# Obtener el repositorio
repo = g.get_repo("AlejandroDiBattista/lab4-c2")
# Listar todos los pull requests pendientes
pulls = repo.get_pulls(state='open', sort='created', base='main')
for pr in pulls:
    print(f"PR #{pr.number}: {pr.title} (created by {pr.user.login})")