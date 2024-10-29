// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Outputs
{

    [OutputType]
    public sealed class VcpuServerNicFirewall
    {
        public readonly string? IcmpCode;
        public readonly string? IcmpType;
        public readonly string? Id;
        /// <summary>
        /// [string] The name of the server.
        /// </summary>
        public readonly string? Name;
        public readonly int? PortRangeEnd;
        public readonly int? PortRangeStart;
        public readonly string Protocol;
        public readonly string? SourceIp;
        public readonly string? SourceMac;
        public readonly string? TargetIp;
        public readonly string? Type;

        [OutputConstructor]
        private VcpuServerNicFirewall(
            string? icmpCode,

            string? icmpType,

            string? id,

            string? name,

            int? portRangeEnd,

            int? portRangeStart,

            string protocol,

            string? sourceIp,

            string? sourceMac,

            string? targetIp,

            string? type)
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
