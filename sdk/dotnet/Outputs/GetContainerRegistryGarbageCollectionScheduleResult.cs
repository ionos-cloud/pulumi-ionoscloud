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
    public sealed class GetContainerRegistryGarbageCollectionScheduleResult
    {
        public readonly ImmutableArray<string> Days;
        public readonly string Time;

        [OutputConstructor]
        private GetContainerRegistryGarbageCollectionScheduleResult(
            ImmutableArray<string> days,

            string time)
        {
            Days = days;
            Time = time;
        }
    }
}
