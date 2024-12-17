// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetLoggingPipeline
    {
        /// <summary>
        /// The **Logging pipeline** datasource can be used to search for and return an existing Logging pipeline.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// 
        /// &gt; ⚠️  Only tokens are accepted for authorization in the **logging_pipeline** data source. Please ensure you are using tokens as other methods will not be valid.
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
        ///     var example = Ionoscloud.GetLoggingPipeline.Invoke(new()
        ///     {
        ///         Location = "de/txl",
        ///         Name = "pipeline_name",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetLoggingPipelineResult> InvokeAsync(GetLoggingPipelineArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetLoggingPipelineResult>("ionoscloud:index/getLoggingPipeline:getLoggingPipeline", args ?? new GetLoggingPipelineArgs(), options.WithDefaults());

        /// <summary>
        /// The **Logging pipeline** datasource can be used to search for and return an existing Logging pipeline.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// 
        /// &gt; ⚠️  Only tokens are accepted for authorization in the **logging_pipeline** data source. Please ensure you are using tokens as other methods will not be valid.
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
        ///     var example = Ionoscloud.GetLoggingPipeline.Invoke(new()
        ///     {
        ///         Location = "de/txl",
        ///         Name = "pipeline_name",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetLoggingPipelineResult> Invoke(GetLoggingPipelineInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetLoggingPipelineResult>("ionoscloud:index/getLoggingPipeline:getLoggingPipeline", args ?? new GetLoggingPipelineInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **Logging pipeline** datasource can be used to search for and return an existing Logging pipeline.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// 
        /// &gt; ⚠️  Only tokens are accepted for authorization in the **logging_pipeline** data source. Please ensure you are using tokens as other methods will not be valid.
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
        ///     var example = Ionoscloud.GetLoggingPipeline.Invoke(new()
        ///     {
        ///         Location = "de/txl",
        ///         Name = "pipeline_name",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetLoggingPipelineResult> Invoke(GetLoggingPipelineInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetLoggingPipelineResult>("ionoscloud:index/getLoggingPipeline:getLoggingPipeline", args ?? new GetLoggingPipelineInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetLoggingPipelineArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [string] The ID of the Logging pipeline you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// [string] The location of the Logging pipeline. Default: `de/txl`. One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`.
        /// </summary>
        [Input("location")]
        public string? Location { get; set; }

        /// <summary>
        /// [string] The name of the Logging pipeline you want to search for.
        /// 
        /// Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetLoggingPipelineArgs()
        {
        }
        public static new GetLoggingPipelineArgs Empty => new GetLoggingPipelineArgs();
    }

    public sealed class GetLoggingPipelineInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [string] The ID of the Logging pipeline you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// [string] The location of the Logging pipeline. Default: `de/txl`. One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// [string] The name of the Logging pipeline you want to search for.
        /// 
        /// Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetLoggingPipelineInvokeArgs()
        {
        }
        public static new GetLoggingPipelineInvokeArgs Empty => new GetLoggingPipelineInvokeArgs();
    }


    [OutputType]
    public sealed class GetLoggingPipelineResult
    {
        /// <summary>
        /// The address of the client's grafana instance.
        /// </summary>
        public readonly string GrafanaAddress;
        /// <summary>
        /// The UUID of the Logging pipeline.
        /// </summary>
        public readonly string? Id;
        public readonly string? Location;
        /// <summary>
        /// [list] Pipeline logs, a list that contains elements with the following structure:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetLoggingPipelineLogResult> Logs;
        /// <summary>
        /// The name of the Logging pipeline.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private GetLoggingPipelineResult(
            string grafanaAddress,

            string? id,

            string? location,

            ImmutableArray<Outputs.GetLoggingPipelineLogResult> logs,

            string name)
        {
            GrafanaAddress = grafanaAddress;
            Id = id;
            Location = location;
            Logs = logs;
            Name = name;
        }
    }
}
