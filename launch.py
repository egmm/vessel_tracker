import subprocess

docker_compose = subprocess.run(['docker-compose', 'up'])
print(docker_compose)
