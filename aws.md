# AWS & DevOps Scenario-Based Interview Questions & Answers (50 Questions)

## AWS Core Services

### 1. **EC2 Instance Not Booting Properly**
**Q:** After creating an EC2 instance, it's not reachable via SSH. What steps do you take to debug?  
**A:**  
- Check security group rules for port 22  
- Validate key pair and correct SSH username (e.g., ec2-user)  
- Use EC2 serial console or instance screenshot  
- Inspect system logs via AWS console

### 2. **S3 Bucket Access Denied**
**Q:** A user with S3 read-only permissions can't list objects. What could be the issue?  
**A:**  
- Missing `s3:ListBucket` on the bucket ARN  
- Bucket policy may override IAM policy  
- Cross-account access missing required role trust

### 3. **High Latency on RDS Queries**
**Q:** An application sees high query latency from RDS. What would you investigate?  
**A:**  
- Check instance CPU, IOPS in CloudWatch  
- Enable Enhanced Monitoring and Performance Insights  
- Optimize slow queries using `EXPLAIN`

### 4. **Lambda Function Timeout**
**Q:** A Lambda times out after 30 seconds. What’s your troubleshooting plan?  
**A:**  
- Increase timeout in Lambda configuration  
- Profile function code for slow I/O (e.g., API calls)  
- Use CloudWatch logs and X-Ray to trace execution

### 5. **VPC Connectivity Issues**
**Q:** Two EC2 instances in same VPC can't talk to each other. What would you check?  
**A:**  
- Ensure they are in the same or peered subnets  
- Validate NACLs and security groups  
- Confirm no route table misconfiguration

## Puppet

### 6. **Puppet Agent Not Receiving Catalog**
**Q:** A Puppet agent is not getting the latest catalog. How do you debug?  
**A:**  
- Check Puppet master logs (`puppetserver.log`)  
- Validate time sync (NTP) between agent and master  
- Run `puppet agent -t --debug`

### 7. **Resource Conflict in Manifest**
**Q:** Puppet throws a duplicate resource declaration error. What's the fix?  
**A:**  
- Use `puppet resource` to identify existing resources  
- Refactor manifest into reusable modules  
- Ensure class inclusion doesn't lead to duplication

### 8. **Puppet Fails on File Resource**
**Q:** A file resource fails to apply. How to resolve?  
**A:**  
- Check file permissions and existence  
- Ensure Puppet user has access to source  
- Use `puppet apply --noop` to simulate

### 9. **Node Classification Not Working**
**Q:** A node isn't applying the expected classes. What's your plan?  
**A:**  
- Check `/etc/puppetlabs/puppet/puppet.conf` for node name  
- Review ENC or site manifest for matching rules  
- Run `puppet lookup` for variable debugging

## ECR

### 10. **Cannot Push Image to ECR**
**Q:** Docker push fails to ECR. What to validate?  
**A:**  
- Auth token expired (`aws ecr get-login-password`)  
- IAM permissions missing `ecr:PutImage`  
- Repository not created in the region

### 11. **ECR Image Pull Fails in ECS Task**
**Q:** ECS task fails to pull image from ECR. How to investigate?  
**A:**  
- Task role lacks `ecr:GetDownloadUrlForLayer`  
- Ensure `executionRole` is configured  
- Check networking for VPC endpoints

### 12. **Old Images Not Deleted in ECR**
**Q:** How do you manage old image cleanup?  
**A:**  
- Use lifecycle policies in ECR  
- Set rules to delete untagged or older images  
- Automate with Lambda if custom logic needed

## ECS

### 13. **Task Fails with Exit Code 137**
**Q:** What does exit code 137 indicate in ECS?  
**A:**  
- Container was OOMKilled (out of memory)  
- Increase task memory or optimize container usage  
- Use CloudWatch metrics for analysis

### 14. **Service Not Replacing Unhealthy Tasks**
**Q:** Why might ECS not replace a failed task?  
**A:**  
- Health checks not configured or incorrect  
- Minimum healthy percent in deployment config too high  
- Container may be exiting too quickly to log

### 15. **Service Fails to Scale**
**Q:** Service doesn’t scale out under CPU load. What do you inspect?  
**A:**  
- Auto Scaling policy tied to ECS metrics  
- Ensure CloudWatch alarms are triggering  
- Capacity provider might be limited

## AMI with Packer

### 16. **AMI Not Booting**
**Q:** A custom AMI created with Packer is not booting. What could be wrong?  
**A:**  
- Ensure you installed and enabled cloud-init  
- Validate partition layout and bootloader settings  
- Use `amazon-ebs` builder for compatibility

### 17. **Provisioner Fails in Packer**
**Q:** Shell provisioner in Packer fails mid-build. What’s your plan?  
**A:**  
- Enable verbose logging with `PACKER_LOG=1`  
- Check script syntax and permissions  
- Validate `sudo` usage inside scripts

### 18. **Packer Build Times Out**
**Q:** Packer fails after waiting for SSH. How to troubleshoot?  
**A:**  
- Ensure security group allows SSH  
- Validate AMI base image and region  
- Check SSH username (e.g., ubuntu vs ec2-user)

### 19. **Reusing AMIs in Auto Scaling Groups**
**Q:** How do you roll out a new AMI to ASGs safely?  
**A:**  
- Create launch template versions with new AMI  
- Use rolling update or instance refresh strategy  
- Validate via health checks and metrics

## Docker

### 20. **Docker Container Exits Immediately**
**Q:** A container exits right after starting. Why?  
**A:**  
- Entrypoint or CMD script fails  
- Main process finishes execution (e.g., shell command ends)  
- Add `tail -f /dev/null` to keep it alive for debug

### 21. **Volume Mount Not Working in Docker**
**Q:** Mounted volume is empty inside container. Why?  
**A:**  
- Host path does not exist  
- Named volume may have stale data  
- Validate Docker Compose paths and mounts

### 22. **Docker Daemon Uses High CPU**
**Q:** Docker daemon consumes high CPU on host. How to analyze?  
**A:**  
- Check for zombie containers or logging loops  
- Use `docker stats` and `strace` on the daemon  
- Consider overlay2 performance issues

### 23. **Docker Compose Not Starting All Services**
**Q:** `docker-compose up` starts only partial services. What’s wrong?  
**A:**  
- Service dependency or restart policy issue  
- Errors in YAML (e.g., indentation, syntax)  
- Use `depends_on` and healthchecks properly

## Linux

### 24. **SSH Freezes on Login**
**Q:** SSH connection hangs after authentication. What could be the cause?  
**A:**  
- `.bashrc` or `.bash_profile` runs a blocking command  
- DNS resolution issues  
- Use `ssh -vvv` for debugging

### 25. **Disk Full Due to Log Rotation**
**Q:** How to prevent disk space exhaustion from logs?  
**A:**  
- Use `logrotate` with compression and retention policies  
- Monitor with `du` and `find`  
- Separate log mounts for large apps

### 26. **Out of Inodes**
**Q:** System has disk space but cannot create files. Why?  
**A:**  
- Inodes exhausted due to too many small files  
- Run `df -i` to check inode usage  
- Clean up temp or cache directories

### 27. **Cron Job Doesn’t Run**
**Q:** A cron job is defined but doesn’t execute. What would you inspect?  
**A:**  
- User’s crontab vs system crontab  
- Correct PATH and permissions  
- Check logs in `/var/log/cron*`

### 28. **Zombie Processes Accumulate**
**Q:** Server has many zombie processes. How to address?  
**A:**  
- Zombies are dead children not reaped by parent  
- Identify parent process and restart it  
- Use `ps -eo pid,ppid,state,cmd | grep Z`

### 29. **High Load Average but Low CPU Usage**
**Q:** What causes high load with low CPU?  
**A:**  
- I/O wait or uninterruptible sleep  
- Run `iostat`, `top`, and `vmstat` to analyze  
- Tune disk access or swap usage

### 30. **User Cannot Sudo**
**Q:** A user receives "not in sudoers file". What’s next?  
**A:**  
- Add user to `sudo` group or configure `/etc/sudoers`  
- Use `visudo` to edit safely  
- Check `/etc/group` for membership

## BONUS – Mixed Real-Time Issues

### 31. **ECS Task Stuck in Provisioning**
### 32. **Dockerfile COPY command fails in GitLab CI**
### 33. **Instance metadata not available in EC2**
### 34. **Dockerfile builds locally but fails in Jenkins**
### 35. **Lambda fails with permissions error**
### 36. **CloudWatch alarms not triggering**
### 37. **AMI-based launch configuration fails post-deploy**
### 38. **Volume detachment fails on EC2 termination**
### 39. **Puppet class dependency chain issues**
### 40. **S3 object uploaded but not available immediately**

### 41-50: Real-world AWS + DevOps blend
_(Let me know if you'd like me to expand each of these with detailed Q&A)_
