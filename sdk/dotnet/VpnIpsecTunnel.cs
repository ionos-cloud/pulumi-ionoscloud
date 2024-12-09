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
    /// An IPSec Gateway Tunnel resource manages the creation, management, and deletion of VPN IPSec Gateway Tunnels within the
    /// IONOS Cloud infrastructure. This resource facilitates the creation of VPN IPSec Gateway Tunnels, enabling secure
    /// connections between your network resources.
    /// 
    /// ## Usage example
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Pulumi.Ionoscloud;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     // Basic example
    ///     var testDatacenter = new Ionoscloud.Compute.Datacenter("testDatacenter", new()
    ///     {
    ///         Location = "de/fra",
    ///     });
    /// 
    ///     var testLan = new Ionoscloud.Compute.Lan("testLan", new()
    ///     {
    ///         Public = false,
    ///         DatacenterId = testDatacenter.Id,
    ///     });
    /// 
    ///     var testIpblock = new Ionoscloud.Compute.IPBlock("testIpblock", new()
    ///     {
    ///         Location = "de/fra",
    ///         Size = 1,
    ///     });
    /// 
    ///     var exampleVpnIpsecGateway = new Ionoscloud.VpnIpsecGateway("exampleVpnIpsecGateway", new()
    ///     {
    ///         Location = "de/fra",
    ///         GatewayIp = testIpblock.Ips.Apply(ips =&gt; ips[0]),
    ///         Version = "IKEv2",
    ///         Description = "This gateway connects site A to VDC X.",
    ///         Connections = new[]
    ///         {
    ///             new Ionoscloud.Inputs.VpnIpsecGatewayConnectionArgs
    ///             {
    ///                 DatacenterId = testDatacenter.Id,
    ///                 LanId = testLan.Id,
    ///                 Ipv4Cidr = "192.168.100.10/24",
    ///             },
    ///         },
    ///     });
    /// 
    ///     var exampleVpnIpsecTunnel = new Ionoscloud.VpnIpsecTunnel("exampleVpnIpsecTunnel", new()
    ///     {
    ///         Location = "de/fra",
    ///         GatewayId = exampleVpnIpsecGateway.Id,
    ///         RemoteHost = "vpn.mycompany.com",
    ///         Description = "Allows local subnet X to connect to virtual network Y.",
    ///         Auth = new Ionoscloud.Inputs.VpnIpsecTunnelAuthArgs
    ///         {
    ///             Method = "PSK",
    ///             PskKey = "X2wosbaw74M8hQGbK3jCCaEusR6CCFRa",
    ///         },
    ///         Ike = new Ionoscloud.Inputs.VpnIpsecTunnelIkeArgs
    ///         {
    ///             DiffieHellmanGroup = "16-MODP4096",
    ///             EncryptionAlgorithm = "AES256",
    ///             IntegrityAlgorithm = "SHA256",
    ///             Lifetime = 86400,
    ///         },
    ///         Esps = new[]
    ///         {
    ///             new Ionoscloud.Inputs.VpnIpsecTunnelEspArgs
    ///             {
    ///                 DiffieHellmanGroup = "16-MODP4096",
    ///                 EncryptionAlgorithm = "AES256",
    ///                 IntegrityAlgorithm = "SHA256",
    ///                 Lifetime = 3600,
    ///             },
    ///         },
    ///         CloudNetworkCidrs = new[]
    ///         {
    ///             "0.0.0.0/0",
    ///         },
    ///         PeerNetworkCidrs = new[]
    ///         {
    ///             "1.2.3.4/32",
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// The resource can be imported using the `location`, `gateway_id` and `tunnel_id`, for example:
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:index/vpnIpsecTunnel:VpnIpsecTunnel example {location}:{gateway_id}:{tunnel_id}
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:index/vpnIpsecTunnel:VpnIpsecTunnel")]
    public partial class VpnIpsecTunnel : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
        /// items: 1.
        /// </summary>
        [Output("auth")]
        public Output<Outputs.VpnIpsecTunnelAuth> Auth { get; private set; } = null!;

        /// <summary>
        /// [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
        /// tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
        /// Maximum items: 20.
        /// </summary>
        [Output("cloudNetworkCidrs")]
        public Output<ImmutableArray<string>> CloudNetworkCidrs { get; private set; } = null!;

        /// <summary>
        /// [string] The human-readable description of your IPSec Gateway Tunnel.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
        /// </summary>
        [Output("esps")]
        public Output<ImmutableArray<Outputs.VpnIpsecTunnelEsp>> Esps { get; private set; } = null!;

        /// <summary>
        /// [string] The ID of the IPSec Gateway that the tunnel belongs to.
        /// </summary>
        [Output("gatewayId")]
        public Output<string> GatewayId { get; private set; } = null!;

        /// <summary>
        /// [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
        /// </summary>
        [Output("ike")]
        public Output<Outputs.VpnIpsecTunnelIke> Ike { get; private set; } = null!;

        /// <summary>
        /// [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
        /// gb/lhr, us/ewr, us/las, us/mci, fr/par
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// [string] The name of the IPSec Gateway Tunnel.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
        /// tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
        /// </summary>
        [Output("peerNetworkCidrs")]
        public Output<ImmutableArray<string>> PeerNetworkCidrs { get; private set; } = null!;

        /// <summary>
        /// [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
        /// </summary>
        [Output("remoteHost")]
        public Output<string> RemoteHost { get; private set; } = null!;


        /// <summary>
        /// Create a VpnIpsecTunnel resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VpnIpsecTunnel(string name, VpnIpsecTunnelArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:index/vpnIpsecTunnel:VpnIpsecTunnel", name, args ?? new VpnIpsecTunnelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VpnIpsecTunnel(string name, Input<string> id, VpnIpsecTunnelState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/vpnIpsecTunnel:VpnIpsecTunnel", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing VpnIpsecTunnel resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VpnIpsecTunnel Get(string name, Input<string> id, VpnIpsecTunnelState? state = null, CustomResourceOptions? options = null)
        {
            return new VpnIpsecTunnel(name, id, state, options);
        }
    }

    public sealed class VpnIpsecTunnelArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
        /// items: 1.
        /// </summary>
        [Input("auth", required: true)]
        public Input<Inputs.VpnIpsecTunnelAuthArgs> Auth { get; set; } = null!;

        [Input("cloudNetworkCidrs", required: true)]
        private InputList<string>? _cloudNetworkCidrs;

        /// <summary>
        /// [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
        /// tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
        /// Maximum items: 20.
        /// </summary>
        public InputList<string> CloudNetworkCidrs
        {
            get => _cloudNetworkCidrs ?? (_cloudNetworkCidrs = new InputList<string>());
            set => _cloudNetworkCidrs = value;
        }

        /// <summary>
        /// [string] The human-readable description of your IPSec Gateway Tunnel.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("esps", required: true)]
        private InputList<Inputs.VpnIpsecTunnelEspArgs>? _esps;

        /// <summary>
        /// [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
        /// </summary>
        public InputList<Inputs.VpnIpsecTunnelEspArgs> Esps
        {
            get => _esps ?? (_esps = new InputList<Inputs.VpnIpsecTunnelEspArgs>());
            set => _esps = value;
        }

        /// <summary>
        /// [string] The ID of the IPSec Gateway that the tunnel belongs to.
        /// </summary>
        [Input("gatewayId", required: true)]
        public Input<string> GatewayId { get; set; } = null!;

        /// <summary>
        /// [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
        /// </summary>
        [Input("ike", required: true)]
        public Input<Inputs.VpnIpsecTunnelIkeArgs> Ike { get; set; } = null!;

        /// <summary>
        /// [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
        /// gb/lhr, us/ewr, us/las, us/mci, fr/par
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        /// <summary>
        /// [string] The name of the IPSec Gateway Tunnel.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("peerNetworkCidrs", required: true)]
        private InputList<string>? _peerNetworkCidrs;

        /// <summary>
        /// [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
        /// tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
        /// </summary>
        public InputList<string> PeerNetworkCidrs
        {
            get => _peerNetworkCidrs ?? (_peerNetworkCidrs = new InputList<string>());
            set => _peerNetworkCidrs = value;
        }

        /// <summary>
        /// [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
        /// </summary>
        [Input("remoteHost", required: true)]
        public Input<string> RemoteHost { get; set; } = null!;

        public VpnIpsecTunnelArgs()
        {
        }
        public static new VpnIpsecTunnelArgs Empty => new VpnIpsecTunnelArgs();
    }

    public sealed class VpnIpsecTunnelState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
        /// items: 1.
        /// </summary>
        [Input("auth")]
        public Input<Inputs.VpnIpsecTunnelAuthGetArgs>? Auth { get; set; }

        [Input("cloudNetworkCidrs")]
        private InputList<string>? _cloudNetworkCidrs;

        /// <summary>
        /// [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
        /// tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
        /// Maximum items: 20.
        /// </summary>
        public InputList<string> CloudNetworkCidrs
        {
            get => _cloudNetworkCidrs ?? (_cloudNetworkCidrs = new InputList<string>());
            set => _cloudNetworkCidrs = value;
        }

        /// <summary>
        /// [string] The human-readable description of your IPSec Gateway Tunnel.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("esps")]
        private InputList<Inputs.VpnIpsecTunnelEspGetArgs>? _esps;

        /// <summary>
        /// [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
        /// </summary>
        public InputList<Inputs.VpnIpsecTunnelEspGetArgs> Esps
        {
            get => _esps ?? (_esps = new InputList<Inputs.VpnIpsecTunnelEspGetArgs>());
            set => _esps = value;
        }

        /// <summary>
        /// [string] The ID of the IPSec Gateway that the tunnel belongs to.
        /// </summary>
        [Input("gatewayId")]
        public Input<string>? GatewayId { get; set; }

        /// <summary>
        /// [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
        /// </summary>
        [Input("ike")]
        public Input<Inputs.VpnIpsecTunnelIkeGetArgs>? Ike { get; set; }

        /// <summary>
        /// [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
        /// gb/lhr, us/ewr, us/las, us/mci, fr/par
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// [string] The name of the IPSec Gateway Tunnel.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("peerNetworkCidrs")]
        private InputList<string>? _peerNetworkCidrs;

        /// <summary>
        /// [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
        /// tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
        /// </summary>
        public InputList<string> PeerNetworkCidrs
        {
            get => _peerNetworkCidrs ?? (_peerNetworkCidrs = new InputList<string>());
            set => _peerNetworkCidrs = value;
        }

        /// <summary>
        /// [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
        /// </summary>
        [Input("remoteHost")]
        public Input<string>? RemoteHost { get; set; }

        public VpnIpsecTunnelState()
        {
        }
        public static new VpnIpsecTunnelState Empty => new VpnIpsecTunnelState();
    }
}
