// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.K8s
{
    [IonoscloudResourceType("ionoscloud:k8s/cluster:Cluster")]
    public partial class Cluster : global::Pulumi.CustomResource
    {
        /// <summary>
        /// When set to true, allows the update of immutable fields by destroying and re-creating the cluster.
        /// </summary>
        [Output("allowReplace")]
        public Output<bool?> AllowReplace { get; private set; } = null!;

        /// <summary>
        /// Access to the K8s API server is restricted to these CIDRs. Cluster-internal traffic is not affected by this restriction.
        /// If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will
        /// be used: 32 for IPv4 and 128 for IPv6.
        /// </summary>
        [Output("apiSubnetAllowLists")]
        public Output<ImmutableArray<string>> ApiSubnetAllowLists { get; private set; } = null!;

        /// <summary>
        /// The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported.
        /// The provider will ignore downgrades of patch level.
        /// </summary>
        [Output("k8sVersion")]
        public Output<string> K8sVersion { get; private set; } = null!;

        /// <summary>
        /// This attribute is mandatory if the cluster is private. The location must be enabled for your contract, or you must have
        /// a data center at that location. This attribute is immutable.
        /// </summary>
        [Output("location")]
        public Output<string?> Location { get; private set; } = null!;

        /// <summary>
        /// A maintenance window comprise of a day of the week and a time for maintenance to be allowed
        /// </summary>
        [Output("maintenanceWindow")]
        public Output<Outputs.ClusterMaintenanceWindow> MaintenanceWindow { get; private set; } = null!;

        /// <summary>
        /// The desired name for the cluster
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The NAT gateway IP of the cluster if the cluster is private. This attribute is immutable. Must be a reserved IP in the
        /// same location as the cluster's location. This attribute is mandatory if the cluster is private.
        /// </summary>
        [Output("natGatewayIp")]
        public Output<string?> NatGatewayIp { get; private set; } = null!;

        /// <summary>
        /// The node subnet of the cluster, if the cluster is private. This attribute is optional and immutable. Must be a valid
        /// CIDR notation for an IPv4 network prefix of 16 bits length.
        /// </summary>
        [Output("nodeSubnet")]
        public Output<string> NodeSubnet { get; private set; } = null!;

        /// <summary>
        /// The indicator if the cluster is public or private.
        /// </summary>
        [Output("public")]
        public Output<bool?> Public { get; private set; } = null!;

        /// <summary>
        /// List of Object Storage bucket configured for K8s usage. For now it contains only an Object Storage bucket used to store
        /// K8s API audit logs.
        /// </summary>
        [Output("s3Buckets")]
        public Output<ImmutableArray<Outputs.ClusterS3Bucket>> S3Buckets { get; private set; } = null!;

        /// <summary>
        /// List of versions that may be used for node pools under this cluster
        /// </summary>
        [Output("viableNodePoolVersions")]
        public Output<ImmutableArray<string>> ViableNodePoolVersions { get; private set; } = null!;


        /// <summary>
        /// Create a Cluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Cluster(string name, ClusterArgs? args = null, CustomResourceOptions? options = null)
            : base("ionoscloud:k8s/cluster:Cluster", name, args ?? new ClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Cluster(string name, Input<string> id, ClusterState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:k8s/cluster:Cluster", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Cluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Cluster Get(string name, Input<string> id, ClusterState? state = null, CustomResourceOptions? options = null)
        {
            return new Cluster(name, id, state, options);
        }
    }

    public sealed class ClusterArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// When set to true, allows the update of immutable fields by destroying and re-creating the cluster.
        /// </summary>
        [Input("allowReplace")]
        public Input<bool>? AllowReplace { get; set; }

        [Input("apiSubnetAllowLists")]
        private InputList<string>? _apiSubnetAllowLists;

        /// <summary>
        /// Access to the K8s API server is restricted to these CIDRs. Cluster-internal traffic is not affected by this restriction.
        /// If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will
        /// be used: 32 for IPv4 and 128 for IPv6.
        /// </summary>
        public InputList<string> ApiSubnetAllowLists
        {
            get => _apiSubnetAllowLists ?? (_apiSubnetAllowLists = new InputList<string>());
            set => _apiSubnetAllowLists = value;
        }

        /// <summary>
        /// The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported.
        /// The provider will ignore downgrades of patch level.
        /// </summary>
        [Input("k8sVersion")]
        public Input<string>? K8sVersion { get; set; }

        /// <summary>
        /// This attribute is mandatory if the cluster is private. The location must be enabled for your contract, or you must have
        /// a data center at that location. This attribute is immutable.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// A maintenance window comprise of a day of the week and a time for maintenance to be allowed
        /// </summary>
        [Input("maintenanceWindow")]
        public Input<Inputs.ClusterMaintenanceWindowArgs>? MaintenanceWindow { get; set; }

        /// <summary>
        /// The desired name for the cluster
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The NAT gateway IP of the cluster if the cluster is private. This attribute is immutable. Must be a reserved IP in the
        /// same location as the cluster's location. This attribute is mandatory if the cluster is private.
        /// </summary>
        [Input("natGatewayIp")]
        public Input<string>? NatGatewayIp { get; set; }

        /// <summary>
        /// The node subnet of the cluster, if the cluster is private. This attribute is optional and immutable. Must be a valid
        /// CIDR notation for an IPv4 network prefix of 16 bits length.
        /// </summary>
        [Input("nodeSubnet")]
        public Input<string>? NodeSubnet { get; set; }

        /// <summary>
        /// The indicator if the cluster is public or private.
        /// </summary>
        [Input("public")]
        public Input<bool>? Public { get; set; }

        [Input("s3Buckets")]
        private InputList<Inputs.ClusterS3BucketArgs>? _s3Buckets;

        /// <summary>
        /// List of Object Storage bucket configured for K8s usage. For now it contains only an Object Storage bucket used to store
        /// K8s API audit logs.
        /// </summary>
        public InputList<Inputs.ClusterS3BucketArgs> S3Buckets
        {
            get => _s3Buckets ?? (_s3Buckets = new InputList<Inputs.ClusterS3BucketArgs>());
            set => _s3Buckets = value;
        }

        public ClusterArgs()
        {
        }
        public static new ClusterArgs Empty => new ClusterArgs();
    }

    public sealed class ClusterState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// When set to true, allows the update of immutable fields by destroying and re-creating the cluster.
        /// </summary>
        [Input("allowReplace")]
        public Input<bool>? AllowReplace { get; set; }

        [Input("apiSubnetAllowLists")]
        private InputList<string>? _apiSubnetAllowLists;

        /// <summary>
        /// Access to the K8s API server is restricted to these CIDRs. Cluster-internal traffic is not affected by this restriction.
        /// If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will
        /// be used: 32 for IPv4 and 128 for IPv6.
        /// </summary>
        public InputList<string> ApiSubnetAllowLists
        {
            get => _apiSubnetAllowLists ?? (_apiSubnetAllowLists = new InputList<string>());
            set => _apiSubnetAllowLists = value;
        }

        /// <summary>
        /// The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported.
        /// The provider will ignore downgrades of patch level.
        /// </summary>
        [Input("k8sVersion")]
        public Input<string>? K8sVersion { get; set; }

        /// <summary>
        /// This attribute is mandatory if the cluster is private. The location must be enabled for your contract, or you must have
        /// a data center at that location. This attribute is immutable.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// A maintenance window comprise of a day of the week and a time for maintenance to be allowed
        /// </summary>
        [Input("maintenanceWindow")]
        public Input<Inputs.ClusterMaintenanceWindowGetArgs>? MaintenanceWindow { get; set; }

        /// <summary>
        /// The desired name for the cluster
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The NAT gateway IP of the cluster if the cluster is private. This attribute is immutable. Must be a reserved IP in the
        /// same location as the cluster's location. This attribute is mandatory if the cluster is private.
        /// </summary>
        [Input("natGatewayIp")]
        public Input<string>? NatGatewayIp { get; set; }

        /// <summary>
        /// The node subnet of the cluster, if the cluster is private. This attribute is optional and immutable. Must be a valid
        /// CIDR notation for an IPv4 network prefix of 16 bits length.
        /// </summary>
        [Input("nodeSubnet")]
        public Input<string>? NodeSubnet { get; set; }

        /// <summary>
        /// The indicator if the cluster is public or private.
        /// </summary>
        [Input("public")]
        public Input<bool>? Public { get; set; }

        [Input("s3Buckets")]
        private InputList<Inputs.ClusterS3BucketGetArgs>? _s3Buckets;

        /// <summary>
        /// List of Object Storage bucket configured for K8s usage. For now it contains only an Object Storage bucket used to store
        /// K8s API audit logs.
        /// </summary>
        public InputList<Inputs.ClusterS3BucketGetArgs> S3Buckets
        {
            get => _s3Buckets ?? (_s3Buckets = new InputList<Inputs.ClusterS3BucketGetArgs>());
            set => _s3Buckets = value;
        }

        [Input("viableNodePoolVersions")]
        private InputList<string>? _viableNodePoolVersions;

        /// <summary>
        /// List of versions that may be used for node pools under this cluster
        /// </summary>
        public InputList<string> ViableNodePoolVersions
        {
            get => _viableNodePoolVersions ?? (_viableNodePoolVersions = new InputList<string>());
            set => _viableNodePoolVersions = value;
        }

        public ClusterState()
        {
        }
        public static new ClusterState Empty => new ClusterState();
    }
}
