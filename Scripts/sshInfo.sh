export SSHPASS=$SSH_CONNECT_PASSWORD
sshpass -e ssh -o StrictHostKeyChecking=no $SSH_CONNECT_USERNAME@$HOST_NAME "echo $SSH_CONNECT_PASSWORD | sudo -S "whoami""
