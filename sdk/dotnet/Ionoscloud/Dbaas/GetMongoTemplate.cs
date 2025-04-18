// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Dbaas
{
    public static class GetMongoTemplate
    {
        /// <summary>
        /// The **DbaaS Mongo Template data source** can be used to search for and return an existing DbaaS MongoDB Template.
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
        ///     var example = Ionoscloud.Dbaas.GetMongoTemplate.Invoke(new()
        ///     {
        ///         Id = "template_id",
        ///     });
        /// 
        /// });
        /// ```
        /// ### By name
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMongoTemplate.Invoke(new()
        ///     {
        ///         Name = "name",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By name, using partial_match
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMongoTemplate.Invoke(new()
        ///     {
        ///         Name = "name",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// * `name` - (Optional) The name of the template you want to search for.
        /// * `id` - (Optional) ID of the template you want to search for.
        /// * `partial_match` - (Optional) Whether partial matching is allowed or not when using name argument. Default value is false.
        /// 
        /// Either `name` or `id` must be provided. If none or both are provided, the datasource will return an error.
        /// </summary>
        public static Task<GetMongoTemplateResult> InvokeAsync(GetMongoTemplateArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetMongoTemplateResult>("ionoscloud:dbaas/getMongoTemplate:getMongoTemplate", args ?? new GetMongoTemplateArgs(), options.WithDefaults());

        /// <summary>
        /// The **DbaaS Mongo Template data source** can be used to search for and return an existing DbaaS MongoDB Template.
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
        ///     var example = Ionoscloud.Dbaas.GetMongoTemplate.Invoke(new()
        ///     {
        ///         Id = "template_id",
        ///     });
        /// 
        /// });
        /// ```
        /// ### By name
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMongoTemplate.Invoke(new()
        ///     {
        ///         Name = "name",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By name, using partial_match
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMongoTemplate.Invoke(new()
        ///     {
        ///         Name = "name",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// * `name` - (Optional) The name of the template you want to search for.
        /// * `id` - (Optional) ID of the template you want to search for.
        /// * `partial_match` - (Optional) Whether partial matching is allowed or not when using name argument. Default value is false.
        /// 
        /// Either `name` or `id` must be provided. If none or both are provided, the datasource will return an error.
        /// </summary>
        public static Output<GetMongoTemplateResult> Invoke(GetMongoTemplateInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetMongoTemplateResult>("ionoscloud:dbaas/getMongoTemplate:getMongoTemplate", args ?? new GetMongoTemplateInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **DbaaS Mongo Template data source** can be used to search for and return an existing DbaaS MongoDB Template.
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
        ///     var example = Ionoscloud.Dbaas.GetMongoTemplate.Invoke(new()
        ///     {
        ///         Id = "template_id",
        ///     });
        /// 
        /// });
        /// ```
        /// ### By name
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMongoTemplate.Invoke(new()
        ///     {
        ///         Name = "name",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By name, using partial_match
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMongoTemplate.Invoke(new()
        ///     {
        ///         Name = "name",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// * `name` - (Optional) The name of the template you want to search for.
        /// * `id` - (Optional) ID of the template you want to search for.
        /// * `partial_match` - (Optional) Whether partial matching is allowed or not when using name argument. Default value is false.
        /// 
        /// Either `name` or `id` must be provided. If none or both are provided, the datasource will return an error.
        /// </summary>
        public static Output<GetMongoTemplateResult> Invoke(GetMongoTemplateInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetMongoTemplateResult>("ionoscloud:dbaas/getMongoTemplate:getMongoTemplate", args ?? new GetMongoTemplateInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetMongoTemplateArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the template.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// The name of the template.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        [Input("partialMatch")]
        public bool? PartialMatch { get; set; }

        public GetMongoTemplateArgs()
        {
        }
        public static new GetMongoTemplateArgs Empty => new GetMongoTemplateArgs();
    }

    public sealed class GetMongoTemplateInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the template.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The name of the template.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("partialMatch")]
        public Input<bool>? PartialMatch { get; set; }

        public GetMongoTemplateInvokeArgs()
        {
        }
        public static new GetMongoTemplateInvokeArgs Empty => new GetMongoTemplateInvokeArgs();
    }


    [OutputType]
    public sealed class GetMongoTemplateResult
    {
        /// <summary>
        /// The number of CPU cores.
        /// </summary>
        public readonly int Cores;
        /// <summary>
        /// The edition of the template (e.g. enterprise).
        /// </summary>
        public readonly string Edition;
        /// <summary>
        /// The ID of the template.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name of the template.
        /// </summary>
        public readonly string Name;
        public readonly bool? PartialMatch;
        /// <summary>
        /// The amount of memory in GB.
        /// </summary>
        public readonly int Ram;
        /// <summary>
        /// The amount of storage size in GB.
        /// </summary>
        public readonly int StorageSize;

        [OutputConstructor]
        private GetMongoTemplateResult(
            int cores,

            string edition,

            string id,

            string name,

            bool? partialMatch,

            int ram,

            int storageSize)
        {
            Cores = cores;
            Edition = edition;
            Id = id;
            Name = name;
            PartialMatch = partialMatch;
            Ram = ram;
            StorageSize = storageSize;
        }
    }
}
