// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute
{
    public static class GetFirewall
    {
        /// <summary>
        /// The **Firewall data source** can be used to search for and return an existing FirewallRules. 
        /// You can provide a string for either id or name parameters which will be compared with provisioned Firewall Rules.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned. 
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Task<GetFirewallResult> InvokeAsync(GetFirewallArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetFirewallResult>("ionoscloud:compute/getFirewall:getFirewall", args ?? new GetFirewallArgs(), options.WithDefaults());

        /// <summary>
        /// The **Firewall data source** can be used to search for and return an existing FirewallRules. 
        /// You can provide a string for either id or name parameters which will be compared with provisioned Firewall Rules.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned. 
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Output<GetFirewallResult> Invoke(GetFirewallInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetFirewallResult>("ionoscloud:compute/getFirewall:getFirewall", args ?? new GetFirewallInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **Firewall data source** can be used to search for and return an existing FirewallRules. 
        /// You can provide a string for either id or name parameters which will be compared with provisioned Firewall Rules.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned. 
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Output<GetFirewallResult> Invoke(GetFirewallInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetFirewallResult>("ionoscloud:compute/getFirewall:getFirewall", args ?? new GetFirewallInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetFirewallArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Virtual Data Center ID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public string DatacenterId { get; set; } = null!;

        /// <summary>
        /// ID of the firewall rule you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of an existing firewall rule that you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The NIC ID.
        /// 
        /// Either `name` or   `id` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("nicId", required: true)]
        public string NicId { get; set; } = null!;

        /// <summary>
        /// The Server ID.
        /// </summary>
        [Input("serverId", required: true)]
        public string ServerId { get; set; } = null!;

        public GetFirewallArgs()
        {
        }
        public static new GetFirewallArgs Empty => new GetFirewallArgs();
    }

    public sealed class GetFirewallInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Virtual Data Center ID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// ID of the firewall rule you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of an existing firewall rule that you want to search for.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The NIC ID.
        /// 
        /// Either `name` or   `id` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("nicId", required: true)]
        public Input<string> NicId { get; set; } = null!;

        /// <summary>
        /// The Server ID.
        /// </summary>
        [Input("serverId", required: true)]
        public Input<string> ServerId { get; set; } = null!;

        public GetFirewallInvokeArgs()
        {
        }
        public static new GetFirewallInvokeArgs Empty => new GetFirewallInvokeArgs();
    }


    [OutputType]
    public sealed class GetFirewallResult
    {
        public readonly string DatacenterId;
        /// <summary>
        /// Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
        /// </summary>
        public readonly string IcmpCode;
        /// <summary>
        /// Defines the allowed type (from 0 to 254) if the protocol ICMP is chosen.
        /// </summary>
        public readonly string IcmpType;
        /// <summary>
        /// The id of the firewall rule.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The name of the firewall rule.
        /// </summary>
        public readonly string? Name;
        public readonly string NicId;
        /// <summary>
        /// Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen.
        /// </summary>
        public readonly int PortRangeEnd;
        /// <summary>
        /// Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen.
        /// </summary>
        public readonly int PortRangeStart;
        /// <summary>
        /// The protocol for the rule: TCP, UDP, ICMP, ANY. This property is immutable.
        /// </summary>
        public readonly string Protocol;
        public readonly string ServerId;
        /// <summary>
        /// Only traffic originating from the respective IPv4 address is allowed.
        /// </summary>
        public readonly string SourceIp;
        /// <summary>
        /// Only traffic originating from the respective MAC address is allowed.
        /// </summary>
        public readonly string SourceMac;
        /// <summary>
        /// Only traffic directed to the respective IP address of the NIC is allowed.
        /// </summary>
        public readonly string TargetIp;
        public readonly string Type;

        [OutputConstructor]
        private GetFirewallResult(
            string datacenterId,

            string icmpCode,

            string icmpType,

            string? id,

            string? name,

            string nicId,

            int portRangeEnd,

            int portRangeStart,

            string protocol,

            string serverId,

            string sourceIp,

            string sourceMac,

            string targetIp,

            string type)
        {
            DatacenterId = datacenterId;
            IcmpCode = icmpCode;
            IcmpType = icmpType;
            Id = id;
            Name = name;
            NicId = nicId;
            PortRangeEnd = portRangeEnd;
            PortRangeStart = portRangeStart;
            Protocol = protocol;
            ServerId = serverId;
            SourceIp = sourceIp;
            SourceMac = sourceMac;
            TargetIp = targetIp;
            Type = type;
        }
    }
}
