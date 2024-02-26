## Install Zowe CLI:
Make sure you have Zowe CLI installed on your machine. You can find installation instructions on the official Zowe documentation.

## Upload COBOL Program:
Use the files upload command to upload your COBOL program to the mainframe.
```
zowe files upload data-set "YOUR.PDS.NAME(MEMBER)" --source "LOCAL/PATH/TO/COBOL/PROGRAM.cbl"
```
## Compile COBOL Program:
After uploading the COBOL program, use the submit command to submit a JCL (Job Control Language) script to compile the COBOL program.

Here's an example of a JCL script to compile a COBOL program:
```
//COBOLJCL JOB ...
//COBOL    EXEC IGYWCL
//SYSUT1   DD  DSN=YOUR.PDS.NAME(MEMBER),DISP=SHR
//SYSUT2   DD  SYSOUT=A
//SYSUT3   DD  SYSOUT=A
//SYSIN    DD  *
    IDENTIFICATION DIVISION.
    PROGRAM-ID. YOURPROGRAM.
    DATA DIVISION.
    WORKING-STORAGE SECTION.
    01 WS-MESSAGE PIC X(50) VALUE 'HELLO, ZOWE!'.
    PROCEDURE DIVISION.
        DISPLAY WS-MESSAGE.
        STOP RUN.
/*

```
```
zowe submit local-file "LOCAL/PATH/TO/compile.jcl"
```

## Check Compilation Output:
You can use the jobs view command to check the status of your submitted job and view the output.
```
zowe jobs view jobname "COBOLJCL"
```


## Jenkins
```
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Assuming your COBOL program is in a Git repository
                git 'https://github.com/your/repo.git'
            }
        }

        stage('Compile COBOL') {
            steps {
                script {
                    // Define your dataset and member name
                    def datasetMember = "YOUR.PDS.NAME(MEMBER)"

                    // Upload COBOL program to the mainframe
                    sh "zowe files upload data-set \"$datasetMember\" --source ./*.cbl"

                    // Create and upload JCL script
                    writeFile file: 'compile.jcl', text: '''
                        //COBOLJCL JOB ...
                        //COBOL    EXEC IGYWCL
                        //SYSUT1   DD  DSN=${datasetMember},DISP=SHR
                        //SYSUT2   DD  SYSOUT=A
                        //SYSUT3   DD  SYSOUT=A
                        //SYSIN    DD  *
                            IDENTIFICATION DIVISION.
                            PROGRAM-ID. YOURPROGRAM.
                            DATA DIVISION.
                            WORKING-STORAGE SECTION.
                            01 WS-MESSAGE PIC X(50) VALUE 'HELLO, ZOWE!'.
                            PROCEDURE DIVISION.
                                DISPLAY WS-MESSAGE.
                                STOP RUN.
                        /*
                    '''

                    sh "zowe files upload data-set \"$datasetMember\" --source compile.jcl"

                    // Submit JCL script
                    sh "zowe submit data-set \"$datasetMember\""
                }
            }
        }

        stage('Check Compilation Output') {
            steps {
                script {
                    // Check the status of the submitted job and view the output
                    sh "zowe jobs view jobname COBOLJCL"
                }
            }
        }
    }
}

```
