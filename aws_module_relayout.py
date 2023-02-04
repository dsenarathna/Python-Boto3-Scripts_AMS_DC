#!/usr/bin/python

import os, requests, json
from datetime import date

git_trf_url = 'https://api.github.com/users/terraform-aws-modules/repos'
git_base_url = 'https://github.com/terraform-aws-modules/'
today = date.today()
dt_string = today.strftime("%b-%d-%Y")

def get_git_trf_mods():
    repos = []
    resp = requests.get(git_trf_url) 
    data  = json.loads(resp.text)
    for repo in data:
        if "terraform" in repo["name"]:
            repos.append(repo["name"])
    return repos

def git_sm_add(mod):
    os.system("git submodule add "+git_base_url+mod)
    print("Adding new submodule "+mod)

def git_sm_update(mod):
    os.system("git submodule update "+mod)
    print("Updating existing submodule "+mod)
    
def git_add_all():
    os.system("git add .")
    
def git_commit():
    commit_msg = "Update/Adding terraform modules "+dt_string
    command = "git commit -m '"+commit_msg+"'"
    os.system(command) 
    
def add_or_update_sm():
    existing_mods = [i for i in os.listdir("./") if os.path.isdir(i) if not i.lstrip().startswith('.')]
    return existing_mods
 
 # CODE 
modules = get_git_trf_mods()
existing_mods = add_or_update_sm()
 
for DIR in modules:
    if DIR in existing_mods:
        git_sm_update(DIR)
    else:
        git_sm_add(DIR)

git_add_all()
git_commit()
 
