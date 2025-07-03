import requests
import os


def get_version():
	request = requests.get('https://github.com/endless-sky/endless-sky/raw/refs/heads/master/changelog')
	with open('changelog.txt', 'wb') as changelog:
		changelog.write(request.content) # downloading the changelog
	with open('changelog.txt', 'r') as sourcefile:
		onlineversion = sourcefile.readline().replace('Version ', '').replace('\n', '') # result example: 0.10.10
	if int(onlineversion[-1])%2 == 0:
		versiontag = 'v' + onlineversion + ': Stable Release'
	else:
		versiontag = 'v' + onlineversion + ': Unstable Release'
	env_file = os.getenv('GITHUB_ENV')
	with open(env_file, "a") as myfile:
		myfile.write("ES_VERSION=" + versiontag + '\n')


def run():
	get_version()


if __name__ == "__main__":
	run()