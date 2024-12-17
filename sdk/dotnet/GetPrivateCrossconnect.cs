// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetPrivateCrossconnect
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
        ///     var example = Ionoscloud.GetPrivateCrossconnect.Invoke(new()
        ///     {
        ///         Name = "Cross Connect Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetPrivateCrossconnectResult> InvokeAsync(GetPrivateCrossconnectArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPrivateCrossconnectResult>("ionoscloud:index/getPrivateCrossconnect:getPrivateCrossconnect", args ?? new GetPrivateCrossconnectArgs(), options.WithDefaults());

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
        ///     var example = Ionoscloud.GetPrivateCrossconnect.Invoke(new()
        ///     {
        ///         Name = "Cross Connect Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetPrivateCrossconnectResult> Invoke(GetPrivateCrossconnectInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPrivateCrossconnectResult>("ionoscloud:index/getPrivateCrossconnect:getPrivateCrossconnect", args ?? new GetPrivateCrossconnectInvokeArgs(), options.WithDefaults());

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
        ///     var example = Ionoscloud.GetPrivateCrossconnect.Invoke(new()
        ///     {
        ///         Name = "Cross Connect Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetPrivateCrossconnectResult> Invoke(GetPrivateCrossconnectInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetPrivateCrossconnectResult>("ionoscloud:index/getPrivateCrossconnect:getPrivateCrossconnect", args ?? new GetPrivateCrossconnectInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPrivateCrossconnectArgs : global::Pulumi.InvokeArgs
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

        public GetPrivateCrossconnectArgs()
        {
        }
        public static new GetPrivateCrossconnectArgs Empty => new GetPrivateCrossconnectArgs();
    }

    public sealed class GetPrivateCrossconnectInvokeArgs : global::Pulumi.InvokeArgs
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

        public GetPrivateCrossconnectInvokeArgs()
        {
        }
        public static new GetPrivateCrossconnectInvokeArgs Empty => new GetPrivateCrossconnectInvokeArgs();
    }


    [OutputType]
    public sealed class GetPrivateCrossconnectResult
    {
        /// <summary>
        /// Lists datacenters that can be joined to this cross connect
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPrivateCrossconnectConnectableDatacenterResult> ConnectableDatacenters;
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
        public readonly ImmutableArray<Outputs.GetPrivateCrossconnectPeerResult> Peers;

        [OutputConstructor]
        private GetPrivateCrossconnectResult(
            ImmutableArray<Outputs.GetPrivateCrossconnectConnectableDatacenterResult> connectableDatacenters,

            string? description,

            string? id,

            string? name,

            ImmutableArray<Outputs.GetPrivateCrossconnectPeerResult> peers)
        {
            ConnectableDatacenters = connectableDatacenters;
            Description = description;
            Id = id;
            Name = name;
            Peers = peers;
        }
    }
}
