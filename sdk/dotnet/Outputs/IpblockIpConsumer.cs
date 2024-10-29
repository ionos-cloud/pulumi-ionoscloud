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
    public sealed class IpblockIpConsumer
    {
        public readonly string? DatacenterId;
        public readonly string? DatacenterName;
        public readonly string? Ip;
        public readonly string? K8sClusterUuid;
        public readonly string? K8sNodepoolUuid;
        public readonly string? Mac;
        public readonly string? NicId;
        public readonly string? ServerId;
        public readonly string? ServerName;

        [OutputConstructor]
        private IpblockIpConsumer(
            string? datacenterId,

            string? datacenterName,

            string? ip,

            string? k8sClusterUuid,

            string? k8sNodepoolUuid,

            string? mac,

            string? nicId,

            string? serverId,

            string? serverName)
        {
            DatacenterId = datacenterId;
            DatacenterName = datacenterName;
            Ip = ip;
            K8sClusterUuid = k8sClusterUuid;
            K8sNodepoolUuid = k8sNodepoolUuid;
            Mac = mac;
            NicId = nicId;
            ServerId = serverId;
            ServerName = serverName;
        }
    }
}
