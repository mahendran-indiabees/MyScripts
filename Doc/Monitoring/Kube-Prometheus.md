## What is Robusta

* Robusta is an open source observability tool for Kubernetes, which extends Prometheus
  
* It’s a full-fledged observability platform designed specifically for Kubernetes.
  
* It seamlessly integrates with Prometheus, automatically fetching data to investigate alerts and attaching it directly to them

## Architecture

![image](https://github.com/user-attachments/assets/fe9e5588-2e25-4a30-952a-1cf22d0cb21a)


## Key Features of Robusta

* **Notifications for Rollouts and Changes:** It will informed about deployments and changes with automated notifications.
  
* **Alert Routing:** Route alerts based on namespace, team, and severity to ensure the right people are notified at the right time
  
* **K8s Problem-Detection:** alert on OOMKills or failing Jobs without PromQL
  
* **Automated Data Fetching:** Robusta automatically fetches relevant data for investigations, saving you time and effort. So no more manually scraping logs or metrics!
  
* **AI Investigation:** - we can integrate with chat GPT for solutions



## How Robusta works

* In Robusta, rules are called playbooks. Every playbook consists of a trigger (e.g. a Crashing Pod, a Prometheus Alert, or some other condition) and one or more actions.
  
* Actions can enrich alerts, silence them, or remediate problems.

#### Robusta does three things:

* Robusta monitors Kubernetes events, Prometheus alerts, and other sources to stay informed about your cluster's current state.

* When important /noteworthy events occur, Robusta actively gathers and correlates information such as logs, graphs, and thread dumps. All according to the playbooks defined in Robusta.

* Sends notifications: Based on your preferences, Robusta notifies in sinks like Slack, MSTeams, and PagerDuty

## Major components in Robusta:

* **Robusta-forwarder** uses a Kubewatch image to monitor changes on your Kubernetes cluster using API server. It sends all the API server events to Robusta-runner.
  
* **Robusta-runner** checks if there’s any playbook that should be triggered by that event. Whether to take an action on an event, is configured via playbooks

## Prerequisites of Installation:

* A Supported K8s Cluster (All Distributions are supported except Minikube)
  
* Helm
  
* A sink (Slack, Teams etc for alerts)

## Installation steps

#### Install Robusta cli for generate helm values & config

```
pip install -U robusta-cli --no-cache
```

#### Run generate config command 

```
robusta gen-config --enable-prometheus-stack
```

###### (InCase) For Existing Prometheues

```
robusta gen-config --no-enable-prometheus-stack
```
* Above command will prompt the terminal. This interactive process asks you various questions about your desired setup, including cluster name, email & sink (Teams, slack). 
* After provide all info, It will create generated_values.yaml file in current directory
* This generated_values.yaml file contains sensitive values. We can manage these Secrets with K8s secret.

#### Add the Robusta Helm Repository

```
helm repo add robusta https://robusta-charts.storage.googleapis.com && helm repo update
helm install robusta robusta/robusta -f ./generated_values.yaml --set clusterName=<YOUR_CLUSTER_NAME>
```

#### Confirm that two Robusta pods are running with no errors in the logs:
```
kubectl get pods -A | grep robusta
robusta logs
```


#### Ensure robusta setup is working or not using deploying crashing pod
```
kubectl apply -f https://gist.githubusercontent.com/robusta-lab/283609047306dc1f05cf59806ade30b6/raw
kubectl get pods -A | grep crashpod
```

#### Robusta UI Dashboard
![image](https://github.com/user-attachments/assets/17e25af3-3a6e-4e1d-bafb-737aa76bb99f)

#### Cleanup crashing pod

```
kubectl delete deployment crashpod
```
