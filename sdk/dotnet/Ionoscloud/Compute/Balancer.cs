// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Compute
{
    /// <summary>
    /// Manages a Load Balancer on IonosCloud.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Ionoscloud.Pulumi.Ionoscloud;
    /// using Random = Pulumi.Random;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var example = new Ionoscloud.Compute.Datacenter("example", new()
    ///     {
    ///         Name = "Datacenter Example",
    ///         Location = "us/las",
    ///         Description = "Datacenter Description",
    ///         SecAuthProtection = false,
    ///     });
    /// 
    ///     var exampleLan = new Ionoscloud.Compute.Lan("example", new()
    ///     {
    ///         DatacenterId = example.Id,
    ///         Public = true,
    ///         Name = "Lan Example",
    ///     });
    /// 
    ///     var serverImagePassword = new Random.Index.Password("server_image_password", new()
    ///     {
    ///         Length = 16,
    ///         Special = false,
    ///     });
    /// 
    ///     var exampleServer = new Ionoscloud.Compute.Server("example", new()
    ///     {
    ///         Name = "Server Example",
    ///         DatacenterId = example.Id,
    ///         Cores = 1,
    ///         Ram = 1024,
    ///         AvailabilityZone = "ZONE_1",
    ///         CpuFamily = "INTEL_XEON",
    ///         ImageName = "Ubuntu-20.04",
    ///         ImagePassword = serverImagePassword.Result,
    ///         Volume = new Ionoscloud.Compute.Inputs.ServerVolumeArgs
    ///         {
    ///             Name = "system",
    ///             Size = 14,
    ///             DiskType = "SSD",
    ///         },
    ///         Nic = new Ionoscloud.Compute.Inputs.ServerNicArgs
    ///         {
    ///             Lan = 1,
    ///             Dhcp = true,
    ///             FirewallActive = true,
    ///         },
    ///     });
    /// 
    ///     var exampleBalancer = new Ionoscloud.Compute.Balancer("example", new()
    ///     {
    ///         DatacenterId = example.Id,
    ///         NicIds = new[]
    ///         {
    ///             exampleServer.PrimaryNic,
    ///         },
    ///         Name = "Load Balancer Example",
    ///         Dhcp = true,
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## A note on nics
    /// 
    /// When declaring NIC resources to be used with the load balancer, please make sure
    /// you use the "lifecycle meta-argument" to make sure changes to the lan attribute
    /// of the nic are ignored.
    /// 
    /// Please see the Nic resource's documentation for an example on how to do that.
    /// 
    /// ## Import
    /// 
    /// Resource Load Balancer can be imported using the `resource id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:compute/balancer:Balancer myloadbalancer datacenter uuid/loadbalancer uuid
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:compute/balancer:Balancer")]
    public partial class Balancer : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [string] The ID of a Virtual Data Center.
        /// </summary>
        [Output("datacenterId")]
        public Output<string> DatacenterId { get; private set; } = null!;

        /// <summary>
        /// [Boolean] Indicates if the load balancer will reserve an IP using DHCP.
        /// </summary>
        [Output("dhcp")]
        public Output<bool?> Dhcp { get; private set; } = null!;

        /// <summary>
        /// [string] IPv4 address of the load balancer.
        /// </summary>
        [Output("ip")]
        public Output<string> Ip { get; private set; } = null!;

        /// <summary>
        /// [string] The name of the load balancer.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [list] A list of NIC IDs that are part of the load balancer.
        /// </summary>
        [Output("nicIds")]
        public Output<ImmutableArray<string>> NicIds { get; private set; } = null!;


        /// <summary>
        /// Create a Balancer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Balancer(string name, BalancerArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/balancer:Balancer", name, args ?? new BalancerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Balancer(string name, Input<string> id, BalancerState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/balancer:Balancer", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Balancer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Balancer Get(string name, Input<string> id, BalancerState? state = null, CustomResourceOptions? options = null)
        {
            return new Balancer(name, id, state, options);
        }
    }

    public sealed class BalancerArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The ID of a Virtual Data Center.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// [Boolean] Indicates if the load balancer will reserve an IP using DHCP.
        /// </summary>
        [Input("dhcp")]
        public Input<bool>? Dhcp { get; set; }

        /// <summary>
        /// [string] IPv4 address of the load balancer.
        /// </summary>
        [Input("ip")]
        public Input<string>? Ip { get; set; }

        /// <summary>
        /// [string] The name of the load balancer.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nicIds", required: true)]
        private InputList<string>? _nicIds;

        /// <summary>
        /// [list] A list of NIC IDs that are part of the load balancer.
        /// </summary>
        public InputList<string> NicIds
        {
            get => _nicIds ?? (_nicIds = new InputList<string>());
            set => _nicIds = value;
        }

        public BalancerArgs()
        {
        }
        public static new BalancerArgs Empty => new BalancerArgs();
    }

    public sealed class BalancerState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The ID of a Virtual Data Center.
        /// </summary>
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        /// <summary>
        /// [Boolean] Indicates if the load balancer will reserve an IP using DHCP.
        /// </summary>
        [Input("dhcp")]
        public Input<bool>? Dhcp { get; set; }

        /// <summary>
        /// [string] IPv4 address of the load balancer.
        /// </summary>
        [Input("ip")]
        public Input<string>? Ip { get; set; }

        /// <summary>
        /// [string] The name of the load balancer.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nicIds")]
        private InputList<string>? _nicIds;

        /// <summary>
        /// [list] A list of NIC IDs that are part of the load balancer.
        /// </summary>
        public InputList<string> NicIds
        {
            get => _nicIds ?? (_nicIds = new InputList<string>());
            set => _nicIds = value;
        }

        public BalancerState()
        {
        }
        public static new BalancerState Empty => new BalancerState();
    }
}
