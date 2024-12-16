// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Vpn
{
    public static class GetWireguardPeer
    {
        public static Task<GetWireguardPeerResult> InvokeAsync(GetWireguardPeerArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetWireguardPeerResult>("ionoscloud:vpn/getWireguardPeer:getWireguardPeer", args ?? new GetWireguardPeerArgs(), options.WithDefaults());

        public static Output<GetWireguardPeerResult> Invoke(GetWireguardPeerInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetWireguardPeerResult>("ionoscloud:vpn/getWireguardPeer:getWireguardPeer", args ?? new GetWireguardPeerInvokeArgs(), options.WithDefaults());

        public static Output<GetWireguardPeerResult> Invoke(GetWireguardPeerInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetWireguardPeerResult>("ionoscloud:vpn/getWireguardPeer:getWireguardPeer", args ?? new GetWireguardPeerInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetWireguardPeerArgs : global::Pulumi.InvokeArgs
    {
        [Input("gatewayId", required: true)]
        public string GatewayId { get; set; } = null!;

        [Input("id")]
        public string? Id { get; set; }

        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        [Input("name")]
        public string? Name { get; set; }

        public GetWireguardPeerArgs()
        {
        }
        public static new GetWireguardPeerArgs Empty => new GetWireguardPeerArgs();
    }

    public sealed class GetWireguardPeerInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("gatewayId", required: true)]
        public Input<string> GatewayId { get; set; } = null!;

        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetWireguardPeerInvokeArgs()
        {
        }
        public static new GetWireguardPeerInvokeArgs Empty => new GetWireguardPeerInvokeArgs();
    }


    [OutputType]
    public sealed class GetWireguardPeerResult
    {
        public readonly ImmutableArray<string> AllowedIps;
        public readonly string Description;
        public readonly ImmutableArray<Outputs.GetWireguardPeerEndpointResult> Endpoints;
        public readonly string GatewayId;
        public readonly string? Id;
        public readonly string Location;
        public readonly string Name;
        public readonly string PublicKey;
        public readonly string Status;

        [OutputConstructor]
        private GetWireguardPeerResult(
            ImmutableArray<string> allowedIps,

            string description,

            ImmutableArray<Outputs.GetWireguardPeerEndpointResult> endpoints,

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
