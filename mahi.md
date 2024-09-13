#### Branch Flow
master
Release-DGB0001
Feature-test

#### Feature
Feature -> Build Jar -> Build Image (#1001-ca5eve7e) -> Deploy to Dev  (#1001-ca5eve7e)

#### Release
Release-DGB0001 -> Build Jar -> Build Image (#1004-8dbuyd88) -> Deploy to SIT (#1004-8dbuyd88) -> Deploy to UAT (#1004-8dbuyd88) 

#### Release
Release-EMER-DGB0001 -> Build Jar -> Build Image (#1003-rkkfkf) -> Deploy to UAT (#1002-rkkfkf) 

#### master
master -> Tagging Source -> Deploy to PROD (#1002-rkkfkf) 
