// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    /// <summary>
    /// Create clusters of Network File Storage (NFS) on IonosCloud.
    /// 
    /// ## Example Usage
    /// 
    /// &lt;!--Start PulumiCodeChooser --&gt;
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Pulumi.Ionoscloud;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     // Basic example
    ///     var nfsDc = new Ionoscloud.Compute.Datacenter("nfsDc", new()
    ///     {
    ///         Location = "de/txl",
    ///         Description = "Datacenter Description",
    ///         SecAuthProtection = false,
    ///     });
    /// 
    ///     var nfsLan = new Ionoscloud.Lan("nfsLan", new()
    ///     {
    ///         DatacenterId = nfsDc.Id,
    ///         Public = false,
    ///     });
    /// 
    ///     var example = new Ionoscloud.NfsCluster("example", new()
    ///     {
    ///         Location = "de/txl",
    ///         Size = 2,
    ///         Nfs = new Ionoscloud.Inputs.NfsClusterNfsArgs
    ///         {
    ///             MinVersion = "4.2",
    ///         },
    ///         Connections = new Ionoscloud.Inputs.NfsClusterConnectionsArgs
    ///         {
    ///             DatacenterId = nfsDc.Id,
    ///             IpAddress = "192.168.100.10/24",
    ///             Lan = nfsLan.Id,
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// &lt;!--End PulumiCodeChooser --&gt;
    /// 
    /// ## Import
    /// 
    /// A Network File Storage Cluster resource can be imported using its `location` and `resource id`:
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:index/nfsCluster:NfsCluster name {location}:{uuid}
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:index/nfsCluster:NfsCluster")]
    public partial class NfsCluster : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The network connections for the Network File Storage Cluster.
        /// </summary>
        [Output("connections")]
        public Output<Outputs.NfsClusterConnections> Connections { get; private set; } = null!;

        /// <summary>
        /// The location where the Network File Storage cluster is located.
        /// - `de/fra` - Frankfurt
        /// - `de/txl` - Berlin
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// The name of the Network File Storage cluster.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("nfs")]
        public Output<Outputs.NfsClusterNfs?> Nfs { get; private set; } = null!;

        /// <summary>
        /// The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
        /// </summary>
        [Output("size")]
        public Output<int> Size { get; private set; } = null!;


        /// <summary>
        /// Create a NfsCluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NfsCluster(string name, NfsClusterArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:index/nfsCluster:NfsCluster", name, args ?? new NfsClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NfsCluster(string name, Input<string> id, NfsClusterState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/nfsCluster:NfsCluster", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/ionos-cloud/pulumi-ionoscloud/",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing NfsCluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NfsCluster Get(string name, Input<string> id, NfsClusterState? state = null, CustomResourceOptions? options = null)
        {
            return new NfsCluster(name, id, state, options);
        }
    }

    public sealed class NfsClusterArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The network connections for the Network File Storage Cluster.
        /// </summary>
        [Input("connections", required: true)]
        public Input<Inputs.NfsClusterConnectionsArgs> Connections { get; set; } = null!;

        /// <summary>
        /// The location where the Network File Storage cluster is located.
        /// - `de/fra` - Frankfurt
        /// - `de/txl` - Berlin
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        /// <summary>
        /// The name of the Network File Storage cluster.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nfs")]
        public Input<Inputs.NfsClusterNfsArgs>? Nfs { get; set; }

        /// <summary>
        /// The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
        /// </summary>
        [Input("size", required: true)]
        public Input<int> Size { get; set; } = null!;

        public NfsClusterArgs()
        {
        }
        public static new NfsClusterArgs Empty => new NfsClusterArgs();
    }

    public sealed class NfsClusterState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The network connections for the Network File Storage Cluster.
        /// </summary>
        [Input("connections")]
        public Input<Inputs.NfsClusterConnectionsGetArgs>? Connections { get; set; }

        /// <summary>
        /// The location where the Network File Storage cluster is located.
        /// - `de/fra` - Frankfurt
        /// - `de/txl` - Berlin
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The name of the Network File Storage cluster.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nfs")]
        public Input<Inputs.NfsClusterNfsGetArgs>? Nfs { get; set; }

        /// <summary>
        /// The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
        /// </summary>
        [Input("size")]
        public Input<int>? Size { get; set; }

        public NfsClusterState()
        {
        }
        public static new NfsClusterState Empty => new NfsClusterState();
    }
}
