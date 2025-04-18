// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Dbaas.Inputs
{

    public sealed class MongoClusterConnectionsGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("cidrLists", required: true)]
        private InputList<string>? _cidrLists;

        /// <summary>
        /// [List] The list of IPs and subnet for your cluster. Note the following unavailable IP ranges:10.233.64.0/18, 10.233.0.0/18, 10.233.114.0/24. example: [192.168.1.100/24, 192.168.1.101/24]. See [Private IPs](https://www.ionos.com/help/server-cloud-infrastructure/private-network/private-ip-address-ranges/) and [Cluster Setup - Preparing the network](https://docs.ionos.com/cloud/databases/mongodb/api-howtos/create-a-cluster#preparing-the-network).
        /// </summary>
        public InputList<string> CidrLists
        {
            get => _cidrLists ?? (_cidrLists = new InputList<string>());
            set => _cidrLists = value;
        }

        /// <summary>
        /// [string] The datacenter to connect your cluster to.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// [string] The LAN to connect your cluster to.
        /// </summary>
        [Input("lanId", required: true)]
        public Input<string> LanId { get; set; } = null!;

        public MongoClusterConnectionsGetArgs()
        {
        }
        public static new MongoClusterConnectionsGetArgs Empty => new MongoClusterConnectionsGetArgs();
    }
}
