#!/bin/bash
#Get the values from shell script command line
GIT_USER=$1
GIT_PASS=$2
ARTIFACT_NUMBER=$3
GIT_SOURCE_URL=$4
GIT_SOURCE_BRANCH=$5
YAML_FILE=$6

#Clone the Github repo
git clone https://$GIT_USER:$GIT_PASS@$GIT_SOURCE_URL

#Switch to respective branch
git switch $GIT_SOURCE_BRANCH

#Update the Build Number
yq -i ".stages[].jobs[].steps[].inputs.buildNumber=$ARTIFACT_NUMBER" $YAML_FILE

#git add the files
git add .

#Commit the files
git commit -m "Build number is updated by Automation"

#Push the files
git push -f origin $GIT_SOURCE_BRANCH