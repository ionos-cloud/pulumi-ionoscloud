// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class NfsClusterNfsGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The minimum supported version of the NFS cluster. Supported values: `4.2`. Default is `4.2`.
        /// </summary>
        [Input("minVersion")]
        public Input<string>? MinVersion { get; set; }

        public NfsClusterNfsGetArgs()
        {
        }
        public static new NfsClusterNfsGetArgs Empty => new NfsClusterNfsGetArgs();
    }
}
