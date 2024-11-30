```
#!/bin/bash

# Header for the output
echo -e "Node\tTotal CPU Allocated\tCPU Usage\tRemaining CPU\tTotal Memory Allocated (GiB)\tMemory Usage (GiB)\tRemaining Memory (GiB)"

# Loop through all nodes in the cluster
for node in $(kubectl get nodes -o jsonpath='{.items[*].metadata.name}'); do
    # Get total CPU and Memory capacity
    total_cpu=$(kubectl get node $node -o jsonpath='{.status.capacity.cpu}')
    total_memory=$(kubectl get node $node -o jsonpath='{.status.capacity.memory}' | awk '{printf "%.2f", $1/1024/1024/1024}') # Convert Ki to GiB

    # Get CPU and Memory usage from kubectl top
    cpu_usage=$(kubectl top node $node | tail -n 1 | awk '{print $2}')
    memory_usage=$(kubectl top node $node | tail -n 1 | awk '{print $4}' | sed 's/Gi//')

    # Calculate remaining resources
    remaining_cpu=$(echo "$total_cpu - $cpu_usage" | bc)
    remaining_memory=$(echo "$total_memory - $memory_usage" | bc)

    # Output the results
    echo -e "$node\t$total_cpu cores\t$cpu_usage cores\t$remaining_cpu cores\t$total_memory GiB\t$memory_usage GiB\t$remaining_memory GiB"
done





```
