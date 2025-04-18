// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud
{
    /// <summary>
    /// The provider type for the ionoscloud package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [IonoscloudResourceType("pulumi:providers:ionoscloud")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        [Output("contractNumber")]
        public Output<string?> ContractNumber { get; private set; } = null!;

        /// <summary>
        /// IonosCloud REST API URL. Usually not necessary to be set, SDKs know internally how to route requests to the API.
        /// </summary>
        [Output("endpoint")]
        public Output<string?> Endpoint { get; private set; } = null!;

        /// <summary>
        /// IonosCloud password for API operations. If token is provided, token is preferred
        /// </summary>
        [Output("password")]
        public Output<string?> Password { get; private set; } = null!;

        /// <summary>
        /// Access key for IONOS Object Storage operations.
        /// </summary>
        [Output("s3AccessKey")]
        public Output<string?> S3AccessKey { get; private set; } = null!;

        /// <summary>
        /// Region for IONOS Object Storage operations.
        /// </summary>
        [Output("s3Region")]
        public Output<string?> S3Region { get; private set; } = null!;

        /// <summary>
        /// Secret key for IONOS Object Storage operations.
        /// </summary>
        [Output("s3SecretKey")]
        public Output<string?> S3SecretKey { get; private set; } = null!;

        /// <summary>
        /// IonosCloud bearer token for API operations.
        /// </summary>
        [Output("token")]
        public Output<string?> Token { get; private set; } = null!;

        /// <summary>
        /// IonosCloud username for API operations. If token is provided, token is preferred
        /// </summary>
        [Output("username")]
        public Output<string?> Username { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, CustomResourceOptions? options = null)
            : base("ionoscloud", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        [Input("contractNumber")]
        public Input<string>? ContractNumber { get; set; }

        /// <summary>
        /// IonosCloud REST API URL. Usually not necessary to be set, SDKs know internally how to route requests to the API.
        /// </summary>
        [Input("endpoint")]
        public Input<string>? Endpoint { get; set; }

        /// <summary>
        /// This field is to be set only for testing purposes. It is not recommended to set this field in production environments.
        /// </summary>
        [Input("insecure", json: true)]
        public Input<bool>? Insecure { get; set; }

        /// <summary>
        /// IonosCloud password for API operations. If token is provided, token is preferred
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        [Input("retries", json: true)]
        public Input<int>? Retries { get; set; }

        /// <summary>
        /// Access key for IONOS Object Storage operations.
        /// </summary>
        [Input("s3AccessKey")]
        public Input<string>? S3AccessKey { get; set; }

        /// <summary>
        /// Region for IONOS Object Storage operations.
        /// </summary>
        [Input("s3Region")]
        public Input<string>? S3Region { get; set; }

        /// <summary>
        /// Secret key for IONOS Object Storage operations.
        /// </summary>
        [Input("s3SecretKey")]
        public Input<string>? S3SecretKey { get; set; }

        /// <summary>
        /// IonosCloud bearer token for API operations.
        /// </summary>
        [Input("token")]
        public Input<string>? Token { get; set; }

        /// <summary>
        /// IonosCloud username for API operations. If token is provided, token is preferred
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public ProviderArgs()
        {
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
