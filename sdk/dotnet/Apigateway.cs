// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    /// <summary>
    /// An API gateway consists of the generic rules and configurations.
    /// 
    /// ## Usage example
    /// 
    /// &lt;!--Start PulumiCodeChooser --&gt;
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Pulumi.Ionoscloud;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var example = new Ionoscloud.Apigateway("example", new()
    ///     {
    ///         Metrics = true,
    ///     });
    /// 
    /// });
    /// ```
    /// &lt;!--End PulumiCodeChooser --&gt;
    /// 
    /// ## Import
    /// 
    /// In order to import an API Gateway, you can define an empty API Gateway resource in the plan:
    /// 
    /// resource "ionoscloud_apigateway" "example" {
    /// 
    /// }
    /// 
    /// The resource can be imported using the `gateway_id`, for example:
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:index/apigateway:Apigateway example {gateway_id}
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:index/apigateway:Apigateway")]
    public partial class Apigateway : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [list] Custom domains for the API Gateway, a list that contains elements with the following structure:
        /// </summary>
        [Output("customDomains")]
        public Output<ImmutableArray<Outputs.ApigatewayCustomDomain>> CustomDomains { get; private set; } = null!;

        /// <summary>
        /// [bool] Enable or disable logging. Defaults to `false`. **NOTE**: Central Logging must be enabled through the Logging API to enable this feature.
        /// </summary>
        [Output("logs")]
        public Output<bool?> Logs { get; private set; } = null!;

        /// <summary>
        /// [bool] Enable or disable metrics. Defaults to `false`.
        /// </summary>
        [Output("metrics")]
        public Output<bool?> Metrics { get; private set; } = null!;

        /// <summary>
        /// [string] The domain name. Externally reachable.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [string] The public endpoint of the API Gateway.
        /// </summary>
        [Output("publicEndpoint")]
        public Output<string> PublicEndpoint { get; private set; } = null!;


        /// <summary>
        /// Create a Apigateway resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Apigateway(string name, ApigatewayArgs? args = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/apigateway:Apigateway", name, args ?? new ApigatewayArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Apigateway(string name, Input<string> id, ApigatewayState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/apigateway:Apigateway", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/ionos-cloud/pulumi-ionoscloud/",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Apigateway resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Apigateway Get(string name, Input<string> id, ApigatewayState? state = null, CustomResourceOptions? options = null)
        {
            return new Apigateway(name, id, state, options);
        }
    }

    public sealed class ApigatewayArgs : global::Pulumi.ResourceArgs
    {
        [Input("customDomains")]
        private InputList<Inputs.ApigatewayCustomDomainArgs>? _customDomains;

        /// <summary>
        /// [list] Custom domains for the API Gateway, a list that contains elements with the following structure:
        /// </summary>
        public InputList<Inputs.ApigatewayCustomDomainArgs> CustomDomains
        {
            get => _customDomains ?? (_customDomains = new InputList<Inputs.ApigatewayCustomDomainArgs>());
            set => _customDomains = value;
        }

        /// <summary>
        /// [bool] Enable or disable logging. Defaults to `false`. **NOTE**: Central Logging must be enabled through the Logging API to enable this feature.
        /// </summary>
        [Input("logs")]
        public Input<bool>? Logs { get; set; }

        /// <summary>
        /// [bool] Enable or disable metrics. Defaults to `false`.
        /// </summary>
        [Input("metrics")]
        public Input<bool>? Metrics { get; set; }

        /// <summary>
        /// [string] The domain name. Externally reachable.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public ApigatewayArgs()
        {
        }
        public static new ApigatewayArgs Empty => new ApigatewayArgs();
    }

    public sealed class ApigatewayState : global::Pulumi.ResourceArgs
    {
        [Input("customDomains")]
        private InputList<Inputs.ApigatewayCustomDomainGetArgs>? _customDomains;

        /// <summary>
        /// [list] Custom domains for the API Gateway, a list that contains elements with the following structure:
        /// </summary>
        public InputList<Inputs.ApigatewayCustomDomainGetArgs> CustomDomains
        {
            get => _customDomains ?? (_customDomains = new InputList<Inputs.ApigatewayCustomDomainGetArgs>());
            set => _customDomains = value;
        }

        /// <summary>
        /// [bool] Enable or disable logging. Defaults to `false`. **NOTE**: Central Logging must be enabled through the Logging API to enable this feature.
        /// </summary>
        [Input("logs")]
        public Input<bool>? Logs { get; set; }

        /// <summary>
        /// [bool] Enable or disable metrics. Defaults to `false`.
        /// </summary>
        [Input("metrics")]
        public Input<bool>? Metrics { get; set; }

        /// <summary>
        /// [string] The domain name. Externally reachable.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [string] The public endpoint of the API Gateway.
        /// </summary>
        [Input("publicEndpoint")]
        public Input<string>? PublicEndpoint { get; set; }

        public ApigatewayState()
        {
        }
        public static new ApigatewayState Empty => new ApigatewayState();
    }
}
