// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.K8s
{
    /// <summary>
    /// Manages a **Managed Kubernetes Node Pool**, part of a managed Kubernetes cluster on IonosCloud.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Ionoscloud.Pulumi.Ionoscloud;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var example = new Ionoscloud.Compute.Datacenter("example", new()
    ///     {
    ///         Name = "Datacenter Example",
    ///         Location = "us/las",
    ///         Description = "datacenter description",
    ///         SecAuthProtection = false,
    ///     });
    /// 
    ///     var exampleLan = new Ionoscloud.Compute.Lan("example", new()
    ///     {
    ///         DatacenterId = example.Id,
    ///         Public = false,
    ///         Name = "Lan Example",
    ///     });
    /// 
    ///     var exampleIPBlock = new Ionoscloud.Compute.IPBlock("example", new()
    ///     {
    ///         Location = "us/las",
    ///         Size = 3,
    ///         Name = "IP Block Example",
    ///     });
    /// 
    ///     var exampleCluster = new Ionoscloud.K8s.Cluster("example", new()
    ///     {
    ///         Name = "k8sClusterExample",
    ///         K8sVersion = "1.31.2",
    ///         MaintenanceWindow = new Ionoscloud.K8s.Inputs.ClusterMaintenanceWindowArgs
    ///         {
    ///             DayOfTheWeek = "Sunday",
    ///             Time = "09:00:00Z",
    ///         },
    ///         ApiSubnetAllowLists = new[]
    ///         {
    ///             "1.2.3.4/32",
    ///         },
    ///         S3Buckets = new[]
    ///         {
    ///             new Ionoscloud.K8s.Inputs.ClusterS3BucketArgs
    ///             {
    ///                 Name = "globally_unique_s3_bucket_name",
    ///             },
    ///         },
    ///     });
    /// 
    ///     var exampleNodePool = new Ionoscloud.K8s.NodePool("example", new()
    ///     {
    ///         DatacenterId = example.Id,
    ///         K8sClusterId = exampleCluster.Id,
    ///         Name = "k8sNodePoolExample",
    ///         K8sVersion = exampleCluster.K8sVersion,
    ///         MaintenanceWindow = new Ionoscloud.K8s.Inputs.NodePoolMaintenanceWindowArgs
    ///         {
    ///             DayOfTheWeek = "Monday",
    ///             Time = "09:00:00Z",
    ///         },
    ///         AutoScaling = new Ionoscloud.K8s.Inputs.NodePoolAutoScalingArgs
    ///         {
    ///             MinNodeCount = 1,
    ///             MaxNodeCount = 2,
    ///         },
    ///         CpuFamily = "INTEL_XEON",
    ///         AvailabilityZone = "AUTO",
    ///         StorageType = "SSD",
    ///         NodeCount = 1,
    ///         CoresCount = 2,
    ///         RamSize = 2048,
    ///         StorageSize = 40,
    ///         PublicIps = new[]
    ///         {
    ///             exampleIPBlock.Ips.Apply(ips =&gt; ips[0]),
    ///             exampleIPBlock.Ips.Apply(ips =&gt; ips[1]),
    ///             exampleIPBlock.Ips.Apply(ips =&gt; ips[2]),
    ///         },
    ///         Lans = new[]
    ///         {
    ///             new Ionoscloud.K8s.Inputs.NodePoolLanArgs
    ///             {
    ///                 Id = exampleLan.Id,
    ///                 Dhcp = true,
    ///                 Routes = new[]
    ///                 {
    ///                     new Ionoscloud.K8s.Inputs.NodePoolLanRouteArgs
    ///                     {
    ///                         Network = "1.2.3.5/24",
    ///                         GatewayIp = "10.1.5.17",
    ///                     },
    ///                 },
    ///             },
    ///         },
    ///         Labels = 
    ///         {
    ///             { "lab1", "value1" },
    ///             { "lab2", "value2" },
    ///         },
    ///         Annotations = 
    ///         {
    ///             { "ann1", "value1" },
    ///             { "ann2", "value2" },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// **Note:** Set `create_before_destroy` on the lan resource if you want to remove it from the nodepool during an update. This is to ensure that the nodepool is updated before the lan is destroyed.
    /// 
    /// ## Import
    /// 
    /// A Kubernetes Node Pool resource can be imported using its Kubernetes cluster's uuid as well as its own UUID, both of which you can retrieve from the cloud API: `resource id`, e.g.:
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:k8s/nodePool:NodePool demo k8s_cluster_uuid/k8s_nodepool_id
    /// ```
    /// 
    /// This can be helpful when you want to import kubernetes node pools which you have already created manually or using other means, outside of pulumi, towards the goal of managing them via Pulumi
    /// 
    /// ⚠️ **_Warning: **During a maintenance window, k8s can update your `k8s_version` if the old one reaches end of life. This upgrade will not be shown in the plan, as we prevent
    /// 
    /// pulumi from doing a downgrade, as downgrading `k8s_version` is not supported._**
    /// 
    /// ⚠️ **_Warning: **If you are upgrading from v5.x.x to v6.x.x**: You have to modify you plan for lans to match the new structure, by putting the ids from the old slice in lans.id fields. This is not backwards compatible._**
    /// </summary>
    [IonoscloudResourceType("ionoscloud:k8s/nodePool:NodePool")]
    public partial class NodePool : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [bool] When set to true, allows the update of immutable fields by first destroying and then re-creating the node pool.
        /// 
        /// ⚠️ **_Warning: `allow_replace` - lets you update immutable fields, but it first destroys and then re-creates the node pool in order to do it. Set the field to true only if you know what you are doing.
        /// This will cause a downtime for all pods on that nodepool. Consider adding multiple nodepools and update one after the other for downtime free nodepool upgrade._**
        /// 
        /// Immutable fields list: name, cpu_family, availability_zone, cores_count, ram_size, storage_size, storage_type.
        /// 
        /// ⚠️ **Note**:
        /// 
        /// Be careful when using `auto_scaling` since the number of nodes can change. Because of that, when running
        /// `pulumi preview`, An update will be considered required (since `node_count` from the `tf` plan will be different
        /// from the number of nodes set by the scheduler). To avoid that, you can use `ignore_changes`.
        /// This will also ignore the manual changes for `node_count` made in the `tf` plan.
        /// You can read more details about the `ignore_changes` attribute here.
        /// </summary>
        [Output("allowReplace")]
        public Output<bool?> AllowReplace { get; private set; } = null!;

        /// <summary>
        /// [map] A key/value map of annotations
        /// </summary>
        [Output("annotations")]
        public Output<ImmutableDictionary<string, string>?> Annotations { get; private set; } = null!;

        /// <summary>
        /// [string] Whether the Node Pool should autoscale. For more details, please check the API documentation
        /// </summary>
        [Output("autoScaling")]
        public Output<Outputs.NodePoolAutoScaling?> AutoScaling { get; private set; } = null!;

        /// <summary>
        /// [string] - The desired Compute availability zone - See the API documentation for more information. *This attribute is immutable*.
        /// </summary>
        [Output("availabilityZone")]
        public Output<string> AvailabilityZone { get; private set; } = null!;

        /// <summary>
        /// [int] - The CPU cores count for each node of the node pool. *This attribute is immutable*.
        /// </summary>
        [Output("coresCount")]
        public Output<int> CoresCount { get; private set; } = null!;

        /// <summary>
        /// [string] The desired CPU Family - See the API documentation for more information. *This attribute is immutable*.
        /// </summary>
        [Output("cpuFamily")]
        public Output<string> CpuFamily { get; private set; } = null!;

        /// <summary>
        /// [string] A Datacenter's UUID
        /// </summary>
        [Output("datacenterId")]
        public Output<string> DatacenterId { get; private set; } = null!;

        /// <summary>
        /// [string] A k8s cluster's UUID
        /// </summary>
        [Output("k8sClusterId")]
        public Output<string> K8sClusterId { get; private set; } = null!;

        /// <summary>
        /// [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
        /// </summary>
        [Output("k8sVersion")]
        public Output<string> K8sVersion { get; private set; } = null!;

        /// <summary>
        /// [map] A key/value map of labels
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        /// <summary>
        /// [list] A list of numeric LAN id's you want this node pool to be part of. For more details, please check the API documentation, as well as the example above
        /// </summary>
        [Output("lans")]
        public Output<ImmutableArray<Outputs.NodePoolLan>> Lans { get; private set; } = null!;

        /// <summary>
        /// See the **maintenance_window** section in the example above
        /// </summary>
        [Output("maintenanceWindow")]
        public Output<Outputs.NodePoolMaintenanceWindow> MaintenanceWindow { get; private set; } = null!;

        /// <summary>
        /// [string] The name of the Kubernetes Cluster. *This attribute is immutable*.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [int] - The desired number of nodes in the node pool
        /// </summary>
        [Output("nodeCount")]
        public Output<int> NodeCount { get; private set; } = null!;

        /// <summary>
        /// [list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements
        /// </summary>
        [Output("publicIps")]
        public Output<ImmutableArray<string>> PublicIps { get; private set; } = null!;

        /// <summary>
        /// [int] - The desired amount of RAM, in MB. *This attribute is immutable*.
        /// </summary>
        [Output("ramSize")]
        public Output<int> RamSize { get; private set; } = null!;

        /// <summary>
        /// [int] - The size of the volume in GB. The size should be greater than 10GB. *This attribute is immutable*.
        /// </summary>
        [Output("storageSize")]
        public Output<int> StorageSize { get; private set; } = null!;

        /// <summary>
        /// [string] - The desired storage type - SSD/HDD. *This attribute is immutable*.
        /// </summary>
        [Output("storageType")]
        public Output<string> StorageType { get; private set; } = null!;


        /// <summary>
        /// Create a NodePool resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NodePool(string name, NodePoolArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:k8s/nodePool:NodePool", name, args ?? new NodePoolArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NodePool(string name, Input<string> id, NodePoolState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:k8s/nodePool:NodePool", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing NodePool resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NodePool Get(string name, Input<string> id, NodePoolState? state = null, CustomResourceOptions? options = null)
        {
            return new NodePool(name, id, state, options);
        }
    }

    public sealed class NodePoolArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [bool] When set to true, allows the update of immutable fields by first destroying and then re-creating the node pool.
        /// 
        /// ⚠️ **_Warning: `allow_replace` - lets you update immutable fields, but it first destroys and then re-creates the node pool in order to do it. Set the field to true only if you know what you are doing.
        /// This will cause a downtime for all pods on that nodepool. Consider adding multiple nodepools and update one after the other for downtime free nodepool upgrade._**
        /// 
        /// Immutable fields list: name, cpu_family, availability_zone, cores_count, ram_size, storage_size, storage_type.
        /// 
        /// ⚠️ **Note**:
        /// 
        /// Be careful when using `auto_scaling` since the number of nodes can change. Because of that, when running
        /// `pulumi preview`, An update will be considered required (since `node_count` from the `tf` plan will be different
        /// from the number of nodes set by the scheduler). To avoid that, you can use `ignore_changes`.
        /// This will also ignore the manual changes for `node_count` made in the `tf` plan.
        /// You can read more details about the `ignore_changes` attribute here.
        /// </summary>
        [Input("allowReplace")]
        public Input<bool>? AllowReplace { get; set; }

        [Input("annotations")]
        private InputMap<string>? _annotations;

        /// <summary>
        /// [map] A key/value map of annotations
        /// </summary>
        public InputMap<string> Annotations
        {
            get => _annotations ?? (_annotations = new InputMap<string>());
            set => _annotations = value;
        }

        /// <summary>
        /// [string] Whether the Node Pool should autoscale. For more details, please check the API documentation
        /// </summary>
        [Input("autoScaling")]
        public Input<Inputs.NodePoolAutoScalingArgs>? AutoScaling { get; set; }

        /// <summary>
        /// [string] - The desired Compute availability zone - See the API documentation for more information. *This attribute is immutable*.
        /// </summary>
        [Input("availabilityZone", required: true)]
        public Input<string> AvailabilityZone { get; set; } = null!;

        /// <summary>
        /// [int] - The CPU cores count for each node of the node pool. *This attribute is immutable*.
        /// </summary>
        [Input("coresCount", required: true)]
        public Input<int> CoresCount { get; set; } = null!;

        /// <summary>
        /// [string] The desired CPU Family - See the API documentation for more information. *This attribute is immutable*.
        /// </summary>
        [Input("cpuFamily", required: true)]
        public Input<string> CpuFamily { get; set; } = null!;

        /// <summary>
        /// [string] A Datacenter's UUID
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// [string] A k8s cluster's UUID
        /// </summary>
        [Input("k8sClusterId", required: true)]
        public Input<string> K8sClusterId { get; set; } = null!;

        /// <summary>
        /// [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
        /// </summary>
        [Input("k8sVersion", required: true)]
        public Input<string> K8sVersion { get; set; } = null!;

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// [map] A key/value map of labels
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("lans")]
        private InputList<Inputs.NodePoolLanArgs>? _lans;

        /// <summary>
        /// [list] A list of numeric LAN id's you want this node pool to be part of. For more details, please check the API documentation, as well as the example above
        /// </summary>
        public InputList<Inputs.NodePoolLanArgs> Lans
        {
            get => _lans ?? (_lans = new InputList<Inputs.NodePoolLanArgs>());
            set => _lans = value;
        }

        /// <summary>
        /// See the **maintenance_window** section in the example above
        /// </summary>
        [Input("maintenanceWindow")]
        public Input<Inputs.NodePoolMaintenanceWindowArgs>? MaintenanceWindow { get; set; }

        /// <summary>
        /// [string] The name of the Kubernetes Cluster. *This attribute is immutable*.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [int] - The desired number of nodes in the node pool
        /// </summary>
        [Input("nodeCount", required: true)]
        public Input<int> NodeCount { get; set; } = null!;

        [Input("publicIps")]
        private InputList<string>? _publicIps;

        /// <summary>
        /// [list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements
        /// </summary>
        public InputList<string> PublicIps
        {
            get => _publicIps ?? (_publicIps = new InputList<string>());
            set => _publicIps = value;
        }

        /// <summary>
        /// [int] - The desired amount of RAM, in MB. *This attribute is immutable*.
        /// </summary>
        [Input("ramSize", required: true)]
        public Input<int> RamSize { get; set; } = null!;

        /// <summary>
        /// [int] - The size of the volume in GB. The size should be greater than 10GB. *This attribute is immutable*.
        /// </summary>
        [Input("storageSize", required: true)]
        public Input<int> StorageSize { get; set; } = null!;

        /// <summary>
        /// [string] - The desired storage type - SSD/HDD. *This attribute is immutable*.
        /// </summary>
        [Input("storageType", required: true)]
        public Input<string> StorageType { get; set; } = null!;

        public NodePoolArgs()
        {
        }
        public static new NodePoolArgs Empty => new NodePoolArgs();
    }

    public sealed class NodePoolState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [bool] When set to true, allows the update of immutable fields by first destroying and then re-creating the node pool.
        /// 
        /// ⚠️ **_Warning: `allow_replace` - lets you update immutable fields, but it first destroys and then re-creates the node pool in order to do it. Set the field to true only if you know what you are doing.
        /// This will cause a downtime for all pods on that nodepool. Consider adding multiple nodepools and update one after the other for downtime free nodepool upgrade._**
        /// 
        /// Immutable fields list: name, cpu_family, availability_zone, cores_count, ram_size, storage_size, storage_type.
        /// 
        /// ⚠️ **Note**:
        /// 
        /// Be careful when using `auto_scaling` since the number of nodes can change. Because of that, when running
        /// `pulumi preview`, An update will be considered required (since `node_count` from the `tf` plan will be different
        /// from the number of nodes set by the scheduler). To avoid that, you can use `ignore_changes`.
        /// This will also ignore the manual changes for `node_count` made in the `tf` plan.
        /// You can read more details about the `ignore_changes` attribute here.
        /// </summary>
        [Input("allowReplace")]
        public Input<bool>? AllowReplace { get; set; }

        [Input("annotations")]
        private InputMap<string>? _annotations;

        /// <summary>
        /// [map] A key/value map of annotations
        /// </summary>
        public InputMap<string> Annotations
        {
            get => _annotations ?? (_annotations = new InputMap<string>());
            set => _annotations = value;
        }

        /// <summary>
        /// [string] Whether the Node Pool should autoscale. For more details, please check the API documentation
        /// </summary>
        [Input("autoScaling")]
        public Input<Inputs.NodePoolAutoScalingGetArgs>? AutoScaling { get; set; }

        /// <summary>
        /// [string] - The desired Compute availability zone - See the API documentation for more information. *This attribute is immutable*.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// [int] - The CPU cores count for each node of the node pool. *This attribute is immutable*.
        /// </summary>
        [Input("coresCount")]
        public Input<int>? CoresCount { get; set; }

        /// <summary>
        /// [string] The desired CPU Family - See the API documentation for more information. *This attribute is immutable*.
        /// </summary>
        [Input("cpuFamily")]
        public Input<string>? CpuFamily { get; set; }

        /// <summary>
        /// [string] A Datacenter's UUID
        /// </summary>
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        /// <summary>
        /// [string] A k8s cluster's UUID
        /// </summary>
        [Input("k8sClusterId")]
        public Input<string>? K8sClusterId { get; set; }

        /// <summary>
        /// [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
        /// </summary>
        [Input("k8sVersion")]
        public Input<string>? K8sVersion { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// [map] A key/value map of labels
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("lans")]
        private InputList<Inputs.NodePoolLanGetArgs>? _lans;

        /// <summary>
        /// [list] A list of numeric LAN id's you want this node pool to be part of. For more details, please check the API documentation, as well as the example above
        /// </summary>
        public InputList<Inputs.NodePoolLanGetArgs> Lans
        {
            get => _lans ?? (_lans = new InputList<Inputs.NodePoolLanGetArgs>());
            set => _lans = value;
        }

        /// <summary>
        /// See the **maintenance_window** section in the example above
        /// </summary>
        [Input("maintenanceWindow")]
        public Input<Inputs.NodePoolMaintenanceWindowGetArgs>? MaintenanceWindow { get; set; }

        /// <summary>
        /// [string] The name of the Kubernetes Cluster. *This attribute is immutable*.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [int] - The desired number of nodes in the node pool
        /// </summary>
        [Input("nodeCount")]
        public Input<int>? NodeCount { get; set; }

        [Input("publicIps")]
        private InputList<string>? _publicIps;

        /// <summary>
        /// [list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements
        /// </summary>
        public InputList<string> PublicIps
        {
            get => _publicIps ?? (_publicIps = new InputList<string>());
            set => _publicIps = value;
        }

        /// <summary>
        /// [int] - The desired amount of RAM, in MB. *This attribute is immutable*.
        /// </summary>
        [Input("ramSize")]
        public Input<int>? RamSize { get; set; }

        /// <summary>
        /// [int] - The size of the volume in GB. The size should be greater than 10GB. *This attribute is immutable*.
        /// </summary>
        [Input("storageSize")]
        public Input<int>? StorageSize { get; set; }

        /// <summary>
        /// [string] - The desired storage type - SSD/HDD. *This attribute is immutable*.
        /// </summary>
        [Input("storageType")]
        public Input<string>? StorageType { get; set; }

        public NodePoolState()
        {
        }
        public static new NodePoolState Empty => new NodePoolState();
    }
}
