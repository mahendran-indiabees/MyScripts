## Prerequisites:

#### Download the installer:

Visit Broadcom's support portal and download the Endeavor Bridge for Git installer for your compatible platform. Refer to the documentation for specific version requirements: https://community.broadcom.com/mainframesoftware/discussion/endevor-bridge-for-git-version-2120-now-available-1
Ensure permissions:

Verify you have the necessary permissions to install and configure the Bridge, Endeavor, and the Git server.
Installation and Configuration:

#### Install the Bridge:

Run the downloaded installer and follow the on-screen instructions. Choose a suitable server within your network for the installation.
Database configuration:

During installation, you'll be prompted to choose an embedded or external database for the Bridge.
Embedded database: Select "Use Embedded Database" and provide a name and location for the database file.
External database: Select "Use External Database" and configure the connection details like hostname, port, username, and password for your existing database server.
#### REST API configuration:

After installation, access the Bridge's web interface (default URL: http://localhost:8080) and navigate to Configuration > REST API.
Enable the REST API by checking the "Enabled" checkbox and optionally configure authentication settings if needed.
#### Endeavor connection:

Navigate to Configuration > Endeavor Connections.
Click "Add Connection" and provide details like:
Hostname: Address of your Endeavor server.
Port: Port number used by Endeavor.
Security: Choose "Basic" or "Kerberos" authentication and provide credentials.
Component details: Specify the system and subsystem associated with the Endeavor components you want to manage through the Bridge.
#### Mapping Configuration:

#### Create a mapping:

Navigate to Configuration > Mappings.
Click "Add Mapping" and provide a name for the mapping.

#### Map elements:

In the "Git Repository URL" field, specify the URL of your Git repository (e.g., GitHub, Bitbucket).
In the "Endeavor Connection" section, select the previously created Endeavor connection.
Define mapping rules to connect specific Git files/folders with corresponding Endeavor components (copybooks, JCLs). Use wildcards () for broader matching if needed (e.g., ".cpy" for all copybook files).
Refer to the documentation for detailed instructions on mapping syntax: https://community.broadcom.com/mainframesoftware/discussion/endevor-bridge-for-git-version-2120-now-available-1
#### Synchronization options:

In the "Synchronization" section, choose the synchronization direction:
Git to Endeavor: Changes in the Git repository trigger updates in Endeavor.
Endeavor to Git: Changes in Endeavor trigger updates in the Git repository.
Bi-directional: Updates in either system trigger synchronization in the other.
Define synchronization triggers: Choose from options like manual trigger, automatic trigger on commit, or schedule-based triggers.
#### Testing and Verification:

After configuring the mapping, you can initiate a test synchronization to verify the bridge functions as expected.
Refer to the Broadcom documentation for detailed instructions on testing and troubleshooting: https://community.broadcom.com/mainframesoftware/discussion/endevor-bridge-for-git-version-2120-now-available-1
