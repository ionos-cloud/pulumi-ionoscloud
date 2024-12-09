// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetVpnWireguardPeer
    {
        /// <summary>
        /// The `ionoscloud.VpnWireguardGateway` data source provides information about a specific IonosCloud VPN WireGuard Gateway. You can use this data source to retrieve details of a WireGuard Gateway for use in other resources and configurations.
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
        ///     var example = Ionoscloud.GetVpnWireguardPeer.Invoke(new()
        ///     {
        ///         Location = "de/fra",
        ///         GatewayId = "example-gateway",
        ///         Name = "example-peer",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["vpnWireguardPeerPublicKey"] = data.Vpn_wireguard_peer.Example.Public_key,
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Task<GetVpnWireguardPeerResult> InvokeAsync(GetVpnWireguardPeerArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVpnWireguardPeerResult>("ionoscloud:index/getVpnWireguardPeer:getVpnWireguardPeer", args ?? new GetVpnWireguardPeerArgs(), options.WithDefaults());

        /// <summary>
        /// The `ionoscloud.VpnWireguardGateway` data source provides information about a specific IonosCloud VPN WireGuard Gateway. You can use this data source to retrieve details of a WireGuard Gateway for use in other resources and configurations.
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
        ///     var example = Ionoscloud.GetVpnWireguardPeer.Invoke(new()
        ///     {
        ///         Location = "de/fra",
        ///         GatewayId = "example-gateway",
        ///         Name = "example-peer",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["vpnWireguardPeerPublicKey"] = data.Vpn_wireguard_peer.Example.Public_key,
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetVpnWireguardPeerResult> Invoke(GetVpnWireguardPeerInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVpnWireguardPeerResult>("ionoscloud:index/getVpnWireguardPeer:getVpnWireguardPeer", args ?? new GetVpnWireguardPeerInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVpnWireguardPeerArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [String] The ID of the WireGuard Gateway.
        /// </summary>
        [Input("gatewayId", required: true)]
        public string GatewayId { get; set; } = null!;

        /// <summary>
        /// [String] The ID of the WireGuard Peer.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// [String] The location of the WireGuard Gateway.
        /// </summary>
        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        /// <summary>
        /// [String] The name of the WireGuard Peer.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetVpnWireguardPeerArgs()
        {
        }
        public static new GetVpnWireguardPeerArgs Empty => new GetVpnWireguardPeerArgs();
    }

    public sealed class GetVpnWireguardPeerInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [String] The ID of the WireGuard Gateway.
        /// </summary>
        [Input("gatewayId", required: true)]
        public Input<string> GatewayId { get; set; } = null!;

        /// <summary>
        /// [String] The ID of the WireGuard Peer.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// [String] The location of the WireGuard Gateway.
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        /// <summary>
        /// [String] The name of the WireGuard Peer.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetVpnWireguardPeerInvokeArgs()
        {
        }
        public static new GetVpnWireguardPeerInvokeArgs Empty => new GetVpnWireguardPeerInvokeArgs();
    }


    [OutputType]
    public sealed class GetVpnWireguardPeerResult
    {
        /// <summary>
        /// The subnet CIDRs that are allowed to connect to the WireGuard Gateway.
        /// </summary>
        public readonly ImmutableArray<string> AllowedIps;
        /// <summary>
        /// The description of the WireGuard Peer.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The endpoint of the WireGuard Peer.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetVpnWireguardPeerEndpointResult> Endpoints;
        public readonly string GatewayId;
        /// <summary>
        /// The unique ID of the WireGuard Peer.
        /// </summary>
        public readonly string? Id;
        public readonly string Location;
        /// <summary>
        /// The name of the WireGuard Peer.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// WireGuard public key of the connecting peer.
        /// </summary>
        public readonly string PublicKey;
        /// <summary>
        /// The current status of the WireGuard Peer.
        /// </summary>
        public readonly string Status;

        [OutputConstructor]
        private GetVpnWireguardPeerResult(
            ImmutableArray<string> allowedIps,

            string description,

            ImmutableArray<Outputs.GetVpnWireguardPeerEndpointResult> endpoints,

            string gatewayId,

            string? id,

            string location,

            string name,

            string publicKey,

            string status)
        {
            AllowedIps = allowedIps;
            Description = description;
            Endpoints = endpoints;
            GatewayId = gatewayId;
            Id = id;
            Location = location;
            Name = name;
            PublicKey = publicKey;
            Status = status;
        }
    }
}
