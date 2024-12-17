// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute
{
    public static class GetNatGateway
    {
        /// <summary>
        /// The **NAT gateway data source** can be used to search for and return existing NAT Gateways.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Task<GetNatGatewayResult> InvokeAsync(GetNatGatewayArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetNatGatewayResult>("ionoscloud:compute/getNatGateway:getNatGateway", args ?? new GetNatGatewayArgs(), options.WithDefaults());

        /// <summary>
        /// The **NAT gateway data source** can be used to search for and return existing NAT Gateways.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Output<GetNatGatewayResult> Invoke(GetNatGatewayInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetNatGatewayResult>("ionoscloud:compute/getNatGateway:getNatGateway", args ?? new GetNatGatewayInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **NAT gateway data source** can be used to search for and return existing NAT Gateways.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Output<GetNatGatewayResult> Invoke(GetNatGatewayInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetNatGatewayResult>("ionoscloud:compute/getNatGateway:getNatGateway", args ?? new GetNatGatewayInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNatGatewayArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Datacenter's UUID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public string DatacenterId { get; set; } = null!;

        /// <summary>
        /// ID of the network load balancer forwarding rule you want to search for.
        /// 
        /// `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of an existing network load balancer forwarding rule that you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetNatGatewayArgs()
        {
        }
        public static new GetNatGatewayArgs Empty => new GetNatGatewayArgs();
    }

    public sealed class GetNatGatewayInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Datacenter's UUID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// ID of the network load balancer forwarding rule you want to search for.
        /// 
        /// `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of an existing network load balancer forwarding rule that you want to search for.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetNatGatewayInvokeArgs()
        {
        }
        public static new GetNatGatewayInvokeArgs Empty => new GetNatGatewayInvokeArgs();
    }


    [OutputType]
    public sealed class GetNatGatewayResult
    {
        public readonly string DatacenterId;
        /// <summary>
        /// Id for the LAN connected to the NAT gateway
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// Collection of LANs connected to the NAT gateway. IPs must contain valid subnet mask. If user will not provide any IP then system will generate an IP with /24 subnet.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetNatGatewayLanResult> Lans;
        /// <summary>
        /// Name of that natgateway
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location
        /// </summary>
        public readonly ImmutableArray<string> PublicIps;

        [OutputConstructor]
        private GetNatGatewayResult(
            string datacenterId,

            string? id,

            ImmutableArray<Outputs.GetNatGatewayLanResult> lans,

            string? name,

            ImmutableArray<string> publicIps)
        {
            DatacenterId = datacenterId;
            Id = id;
            Lans = lans;
            Name = name;
            PublicIps = publicIps;
        }
    }
}
