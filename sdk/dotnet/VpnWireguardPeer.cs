// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    /// <summary>
    /// This page provides an overview of the `ionoscloud.VpnWireguardPeer` resource, which allows you to manage a WireGuard Peer in your cloud infrastructure.
    /// This resource enables the creation, management, and deletion of a WireGuard VPN Peer, facilitating secure connections between your network resources.
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
    ///     var example = new Ionoscloud.VpnWireguardPeer("example", new()
    ///     {
    ///         AllowedIps = new[]
    ///         {
    ///             "10.0.0.0/8",
    ///             "192.168.1.0/24",
    ///         },
    ///         Description = "An example WireGuard peer",
    ///         Endpoint = new Ionoscloud.Inputs.VpnWireguardPeerEndpointArgs
    ///         {
    ///             Host = "1.2.3.4",
    ///             Port = 51820,
    ///         },
    ///         GatewayId = "your gateway id here",
    ///         Location = "de/fra",
    ///         PublicKey = "examplePublicKey==",
    ///     });
    /// 
    /// });
    /// ```
    /// &lt;!--End PulumiCodeChooser --&gt;
    /// 
    /// ## Import
    /// 
    /// WireGuard Peers can be imported using the `gateway_id` and `id`, e.g.,
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:index/vpnWireguardPeer:VpnWireguardPeer example &lt;gateway_id&gt;:&lt;peer_id&gt;
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:index/vpnWireguardPeer:VpnWireguardPeer")]
    public partial class VpnWireguardPeer : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [list, string] A list of subnet CIDRs that are allowed to connect to the WireGuard Gateway.
        /// </summary>
        [Output("allowedIps")]
        public Output<ImmutableArray<string>> AllowedIps { get; private set; } = null!;

        /// <summary>
        /// [string] A description of the WireGuard Gateway.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// [block] An endpoint configuration block for the WireGuard Gateway. The structure of this block is as follows:
        /// </summary>
        [Output("endpoint")]
        public Output<Outputs.VpnWireguardPeerEndpoint?> Endpoint { get; private set; } = null!;

        /// <summary>
        /// [string] The ID of the WireGuard Gateway that the Peer will connect to.
        /// </summary>
        [Output("gatewayId")]
        public Output<string> GatewayId { get; private set; } = null!;

        /// <summary>
        /// [string] The location of the WireGuard Gateway.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// [string] The human-readable name of the WireGuard Gateway.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [string] The public key for the WireGuard Gateway.
        /// </summary>
        [Output("publicKey")]
        public Output<string> PublicKey { get; private set; } = null!;

        /// <summary>
        /// The current status of the WireGuard Gateway Peer.
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;


        /// <summary>
        /// Create a VpnWireguardPeer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VpnWireguardPeer(string name, VpnWireguardPeerArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:index/vpnWireguardPeer:VpnWireguardPeer", name, args ?? new VpnWireguardPeerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VpnWireguardPeer(string name, Input<string> id, VpnWireguardPeerState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/vpnWireguardPeer:VpnWireguardPeer", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/ionos-cloud/pulumi-ionoscloud/",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing VpnWireguardPeer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VpnWireguardPeer Get(string name, Input<string> id, VpnWireguardPeerState? state = null, CustomResourceOptions? options = null)
        {
            return new VpnWireguardPeer(name, id, state, options);
        }
    }

    public sealed class VpnWireguardPeerArgs : global::Pulumi.ResourceArgs
    {
        [Input("allowedIps", required: true)]
        private InputList<string>? _allowedIps;

        /// <summary>
        /// [list, string] A list of subnet CIDRs that are allowed to connect to the WireGuard Gateway.
        /// </summary>
        public InputList<string> AllowedIps
        {
            get => _allowedIps ?? (_allowedIps = new InputList<string>());
            set => _allowedIps = value;
        }

        /// <summary>
        /// [string] A description of the WireGuard Gateway.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// [block] An endpoint configuration block for the WireGuard Gateway. The structure of this block is as follows:
        /// </summary>
        [Input("endpoint")]
        public Input<Inputs.VpnWireguardPeerEndpointArgs>? Endpoint { get; set; }

        /// <summary>
        /// [string] The ID of the WireGuard Gateway that the Peer will connect to.
        /// </summary>
        [Input("gatewayId", required: true)]
        public Input<string> GatewayId { get; set; } = null!;

        /// <summary>
        /// [string] The location of the WireGuard Gateway.
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        /// <summary>
        /// [string] The human-readable name of the WireGuard Gateway.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [string] The public key for the WireGuard Gateway.
        /// </summary>
        [Input("publicKey", required: true)]
        public Input<string> PublicKey { get; set; } = null!;

        public VpnWireguardPeerArgs()
        {
        }
        public static new VpnWireguardPeerArgs Empty => new VpnWireguardPeerArgs();
    }

    public sealed class VpnWireguardPeerState : global::Pulumi.ResourceArgs
    {
        [Input("allowedIps")]
        private InputList<string>? _allowedIps;

        /// <summary>
        /// [list, string] A list of subnet CIDRs that are allowed to connect to the WireGuard Gateway.
        /// </summary>
        public InputList<string> AllowedIps
        {
            get => _allowedIps ?? (_allowedIps = new InputList<string>());
            set => _allowedIps = value;
        }

        /// <summary>
        /// [string] A description of the WireGuard Gateway.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// [block] An endpoint configuration block for the WireGuard Gateway. The structure of this block is as follows:
        /// </summary>
        [Input("endpoint")]
        public Input<Inputs.VpnWireguardPeerEndpointGetArgs>? Endpoint { get; set; }

        /// <summary>
        /// [string] The ID of the WireGuard Gateway that the Peer will connect to.
        /// </summary>
        [Input("gatewayId")]
        public Input<string>? GatewayId { get; set; }

        /// <summary>
        /// [string] The location of the WireGuard Gateway.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// [string] The human-readable name of the WireGuard Gateway.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [string] The public key for the WireGuard Gateway.
        /// </summary>
        [Input("publicKey")]
        public Input<string>? PublicKey { get; set; }

        /// <summary>
        /// The current status of the WireGuard Gateway Peer.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        public VpnWireguardPeerState()
        {
        }
        public static new VpnWireguardPeerState Empty => new VpnWireguardPeerState();
    }
}
