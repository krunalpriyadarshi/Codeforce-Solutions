# Cloud computing

## Hosting Types Comparison

| Feature         | Shared Hosting | VPS        | Dedicated Server | Cloud Hosting |
|-----------------|----------------|------------|------------------|---------------|
| Physical server | Shared         | Shared     | Single tenant    | Pooled        |
| OS isolation    | ❌ No          | ✅ Yes     | ✅ Yes           | ✅ Yes        |
| Root access     | ❌ No          | ✅ Yes     | ✅ Yes           | ✅ Yes        |
| Scalability     | ❌ No          | ⚠️ Limited | ❌ No            | ✅ Yes        |
| Auto scaling    | ❌ No          | ❌ No      | ❌ No            | ✅ Yes        |
| Fault tolerance | ❌ No          | ❌ No      | ❌ No            | ✅ Yes        |
| Cost            | Very low       | Low        | High             | Variable      |
| Maintenance     | Provider       | You        | You              | Mostly provider |
| Performance     | Low            | Medium     | High             | Variable      |
| Compliance      | ❌ No          | ⚠️ Partial | ✅ Yes           | ✅ Yes        |

### Dedicated Hosting

- A physical server that is being used by a single client or an application.
  - Companies who wants High performance, and low-stable latency prefers `Dedicated hosting` like Gaming, Trading, and High Data processing companies. Also, Government, HealthCare, and Banking prefer this server since it provides full control, security and compliance.
  - Disadantages:
    - Expensive  
    - No auto-scaling since it is one fixed machine. Hence, performance of application is impacted when number of requests are increased by a lot.
    - Less fault tolerence. Hardware, disk or CPU fault affect whole system.
    - Less portability: To create new instance, it requires new machine, resources and manual efforts for setup.
    - Engineers need to setup CPU+RAM, If overestimated --> Charge more else underestimated --> Performance issue.

### VPS (Virtual Private Server)

- A virtual machine created by dividing one physical server into multiple isolated virtual servers using Virtulization.

  - An Individual business is using this type of hosting because it is more cost effective and easy to manage than Dedicated hosting server. Additionally, It provides isolation and security through Virtualization.
  - Disadvantages:

    - Still shared Hardware result in `noisy neighbour problem`. Sudden traffic to an app will affect performance of other apps.
    - Limited scaling, fixed resources, and no support for auo-scaling.
    - Single point of failure means all apps are affected if main server is down.

### Shared Hosting

- A single physical machine shared by multiple hosts to host multiple applications.

  - Individuals and small businesses, who have limited budgets to host portfolios or websites. Additionally, Maintability of server is taken care by Hosts hence it requires less maintanence.
  - Disadvantages:

    - Poor performance. (Noisy neighbour problem exist)
    - No control. Can't install new softwares to virtual machine.
    - Security risk and weak isolation
    - Not scalable

### Cloud Hosting

- Multiple physical servers creates one server to maintain and host multiple application.

  - Industries, Enterprise, and startups prefers because it provides High availablility, elastic scaling, Pay-as-you-go service, and multiple cloud native services like load balancer, monitoring, logging etc.
  - Disadvantages:

    - High Complexity
    - Cost can grow rapidly
    - Less physical control

## Scaling

- Scaling is the process of adjusting resources (RAM, ROM, CPU, Storage) to handle system workload.

  - Scale up = Increasing resources when workload increased
  - Scale down = Decreasing resources when workload decreased

### Vertical scaling (Scale up)

- Make existing server more powerful by adding more resources (RAM, ROM, CPU, Storage).

  - ```text
    Before Scaling:  Server → handles 1,000 users
    After Scaling:   Server → handles 2,000 users
    ```

- Simple to implement. No code change needed.
- Disadvantages:

  - Has limit to add resources (Can't add RAM forever) and expensive.
  - Single point of failure (System dies then everything dies)
  - Downtime expected during scaling.

### Horizontal scaling (Scale out)

- Adding more servers instead of upgrading current one.

  - ```text
    Before Scaling:  1 server  → handles 1,000 users
    After Scaling:   5 servers → handles 5,000 users
    ```

- Complex architecture to implement but It is more cost effective, no downtime expected and no single point of failure.

- Disadvantages:

  - Complex architecture (Need load balancer) and planning needed.

## Auto-scaling

- Auto-scaling only performs Horizontal scaling (Scale out) approach. More practical in daily life since traffic is highly volitile.

- Set of rules are created to add more servers and to remove newly added servers.

- Advantages:

  - Cost effective
  - High availability and Fault tolerance (if one server dies, it adds one more to handle traffic automatically)
  - Better performance
  - No manual monitoring requries

- Disadvantages:

  - Complex to implement
  - Configuration overhead
  - Hard to debug while unexpected prodution issue rises
  - Not applicable for all application (like local storage systems, database and log-running batch jobs). It is useful for web servers and APIs.
