// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Dsaas
{
    public static class GetNodePool
    {
        /// <summary>
        /// The **Dataplatform Node Pool Data Source** can be used to search for and return an existing Dataplatform Node Pool under a Dataplatform Cluster.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dsaas.GetNodePool.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Id = "node_pool_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dsaas.GetNodePool.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Name = "Dataplatform_Node_Pool_Example",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name with Partial Match
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dsaas.GetNodePool.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Name = "_Example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetNodePoolResult> InvokeAsync(GetNodePoolArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetNodePoolResult>("ionoscloud:dsaas/getNodePool:getNodePool", args ?? new GetNodePoolArgs(), options.WithDefaults());

        /// <summary>
        /// The **Dataplatform Node Pool Data Source** can be used to search for and return an existing Dataplatform Node Pool under a Dataplatform Cluster.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dsaas.GetNodePool.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Id = "node_pool_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dsaas.GetNodePool.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Name = "Dataplatform_Node_Pool_Example",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name with Partial Match
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dsaas.GetNodePool.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Name = "_Example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetNodePoolResult> Invoke(GetNodePoolInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetNodePoolResult>("ionoscloud:dsaas/getNodePool:getNodePool", args ?? new GetNodePoolInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **Dataplatform Node Pool Data Source** can be used to search for and return an existing Dataplatform Node Pool under a Dataplatform Cluster.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dsaas.GetNodePool.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Id = "node_pool_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dsaas.GetNodePool.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Name = "Dataplatform_Node_Pool_Example",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name with Partial Match
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dsaas.GetNodePool.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Name = "_Example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetNodePoolResult> Invoke(GetNodePoolInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetNodePoolResult>("ionoscloud:dsaas/getNodePool:getNodePool", args ?? new GetNodePoolInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNodePoolArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the cluster the searched node pool is part of.
        /// </summary>
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        /// <summary>
        /// ID of the node pool you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// Whether partial matching is allowed or not when using name argument. Default value is false.
        /// 
        /// Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("partialMatch")]
        public bool? PartialMatch { get; set; }

        public GetNodePoolArgs()
        {
        }
        public static new GetNodePoolArgs Empty => new GetNodePoolArgs();
    }

    public sealed class GetNodePoolInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the cluster the searched node pool is part of.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// ID of the node pool you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Whether partial matching is allowed or not when using name argument. Default value is false.
        /// 
        /// Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("partialMatch")]
        public Input<bool>? PartialMatch { get; set; }

        public GetNodePoolInvokeArgs()
        {
        }
        public static new GetNodePoolInvokeArgs Empty => new GetNodePoolInvokeArgs();
    }


    [OutputType]
    public sealed class GetNodePoolResult
    {
        /// <summary>
        /// Key-value pairs attached to node pool resource as [Kubernetes annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).
        /// </summary>
        public readonly ImmutableDictionary<string, string> Annotations;
        /// <summary>
        /// Whether the Node Pool should autoscale. For more details, please check the API documentation
        /// </summary>
        public readonly ImmutableArray<Outputs.GetNodePoolAutoScalingResult> AutoScalings;
        /// <summary>
        /// The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
        /// </summary>
        public readonly string AvailabilityZone;
        /// <summary>
        /// ID of the cluster the searched node pool is part of.
        /// </summary>
        public readonly string ClusterId;
        /// <summary>
        /// The number of CPU cores per node.
        /// </summary>
        public readonly int CoresCount;
        /// <summary>
        /// A CPU family.
        /// </summary>
        public readonly string CpuFamily;
        /// <summary>
        /// The UUID of the virtual data center (VDC) the cluster is provisioned.
        /// </summary>
        public readonly string DatacenterId;
        /// <summary>
        /// ID of your node pool.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Key-value pairs attached to the node pool resource as [Kubernetes labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).
        /// </summary>
        public readonly ImmutableDictionary<string, string> Labels;
        /// <summary>
        /// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        /// </summary>
        public readonly ImmutableArray<Outputs.GetNodePoolMaintenanceWindowResult> MaintenanceWindows;
        /// <summary>
        /// The name of your node pool
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The number of nodes that make up the node pool.
        /// </summary>
        public readonly int NodeCount;
        public readonly bool? PartialMatch;
        /// <summary>
        /// The RAM size for one node in MB.
        /// </summary>
        public readonly int RamSize;
        /// <summary>
        /// The size of the volume in GB.
        /// </summary>
        public readonly int StorageSize;
        /// <summary>
        /// The type of hardware for the volume.
        /// </summary>
        public readonly string StorageType;
        /// <summary>
        /// The version of the Data Platform.
        /// </summary>
        public readonly string Version;

        [OutputConstructor]
        private GetNodePoolResult(
            ImmutableDictionary<string, string> annotations,

            ImmutableArray<Outputs.GetNodePoolAutoScalingResult> autoScalings,

            string availabilityZone,

            string clusterId,

            int coresCount,

            string cpuFamily,

            string datacenterId,

            string id,

            ImmutableDictionary<string, string> labels,

            ImmutableArray<Outputs.GetNodePoolMaintenanceWindowResult> maintenanceWindows,

            string name,

            int nodeCount,

            bool? partialMatch,

            int ramSize,

            int storageSize,

            string storageType,

            string version)
        {
            Annotations = annotations;
            AutoScalings = autoScalings;
            AvailabilityZone = availabilityZone;
            ClusterId = clusterId;
            CoresCount = coresCount;
            CpuFamily = cpuFamily;
            DatacenterId = datacenterId;
            Id = id;
            Labels = labels;
            MaintenanceWindows = maintenanceWindows;
            Name = name;
            NodeCount = nodeCount;
            PartialMatch = partialMatch;
            RamSize = ramSize;
            StorageSize = storageSize;
            StorageType = storageType;
            Version = version;
        }
    }
}
