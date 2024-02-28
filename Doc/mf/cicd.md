## Groovy
```
pipeline {
    agent any

    environment {
        ZOWE_HOME = "/path/to/zowe" // Adjust the path to your Zowe CLI installation
        ENDEVOR_SYSTEM = "YOUR_ENDEVOR_SYSTEM"
        ENDEVOR_SUBSYSTEM = "YOUR_ENDEVOR_SUBSYSTEM"
        ENDEVOR_ENVIRONMENT = "YOUR_ENDEVOR_ENVIRONMENT"
        ELEMENT_TYPE = "YOUR_ELEMENT_TYPE"
        ELEMENT_NAME = "YOUR_ELEMENT_NAME"
        BUILD_PACKAGE = "YOUR_BUILD_PACKAGE"
        PROCESSOR = "YOUR_PROCESSOR"
        C1CMACRO = "YOUR_C1CMACRO"
        TARGET_ENVIRONMENT = "YOUR_TARGET_ENVIRONMENT"
    }

    stages {
        stage('Compile') {
            steps {
                script {
                    sh "${ZOWE_HOME}/bin/zowe endevor submit compile" +
                    " --system ${ENDEVOR_SYSTEM}" +
                    " --subsys ${ENDEVOR_SUBSYSTEM}" +
                    " --env ${ENDEVOR_ENVIRONMENT}" +
                    " --type ${ELEMENT_TYPE}" +
                    " --name ${ELEMENT_NAME}"
                }
            }
        }

        stage('Build and Package') {
            steps {
                script {
                    sh "${ZOWE_HOME}/bin/zowe endevor submit build-package" +
                    " --system ${ENDEVOR_SYSTEM}" +
                    " --subsys ${ENDEVOR_SUBSYSTEM}" +
                    " --env ${ENDEVOR_ENVIRONMENT}" +
                    " --type ${ELEMENT_TYPE}" +
                    " --name ${ELEMENT_NAME}" +
                    " --package ${BUILD_PACKAGE}" +
                    " --processor ${PROCESSOR}" +
                    " --c1cmacro ${C1CMACRO}" +
                    " --generate-pkgdef"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh "${ZOWE_HOME}/bin/zowe endevor submit deploy" +
                    " --system ${ENDEVOR_SYSTEM}" +
                    " --subsys ${ENDEVOR_SUBSYSTEM}" +
                    " --env ${ENDEVOR_ENVIRONMENT}" +
                    " --type ${ELEMENT_TYPE}" +
                    " --name ${ELEMENT_NAME}" +
                    " --package ${BUILD_PACKAGE}" +
                    " --target-environment ${TARGET_ENVIRONMENT}"
                }
            }
        }
    }
}

```
