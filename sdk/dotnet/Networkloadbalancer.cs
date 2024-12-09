// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    /// <summary>
    /// Manages a **Network Load Balancer**  on IonosCloud.
    /// 
    /// ## Example Usage
    /// 
    /// &lt;!--Start PulumiCodeChooser --&gt;
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Pulumi.Ionoscloud;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var exampleDatacenter = new Ionoscloud.Compute.Datacenter("exampleDatacenter", new()
    ///     {
    ///         Location = "us/las",
    ///         Description = "Datacenter Description",
    ///         SecAuthProtection = false,
    ///     });
    /// 
    ///     var example1 = new Ionoscloud.Compute.Lan("example1", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         Public = false,
    ///     });
    /// 
    ///     var example2 = new Ionoscloud.Compute.Lan("example2", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         Public = false,
    ///     });
    /// 
    ///     var exampleNetworkloadbalancer = new Ionoscloud.Networkloadbalancer("exampleNetworkloadbalancer", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         ListenerLan = example1.Id,
    ///         TargetLan = example2.Id,
    ///         Ips = new[]
    ///         {
    ///             "10.12.118.224",
    ///         },
    ///         LbPrivateIps = new[]
    ///         {
    ///             "10.13.72.225/24",
    ///         },
    ///         CentralLogging = true,
    ///         LoggingFormat = "%{+Q}o %{-Q}ci - - [%trg] %r %ST %B \"\" \"\" %cp %ms %ft %b %s %TR %Tw %Tc %Tr %Ta %tsc %ac %fc %bc %sc %rc %sq %bq %CC %CS %hrl %hsl",
    ///     });
    /// 
    /// });
    /// ```
    /// &lt;!--End PulumiCodeChooser --&gt;
    /// 
    /// ## Example configuring Flowlog
    /// 
    /// &lt;!--Start PulumiCodeChooser --&gt;
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Pulumi.Ionoscloud;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var example = new Ionoscloud.Networkloadbalancer("example", new()
    ///     {
    ///         DatacenterId = ionoscloud_datacenter.Example.Id,
    ///         ListenerLan = ionoscloud_lan.Example1.Id,
    ///         TargetLan = ionoscloud_lan.Example2.Id,
    ///         Ips = new[]
    ///         {
    ///             "10.12.118.224",
    ///         },
    ///         LbPrivateIps = new[]
    ///         {
    ///             "10.13.72.225/24",
    ///         },
    ///         Flowlog = new Ionoscloud.Inputs.NetworkloadbalancerFlowlogArgs
    ///         {
    ///             Action = "ALL",
    ///             Bucket = "flowlog-bucket",
    ///             Direction = "INGRESS",
    ///             Name = "flowlog",
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// &lt;!--End PulumiCodeChooser --&gt;
    /// 
    /// This will configure flowlog for ALL(rejected and accepted) ingress traffic and will log it into an existing ionos bucket named `flowlog-bucket`. Any s3 compatible client can be used to create it. Adding a flowlog does not force re-creation or the nic, but changing any other field than
    /// `name` will. Deleting a flowlog will also force nic re-creation.
    /// 
    /// ## Import
    /// 
    /// A Network Load Balancer resource can be imported using its `resource id` and the `datacenter id` e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:index/networkloadbalancer:Networkloadbalancer my_networkloadbalancer {datacenter uuid}/{networkloadbalancer uuid}
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:index/networkloadbalancer:Networkloadbalancer")]
    public partial class Networkloadbalancer : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [bool] Turn logging on and off for this product. Default value is 'false'.
        /// </summary>
        [Output("centralLogging")]
        public Output<bool?> CentralLogging { get; private set; } = null!;

        /// <summary>
        /// [string] A Datacenter's UUID.
        /// </summary>
        [Output("datacenterId")]
        public Output<string> DatacenterId { get; private set; } = null!;

        /// <summary>
        /// [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
        /// </summary>
        [Output("flowlog")]
        public Output<Outputs.NetworkloadbalancerFlowlog?> Flowlog { get; private set; } = null!;

        /// <summary>
        /// [list] Collection of IP addresses of the Network Load Balancer. (inbound and outbound) IP of the listenerLan must be a customer reserved IP for the public load balancer and private IP for the private load balancer.
        /// </summary>
        [Output("ips")]
        public Output<ImmutableArray<string>> Ips { get; private set; } = null!;

        /// <summary>
        /// [list] Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain valid subnet mask. If user will not provide any IP then the system will generate one IP with /24 subnet.
        /// </summary>
        [Output("lbPrivateIps")]
        public Output<ImmutableArray<string>> LbPrivateIps { get; private set; } = null!;

        /// <summary>
        /// [int] Id of the listening LAN. (inbound)
        /// </summary>
        [Output("listenerLan")]
        public Output<int> ListenerLan { get; private set; } = null!;

        /// <summary>
        /// Specifies the format of the logs.
        /// </summary>
        [Output("loggingFormat")]
        public Output<string?> LoggingFormat { get; private set; } = null!;

        /// <summary>
        /// [string] Specifies the name of the flow log.
        /// 
        /// ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the network load balancer resource.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [int] Id of the balanced private target LAN. (outbound)
        /// </summary>
        [Output("targetLan")]
        public Output<int> TargetLan { get; private set; } = null!;


        /// <summary>
        /// Create a Networkloadbalancer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Networkloadbalancer(string name, NetworkloadbalancerArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:index/networkloadbalancer:Networkloadbalancer", name, args ?? new NetworkloadbalancerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Networkloadbalancer(string name, Input<string> id, NetworkloadbalancerState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/networkloadbalancer:Networkloadbalancer", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Networkloadbalancer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Networkloadbalancer Get(string name, Input<string> id, NetworkloadbalancerState? state = null, CustomResourceOptions? options = null)
        {
            return new Networkloadbalancer(name, id, state, options);
        }
    }

    public sealed class NetworkloadbalancerArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [bool] Turn logging on and off for this product. Default value is 'false'.
        /// </summary>
        [Input("centralLogging")]
        public Input<bool>? CentralLogging { get; set; }

        /// <summary>
        /// [string] A Datacenter's UUID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
        /// </summary>
        [Input("flowlog")]
        public Input<Inputs.NetworkloadbalancerFlowlogArgs>? Flowlog { get; set; }

        [Input("ips")]
        private InputList<string>? _ips;

        /// <summary>
        /// [list] Collection of IP addresses of the Network Load Balancer. (inbound and outbound) IP of the listenerLan must be a customer reserved IP for the public load balancer and private IP for the private load balancer.
        /// </summary>
        public InputList<string> Ips
        {
            get => _ips ?? (_ips = new InputList<string>());
            set => _ips = value;
        }

        [Input("lbPrivateIps")]
        private InputList<string>? _lbPrivateIps;

        /// <summary>
        /// [list] Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain valid subnet mask. If user will not provide any IP then the system will generate one IP with /24 subnet.
        /// </summary>
        public InputList<string> LbPrivateIps
        {
            get => _lbPrivateIps ?? (_lbPrivateIps = new InputList<string>());
            set => _lbPrivateIps = value;
        }

        /// <summary>
        /// [int] Id of the listening LAN. (inbound)
        /// </summary>
        [Input("listenerLan", required: true)]
        public Input<int> ListenerLan { get; set; } = null!;

        /// <summary>
        /// Specifies the format of the logs.
        /// </summary>
        [Input("loggingFormat")]
        public Input<string>? LoggingFormat { get; set; }

        /// <summary>
        /// [string] Specifies the name of the flow log.
        /// 
        /// ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the network load balancer resource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [int] Id of the balanced private target LAN. (outbound)
        /// </summary>
        [Input("targetLan", required: true)]
        public Input<int> TargetLan { get; set; } = null!;

        public NetworkloadbalancerArgs()
        {
        }
        public static new NetworkloadbalancerArgs Empty => new NetworkloadbalancerArgs();
    }

    public sealed class NetworkloadbalancerState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [bool] Turn logging on and off for this product. Default value is 'false'.
        /// </summary>
        [Input("centralLogging")]
        public Input<bool>? CentralLogging { get; set; }

        /// <summary>
        /// [string] A Datacenter's UUID.
        /// </summary>
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        /// <summary>
        /// [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
        /// </summary>
        [Input("flowlog")]
        public Input<Inputs.NetworkloadbalancerFlowlogGetArgs>? Flowlog { get; set; }

        [Input("ips")]
        private InputList<string>? _ips;

        /// <summary>
        /// [list] Collection of IP addresses of the Network Load Balancer. (inbound and outbound) IP of the listenerLan must be a customer reserved IP for the public load balancer and private IP for the private load balancer.
        /// </summary>
        public InputList<string> Ips
        {
            get => _ips ?? (_ips = new InputList<string>());
            set => _ips = value;
        }

        [Input("lbPrivateIps")]
        private InputList<string>? _lbPrivateIps;

        /// <summary>
        /// [list] Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain valid subnet mask. If user will not provide any IP then the system will generate one IP with /24 subnet.
        /// </summary>
        public InputList<string> LbPrivateIps
        {
            get => _lbPrivateIps ?? (_lbPrivateIps = new InputList<string>());
            set => _lbPrivateIps = value;
        }

        /// <summary>
        /// [int] Id of the listening LAN. (inbound)
        /// </summary>
        [Input("listenerLan")]
        public Input<int>? ListenerLan { get; set; }

        /// <summary>
        /// Specifies the format of the logs.
        /// </summary>
        [Input("loggingFormat")]
        public Input<string>? LoggingFormat { get; set; }

        /// <summary>
        /// [string] Specifies the name of the flow log.
        /// 
        /// ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the network load balancer resource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [int] Id of the balanced private target LAN. (outbound)
        /// </summary>
        [Input("targetLan")]
        public Input<int>? TargetLan { get; set; }

        public NetworkloadbalancerState()
        {
        }
        public static new NetworkloadbalancerState Empty => new NetworkloadbalancerState();
    }
}
