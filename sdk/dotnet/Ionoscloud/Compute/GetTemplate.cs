// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Compute
{
    public static class GetTemplate
    {
        /// <summary>
        /// The **Template data source** can be used to search for and return existing templates by providing any of template properties (name, cores, ram, storage_size).
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
        ///     var example = Ionoscloud.Compute.GetTemplate.Invoke(new()
        ///     {
        ///         Name = "CUBES S",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Cores
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetTemplate.Invoke(new()
        ///     {
        ///         Cores = 6,
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Ram
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetTemplate.Invoke(new()
        ///     {
        ///         Ram = 49152,
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Storage Size
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetTemplate.Invoke(new()
        ///     {
        ///         StorageSize = 80,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetTemplateResult> InvokeAsync(GetTemplateArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetTemplateResult>("ionoscloud:compute/getTemplate:getTemplate", args ?? new GetTemplateArgs(), options.WithDefaults());

        /// <summary>
        /// The **Template data source** can be used to search for and return existing templates by providing any of template properties (name, cores, ram, storage_size).
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
        ///     var example = Ionoscloud.Compute.GetTemplate.Invoke(new()
        ///     {
        ///         Name = "CUBES S",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Cores
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetTemplate.Invoke(new()
        ///     {
        ///         Cores = 6,
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Ram
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetTemplate.Invoke(new()
        ///     {
        ///         Ram = 49152,
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Storage Size
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetTemplate.Invoke(new()
        ///     {
        ///         StorageSize = 80,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetTemplateResult> Invoke(GetTemplateInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetTemplateResult>("ionoscloud:compute/getTemplate:getTemplate", args ?? new GetTemplateInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **Template data source** can be used to search for and return existing templates by providing any of template properties (name, cores, ram, storage_size).
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
        ///     var example = Ionoscloud.Compute.GetTemplate.Invoke(new()
        ///     {
        ///         Name = "CUBES S",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Cores
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetTemplate.Invoke(new()
        ///     {
        ///         Cores = 6,
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Ram
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetTemplate.Invoke(new()
        ///     {
        ///         Ram = 49152,
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Storage Size
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetTemplate.Invoke(new()
        ///     {
        ///         StorageSize = 80,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetTemplateResult> Invoke(GetTemplateInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetTemplateResult>("ionoscloud:compute/getTemplate:getTemplate", args ?? new GetTemplateInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTemplateArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The CPU cores count.
        /// </summary>
        [Input("cores")]
        public double? Cores { get; set; }

        /// <summary>
        /// A name of that resource.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The RAM size in MB.
        /// </summary>
        [Input("ram")]
        public double? Ram { get; set; }

        /// <summary>
        /// The storage size in GB.
        /// 
        /// Any of the arguments ca be provided. If none, the datasource will return an error.
        /// </summary>
        [Input("storageSize")]
        public double? StorageSize { get; set; }

        public GetTemplateArgs()
        {
        }
        public static new GetTemplateArgs Empty => new GetTemplateArgs();
    }

    public sealed class GetTemplateInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The CPU cores count.
        /// </summary>
        [Input("cores")]
        public Input<double>? Cores { get; set; }

        /// <summary>
        /// A name of that resource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The RAM size in MB.
        /// </summary>
        [Input("ram")]
        public Input<double>? Ram { get; set; }

        /// <summary>
        /// The storage size in GB.
        /// 
        /// Any of the arguments ca be provided. If none, the datasource will return an error.
        /// </summary>
        [Input("storageSize")]
        public Input<double>? StorageSize { get; set; }

        public GetTemplateInvokeArgs()
        {
        }
        public static new GetTemplateInvokeArgs Empty => new GetTemplateInvokeArgs();
    }


    [OutputType]
    public sealed class GetTemplateResult
    {
        /// <summary>
        /// The CPU cores count
        /// </summary>
        public readonly double Cores;
        /// <summary>
        /// Id of template
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Name of template
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The RAM size in MB
        /// </summary>
        public readonly double Ram;
        /// <summary>
        /// The storage size in GB
        /// </summary>
        public readonly double StorageSize;

        [OutputConstructor]
        private GetTemplateResult(
            double cores,

            string id,

            string name,

            double ram,

            double storageSize)
        {
            Cores = cores;
            Id = id;
            Name = name;
            Ram = ram;
            StorageSize = storageSize;
        }
    }
}
