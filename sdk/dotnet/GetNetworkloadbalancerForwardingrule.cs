// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetNetworkloadbalancerForwardingrule
    {
        /// <summary>
        /// The **Network Load Balancer Forwarding Rule data source** can be used to search for and return existing network forwarding rules.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// </summary>
        public static Task<GetNetworkloadbalancerForwardingruleResult> InvokeAsync(GetNetworkloadbalancerForwardingruleArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetNetworkloadbalancerForwardingruleResult>("ionoscloud:index/getNetworkloadbalancerForwardingrule:getNetworkloadbalancerForwardingrule", args ?? new GetNetworkloadbalancerForwardingruleArgs(), options.WithDefaults());

        /// <summary>
        /// The **Network Load Balancer Forwarding Rule data source** can be used to search for and return existing network forwarding rules.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// </summary>
        public static Output<GetNetworkloadbalancerForwardingruleResult> Invoke(GetNetworkloadbalancerForwardingruleInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetNetworkloadbalancerForwardingruleResult>("ionoscloud:index/getNetworkloadbalancerForwardingrule:getNetworkloadbalancerForwardingrule", args ?? new GetNetworkloadbalancerForwardingruleInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **Network Load Balancer Forwarding Rule data source** can be used to search for and return existing network forwarding rules.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// </summary>
        public static Output<GetNetworkloadbalancerForwardingruleResult> Invoke(GetNetworkloadbalancerForwardingruleInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetNetworkloadbalancerForwardingruleResult>("ionoscloud:index/getNetworkloadbalancerForwardingrule:getNetworkloadbalancerForwardingrule", args ?? new GetNetworkloadbalancerForwardingruleInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNetworkloadbalancerForwardingruleArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Datacenter's UUID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public string DatacenterId { get; set; } = null!;

        /// <summary>
        /// ID of the network load balancer forwarding rule you want to search for.
        /// 
        /// Both `datacenter_id` and `networkloadbalancer_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of an existing network load balancer forwarding rule that you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// Network Load Balancer's UUID.
        /// </summary>
        [Input("networkloadbalancerId", required: true)]
        public string NetworkloadbalancerId { get; set; } = null!;

        public GetNetworkloadbalancerForwardingruleArgs()
        {
        }
        public static new GetNetworkloadbalancerForwardingruleArgs Empty => new GetNetworkloadbalancerForwardingruleArgs();
    }

    public sealed class GetNetworkloadbalancerForwardingruleInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Datacenter's UUID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// ID of the network load balancer forwarding rule you want to search for.
        /// 
        /// Both `datacenter_id` and `networkloadbalancer_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of an existing network load balancer forwarding rule that you want to search for.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Network Load Balancer's UUID.
        /// </summary>
        [Input("networkloadbalancerId", required: true)]
        public Input<string> NetworkloadbalancerId { get; set; } = null!;

        public GetNetworkloadbalancerForwardingruleInvokeArgs()
        {
        }
        public static new GetNetworkloadbalancerForwardingruleInvokeArgs Empty => new GetNetworkloadbalancerForwardingruleInvokeArgs();
    }


    [OutputType]
    public sealed class GetNetworkloadbalancerForwardingruleResult
    {
        /// <summary>
        /// Algorithm for the balancing.
        /// </summary>
        public readonly string Algorithm;
        public readonly string DatacenterId;
        /// <summary>
        /// Health check attributes for Network Load Balancer forwarding rule target.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetNetworkloadbalancerForwardingruleHealthCheckResult> HealthChecks;
        /// <summary>
        /// The id of that Network Load Balancer forwarding rule.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// Listening IP. (inbound)
        /// </summary>
        public readonly string ListenerIp;
        /// <summary>
        /// Listening port number. (inbound) (range: 1 to 65535)
        /// </summary>
        public readonly int ListenerPort;
        /// <summary>
        /// The name of that Network Load Balancer forwarding rule.
        /// </summary>
        public readonly string? Name;
        public readonly string NetworkloadbalancerId;
        /// <summary>
        /// Protocol of the balancing.
        /// </summary>
        public readonly string Protocol;
        /// <summary>
        /// Array of items in that collection.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetNetworkloadbalancerForwardingruleTargetResult> Targets;

        [OutputConstructor]
        private GetNetworkloadbalancerForwardingruleResult(
            string algorithm,

            string datacenterId,

            ImmutableArray<Outputs.GetNetworkloadbalancerForwardingruleHealthCheckResult> healthChecks,

            string? id,

            string listenerIp,

            int listenerPort,

            string? name,

            string networkloadbalancerId,

            string protocol,

            ImmutableArray<Outputs.GetNetworkloadbalancerForwardingruleTargetResult> targets)
        {
            Algorithm = algorithm;
            DatacenterId = datacenterId;
            HealthChecks = healthChecks;
            Id = id;
            ListenerIp = listenerIp;
            ListenerPort = listenerPort;
            Name = name;
            NetworkloadbalancerId = networkloadbalancerId;
            Protocol = protocol;
            Targets = targets;
        }
    }
}
