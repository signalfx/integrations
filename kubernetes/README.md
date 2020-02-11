# ![](./img/integrations_kubernetes.png) Kubernetes


### USAGE


Use the Kubernetes integration to monitor the health and performance of your microservices, the Kubernetes orchestration services, and the infrastructure that they are running on.

- Explore the relationships between the various layers of your infrastructure with the Navigator
- Discover and automatically configure the monitoring of supported services running in the containers
- Use the built-in dashboards to view key metrics that are indicators of the health of your infrastructure and the orchestrator

#### Infrastructure Navigator

The Infrastructure Navigator gives you an immediate, at-a-glance view of your Kubernetes overall architecture as well as nodes and pods, colored by critical health metrics.The Infrastructure Navigator also provides visibility all the way through the stack as you drill down and across elements of your environment, reflecting the fact that the infrastructure, the orchestrator, the containers and the apps are all related layers, not just individual system components.

  [<img src='./img/Navigator.png' width=200px>](./img/Navigator.png)

#### Built-in Dashboards

SignalFx provides built-in dashboards for Kubernetes. Examples are shown below.

- **Kubernetes Overview**: This dashboard is populated by the metrics emitted from the ```kubernetes-cluster``` and ```kubelet-stats monitors```. Charts refer to the health of your Kubernetes nodes and pods. When filtered by Deployment or Service, charts will be filtered by the selected pods running on the nodes.

  [<img src='./img/Overview.png' width=200px>](./img/Overview.png)

- **Kubernetes Clusters**: Overview of multiple Kubernetes clusters.

  [<img src='./img/Clusters.png' width=200px>](./img/Clusters.png)

#### Learning More

After data is flowing, try the <a target="_blank" href="https://docs.signalfx.com/en/latest/integrations/kubernetes/k8s-built-in.html#k8s-built-in">Kubernetes Built-in Content tour</a> to get familiar with the ways to visualize data from your nodes, pods, and network in the Infrastructure tab and built-in dashboards.

### TROUBLESHOOTING

#### Where's My Data?

There may be possible errors on an agent container preventing data from streaming to the SignalFx web application.

Run the `signalfx-agent status` command inside any of the Smart Agent container(s) to get a diagnostic output from the Smart Agent to quickly see what services the Smart Agent has discovered.

```
while read -r line; do kubectl exec --namespace `echo $line` signalfx-agent status; done <<< `kubectl get pods -l app=signalfx-agent --all-namespaces --no-headers | tr -s " " | cut -d " " -f 1,2`
```

#### How Do I View the Smart Agent Logs?

Run this command to view the last 20 lines of Smart Agent logs from all agent pods running in the cluster.

```
while read -r line; do echo "\n`echo $line | cut -d " " -f 2`:" ; kubectl logs --namespace `echo $line` --tail 20 ; done <<< `kubectl get pods -l app=signalfx-agent --all-namespaces --no-headers | tr -s " " | cut -d " " -f 1,2`
```

#### The Smart Agent Cannot Authenicate to the Kubelet

If you see errors like the following, the Smart Agent cannot authenticate to the kubelet.

```
Couldn't get machine info: Kubelet request failed - "401 Unauthorized", response:"Unauthorized"
```

```
Couldn't get cAdvisor container stats" error="failed to get all container stats fromKubeletURL "https://localhost:10250/stats/container/": Kubelet request failed - "401Unauthorized", response: "Unauthorized"
```

If you have `ClusterRole` and `ClusterRoleBinding` properly applied to the Smart Agent container service account, then this could indicate that the kubelet doesn’t honor RBAC authentication. Instead, the kubelet will expose a separate endpoint on port 10255 that allows reading stats and metrics about the kubelet. You can configure the Smart Agent to read from this port by replacing the original `kubelet-stats` monitor config in <a target="_blank" href="https://github.com/signalfx/signalfx-agent/blob/master/deployments/k8s/configmap.yaml">configmap.yaml</a> with the following:

```
monitors:
  - type: kubelet-stats
    kubeletAPI:
      authType: none
      url: http://localhost:10255
```
