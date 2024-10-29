// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Outputs
{

    [OutputType]
    public sealed class GetLocationCpuArchitectureResult
    {
        /// <summary>
        /// A valid CPU family name.
        /// </summary>
        public readonly string CpuFamily;
        /// <summary>
        /// The maximum number of cores available.
        /// </summary>
        public readonly int MaxCores;
        /// <summary>
        /// The maximum number of RAM in MB.
        /// </summary>
        public readonly int MaxRam;
        /// <summary>
        /// A valid CPU vendor name.
        /// </summary>
        public readonly string Vendor;

        [OutputConstructor]
        private GetLocationCpuArchitectureResult(
            string cpuFamily,

            int maxCores,

            int maxRam,

            string vendor)
        {
            CpuFamily = cpuFamily;
            MaxCores = maxCores;
            MaxRam = maxRam;
            Vendor = vendor;
        }
    }
}
