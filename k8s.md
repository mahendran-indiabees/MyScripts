# Kubernetes Scenario-Based Interview Questions & Answers (30 Questions)

## 1. **Pod Stuck in Init State**
**Q:** A pod is stuck in the `Init` state for several minutes. How would you troubleshoot this?  
**A:**  
- Use `kubectl describe pod <pod>` to view init container logs and status  
- Check if init container is waiting on resources (e.g., ConfigMap, volume mount)  
- Look at imagePull errors or slow startup commands  
- Validate dependencies (e.g., initContainer waiting for a DB connection)

## 2. **Application Not Accessible via Ingress**
**Q:** Your app is deployed and service is accessible, but the Ingress endpoint shows 404. What would you check?  
**A:**  
- Verify Ingress rules and path configuration  
- Confirm the IngressClass annotation is present  
- Check Ingress controller logs (e.g., NGINX) for routing issues  
- Ensure backend service has healthy pods

## 3. **PVC Stuck in Pending**
**Q:** Why would a PVC be stuck in Pending status?  
**A:**  
- No matching PV available with the required storage class, size, or access mode  
- Misconfigured StorageClass or CSI driver  
- Use `kubectl describe pvc` and `kubectl get sc` to diagnose

## 4. **Deployment Rollout Stuck**
**Q:** A deployment hangs during rollout. How do you debug it?  
**A:**  
- Run `kubectl rollout status deployment <name>`  
- Check pod events and logs  
- Verify probes, image versions, and startup time  
- Ensure old pods terminate cleanly and new ones pass readiness checks

## 5. **Service Has No Endpoints**
**Q:** A service exists, but `kubectl get endpoints` shows none. What’s wrong?  
**A:**  
- Check service selector matches pod labels  
- Ensure pods are running and in `Ready` state  
- Validate that namespace is correct

## 6. **Kubelet Not Registering Node**
**Q:** A new worker node joins the cluster but doesn’t appear in `kubectl get nodes`. Why?  
**A:**  
- Kubelet may not have correct API server credentials  
- Check `kubelet` logs  
- Validate the node's hostname is resolvable and unique

## 7. **ImagePullBackOff on Private Registry**
**Q:** Why would a private image fail to pull even when the secret is configured?  
**A:**  
- Secret not referenced in the pod spec under `imagePullSecrets`  
- Wrong Docker registry URL or incorrect credentials  
- Check `kubectl describe pod` for exact error

## 8. **Pods Randomly OOMKilled**
**Q:** What causes OOMKilled pods, and how to avoid them?  
**A:**  
- Memory usage exceeded limits defined in pod spec  
- Use `kubectl top pod` to monitor usage  
- Set realistic resource `requests` and `limits`

## 9. **High Latency Observed Between Pods**
**Q:** What tools and techniques would you use to debug high latency?  
**A:**  
- Use `ping`, `curl`, or `wrk` via `kubectl exec`  
- Inspect CNI plugin metrics/logs  
- Validate NetworkPolicy and pod CPU throttling

## 10. **Helm Install Timeout**
**Q:** Helm install times out on a complex chart. How to approach this?  
**A:**  
- Run `helm install --debug --wait`  
- Check if CRDs are being created properly  
- Validate initContainers and readiness probes

## 11. **CrashLoopBackOff on Update**
**Q:** A deployment update causes CrashLoopBackOff. How do you investigate?  
**A:**  
- Compare old vs new config in deployment YAML  
- Use `kubectl rollout history`  
- Check app logs, especially environment variables and secrets

## 12. **Pod Affinity Rules Ignored**
**Q:** Pods don’t schedule as per affinity rules. What could be wrong?  
**A:**  
- Mismatched label selectors  
- Rules too strict (use `preferredDuringScheduling`)  
- Review events with `kubectl describe pod`

## 13. **DaemonSet Not Scheduling on All Nodes**
**Q:** A DaemonSet is missing from a node. Why?  
**A:**  
- Node tainted, and pod lacks toleration  
- Node selector or affinity doesn’t match  
- Check DaemonSet logs and events

## 14. **NetworkPolicy Blocks Expected Traffic**
**Q:** App stopped working after applying NetworkPolicy. How do you debug?  
**A:**  
- Inspect rules using `kubectl get networkpolicy`  
- Use `kubectl exec` to test connectivity  
- Add logging to policy engine (e.g., Calico audit logs)

## 15. **Pod Uses Excess CPU Unexpectedly**
**Q:** A pod is throttled or using excess CPU. What’s the approach?  
**A:**  
- Use `kubectl top pod` and `kubectl describe pod`  
- Review requests and limits  
- Analyze containerized app for infinite loops or CPU-bound code

## 16. **Node Pressure Causes Pod Eviction**
**Q:** Why are pods evicted when node has free memory?  
**A:**  
- Check for disk pressure or inode exhaustion  
- Use `kubectl describe node` and look at `Conditions` section  
- Eviction threshold may be exceeded

## 17. **External DNS Entry Not Created**
**Q:** External DNS controller fails to create route53 record. Why?  
**A:**  
- Service missing required annotations  
- RBAC rules prevent controller access  
- Check controller logs and cloud API limits

## 18. **Pod Disruption Budget Blocking Upgrade**
**Q:** A rollout is blocked by a PodDisruptionBudget. What’s next?  
**A:**  
- Check `kubectl get pdb` for minAvailable or maxUnavailable  
- Adjust budget temporarily  
- Verify that enough healthy pods exist

## 19. **Kube-Proxy Not Routing Traffic**
**Q:** Internal service-to-service traffic fails randomly. What to check?  
**A:**  
- Inspect kube-proxy logs  
- Confirm correct mode (`iptables`/`ipvs`)  
- Validate CNI plugin compatibility

## 20. **Can’t Exec into Running Pod**
**Q:** You get a connection error while trying to `kubectl exec`. What might be wrong?  
**A:**  
- Check API server and kubelet connectivity  
- Confirm RBAC permissions on the user account  
- Investigate network policies blocking traffic

## 21. **Volume Mount Succeeds but File Missing**
**Q:** A pod starts, but mounted ConfigMap file is not found. Why?  
**A:**  
- Mount path mismatch  
- Key may not match file reference  
- Confirm pod spec and ConfigMap contents

## 22. **Unauthorized Access to Kubernetes Dashboard**
**Q:** Someone accessed the dashboard without RBAC. How?  
**A:**  
- Dashboard runs with cluster-admin by default in some setups  
- Check roleBindings and service account token exposure  
- Restrict access via Ingress and OAuth

## 23. **Job Stuck in Active State**
**Q:** A batch job remains active indefinitely. How to resolve?  
**A:**  
- Look for `backoffLimit` exceeded  
- Validate exit code and logs  
- Check if the pod is waiting on a nonexistent input or stuck loop

## 24. **Pod Scheduling Delay in Large Cluster**
**Q:** Pod scheduling takes unusually long. What could be reasons?  
**A:**  
- High API server or scheduler load  
- Many pending pods competing for resources  
- Use metrics-server or Prometheus to monitor bottlenecks

## 25. **RBAC Rule Misconfiguration**
**Q:** A developer can't access secrets despite being in the right group. What’s missing?  
**A:**  
- Validate role and roleBinding exist in the correct namespace  
- Check if ClusterRole is needed instead of Role  
- Use `kubectl auth can-i` to simulate access

## 26. **CoreDNS High CPU Consumption**
**Q:** CoreDNS pods consume high CPU. How to tune it?  
**A:**  
- Review DNS request volume using metrics  
- Enable cache and limit log level  
- Validate readiness probes of applications making excessive DNS calls

## 27. **Failed to Mount Secret Volume**
**Q:** Secret volume fails to mount. What to inspect?  
**A:**  
- Secret key may be missing or malformed  
- Check for typo in secret name or projection key  
- Ensure pod’s service account has access

## 28. **Cluster Autoscaler Doesn’t Scale Up**
**Q:** Workloads are pending, but autoscaler doesn’t provision nodes. Why?  
**A:**  
- Constraints like nodeAffinity or taints prevent scheduling  
- Node group lacks capacity or scaling limits hit  
- Check autoscaler logs for reasons

## 29. **Etcd Disk Full and Cluster Crash**
**Q:** Etcd ran out of disk. What recovery steps do you take?  
**A:**  
- Free up space immediately  
- Compact etcd database using `etcdctl`  
- Tune retention settings (`--auto-compaction-retention`)

## 30. **API Server Becomes Unresponsive**
**Q:** The Kubernetes API server becomes unresponsive. What’s your response plan?  
**A:**  
- Check control plane node metrics and disk pressure  
- Review etcd health and connectivity  
- Investigate log volume flood or RBAC loop
