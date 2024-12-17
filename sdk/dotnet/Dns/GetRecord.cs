// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Dns
{
    public static class GetRecord
    {
        /// <summary>
        /// The **DNS Record** can be used to search for and return an existing DNS Record.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// &gt; ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_record** data source. Please ensure you are using tokens as other methods will not be valid.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Task<GetRecordResult> InvokeAsync(GetRecordArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetRecordResult>("ionoscloud:dns/getRecord:getRecord", args ?? new GetRecordArgs(), options.WithDefaults());

        /// <summary>
        /// The **DNS Record** can be used to search for and return an existing DNS Record.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// &gt; ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_record** data source. Please ensure you are using tokens as other methods will not be valid.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Output<GetRecordResult> Invoke(GetRecordInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetRecordResult>("ionoscloud:dns/getRecord:getRecord", args ?? new GetRecordInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **DNS Record** can be used to search for and return an existing DNS Record.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// &gt; ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_record** data source. Please ensure you are using tokens as other methods will not be valid.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Output<GetRecordResult> Invoke(GetRecordInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetRecordResult>("ionoscloud:dns/getRecord:getRecord", args ?? new GetRecordInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetRecordArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [string] The ID of the DNS Record you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// [string] The name of the DNS Record you want to search for.
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

        /// <summary>
        /// [string] The ID of the DNS Zone in which the DNS Record can be found.
        /// </summary>
        [Input("zoneId", required: true)]
        public string ZoneId { get; set; } = null!;

        public GetRecordArgs()
        {
        }
        public static new GetRecordArgs Empty => new GetRecordArgs();
    }

    public sealed class GetRecordInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [string] The ID of the DNS Record you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// [string] The name of the DNS Record you want to search for.
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

        /// <summary>
        /// [string] The ID of the DNS Zone in which the DNS Record can be found.
        /// </summary>
        [Input("zoneId", required: true)]
        public Input<string> ZoneId { get; set; } = null!;

        public GetRecordInvokeArgs()
        {
        }
        public static new GetRecordInvokeArgs Empty => new GetRecordInvokeArgs();
    }


    [OutputType]
    public sealed class GetRecordResult
    {
        /// <summary>
        /// The content of the DNS Record.
        /// </summary>
        public readonly string Content;
        /// <summary>
        /// Indicates if the DNS Record is active or not.
        /// </summary>
        public readonly bool Enabled;
        public readonly string Fqdn;
        /// <summary>
        /// The UUID of the DNS Record.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The name of the DNS Record.
        /// </summary>
        public readonly string? Name;
        public readonly bool? PartialMatch;
        /// <summary>
        /// The priority for the DNS Record.
        /// </summary>
        public readonly int Priority;
        /// <summary>
        /// The time to live of the DNS Record.
        /// </summary>
        public readonly int Ttl;
        /// <summary>
        /// The type of the DNS Record.
        /// </summary>
        public readonly string Type;
        public readonly string ZoneId;

        [OutputConstructor]
        private GetRecordResult(
            string content,

            bool enabled,

            string fqdn,

            string? id,

            string? name,

            bool? partialMatch,

            int priority,

            int ttl,

            string type,

            string zoneId)
        {
            Content = content;
            Enabled = enabled;
            Fqdn = fqdn;
            Id = id;
            Name = name;
            PartialMatch = partialMatch;
            Priority = priority;
            Ttl = ttl;
            Type = type;
            ZoneId = zoneId;
        }
    }
}
