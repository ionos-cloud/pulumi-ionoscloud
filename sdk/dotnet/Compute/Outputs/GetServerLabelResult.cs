// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute.Outputs
{

    [OutputType]
    public sealed class GetServerLabelResult
    {
        /// <summary>
        /// ID of the server you want to search for.
        /// 
        /// `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The key of the label
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// The value of the label
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private GetServerLabelResult(
            string id,

            string key,

            string value)
        {
            Id = id;
            Key = key;
            Value = value;
        }
    }
}
