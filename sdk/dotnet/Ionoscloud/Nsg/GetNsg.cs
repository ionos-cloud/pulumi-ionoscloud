// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Nsg
{
    public static class GetNsg
    {
        /// <summary>
        /// The **NSG Data source** can be used to search for and return an existing security group.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Nsg.GetNsg.Invoke(new()
        ///     {
        ///         DatacenterId = exampleIonoscloudDatacenter.Id,
        ///         Id = nsgId,
        ///     });
        /// 
        /// });
        /// ```
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
        ///     var example = Ionoscloud.Nsg.GetNsg.Invoke(new()
        ///     {
        ///         DatacenterId = exampleIonoscloudDatacenter.Id,
        ///         Name = "NSG Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetNsgResult> InvokeAsync(GetNsgArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetNsgResult>("ionoscloud:nsg/getNsg:getNsg", args ?? new GetNsgArgs(), options.WithDefaults());

        /// <summary>
        /// The **NSG Data source** can be used to search for and return an existing security group.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Nsg.GetNsg.Invoke(new()
        ///     {
        ///         DatacenterId = exampleIonoscloudDatacenter.Id,
        ///         Id = nsgId,
        ///     });
        /// 
        /// });
        /// ```
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
        ///     var example = Ionoscloud.Nsg.GetNsg.Invoke(new()
        ///     {
        ///         DatacenterId = exampleIonoscloudDatacenter.Id,
        ///         Name = "NSG Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetNsgResult> Invoke(GetNsgInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetNsgResult>("ionoscloud:nsg/getNsg:getNsg", args ?? new GetNsgInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **NSG Data source** can be used to search for and return an existing security group.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Nsg.GetNsg.Invoke(new()
        ///     {
        ///         DatacenterId = exampleIonoscloudDatacenter.Id,
        ///         Id = nsgId,
        ///     });
        /// 
        /// });
        /// ```
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
        ///     var example = Ionoscloud.Nsg.GetNsg.Invoke(new()
        ///     {
        ///         DatacenterId = exampleIonoscloudDatacenter.Id,
        ///         Name = "NSG Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetNsgResult> Invoke(GetNsgInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetNsgResult>("ionoscloud:nsg/getNsg:getNsg", args ?? new GetNsgInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNsgArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Datacenter's UUID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public string DatacenterId { get; set; } = null!;

        /// <summary>
        /// Id of an existing Network Security Group that you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of an existing Network Security Group that you want to search for.
        /// 
        /// Either `name`, or `id` must be provided. If none, the datasource will return an error.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetNsgArgs()
        {
        }
        public static new GetNsgArgs Empty => new GetNsgArgs();
    }

    public sealed class GetNsgInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Datacenter's UUID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// Id of an existing Network Security Group that you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of an existing Network Security Group that you want to search for.
        /// 
        /// Either `name`, or `id` must be provided. If none, the datasource will return an error.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetNsgInvokeArgs()
        {
        }
        public static new GetNsgInvokeArgs Empty => new GetNsgInvokeArgs();
    }


    [OutputType]
    public sealed class GetNsgResult
    {
        /// <summary>
        /// UUID of the Virtual Data Center
        /// </summary>
        public readonly string DatacenterId;
        /// <summary>
        /// Description for the Network Security Group
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// UUID of the Network Security Group
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name of the Network Security Group
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// List of IDs for the Firewall Rules attached to this group
        /// </summary>
        public readonly ImmutableArray<string> RuleIds;
        /// <summary>
        /// List of Firewall Rule objects attached to this group
        /// </summary>
        public readonly ImmutableArray<Outputs.GetNsgRuleResult> Rules;

        [OutputConstructor]
        private GetNsgResult(
            string datacenterId,

            string description,

            string id,

            string name,

            ImmutableArray<string> ruleIds,

            ImmutableArray<Outputs.GetNsgRuleResult> rules)
        {
            DatacenterId = datacenterId;
            Description = description;
            Id = id;
            Name = name;
            RuleIds = ruleIds;
            Rules = rules;
        }
    }
}
