// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Cdn
{
    public static class GetDistribution
    {
        /// <summary>
        /// The Distribution data source can be used to search for and return an existing Distributions.
        /// You can provide a string for the domain parameter which will be compared with provisioned Distributions.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique domains.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Id
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cdn.GetDistribution.Invoke(new()
        ///     {
        ///         Id = "distr_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Domain
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cdn.GetDistribution.Invoke(new()
        ///     {
        ///         Domain = "example.com",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Domain with Partial Match
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cdn.GetDistribution.Invoke(new()
        ///     {
        ///         Domain = "example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetDistributionResult> InvokeAsync(GetDistributionArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDistributionResult>("ionoscloud:cdn/getDistribution:getDistribution", args ?? new GetDistributionArgs(), options.WithDefaults());

        /// <summary>
        /// The Distribution data source can be used to search for and return an existing Distributions.
        /// You can provide a string for the domain parameter which will be compared with provisioned Distributions.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique domains.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Id
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cdn.GetDistribution.Invoke(new()
        ///     {
        ///         Id = "distr_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Domain
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cdn.GetDistribution.Invoke(new()
        ///     {
        ///         Domain = "example.com",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Domain with Partial Match
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cdn.GetDistribution.Invoke(new()
        ///     {
        ///         Domain = "example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetDistributionResult> Invoke(GetDistributionInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDistributionResult>("ionoscloud:cdn/getDistribution:getDistribution", args ?? new GetDistributionInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The Distribution data source can be used to search for and return an existing Distributions.
        /// You can provide a string for the domain parameter which will be compared with provisioned Distributions.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique domains.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Id
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cdn.GetDistribution.Invoke(new()
        ///     {
        ///         Id = "distr_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Domain
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cdn.GetDistribution.Invoke(new()
        ///     {
        ///         Domain = "example.com",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Domain with Partial Match
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cdn.GetDistribution.Invoke(new()
        ///     {
        ///         Domain = "example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetDistributionResult> Invoke(GetDistributionInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetDistributionResult>("ionoscloud:cdn/getDistribution:getDistribution", args ?? new GetDistributionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDistributionArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Domain of an existing distribution that you want to search for. Search by domain is case-insensitive. The whole resource domain is required if `partial_match` parameter is not set to true.
        /// </summary>
        [Input("domain")]
        public string? Domain { get; set; }

        /// <summary>
        /// ID of the distribution you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Whether partial matching is allowed or not when using domain argument. Default value is false.
        /// 
        /// Either `domain` or `id` must be provided. If none, or both of `domain` and `id` are provided, the datasource will return an error.
        /// </summary>
        [Input("partialMatch")]
        public bool? PartialMatch { get; set; }

        public GetDistributionArgs()
        {
        }
        public static new GetDistributionArgs Empty => new GetDistributionArgs();
    }

    public sealed class GetDistributionInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Domain of an existing distribution that you want to search for. Search by domain is case-insensitive. The whole resource domain is required if `partial_match` parameter is not set to true.
        /// </summary>
        [Input("domain")]
        public Input<string>? Domain { get; set; }

        /// <summary>
        /// ID of the distribution you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Whether partial matching is allowed or not when using domain argument. Default value is false.
        /// 
        /// Either `domain` or `id` must be provided. If none, or both of `domain` and `id` are provided, the datasource will return an error.
        /// </summary>
        [Input("partialMatch")]
        public Input<bool>? PartialMatch { get; set; }

        public GetDistributionInvokeArgs()
        {
        }
        public static new GetDistributionInvokeArgs Empty => new GetDistributionInvokeArgs();
    }


    [OutputType]
    public sealed class GetDistributionResult
    {
        /// <summary>
        /// The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
        /// </summary>
        public readonly string CertificateId;
        /// <summary>
        /// The domain of the distribution.
        /// </summary>
        public readonly string? Domain;
        public readonly string Id;
        public readonly bool? PartialMatch;
        /// <summary>
        /// IP of the distribution, it has to be included on the domain DNS Zone as A record.
        /// </summary>
        public readonly string PublicEndpointV4;
        /// <summary>
        /// IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
        /// </summary>
        public readonly string PublicEndpointV6;
        /// <summary>
        /// Unique resource identifier.
        /// </summary>
        public readonly string ResourceUrn;
        /// <summary>
        /// The routing rules for the distribution.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetDistributionRoutingRuleResult> RoutingRules;

        [OutputConstructor]
        private GetDistributionResult(
            string certificateId,

            string? domain,

            string id,

            bool? partialMatch,

            string publicEndpointV4,

            string publicEndpointV6,

            string resourceUrn,

            ImmutableArray<Outputs.GetDistributionRoutingRuleResult> routingRules)
        {
            CertificateId = certificateId;
            Domain = domain;
            Id = id;
            PartialMatch = partialMatch;
            PublicEndpointV4 = publicEndpointV4;
            PublicEndpointV6 = publicEndpointV6;
            ResourceUrn = resourceUrn;
            RoutingRules = routingRules;
        }
    }
}
