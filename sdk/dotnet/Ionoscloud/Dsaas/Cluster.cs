// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Dsaas
{
    /// <summary>
    /// Manages a **Dataplatform Cluster**.
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
    ///         Name = "Datacenter_Example",
    ///         Location = "de/txl",
    ///         Description = "Datacenter for testing Dataplatform Cluster",
    ///     });
    /// 
    ///     var exampleLan = new Ionoscloud.Compute.Lan("example", new()
    ///     {
    ///         DatacenterId = example.Id,
    ///         Public = false,
    ///         Name = "LAN_Example",
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
    ///         Version = "23.11",
    ///         Lans = new[]
    ///         {
    ///             new Ionoscloud.Dsaas.Inputs.ClusterLanArgs
    ///             {
    ///                 LanId = exampleLan.Id,
    ///                 Dhcp = false,
    ///                 Routes = new[]
    ///                 {
    ///                     new Ionoscloud.Dsaas.Inputs.ClusterLanRouteArgs
    ///                     {
    ///                         Network = "182.168.42.1/24",
    ///                         Gateway = "192.168.42.1",
    ///                     },
    ///                 },
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Resource Dataplatform Cluster can be imported using the `cluster_id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:dsaas/cluster:Cluster mycluser cluster uuid
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:dsaas/cluster:Cluster")]
    public partial class Cluster : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
        /// </summary>
        [Output("datacenterId")]
        public Output<string> DatacenterId { get; private set; } = null!;

        /// <summary>
        /// [list] A list of LANs you want this node pool to be part of.
        /// </summary>
        [Output("lans")]
        public Output<ImmutableArray<Outputs.ClusterLan>> Lans { get; private set; } = null!;

        /// <summary>
        /// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        /// </summary>
        [Output("maintenanceWindows")]
        public Output<ImmutableArray<Outputs.ClusterMaintenanceWindow>> MaintenanceWindows { get; private set; } = null!;

        /// <summary>
        /// [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [int] The version of the Data Platform.
        /// </summary>
        [Output("version")]
        public Output<string> Version { get; private set; } = null!;


        /// <summary>
        /// Create a Cluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Cluster(string name, ClusterArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:dsaas/cluster:Cluster", name, args ?? new ClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Cluster(string name, Input<string> id, ClusterState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:dsaas/cluster:Cluster", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Cluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Cluster Get(string name, Input<string> id, ClusterState? state = null, CustomResourceOptions? options = null)
        {
            return new Cluster(name, id, state, options);
        }
    }

    public sealed class ClusterArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        [Input("lans")]
        private InputList<Inputs.ClusterLanArgs>? _lans;

        /// <summary>
        /// [list] A list of LANs you want this node pool to be part of.
        /// </summary>
        public InputList<Inputs.ClusterLanArgs> Lans
        {
            get => _lans ?? (_lans = new InputList<Inputs.ClusterLanArgs>());
            set => _lans = value;
        }

        [Input("maintenanceWindows")]
        private InputList<Inputs.ClusterMaintenanceWindowArgs>? _maintenanceWindows;

        /// <summary>
        /// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        /// </summary>
        public InputList<Inputs.ClusterMaintenanceWindowArgs> MaintenanceWindows
        {
            get => _maintenanceWindows ?? (_maintenanceWindows = new InputList<Inputs.ClusterMaintenanceWindowArgs>());
            set => _maintenanceWindows = value;
        }

        /// <summary>
        /// [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [int] The version of the Data Platform.
        /// </summary>
        [Input("version")]
        public Input<string>? Version { get; set; }

        public ClusterArgs()
        {
        }
        public static new ClusterArgs Empty => new ClusterArgs();
    }

    public sealed class ClusterState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
        /// </summary>
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        [Input("lans")]
        private InputList<Inputs.ClusterLanGetArgs>? _lans;

        /// <summary>
        /// [list] A list of LANs you want this node pool to be part of.
        /// </summary>
        public InputList<Inputs.ClusterLanGetArgs> Lans
        {
            get => _lans ?? (_lans = new InputList<Inputs.ClusterLanGetArgs>());
            set => _lans = value;
        }

        [Input("maintenanceWindows")]
        private InputList<Inputs.ClusterMaintenanceWindowGetArgs>? _maintenanceWindows;

        /// <summary>
        /// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        /// </summary>
        public InputList<Inputs.ClusterMaintenanceWindowGetArgs> MaintenanceWindows
        {
            get => _maintenanceWindows ?? (_maintenanceWindows = new InputList<Inputs.ClusterMaintenanceWindowGetArgs>());
            set => _maintenanceWindows = value;
        }

        /// <summary>
        /// [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [int] The version of the Data Platform.
        /// </summary>
        [Input("version")]
        public Input<string>? Version { get; set; }

        public ClusterState()
        {
        }
        public static new ClusterState Empty => new ClusterState();
    }
}
