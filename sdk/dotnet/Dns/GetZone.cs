// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Dns
{
    public static class GetZone
    {
        /// <summary>
        /// The **DNS Zone** can be used to search for and return an existing DNS Zone.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// &gt; ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_zone** data source. Please ensure you are using tokens as other methods will not be valid.
        /// 
        /// ## Example Usage
        /// 
        /// ### By name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dns.GetZone.Invoke(new()
        ///     {
        ///         Name = "example.com",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By name with partial match
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dns.GetZone.Invoke(new()
        ///     {
        ///         Name = "example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetZoneResult> InvokeAsync(GetZoneArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetZoneResult>("ionoscloud:dns/getZone:getZone", args ?? new GetZoneArgs(), options.WithDefaults());

        /// <summary>
        /// The **DNS Zone** can be used to search for and return an existing DNS Zone.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// &gt; ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_zone** data source. Please ensure you are using tokens as other methods will not be valid.
        /// 
        /// ## Example Usage
        /// 
        /// ### By name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dns.GetZone.Invoke(new()
        ///     {
        ///         Name = "example.com",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By name with partial match
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dns.GetZone.Invoke(new()
        ///     {
        ///         Name = "example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetZoneResult> Invoke(GetZoneInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetZoneResult>("ionoscloud:dns/getZone:getZone", args ?? new GetZoneInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **DNS Zone** can be used to search for and return an existing DNS Zone.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// &gt; ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_zone** data source. Please ensure you are using tokens as other methods will not be valid.
        /// 
        /// ## Example Usage
        /// 
        /// ### By name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dns.GetZone.Invoke(new()
        ///     {
        ///         Name = "example.com",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By name with partial match
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dns.GetZone.Invoke(new()
        ///     {
        ///         Name = "example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetZoneResult> Invoke(GetZoneInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetZoneResult>("ionoscloud:dns/getZone:getZone", args ?? new GetZoneInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetZoneArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [string] The ID of the DNS Zone you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// [string] The name of the DNS Zone you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
        /// 
        /// Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("partialMatch")]
        public bool? PartialMatch { get; set; }

        public GetZoneArgs()
        {
        }
        public static new GetZoneArgs Empty => new GetZoneArgs();
    }

    public sealed class GetZoneInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [string] The ID of the DNS Zone you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// [string] The name of the DNS Zone you want to search for.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
        /// 
        /// Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("partialMatch")]
        public Input<bool>? PartialMatch { get; set; }

        public GetZoneInvokeArgs()
        {
        }
        public static new GetZoneInvokeArgs Empty => new GetZoneInvokeArgs();
    }


    [OutputType]
    public sealed class GetZoneResult
    {
        /// <summary>
        /// The description of the DNS Zone.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// Indicates if the DNS Zone is activated or not.
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// The UUID of the DNS Zone.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The name of the DNS Zone.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// A list of available name servers.
        /// </summary>
        public readonly ImmutableArray<string> Nameservers;
        public readonly bool? PartialMatch;

        [OutputConstructor]
        private GetZoneResult(
            string description,

            bool enabled,

            string? id,

            string? name,

            ImmutableArray<string> nameservers,

            bool? partialMatch)
        {
            Description = description;
            Enabled = enabled;
            Id = id;
            Name = name;
            Nameservers = nameservers;
            PartialMatch = partialMatch;
        }
    }
}
