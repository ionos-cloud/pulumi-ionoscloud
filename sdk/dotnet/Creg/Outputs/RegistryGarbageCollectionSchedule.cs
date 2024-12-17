// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Creg.Outputs
{

    [OutputType]
    public sealed class RegistryGarbageCollectionSchedule
    {
        public readonly ImmutableArray<string> Days;
        /// <summary>
        /// UTC time of day e.g. 01:00:00 - as defined by partial-time - RFC3339
        /// </summary>
        public readonly string Time;

        [OutputConstructor]
        private RegistryGarbageCollectionSchedule(
            ImmutableArray<string> days,

            string time)
        {
            Days = days;
            Time = time;
        }
    }
}
