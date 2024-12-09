// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetS3Key
    {
        /// <summary>
        /// The **IONOS Object Storage key data source** can be used to search for and return an existing IONOS Object Storage key.
        /// You can provide a string id which will be compared with provisioned IONOS Object Storage keys.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// </summary>
        public static Task<GetS3KeyResult> InvokeAsync(GetS3KeyArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetS3KeyResult>("ionoscloud:index/getS3Key:getS3Key", args ?? new GetS3KeyArgs(), options.WithDefaults());

        /// <summary>
        /// The **IONOS Object Storage key data source** can be used to search for and return an existing IONOS Object Storage key.
        /// You can provide a string id which will be compared with provisioned IONOS Object Storage keys.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// </summary>
        public static Output<GetS3KeyResult> Invoke(GetS3KeyInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetS3KeyResult>("ionoscloud:index/getS3Key:getS3Key", args ?? new GetS3KeyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetS3KeyArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The state of the IONOS Object Storage key
        /// </summary>
        [Input("active")]
        public bool? Active { get; set; }

        /// <summary>
        /// ID of the IONOS Object Storage key you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// [string] The UUID of the user owning the IONOS Object Storage Key.
        /// </summary>
        [Input("userId", required: true)]
        public string UserId { get; set; } = null!;

        public GetS3KeyArgs()
        {
        }
        public static new GetS3KeyArgs Empty => new GetS3KeyArgs();
    }

    public sealed class GetS3KeyInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The state of the IONOS Object Storage key
        /// </summary>
        [Input("active")]
        public Input<bool>? Active { get; set; }

        /// <summary>
        /// ID of the IONOS Object Storage key you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// [string] The UUID of the user owning the IONOS Object Storage Key.
        /// </summary>
        [Input("userId", required: true)]
        public Input<string> UserId { get; set; } = null!;

        public GetS3KeyInvokeArgs()
        {
        }
        public static new GetS3KeyInvokeArgs Empty => new GetS3KeyInvokeArgs();
    }


    [OutputType]
    public sealed class GetS3KeyResult
    {
        /// <summary>
        /// The state of the IONOS Object Storage key
        /// </summary>
        public readonly bool? Active;
        /// <summary>
        /// The id of the IONOS Object Storage key
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// (Computed)The IONOS Object Storage Secret key.
        /// </summary>
        public readonly string SecretKey;
        /// <summary>
        /// The ID of the user that owns the key
        /// </summary>
        public readonly string UserId;

        [OutputConstructor]
        private GetS3KeyResult(
            bool? active,

            string? id,

            string secretKey,

            string userId)
        {
            Active = active;
            Id = id;
            SecretKey = secretKey;
            UserId = userId;
        }
    }
}
