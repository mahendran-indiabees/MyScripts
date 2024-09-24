Here is a Dockerfile for creating a custom image that contains both **Kaniko** and **Crane**:

```Dockerfile
# Use a lightweight base image with Kaniko
FROM gcr.io/kaniko-project/executor:latest

# Install Crane
RUN apk add --no-cache bash curl \
    && curl -L https://github.com/google/go-containerregistry/releases/download/v0.12.0/go-containerregistry_Linux_x86_64.tar.gz \
    | tar xz -C /usr/local/bin crane

# Verify installation of both Kaniko and Crane
RUN executor --help && crane --help

# Set Kaniko as the default entrypoint (can be overridden)
ENTRYPOINT ["/kaniko/executor"]
```

### Explanation:
- **Base Image**: Starts with the Kaniko executor image.
- **Crane Installation**: Installs Crane using the `apk` package manager and downloads the binary from the official release.
- **Verification**: After installation, it runs a check to ensure both Kaniko and Crane are installed.
- **Entrypoint**: Sets Kaniko as the default entrypoint, but you can change it as needed.

You can build this custom image with the following command:

```bash
docker build -t custom-kaniko-crane-image .
```

Let me know if you need additional configurations or adjustments!
