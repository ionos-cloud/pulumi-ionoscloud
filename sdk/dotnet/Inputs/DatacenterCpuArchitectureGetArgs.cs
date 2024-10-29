// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class DatacenterCpuArchitectureGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("cpuFamily")]
        public Input<string>? CpuFamily { get; set; }

        [Input("maxCores")]
        public Input<int>? MaxCores { get; set; }

        [Input("maxRam")]
        public Input<int>? MaxRam { get; set; }

        [Input("vendor")]
        public Input<string>? Vendor { get; set; }

        public DatacenterCpuArchitectureGetArgs()
        {
        }
        public static new DatacenterCpuArchitectureGetArgs Empty => new DatacenterCpuArchitectureGetArgs();
    }
}
