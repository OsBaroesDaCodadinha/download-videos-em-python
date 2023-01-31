# -*- coding: utf-8 -*-
from fastdownload import FastDownload
from urllib.request import urlopen
import json



urlInput = input(f"Digite a url dara download:\n\nLEMBRANDO QUE A URL NÃO DEVE TER UMA BARA '/' NO FINAL\n\n")

# # store the URL in url as
# # parameter for urlopen
url = f"{urlInput}/files"
print(url)
# store the response of URL

response = urlopen(url)


# storing the JSON response
# from url in data
data_json = json.loads(response.read())
folder = input(f'Caminho de onde baixar:\n')
if folder == '':
    folder = 'api_ead_video_test/storage'
# print the json response
secrets = data_json['secrets']
type = 'secrets'
for keys in secrets:
    curso = keys
    for keysM in secrets[keys]:
        module = keysM
        for keysL in secrets[keys][keysM]:
            lecture = keysL
            for keysLKey in secrets[keys][keysM][keysL]:
                lectureKey = keysLKey
                d = FastDownload(
                    base=f'../{folder}/app/{type}/videos/{curso}/{module}/{lecture}', archive=lecture)
                d.download(
                    f"{urlInput}/download/{type}/{curso}/{module}/{lecture}/{lectureKey}")


print(f"{type} atualizado com sucesso!")
videos = data_json['videos']
type = 'public'
for keys in videos:
    curso = keys
    for keysM in videos[keys]:
        module = keysM
        for keysL in videos[keys][keysM]:
            lecture = keysL
            for keysLKey in videos[keys][keysM][keysL]:
                lectureKey = keysLKey
                d = FastDownload(
                    base=f'../{folder}/{type}/videos/{curso}/{module}/{lecture}', archive=lecture)
                d.download(
                    f"{urlInput}/download/{type}/{curso}/{module}/{lecture}/{lectureKey}")
print(f"{type} atualizado com sucesso!")
