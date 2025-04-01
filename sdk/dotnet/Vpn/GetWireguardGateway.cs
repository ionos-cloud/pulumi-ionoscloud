// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Vpn
{
    public static class GetWireguardGateway
    {
        /// <summary>
        /// The `ionoscloud.vpn.WireguardGateway` data source provides information about a specific IonosCloud VPN WireGuard Gateway. You can use this data source to retrieve details of a WireGuard Gateway for use in other resources and configurations.
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
        ///     var example = Ionoscloud.Vpn.GetWireguardGateway.Invoke(new()
        ///     {
        ///         Location = "de/fra",
        ///         Name = "example-gateway",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["vpnWireguardGatewayPublicKey"] = exampleVpnWireguardGateway.PublicKey,
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Task<GetWireguardGatewayResult> InvokeAsync(GetWireguardGatewayArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetWireguardGatewayResult>("ionoscloud:vpn/getWireguardGateway:getWireguardGateway", args ?? new GetWireguardGatewayArgs(), options.WithDefaults());

        /// <summary>
        /// The `ionoscloud.vpn.WireguardGateway` data source provides information about a specific IonosCloud VPN WireGuard Gateway. You can use this data source to retrieve details of a WireGuard Gateway for use in other resources and configurations.
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
        ///     var example = Ionoscloud.Vpn.GetWireguardGateway.Invoke(new()
        ///     {
        ///         Location = "de/fra",
        ///         Name = "example-gateway",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["vpnWireguardGatewayPublicKey"] = exampleVpnWireguardGateway.PublicKey,
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetWireguardGatewayResult> Invoke(GetWireguardGatewayInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetWireguardGatewayResult>("ionoscloud:vpn/getWireguardGateway:getWireguardGateway", args ?? new GetWireguardGatewayInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The `ionoscloud.vpn.WireguardGateway` data source provides information about a specific IonosCloud VPN WireGuard Gateway. You can use this data source to retrieve details of a WireGuard Gateway for use in other resources and configurations.
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
        ///     var example = Ionoscloud.Vpn.GetWireguardGateway.Invoke(new()
        ///     {
        ///         Location = "de/fra",
        ///         Name = "example-gateway",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["vpnWireguardGatewayPublicKey"] = exampleVpnWireguardGateway.PublicKey,
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetWireguardGatewayResult> Invoke(GetWireguardGatewayInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetWireguardGatewayResult>("ionoscloud:vpn/getWireguardGateway:getWireguardGateway", args ?? new GetWireguardGatewayInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetWireguardGatewayArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The description of the WireGuard Gateway.
        /// </summary>
        [Input("description")]
        public string? Description { get; set; }

        /// <summary>
        /// [String] The ID of the WireGuard Gateway.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// [String] The location of the WireGuard Gateway.
        /// </summary>
        [Input("location")]
        public string? Location { get; set; }

        /// <summary>
        /// [String] The name of the WireGuard Gateway.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetWireguardGatewayArgs()
        {
        }
        public static new GetWireguardGatewayArgs Empty => new GetWireguardGatewayArgs();
    }

    public sealed class GetWireguardGatewayInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The description of the WireGuard Gateway.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// [String] The ID of the WireGuard Gateway.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// [String] The location of the WireGuard Gateway.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// [String] The name of the WireGuard Gateway.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetWireguardGatewayInvokeArgs()
        {
        }
        public static new GetWireguardGatewayInvokeArgs Empty => new GetWireguardGatewayInvokeArgs();
    }


    [OutputType]
    public sealed class GetWireguardGatewayResult
    {
        /// <summary>
        /// A list of connection configurations for the WireGuard Gateway. Each `connections` block contains:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetWireguardGatewayConnectionResult> Connections;
        /// <summary>
        /// The description of the WireGuard Gateway.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The IP address of the WireGuard Gateway.
        /// </summary>
        public readonly string GatewayIp;
        public readonly string Id;
        /// <summary>
        /// The IPv4 CIDR for the WireGuard Gateway interface.
        /// </summary>
        public readonly string InterfaceIpv4Cidr;
        /// <summary>
        /// The IPv6 CIDR for the WireGuard Gateway interface.
        /// </summary>
        public readonly string InterfaceIpv6Cidr;
        public readonly int ListenPort;
        public readonly string? Location;
        /// <summary>
        /// A weekly 4 hour-long window, during which maintenance might occur.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetWireguardGatewayMaintenanceWindowResult> MaintenanceWindows;
        public readonly string Name;
        /// <summary>
        /// The public key for the WireGuard Gateway.
        /// </summary>
        public readonly string PublicKey;
        /// <summary>
        /// The current status of the WireGuard Gateway.
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// Gateway performance options.
        /// </summary>
        public readonly string Tier;

        [OutputConstructor]
        private GetWireguardGatewayResult(
            ImmutableArray<Outputs.GetWireguardGatewayConnectionResult> connections,

            string? description,

            string gatewayIp,

            string id,

            string interfaceIpv4Cidr,

            string interfaceIpv6Cidr,

            int listenPort,

            string? location,

            ImmutableArray<Outputs.GetWireguardGatewayMaintenanceWindowResult> maintenanceWindows,

            string name,

            string publicKey,

            string status,

            string tier)
        {
            Connections = connections;
            Description = description;
            GatewayIp = gatewayIp;
            Id = id;
            InterfaceIpv4Cidr = interfaceIpv4Cidr;
            InterfaceIpv6Cidr = interfaceIpv6Cidr;
            ListenPort = listenPort;
            Location = location;
            MaintenanceWindows = maintenanceWindows;
            Name = name;
            PublicKey = publicKey;
            Status = status;
            Tier = tier;
        }
    }
}
