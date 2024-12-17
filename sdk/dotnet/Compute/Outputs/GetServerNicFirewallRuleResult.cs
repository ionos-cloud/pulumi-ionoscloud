// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute.Outputs
{

    [OutputType]
    public sealed class GetServerNicFirewallRuleResult
    {
        /// <summary>
        /// Defines the allowed code (from 0 to 254) if protocol ICMP is chosen
        /// </summary>
        public readonly int IcmpCode;
        /// <summary>
        /// Defines the allowed type (from 0 to 254) if the protocol ICMP is chosen
        /// </summary>
        public readonly int IcmpType;
        /// <summary>
        /// ID of the server you want to search for.
        /// 
        /// `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Name of an existing server that you want to search for.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen
        /// </summary>
        public readonly int PortRangeEnd;
        /// <summary>
        /// Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen
        /// </summary>
        public readonly int PortRangeStart;
        /// <summary>
        /// he protocol for the rule
        /// </summary>
        public readonly string Protocol;
        /// <summary>
        /// Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs
        /// </summary>
        public readonly string SourceIp;
        /// <summary>
        /// Only traffic originating from the respective MAC address is allowed
        /// </summary>
        public readonly string SourceMac;
        /// <summary>
        /// In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed
        /// </summary>
        public readonly string TargetIp;
        /// <summary>
        /// The type of firewall rule
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GetServerNicFirewallRuleResult(
            int icmpCode,

            int icmpType,

            string id,

            string name,

            int portRangeEnd,

            int portRangeStart,

            string protocol,

            string sourceIp,

            string sourceMac,

            string targetIp,

            string type)
        {
            IcmpCode = icmpCode;
            IcmpType = icmpType;
            Id = id;
            Name = name;
            PortRangeEnd = portRangeEnd;
            PortRangeStart = portRangeStart;
            Protocol = protocol;
            SourceIp = sourceIp;
            SourceMac = sourceMac;
            TargetIp = targetIp;
            Type = type;
        }
    }
}
