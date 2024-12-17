// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute
{
    public static class GetCrossconnect
    {
        /// <summary>
        /// The **Cross Connect data source** can be used to search for and return existing cross connects.
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
        ///     var example = Ionoscloud.Compute.GetCrossconnect.Invoke(new()
        ///     {
        ///         Name = "Cross Connect Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetCrossconnectResult> InvokeAsync(GetCrossconnectArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetCrossconnectResult>("ionoscloud:compute/getCrossconnect:getCrossconnect", args ?? new GetCrossconnectArgs(), options.WithDefaults());

        /// <summary>
        /// The **Cross Connect data source** can be used to search for and return existing cross connects.
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
        ///     var example = Ionoscloud.Compute.GetCrossconnect.Invoke(new()
        ///     {
        ///         Name = "Cross Connect Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetCrossconnectResult> Invoke(GetCrossconnectInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetCrossconnectResult>("ionoscloud:compute/getCrossconnect:getCrossconnect", args ?? new GetCrossconnectInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **Cross Connect data source** can be used to search for and return existing cross connects.
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
        ///     var example = Ionoscloud.Compute.GetCrossconnect.Invoke(new()
        ///     {
        ///         Name = "Cross Connect Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetCrossconnectResult> Invoke(GetCrossconnectInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetCrossconnectResult>("ionoscloud:compute/getCrossconnect:getCrossconnect", args ?? new GetCrossconnectInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCrossconnectArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Description of cross connect
        /// </summary>
        [Input("description")]
        public string? Description { get; set; }

        /// <summary>
        /// ID of the cross connect you want to search for.
        /// 
        /// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of an existing cross connect that you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetCrossconnectArgs()
        {
        }
        public static new GetCrossconnectArgs Empty => new GetCrossconnectArgs();
    }

    public sealed class GetCrossconnectInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Description of cross connect
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// ID of the cross connect you want to search for.
        /// 
        /// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of an existing cross connect that you want to search for.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetCrossconnectInvokeArgs()
        {
        }
        public static new GetCrossconnectInvokeArgs Empty => new GetCrossconnectInvokeArgs();
    }


    [OutputType]
    public sealed class GetCrossconnectResult
    {
        /// <summary>
        /// Lists datacenters that can be joined to this cross connect
        /// </summary>
        public readonly ImmutableArray<Outputs.GetCrossconnectConnectableDatacenterResult> ConnectableDatacenters;
        /// <summary>
        /// Description of cross connect
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The UUID of the connectable datacenter
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The name of the connectable datacenter
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// Lists LAN's joined to this cross connect
        /// </summary>
        public readonly ImmutableArray<Outputs.GetCrossconnectPeerResult> Peers;

        [OutputConstructor]
        private GetCrossconnectResult(
            ImmutableArray<Outputs.GetCrossconnectConnectableDatacenterResult> connectableDatacenters,

            string? description,

            string? id,

            string? name,

            ImmutableArray<Outputs.GetCrossconnectPeerResult> peers)
        {
            ConnectableDatacenters = connectableDatacenters;
            Description = description;
            Id = id;
            Name = name;
            Peers = peers;
        }
    }
}
