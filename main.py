#!/usr/bin/python

"""
Author - Vishwanath Malipatil <vishmalipatil@gmail.com>
Date - 15/06/2019

This is main the method which takes a filename as argument and commits it to current reposotory.
:param filename:  Name of the file to be commited to GIT to store that data in commits.

"""

import time
import os.path
import sys

def getCommitMessage(commit_message):
    # commit message will have current timestamp enclosed in [] followed by customer message set.
    return  "[ " + str(time.ctime(to_time)) + " ]" + " : " + commit_message


if __name__ == "__main__":
    filename=sys.argv[1]
    repo_directory = os.curdir
    # set a dynamic message so that you reference it while fetching data
    commit_message = "CUSTOM_MESSAGE_TO_BE_SET"

    # commit to git.
    from git_utils import GitCommandMethods
    gitutils = GitCommandMethods()
    gitutils.gitAdd(filename,repo_directory)
    gitutils.gitCommit(getCommitMessage(commit_message,repo_directory)
    gitutils.gitPush(repo_directory)
