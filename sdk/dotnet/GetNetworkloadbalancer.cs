// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetNetworkloadbalancer
    {
        /// <summary>
        /// The **Network Load Balancer data source** can be used to search for and return existing network load balancers.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.GetNetworkloadbalancer.Invoke(new()
        ///     {
        ///         DatacenterId = ionoscloud_datacenter.Example.Id,
        ///         Name = "Network Load Balancer Name",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetNetworkloadbalancerResult> InvokeAsync(GetNetworkloadbalancerArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetNetworkloadbalancerResult>("ionoscloud:index/getNetworkloadbalancer:getNetworkloadbalancer", args ?? new GetNetworkloadbalancerArgs(), options.WithDefaults());

        /// <summary>
        /// The **Network Load Balancer data source** can be used to search for and return existing network load balancers.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.GetNetworkloadbalancer.Invoke(new()
        ///     {
        ///         DatacenterId = ionoscloud_datacenter.Example.Id,
        ///         Name = "Network Load Balancer Name",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetNetworkloadbalancerResult> Invoke(GetNetworkloadbalancerInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetNetworkloadbalancerResult>("ionoscloud:index/getNetworkloadbalancer:getNetworkloadbalancer", args ?? new GetNetworkloadbalancerInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNetworkloadbalancerArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Datacenter's UUID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public string DatacenterId { get; set; } = null!;

        /// <summary>
        /// ID of the network load balancer you want to search for.
        /// 
        /// `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of an existing network load balancer that you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetNetworkloadbalancerArgs()
        {
        }
        public static new GetNetworkloadbalancerArgs Empty => new GetNetworkloadbalancerArgs();
    }

    public sealed class GetNetworkloadbalancerInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Datacenter's UUID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// ID of the network load balancer you want to search for.
        /// 
        /// `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of an existing network load balancer that you want to search for.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetNetworkloadbalancerInvokeArgs()
        {
        }
        public static new GetNetworkloadbalancerInvokeArgs Empty => new GetNetworkloadbalancerInvokeArgs();
    }


    [OutputType]
    public sealed class GetNetworkloadbalancerResult
    {
        /// <summary>
        /// Turn logging on and off for this product. Default value is 'false'.
        /// </summary>
        public readonly bool CentralLogging;
        public readonly string DatacenterId;
        /// <summary>
        /// Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetNetworkloadbalancerFlowlogResult> Flowlogs;
        /// <summary>
        /// Id of that Network Load Balancer
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// Collection of IP addresses of the Network Load Balancer. (inbound and outbound) IP of the listenerLan must be a customer reserved IP for the public load balancer and private IP for the private load balancer.
        /// </summary>
        public readonly ImmutableArray<string> Ips;
        /// <summary>
        /// Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain valid subnet mask. If user will not provide any IP then the system will generate one IP with /24 subnet.
        /// </summary>
        public readonly ImmutableArray<string> LbPrivateIps;
        /// <summary>
        /// Id of the listening LAN. (inbound)
        /// </summary>
        public readonly int ListenerLan;
        public readonly string LoggingFormat;
        /// <summary>
        /// Specifies the name of the flow log.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// Id of the balanced private target LAN. (outbound)
        /// </summary>
        public readonly int TargetLan;

        [OutputConstructor]
        private GetNetworkloadbalancerResult(
            bool centralLogging,

            string datacenterId,

            ImmutableArray<Outputs.GetNetworkloadbalancerFlowlogResult> flowlogs,

            string? id,

            ImmutableArray<string> ips,

            ImmutableArray<string> lbPrivateIps,

            int listenerLan,

            string loggingFormat,

            string? name,

            int targetLan)
        {
            CentralLogging = centralLogging;
            DatacenterId = datacenterId;
            Flowlogs = flowlogs;
            Id = id;
            Ips = ips;
            LbPrivateIps = lbPrivateIps;
            ListenerLan = listenerLan;
            LoggingFormat = loggingFormat;
            Name = name;
            TargetLan = targetLan;
        }
    }
}
