// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute
{
    /// <summary>
    /// Manages a **Nat Gateway** on IonosCloud.
    /// 
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
    ///     var exampleDatacenter = new Ionoscloud.Compute.Datacenter("exampleDatacenter", new()
    ///     {
    ///         Location = "us/las",
    ///         Description = "Datacenter Description",
    ///         SecAuthProtection = false,
    ///     });
    /// 
    ///     var exampleIPBlock = new Ionoscloud.Compute.IPBlock("exampleIPBlock", new()
    ///     {
    ///         Location = "us/las",
    ///         Size = 2,
    ///     });
    /// 
    ///     var exampleLan = new Ionoscloud.Compute.Lan("exampleLan", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         Public = true,
    ///     });
    /// 
    ///     var exampleNatGateway = new Ionoscloud.Compute.NatGateway("exampleNatGateway", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         PublicIps = new[]
    ///         {
    ///             exampleIPBlock.Ips.Apply(ips =&gt; ips[0]),
    ///             exampleIPBlock.Ips.Apply(ips =&gt; ips[1]),
    ///         },
    ///         Lans = new[]
    ///         {
    ///             new Ionoscloud.Compute.Inputs.NatGatewayLanArgs
    ///             {
    ///                 Id = exampleLan.Id,
    ///                 GatewayIps = new[]
    ///                 {
    ///                     "10.11.2.5",
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
    /// A Nat Gateway resource can be imported using its `resource id` and the `datacenter id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:compute/natGateway:NatGateway my_natgateway {datacenter uuid}/{nat gateway uuid}
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:compute/natGateway:NatGateway")]
    public partial class NatGateway : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [string] A Datacenter's UUID.
        /// </summary>
        [Output("datacenterId")]
        public Output<string> DatacenterId { get; private set; } = null!;

        /// <summary>
        /// [list] A list of Local Area Networks the node pool should be part of.
        /// </summary>
        [Output("lans")]
        public Output<ImmutableArray<Outputs.NatGatewayLan>> Lans { get; private set; } = null!;

        /// <summary>
        /// [string] Name of the NAT gateway.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
        /// </summary>
        [Output("publicIps")]
        public Output<ImmutableArray<string>> PublicIps { get; private set; } = null!;


        /// <summary>
        /// Create a NatGateway resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NatGateway(string name, NatGatewayArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/natGateway:NatGateway", name, args ?? new NatGatewayArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NatGateway(string name, Input<string> id, NatGatewayState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/natGateway:NatGateway", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing NatGateway resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NatGateway Get(string name, Input<string> id, NatGatewayState? state = null, CustomResourceOptions? options = null)
        {
            return new NatGateway(name, id, state, options);
        }
    }

    public sealed class NatGatewayArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] A Datacenter's UUID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        [Input("lans", required: true)]
        private InputList<Inputs.NatGatewayLanArgs>? _lans;

        /// <summary>
        /// [list] A list of Local Area Networks the node pool should be part of.
        /// </summary>
        public InputList<Inputs.NatGatewayLanArgs> Lans
        {
            get => _lans ?? (_lans = new InputList<Inputs.NatGatewayLanArgs>());
            set => _lans = value;
        }

        /// <summary>
        /// [string] Name of the NAT gateway.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("publicIps", required: true)]
        private InputList<string>? _publicIps;

        /// <summary>
        /// [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
        /// </summary>
        public InputList<string> PublicIps
        {
            get => _publicIps ?? (_publicIps = new InputList<string>());
            set => _publicIps = value;
        }

        public NatGatewayArgs()
        {
        }
        public static new NatGatewayArgs Empty => new NatGatewayArgs();
    }

    public sealed class NatGatewayState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] A Datacenter's UUID.
        /// </summary>
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        [Input("lans")]
        private InputList<Inputs.NatGatewayLanGetArgs>? _lans;

        /// <summary>
        /// [list] A list of Local Area Networks the node pool should be part of.
        /// </summary>
        public InputList<Inputs.NatGatewayLanGetArgs> Lans
        {
            get => _lans ?? (_lans = new InputList<Inputs.NatGatewayLanGetArgs>());
            set => _lans = value;
        }

        /// <summary>
        /// [string] Name of the NAT gateway.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("publicIps")]
        private InputList<string>? _publicIps;

        /// <summary>
        /// [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
        /// </summary>
        public InputList<string> PublicIps
        {
            get => _publicIps ?? (_publicIps = new InputList<string>());
            set => _publicIps = value;
        }

        public NatGatewayState()
        {
        }
        public static new NatGatewayState Empty => new NatGatewayState();
    }
}
