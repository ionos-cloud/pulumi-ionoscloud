// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Dsaas
{
    /// <summary>
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Pulumi.Ionoscloud;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var example = new Ionoscloud.Compute.Datacenter("example", new()
    ///     {
    ///         Name = "Datacenter_Example",
    ///         Location = "de/txl",
    ///         Description = "Datacenter for testing Dataplatform Cluster",
    ///     });
    /// 
    ///     var exampleCluster = new Ionoscloud.Dsaas.Cluster("example", new()
    ///     {
    ///         DatacenterId = example.Id,
    ///         Name = "Dataplatform_Cluster_Example",
    ///         MaintenanceWindows = new[]
    ///         {
    ///             new Ionoscloud.Dsaas.Inputs.ClusterMaintenanceWindowArgs
    ///             {
    ///                 DayOfTheWeek = "Sunday",
    ///                 Time = "09:00:00",
    ///             },
    ///         },
    ///         Version = "23.7",
    ///     });
    /// 
    ///     var exampleNodePool = new Ionoscloud.Dsaas.NodePool("example", new()
    ///     {
    ///         ClusterId = exampleCluster.Id,
    ///         Name = "Dataplatform_Node_Pool_Example",
    ///         NodeCount = 1,
    ///         CpuFamily = "INTEL_SKYLAKE",
    ///         CoresCount = 1,
    ///         RamSize = 2048,
    ///         AvailabilityZone = "AUTO",
    ///         StorageType = "HDD",
    ///         StorageSize = 10,
    ///         MaintenanceWindows = new[]
    ///         {
    ///             new Ionoscloud.Dsaas.Inputs.NodePoolMaintenanceWindowArgs
    ///             {
    ///                 DayOfTheWeek = "Monday",
    ///                 Time = "09:00:00",
    ///             },
    ///         },
    ///         Labels = 
    ///         {
    ///             { "foo", "bar" },
    ///             { "color", "green" },
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
    /// 
    /// ## Import
    /// 
    /// A Dataplatform Node Pool resource can be imported using its cluster's UUID as well as its own UUID, e.g.:
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:dsaas/nodePool:NodePool mynodepool dataplatform_cluster_uuid/dataplatform_nodepool_id
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:dsaas/nodePool:NodePool")]
    public partial class NodePool : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [map] Key-value pairs attached to node pool resource as [Kubernetes annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).
        /// </summary>
        [Output("annotations")]
        public Output<ImmutableDictionary<string, string>?> Annotations { get; private set; } = null!;

        /// <summary>
        /// [string] Whether the Node Pool should autoscale. For more details, please check the API documentation
        /// </summary>
        [Output("autoScaling")]
        public Output<Outputs.NodePoolAutoScaling?> AutoScaling { get; private set; } = null!;

        /// <summary>
        /// [string] The availability zone of the virtual datacenter region where the node pool resources should be provisioned. Must be set with one of the values `AUTO`, `ZONE_1` or `ZONE_2`. The default value is `AUTO`.
        /// </summary>
        [Output("availabilityZone")]
        public Output<string> AvailabilityZone { get; private set; } = null!;

        /// <summary>
        /// [string] The UUID of an existing Dataplatform cluster.
        /// </summary>
        [Output("clusterId")]
        public Output<string> ClusterId { get; private set; } = null!;

        /// <summary>
        /// [int] The number of CPU cores per node. Must be set with a minimum value of 1. The default value is `4`.
        /// </summary>
        [Output("coresCount")]
        public Output<int> CoresCount { get; private set; } = null!;

        /// <summary>
        /// [string] A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can be retrieved from the datacenter resource. The default value is `AUTO`.
        /// </summary>
        [Output("cpuFamily")]
        public Output<string> CpuFamily { get; private set; } = null!;

        /// <summary>
        /// The UUID of the virtual data center (VDC) in which the nodepool is provisioned
        /// </summary>
        [Output("datacenterId")]
        public Output<string> DatacenterId { get; private set; } = null!;

        /// <summary>
        /// [map] Key-value pairs attached to the node pool resource as [Kubernetes labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        /// <summary>
        /// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        /// </summary>
        [Output("maintenanceWindows")]
        public Output<ImmutableArray<Outputs.NodePoolMaintenanceWindow>> MaintenanceWindows { get; private set; } = null!;

        /// <summary>
        /// [string] The name of your node pool. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [int] The number of nodes that make up the node pool. Must be set with a minimum value of 1.
        /// </summary>
        [Output("nodeCount")]
        public Output<int> NodeCount { get; private set; } = null!;

        /// <summary>
        /// [int] The RAM size for one node in MB. Must be set in multiples of `1024`MB, with a minimum size is of `2048`MB. The default value is `4096`.
        /// </summary>
        [Output("ramSize")]
        public Output<int> RamSize { get; private set; } = null!;

        /// <summary>
        /// [int] The size of the volume in GB. The size must be greater than `10`GB. The default value is `20`.
        /// </summary>
        [Output("storageSize")]
        public Output<int> StorageSize { get; private set; } = null!;

        /// <summary>
        /// [int] The type of hardware for the volume. Must be set with one of the values `HDD` or `SSD`. The default value is `SSD`.
        /// </summary>
        [Output("storageType")]
        public Output<string> StorageType { get; private set; } = null!;

        /// <summary>
        /// The version of the Data Platform.
        /// </summary>
        [Output("version")]
        public Output<string> Version { get; private set; } = null!;


        /// <summary>
        /// Create a NodePool resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NodePool(string name, NodePoolArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:dsaas/nodePool:NodePool", name, args ?? new NodePoolArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NodePool(string name, Input<string> id, NodePoolState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:dsaas/nodePool:NodePool", name, state, MakeResourceOptions(options, id))
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
        [Input("annotations")]
        private InputMap<string>? _annotations;

        /// <summary>
        /// [map] Key-value pairs attached to node pool resource as [Kubernetes annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).
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
        /// [string] The availability zone of the virtual datacenter region where the node pool resources should be provisioned. Must be set with one of the values `AUTO`, `ZONE_1` or `ZONE_2`. The default value is `AUTO`.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// [string] The UUID of an existing Dataplatform cluster.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// [int] The number of CPU cores per node. Must be set with a minimum value of 1. The default value is `4`.
        /// </summary>
        [Input("coresCount")]
        public Input<int>? CoresCount { get; set; }

        /// <summary>
        /// [string] A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can be retrieved from the datacenter resource. The default value is `AUTO`.
        /// </summary>
        [Input("cpuFamily")]
        public Input<string>? CpuFamily { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// [map] Key-value pairs attached to the node pool resource as [Kubernetes labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("maintenanceWindows")]
        private InputList<Inputs.NodePoolMaintenanceWindowArgs>? _maintenanceWindows;

        /// <summary>
        /// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        /// </summary>
        public InputList<Inputs.NodePoolMaintenanceWindowArgs> MaintenanceWindows
        {
            get => _maintenanceWindows ?? (_maintenanceWindows = new InputList<Inputs.NodePoolMaintenanceWindowArgs>());
            set => _maintenanceWindows = value;
        }

        /// <summary>
        /// [string] The name of your node pool. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [int] The number of nodes that make up the node pool. Must be set with a minimum value of 1.
        /// </summary>
        [Input("nodeCount", required: true)]
        public Input<int> NodeCount { get; set; } = null!;

        /// <summary>
        /// [int] The RAM size for one node in MB. Must be set in multiples of `1024`MB, with a minimum size is of `2048`MB. The default value is `4096`.
        /// </summary>
        [Input("ramSize")]
        public Input<int>? RamSize { get; set; }

        /// <summary>
        /// [int] The size of the volume in GB. The size must be greater than `10`GB. The default value is `20`.
        /// </summary>
        [Input("storageSize")]
        public Input<int>? StorageSize { get; set; }

        /// <summary>
        /// [int] The type of hardware for the volume. Must be set with one of the values `HDD` or `SSD`. The default value is `SSD`.
        /// </summary>
        [Input("storageType")]
        public Input<string>? StorageType { get; set; }

        public NodePoolArgs()
        {
        }
        public static new NodePoolArgs Empty => new NodePoolArgs();
    }

    public sealed class NodePoolState : global::Pulumi.ResourceArgs
    {
        [Input("annotations")]
        private InputMap<string>? _annotations;

        /// <summary>
        /// [map] Key-value pairs attached to node pool resource as [Kubernetes annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).
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
        /// [string] The availability zone of the virtual datacenter region where the node pool resources should be provisioned. Must be set with one of the values `AUTO`, `ZONE_1` or `ZONE_2`. The default value is `AUTO`.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// [string] The UUID of an existing Dataplatform cluster.
        /// </summary>
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        /// <summary>
        /// [int] The number of CPU cores per node. Must be set with a minimum value of 1. The default value is `4`.
        /// </summary>
        [Input("coresCount")]
        public Input<int>? CoresCount { get; set; }

        /// <summary>
        /// [string] A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can be retrieved from the datacenter resource. The default value is `AUTO`.
        /// </summary>
        [Input("cpuFamily")]
        public Input<string>? CpuFamily { get; set; }

        /// <summary>
        /// The UUID of the virtual data center (VDC) in which the nodepool is provisioned
        /// </summary>
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// [map] Key-value pairs attached to the node pool resource as [Kubernetes labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("maintenanceWindows")]
        private InputList<Inputs.NodePoolMaintenanceWindowGetArgs>? _maintenanceWindows;

        /// <summary>
        /// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        /// </summary>
        public InputList<Inputs.NodePoolMaintenanceWindowGetArgs> MaintenanceWindows
        {
            get => _maintenanceWindows ?? (_maintenanceWindows = new InputList<Inputs.NodePoolMaintenanceWindowGetArgs>());
            set => _maintenanceWindows = value;
        }

        /// <summary>
        /// [string] The name of your node pool. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [int] The number of nodes that make up the node pool. Must be set with a minimum value of 1.
        /// </summary>
        [Input("nodeCount")]
        public Input<int>? NodeCount { get; set; }

        /// <summary>
        /// [int] The RAM size for one node in MB. Must be set in multiples of `1024`MB, with a minimum size is of `2048`MB. The default value is `4096`.
        /// </summary>
        [Input("ramSize")]
        public Input<int>? RamSize { get; set; }

        /// <summary>
        /// [int] The size of the volume in GB. The size must be greater than `10`GB. The default value is `20`.
        /// </summary>
        [Input("storageSize")]
        public Input<int>? StorageSize { get; set; }

        /// <summary>
        /// [int] The type of hardware for the volume. Must be set with one of the values `HDD` or `SSD`. The default value is `SSD`.
        /// </summary>
        [Input("storageType")]
        public Input<string>? StorageType { get; set; }

        /// <summary>
        /// The version of the Data Platform.
        /// </summary>
        [Input("version")]
        public Input<string>? Version { get; set; }

        public NodePoolState()
        {
        }
        public static new NodePoolState Empty => new NodePoolState();
    }
}
