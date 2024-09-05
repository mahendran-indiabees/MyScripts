
Based on your requirements, here is a detailed GitLab CI/CD pipeline configuration (`.gitlab-ci.yml`) for automating the deployment process across various environments with semantic versioning, automated rollbacks, and handling of different branch types.

### GitLab CI/CD Pipeline Configuration (`.gitlab-ci.yml`)

```yaml
variables:
  ACR_REGISTRY: "your-acr-registry.azurecr.io"
  IMAGE_NAME: "your-app-name"
  DOCKER_DRIVER: overlay2
  VERSION_FILE: "version.txt"
  PROD_IMAGE_TAG: "v$(cat $VERSION_FILE)"

stages:
  - build
  - deploy_dev
  - deploy_sit
  - deploy_uat
  - deploy_preprod
  - deploy_prod
  - tagging
  - rollback

# Define the jobs

build_job:
  stage: build
  script:
    - echo "Building JAR..."
    - ./mvnw clean package -DskipTests
    - echo "Building Docker Image..."
    - docker build -t $ACR_REGISTRY/$IMAGE_NAME:$CI_COMMIT_REF_SLUG-$CI_COMMIT_SHORT_SHA .
    - echo "Pushing Docker Image to ACR..."
    - echo $ACR_PASSWORD | docker login $ACR_REGISTRY -u $ACR_USERNAME --password-stdin
    - docker push $ACR_REGISTRY/$IMAGE_NAME:$CI_COMMIT_REF_SLUG-$CI_COMMIT_SHORT_SHA
  only:
    - /^feature\/.*$/  # Runs only on feature branches
    - /^release\/.*$/  # Runs only on release branches

deploy_dev:
  stage: deploy_dev
  script:
    - echo "Deploying to DEV environment..."
    - ./deploy.sh dev $ACR_REGISTRY/$IMAGE_NAME:$CI_COMMIT_REF_SLUG-$CI_COMMIT_SHORT_SHA
  only:
    - /^feature\/.*$/  # Runs only on feature branches
  dependencies:
    - build_job

deploy_sit:
  stage: deploy_sit
  script:
    - echo "Deploying to SIT environment..."
    - ./deploy.sh sit $ACR_REGISTRY/$IMAGE_NAME:$CI_COMMIT_REF_SLUG-$CI_COMMIT_SHORT_SHA
  only:
    - /^release\/.*$/  # Runs only on release branches
  when: manual
  dependencies:
    - build_job

deploy_uat:
  stage: deploy_uat
  script:
    - echo "Deploying to UAT environment..."
    - ./deploy.sh uat $ACR_REGISTRY/$IMAGE_NAME:$CI_COMMIT_REF_SLUG-$CI_COMMIT_SHORT_SHA
  only:
    - /^release\/.*$/  # Runs only on release branches
  when: manual
  dependencies:
    - build_job

deploy_preprod:
  stage: deploy_preprod
  script:
    - echo "Deploying to PrePROD environment..."
    - ./deploy.sh preprod $ACR_REGISTRY/$IMAGE_NAME:$CI_COMMIT_REF_SLUG-$CI_COMMIT_SHORT_SHA
  only:
    - /^release\/.*$/  # Runs only on release branches
  when: manual
  dependencies:
    - build_job

deploy_prod:
  stage: deploy_prod
  script:
    - echo "Deploying to PROD environment with tag $PROD_IMAGE_TAG..."
    - ./deploy.sh prod $ACR_REGISTRY/$IMAGE_NAME:$PROD_IMAGE_TAG
  only:
    - master
  dependencies:
    - build_job

tagging_source:
  stage: tagging
  script:
    - echo "Tagging source with $PROD_IMAGE_TAG..."
    - git tag $PROD_IMAGE_TAG
    - git push origin $PROD_IMAGE_TAG
    - echo "Incrementing version for the next release..."
    - echo $(($CI_PIPELINE_IID+1)) > $VERSION_FILE
    - git add $VERSION_FILE
    - git commit -m "Bump version to $PROD_IMAGE_TAG"
    - git push origin master
  only:
    - master
  dependencies:
    - deploy_prod

rollback:
  stage:
