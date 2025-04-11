// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Vpn
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
    /// using Ionoscloud = Ionoscloud.Pulumi.Ionoscloud;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     // Basic example
    ///     var testDatacenter = new Ionoscloud.Compute.Datacenter("test_datacenter", new()
    ///     {
    ///         Name = "test_vpn_gateway_basic",
    ///         Location = "de/fra",
    ///     });
    /// 
    ///     var testLan = new Ionoscloud.Compute.Lan("test_lan", new()
    ///     {
    ///         Name = "test_lan_basic",
    ///         Public = false,
    ///         DatacenterId = testDatacenter.Id,
    ///     });
    /// 
    ///     var testIpblock = new Ionoscloud.Compute.IPBlock("test_ipblock", new()
    ///     {
    ///         Name = "test_ipblock_basic",
    ///         Location = "de/fra",
    ///         Size = 1,
    ///     });
    /// 
    ///     var example = new Ionoscloud.Vpn.IpsecGateway("example", new()
    ///     {
    ///         Name = "ipsec_gateway_basic",
    ///         Location = "de/fra",
    ///         GatewayIp = testIpblock.Ips.Apply(ips =&gt; ips[0]),
    ///         Version = "IKEv2",
    ///         Description = "This gateway connects site A to VDC X.",
    ///         Connections = new[]
    ///         {
    ///             new Ionoscloud.Vpn.Inputs.IpsecGatewayConnectionArgs
    ///             {
    ///                 DatacenterId = testDatacenter.Id,
    ///                 LanId = testLan.Id,
    ///                 Ipv4Cidr = "192.168.100.10/24",
    ///             },
    ///         },
    ///     });
    /// 
    ///     var exampleIpsecTunnel = new Ionoscloud.Vpn.IpsecTunnel("example", new()
    ///     {
    ///         Location = "de/fra",
    ///         GatewayId = example.Id,
    ///         Name = "example-tunnel",
    ///         RemoteHost = "vpn.mycompany.com",
    ///         Description = "Allows local subnet X to connect to virtual network Y.",
    ///         Auth = new Ionoscloud.Vpn.Inputs.IpsecTunnelAuthArgs
    ///         {
    ///             Method = "PSK",
    ///             PskKey = "X2wosbaw74M8hQGbK3jCCaEusR6CCFRa",
    ///         },
    ///         Ike = new Ionoscloud.Vpn.Inputs.IpsecTunnelIkeArgs
    ///         {
    ///             DiffieHellmanGroup = "16-MODP4096",
    ///             EncryptionAlgorithm = "AES256",
    ///             IntegrityAlgorithm = "SHA256",
    ///             Lifetime = 86400,
    ///         },
    ///         Esps = new[]
    ///         {
    ///             new Ionoscloud.Vpn.Inputs.IpsecTunnelEspArgs
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
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Ionoscloud.Pulumi.Ionoscloud;
    /// using Random = Pulumi.Random;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     // Complete example
    ///     var testDatacenter = new Ionoscloud.Compute.Datacenter("test_datacenter", new()
    ///     {
    ///         Name = "vpn_gateway_test",
    ///         Location = "de/fra",
    ///     });
    /// 
    ///     var testLan = new Ionoscloud.Compute.Lan("test_lan", new()
    ///     {
    ///         Name = "test_lan",
    ///         Public = false,
    ///         DatacenterId = testDatacenter.Id,
    ///         Ipv6CidrBlock = lanIpv6CidrBlock,
    ///     });
    /// 
    ///     var testIpblock = new Ionoscloud.Compute.IPBlock("test_ipblock", new()
    ///     {
    ///         Name = "test_ipblock",
    ///         Location = "de/fra",
    ///         Size = 1,
    ///     });
    /// 
    ///     var serverImagePassword = new Random.Index.Password("server_image_password", new()
    ///     {
    ///         Length = 16,
    ///         Special = false,
    ///     });
    /// 
    ///     var testServer = new Ionoscloud.Compute.Server("test_server", new()
    ///     {
    ///         Name = "test_server",
    ///         DatacenterId = testDatacenter.Id,
    ///         Cores = 1,
    ///         Ram = 2048,
    ///         ImageName = "ubuntu:latest",
    ///         ImagePassword = serverImagePassword.Result,
    ///         Nic = new Ionoscloud.Compute.Inputs.ServerNicArgs
    ///         {
    ///             Lan = testLan.Id,
    ///             Name = "test_nic",
    ///             Dhcp = true,
    ///             Dhcpv6 = false,
    ///             Ipv6CidrBlock = ipv6CidrBlock,
    ///             FirewallActive = false,
    ///         },
    ///         Volume = new Ionoscloud.Compute.Inputs.ServerVolumeArgs
    ///         {
    ///             Name = "test_volume",
    ///             DiskType = "HDD",
    ///             Size = 10,
    ///             LicenceType = "OTHER",
    ///         },
    ///     });
    /// 
    ///     var example = new Ionoscloud.Vpn.IpsecGateway("example", new()
    ///     {
    ///         Name = "ipsec-gateway",
    ///         Location = "de/fra",
    ///         GatewayIp = testIpblock.Ips.Apply(ips =&gt; ips[0]),
    ///         Version = "IKEv2",
    ///         Description = "This gateway connects site A to VDC X.",
    ///         Connections = new[]
    ///         {
    ///             new Ionoscloud.Vpn.Inputs.IpsecGatewayConnectionArgs
    ///             {
    ///                 DatacenterId = testDatacenter.Id,
    ///                 LanId = testLan.Id,
    ///                 Ipv4Cidr = "ipv4_cidr_block_from_nic",
    ///                 Ipv6Cidr = "ipv6_cidr_block_from_dc",
    ///             },
    ///         },
    ///     });
    /// 
    ///     var exampleIpsecTunnel = new Ionoscloud.Vpn.IpsecTunnel("example", new()
    ///     {
    ///         Location = "de/fra",
    ///         GatewayId = example.Id,
    ///         Name = "example-tunnel",
    ///         RemoteHost = "vpn.mycompany.com",
    ///         Description = "Allows local subnet X to connect to virtual network Y.",
    ///         Auth = new Ionoscloud.Vpn.Inputs.IpsecTunnelAuthArgs
    ///         {
    ///             Method = "PSK",
    ///             PskKey = "X2wosbaw74M8hQGbK3jCCaEusR6CCFRa",
    ///         },
    ///         Ike = new Ionoscloud.Vpn.Inputs.IpsecTunnelIkeArgs
    ///         {
    ///             DiffieHellmanGroup = "16-MODP4096",
    ///             EncryptionAlgorithm = "AES256",
    ///             IntegrityAlgorithm = "SHA256",
    ///             Lifetime = 86400,
    ///         },
    ///         Esps = new[]
    ///         {
    ///             new Ionoscloud.Vpn.Inputs.IpsecTunnelEspArgs
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
    /// $ pulumi import ionoscloud:vpn/ipsecTunnel:IpsecTunnel example location:gateway_id:tunnel_id
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:vpn/ipsecTunnel:IpsecTunnel")]
    public partial class IpsecTunnel : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
        /// items: 1.
        /// </summary>
        [Output("auth")]
        public Output<Outputs.IpsecTunnelAuth> Auth { get; private set; } = null!;

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
        public Output<ImmutableArray<Outputs.IpsecTunnelEsp>> Esps { get; private set; } = null!;

        /// <summary>
        /// [string] The ID of the IPSec Gateway that the tunnel belongs to.
        /// </summary>
        [Output("gatewayId")]
        public Output<string> GatewayId { get; private set; } = null!;

        /// <summary>
        /// [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
        /// </summary>
        [Output("ike")]
        public Output<Outputs.IpsecTunnelIke> Ike { get; private set; } = null!;

        /// <summary>
        /// [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
        /// gb/lhr, us/ewr, us/las, us/mci, fr/par
        /// </summary>
        [Output("location")]
        public Output<string?> Location { get; private set; } = null!;

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
        /// Create a IpsecTunnel resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public IpsecTunnel(string name, IpsecTunnelArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:vpn/ipsecTunnel:IpsecTunnel", name, args ?? new IpsecTunnelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private IpsecTunnel(string name, Input<string> id, IpsecTunnelState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:vpn/ipsecTunnel:IpsecTunnel", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing IpsecTunnel resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static IpsecTunnel Get(string name, Input<string> id, IpsecTunnelState? state = null, CustomResourceOptions? options = null)
        {
            return new IpsecTunnel(name, id, state, options);
        }
    }

    public sealed class IpsecTunnelArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
        /// items: 1.
        /// </summary>
        [Input("auth", required: true)]
        public Input<Inputs.IpsecTunnelAuthArgs> Auth { get; set; } = null!;

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
        private InputList<Inputs.IpsecTunnelEspArgs>? _esps;

        /// <summary>
        /// [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
        /// </summary>
        public InputList<Inputs.IpsecTunnelEspArgs> Esps
        {
            get => _esps ?? (_esps = new InputList<Inputs.IpsecTunnelEspArgs>());
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
        public Input<Inputs.IpsecTunnelIkeArgs> Ike { get; set; } = null!;

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

        public IpsecTunnelArgs()
        {
        }
        public static new IpsecTunnelArgs Empty => new IpsecTunnelArgs();
    }

    public sealed class IpsecTunnelState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
        /// items: 1.
        /// </summary>
        [Input("auth")]
        public Input<Inputs.IpsecTunnelAuthGetArgs>? Auth { get; set; }

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
        private InputList<Inputs.IpsecTunnelEspGetArgs>? _esps;

        /// <summary>
        /// [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
        /// </summary>
        public InputList<Inputs.IpsecTunnelEspGetArgs> Esps
        {
            get => _esps ?? (_esps = new InputList<Inputs.IpsecTunnelEspGetArgs>());
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
        public Input<Inputs.IpsecTunnelIkeGetArgs>? Ike { get; set; }

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

        public IpsecTunnelState()
        {
        }
        public static new IpsecTunnelState Empty => new IpsecTunnelState();
    }
}
