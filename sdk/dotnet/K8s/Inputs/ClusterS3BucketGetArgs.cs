// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.K8s.Inputs
{

    public sealed class ClusterS3BucketGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the Object Storage bucket
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public ClusterS3BucketGetArgs()
        {
        }
        public static new ClusterS3BucketGetArgs Empty => new ClusterS3BucketGetArgs();
    }
}
