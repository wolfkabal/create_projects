#!/usr/bin/env bash

import sys
import os
import requests
import json
import git


path = "E:\\Coding\\Python\\_automation\\"
token = os.getenv('github_api')
githubURL = "https://api.github.com/"
headers = {
    'Authorization': 'token <token>',
    'Content-Type': 'application/json; charset=utf-8'
    }

print(headers)


def create():
    folderName = str(sys.argv[1])                   #get folder from args
    os.makedirs(path + folderName)                  #create folder in designated directory (path)
    repo_dir = os.path.join(path, folderName)       #create git object
    r = git.Repo.init(repo_dir)                     #git init

    j = createGithubProject(folderName)  #create new repository on github
    remote = j["html_url"]                          #get new repo url
    print(remote)
    origin = r.create_remote('origin', remote)      #set new remote url to our github one
    # -- done by default on repo creation --create a readme file
    #git add
    #git commit
    #git push
    #open vscode "code ."


def createGithubProject(projectName):
    json =  {
    "name": projectName,
    "description": "",
    "private": False,
    "has_issues": True,
    "has_projects": True,
    "has_wiki": False,
    "auto_init": True,
    "license_template": "mit"}
    return run_query(json)
    #print(ret)


def run_query(query):
    request = requests.post(githubURL + "user/repos", data=json.dumps(query), headers=headers)
    if request.status_code == 201:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, request.raw))

if __name__ == "__main__":
    create()

