// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Nfs
{
    public static class GetShare
    {
        /// <summary>
        /// Returns information about shares of Network File Storage (NFS) on IonosCloud.
        /// 
        /// ## By ID
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Nfs.GetShare.Invoke(new()
        ///     {
        ///         Location = "location",
        ///         ClusterId = "cluster-id",
        ///         Id = "share-id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ## By Name
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Nfs.GetShare.Invoke(new()
        ///     {
        ///         Location = "location",
        ///         ClusterId = "cluster-id",
        ///         Name = "partial-name",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetShareResult> InvokeAsync(GetShareArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetShareResult>("ionoscloud:nfs/getShare:getShare", args ?? new GetShareArgs(), options.WithDefaults());

        /// <summary>
        /// Returns information about shares of Network File Storage (NFS) on IonosCloud.
        /// 
        /// ## By ID
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Nfs.GetShare.Invoke(new()
        ///     {
        ///         Location = "location",
        ///         ClusterId = "cluster-id",
        ///         Id = "share-id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ## By Name
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Nfs.GetShare.Invoke(new()
        ///     {
        ///         Location = "location",
        ///         ClusterId = "cluster-id",
        ///         Name = "partial-name",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetShareResult> Invoke(GetShareInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetShareResult>("ionoscloud:nfs/getShare:getShare", args ?? new GetShareInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// Returns information about shares of Network File Storage (NFS) on IonosCloud.
        /// 
        /// ## By ID
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Nfs.GetShare.Invoke(new()
        ///     {
        ///         Location = "location",
        ///         ClusterId = "cluster-id",
        ///         Id = "share-id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ## By Name
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Nfs.GetShare.Invoke(new()
        ///     {
        ///         Location = "location",
        ///         ClusterId = "cluster-id",
        ///         Name = "partial-name",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetShareResult> Invoke(GetShareInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetShareResult>("ionoscloud:nfs/getShare:getShare", args ?? new GetShareInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetShareArgs : global::Pulumi.InvokeArgs
    {
        [Input("clientGroups")]
        private List<Inputs.GetShareClientGroupArgs>? _clientGroups;

        /// <summary>
        /// The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
        /// </summary>
        public List<Inputs.GetShareClientGroupArgs> ClientGroups
        {
            get => _clientGroups ?? (_clientGroups = new List<Inputs.GetShareClientGroupArgs>());
            set => _clientGroups = value;
        }

        /// <summary>
        /// The ID of the Network File Storage cluster.
        /// </summary>
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        /// <summary>
        /// The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        /// </summary>
        [Input("gid")]
        public int? Gid { get; set; }

        /// <summary>
        /// ID of the Network File Storage share.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// The location where the Network File Storage share is located.
        /// </summary>
        [Input("location")]
        public string? Location { get; set; }

        /// <summary>
        /// Name of the Network File Storage share.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
        /// </summary>
        [Input("partialMatch")]
        public bool? PartialMatch { get; set; }

        /// <summary>
        /// The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
        /// </summary>
        [Input("quota")]
        public int? Quota { get; set; }

        /// <summary>
        /// The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        /// </summary>
        [Input("uid")]
        public int? Uid { get; set; }

        public GetShareArgs()
        {
        }
        public static new GetShareArgs Empty => new GetShareArgs();
    }

    public sealed class GetShareInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("clientGroups")]
        private InputList<Inputs.GetShareClientGroupInputArgs>? _clientGroups;

        /// <summary>
        /// The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
        /// </summary>
        public InputList<Inputs.GetShareClientGroupInputArgs> ClientGroups
        {
            get => _clientGroups ?? (_clientGroups = new InputList<Inputs.GetShareClientGroupInputArgs>());
            set => _clientGroups = value;
        }

        /// <summary>
        /// The ID of the Network File Storage cluster.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        /// </summary>
        [Input("gid")]
        public Input<int>? Gid { get; set; }

        /// <summary>
        /// ID of the Network File Storage share.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The location where the Network File Storage share is located.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Name of the Network File Storage share.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
        /// </summary>
        [Input("partialMatch")]
        public Input<bool>? PartialMatch { get; set; }

        /// <summary>
        /// The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
        /// </summary>
        [Input("quota")]
        public Input<int>? Quota { get; set; }

        /// <summary>
        /// The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        /// </summary>
        [Input("uid")]
        public Input<int>? Uid { get; set; }

        public GetShareInvokeArgs()
        {
        }
        public static new GetShareInvokeArgs Empty => new GetShareInvokeArgs();
    }


    [OutputType]
    public sealed class GetShareResult
    {
        /// <summary>
        /// The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetShareClientGroupResult> ClientGroups;
        /// <summary>
        /// The ID of the Network File Storage cluster.
        /// </summary>
        public readonly string ClusterId;
        /// <summary>
        /// The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        /// </summary>
        public readonly int Gid;
        /// <summary>
        /// The ID of the Network File Storage share.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The location where the Network File Storage share is located.
        /// </summary>
        public readonly string? Location;
        /// <summary>
        /// The name of the Network File Storage share.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Path to the NFS export. The NFS path is the path to the directory being exported.
        /// </summary>
        public readonly string NfsPath;
        public readonly bool? PartialMatch;
        /// <summary>
        /// The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
        /// </summary>
        public readonly int Quota;
        /// <summary>
        /// The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        /// </summary>
        public readonly int Uid;

        [OutputConstructor]
        private GetShareResult(
            ImmutableArray<Outputs.GetShareClientGroupResult> clientGroups,

            string clusterId,

            int gid,

            string id,

            string? location,

            string name,

            string nfsPath,

            bool? partialMatch,

            int quota,

            int uid)
        {
            ClientGroups = clientGroups;
            ClusterId = clusterId;
            Gid = gid;
            Id = id;
            Location = location;
            Name = name;
            NfsPath = nfsPath;
            PartialMatch = partialMatch;
            Quota = quota;
            Uid = uid;
        }
    }
}
