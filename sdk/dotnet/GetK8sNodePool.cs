// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetK8sNodePool
    {
        /// <summary>
        /// The **k8s Node Pool** data source can be used to search for and return existing k8s Node Pools.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Task<GetK8sNodePoolResult> InvokeAsync(GetK8sNodePoolArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetK8sNodePoolResult>("ionoscloud:index/getK8sNodePool:getK8sNodePool", args ?? new GetK8sNodePoolArgs(), options.WithDefaults());

        /// <summary>
        /// The **k8s Node Pool** data source can be used to search for and return existing k8s Node Pools.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Output<GetK8sNodePoolResult> Invoke(GetK8sNodePoolInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetK8sNodePoolResult>("ionoscloud:index/getK8sNodePool:getK8sNodePool", args ?? new GetK8sNodePoolInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetK8sNodePoolArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the node pool you want to search for.
        /// 
        /// `k8s_cluster_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// K8s Cluster' UUID
        /// </summary>
        [Input("k8sClusterId", required: true)]
        public string K8sClusterId { get; set; } = null!;

        /// <summary>
        /// Name of an existing node pool that you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetK8sNodePoolArgs()
        {
        }
        public static new GetK8sNodePoolArgs Empty => new GetK8sNodePoolArgs();
    }

    public sealed class GetK8sNodePoolInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the node pool you want to search for.
        /// 
        /// `k8s_cluster_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// K8s Cluster' UUID
        /// </summary>
        [Input("k8sClusterId", required: true)]
        public Input<string> K8sClusterId { get; set; } = null!;

        /// <summary>
        /// Name of an existing node pool that you want to search for.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetK8sNodePoolInvokeArgs()
        {
        }
        public static new GetK8sNodePoolInvokeArgs Empty => new GetK8sNodePoolInvokeArgs();
    }


    [OutputType]
    public sealed class GetK8sNodePoolResult
    {
        /// <summary>
        /// A map of annotations in the form of key &gt; value
        /// </summary>
        public readonly ImmutableDictionary<string, string> Annotations;
        /// <summary>
        /// The range defining the minimum and maximum number of worker nodes that the managed node group can scale in
        /// </summary>
        public readonly ImmutableArray<Outputs.GetK8sNodePoolAutoScalingResult> AutoScalings;
        /// <summary>
        /// The compute availability zone in which the nodes should exist
        /// </summary>
        public readonly string AvailabilityZone;
        /// <summary>
        /// A list of kubernetes versions available for upgrade
        /// </summary>
        public readonly ImmutableArray<string> AvailableUpgradeVersions;
        /// <summary>
        /// CPU cores count
        /// </summary>
        public readonly int CoresCount;
        /// <summary>
        /// CPU Family
        /// </summary>
        public readonly string CpuFamily;
        /// <summary>
        /// The UUID of the VDC
        /// </summary>
        public readonly string DatacenterId;
        /// <summary>
        /// The LAN ID of an existing LAN at the related datacenter
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// ID of the cluster this node pool is part of
        /// </summary>
        public readonly string K8sClusterId;
        /// <summary>
        /// The kubernetes version
        /// </summary>
        public readonly string K8sVersion;
        /// <summary>
        /// A map of labels in the form of key &gt; value
        /// </summary>
        public readonly ImmutableDictionary<string, string> Labels;
        /// <summary>
        /// A list of Local Area Networks the node pool is a part of
        /// </summary>
        public readonly ImmutableArray<Outputs.GetK8sNodePoolLanResult> Lans;
        /// <summary>
        /// A maintenance window comprise of a day of the week and a time for maintenance to be allowed
        /// </summary>
        public readonly ImmutableArray<Outputs.GetK8sNodePoolMaintenanceWindowResult> MaintenanceWindows;
        /// <summary>
        /// name of the node pool
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The number of nodes in this node pool
        /// </summary>
        public readonly int NodeCount;
        /// <summary>
        /// The list of fixed IPs associated with this node pool
        /// </summary>
        public readonly ImmutableArray<string> PublicIps;
        /// <summary>
        /// The amount of RAM in MB
        /// </summary>
        public readonly int RamSize;
        /// <summary>
        /// one of "AVAILABLE",
        /// "INACTIVE",
        /// "BUSY",
        /// "DEPLOYING",
        /// "ACTIVE",
        /// "FAILED",
        /// "SUSPENDED",
        /// "FAILED_SUSPENDED",
        /// "UPDATING",
        /// "FAILED_UPDATING",
        /// "DESTROYING",
        /// "FAILED_DESTROYING",
        /// "TERMINATED"
        /// </summary>
        public readonly string State;
        /// <summary>
        /// The size of the volume in GB. The size should be greater than 10GB.
        /// </summary>
        public readonly int StorageSize;
        /// <summary>
        /// HDD or SDD
        /// </summary>
        public readonly string StorageType;

        [OutputConstructor]
        private GetK8sNodePoolResult(
            ImmutableDictionary<string, string> annotations,

            ImmutableArray<Outputs.GetK8sNodePoolAutoScalingResult> autoScalings,

            string availabilityZone,

            ImmutableArray<string> availableUpgradeVersions,

            int coresCount,

            string cpuFamily,

            string datacenterId,

            string? id,

            string k8sClusterId,

            string k8sVersion,

            ImmutableDictionary<string, string> labels,

            ImmutableArray<Outputs.GetK8sNodePoolLanResult> lans,

            ImmutableArray<Outputs.GetK8sNodePoolMaintenanceWindowResult> maintenanceWindows,

            string? name,

            int nodeCount,

            ImmutableArray<string> publicIps,

            int ramSize,

            string state,

            int storageSize,

            string storageType)
        {
            Annotations = annotations;
            AutoScalings = autoScalings;
            AvailabilityZone = availabilityZone;
            AvailableUpgradeVersions = availableUpgradeVersions;
            CoresCount = coresCount;
            CpuFamily = cpuFamily;
            DatacenterId = datacenterId;
            Id = id;
            K8sClusterId = k8sClusterId;
            K8sVersion = k8sVersion;
            Labels = labels;
            Lans = lans;
            MaintenanceWindows = maintenanceWindows;
            Name = name;
            NodeCount = nodeCount;
            PublicIps = publicIps;
            RamSize = ramSize;
            State = state;
            StorageSize = storageSize;
            StorageType = storageType;
        }
    }
}
