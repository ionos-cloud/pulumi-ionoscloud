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
    /// Manages **IP Blocks** on IonosCloud. IP Blocks contain reserved public IP addresses that can be assigned servers or other resources.
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
    ///     var example = new Ionoscloud.Compute.IPBlock("example", new()
    ///     {
    ///         Location = "us/las",
    ///         Size = 1,
    ///         Name = "IP Block Example",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Resource Ipblock can be imported using the `resource id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:compute/iPBlock:IPBlock myipblock ipblock uuid
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:compute/iPBlock:IPBlock")]
    public partial class IPBlock : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Read-Only attribute. Lists consumption detail of an individual ip
        /// </summary>
        [Output("ipConsumers")]
        public Output<ImmutableArray<Outputs.IPBlockIpConsumer>> IpConsumers { get; private set; } = null!;

        /// <summary>
        /// [integer] The list of IP addresses associated with this block.
        /// </summary>
        [Output("ips")]
        public Output<ImmutableArray<string>> Ips { get; private set; } = null!;

        /// <summary>
        /// [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// [string] The name of Ip Block
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [integer] The number of IP addresses to reserve for this block.
        /// </summary>
        [Output("size")]
        public Output<int> Size { get; private set; } = null!;


        /// <summary>
        /// Create a IPBlock resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public IPBlock(string name, IPBlockArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/iPBlock:IPBlock", name, args ?? new IPBlockArgs(), MakeResourceOptions(options, ""))
        {
        }

        private IPBlock(string name, Input<string> id, IPBlockState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/iPBlock:IPBlock", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing IPBlock resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static IPBlock Get(string name, Input<string> id, IPBlockState? state = null, CustomResourceOptions? options = null)
        {
            return new IPBlock(name, id, state, options);
        }
    }

    public sealed class IPBlockArgs : global::Pulumi.ResourceArgs
    {
        [Input("ipConsumers")]
        private InputList<Inputs.IPBlockIpConsumerArgs>? _ipConsumers;

        /// <summary>
        /// Read-Only attribute. Lists consumption detail of an individual ip
        /// </summary>
        public InputList<Inputs.IPBlockIpConsumerArgs> IpConsumers
        {
            get => _ipConsumers ?? (_ipConsumers = new InputList<Inputs.IPBlockIpConsumerArgs>());
            set => _ipConsumers = value;
        }

        /// <summary>
        /// [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        /// <summary>
        /// [string] The name of Ip Block
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [integer] The number of IP addresses to reserve for this block.
        /// </summary>
        [Input("size", required: true)]
        public Input<int> Size { get; set; } = null!;

        public IPBlockArgs()
        {
        }
        public static new IPBlockArgs Empty => new IPBlockArgs();
    }

    public sealed class IPBlockState : global::Pulumi.ResourceArgs
    {
        [Input("ipConsumers")]
        private InputList<Inputs.IPBlockIpConsumerGetArgs>? _ipConsumers;

        /// <summary>
        /// Read-Only attribute. Lists consumption detail of an individual ip
        /// </summary>
        public InputList<Inputs.IPBlockIpConsumerGetArgs> IpConsumers
        {
            get => _ipConsumers ?? (_ipConsumers = new InputList<Inputs.IPBlockIpConsumerGetArgs>());
            set => _ipConsumers = value;
        }

        [Input("ips")]
        private InputList<string>? _ips;

        /// <summary>
        /// [integer] The list of IP addresses associated with this block.
        /// </summary>
        public InputList<string> Ips
        {
            get => _ips ?? (_ips = new InputList<string>());
            set => _ips = value;
        }

        /// <summary>
        /// [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// [string] The name of Ip Block
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [integer] The number of IP addresses to reserve for this block.
        /// </summary>
        [Input("size")]
        public Input<int>? Size { get; set; }

        public IPBlockState()
        {
        }
        public static new IPBlockState Empty => new IPBlockState();
    }
}
