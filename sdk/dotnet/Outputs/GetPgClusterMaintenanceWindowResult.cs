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
    public sealed class GetPgClusterMaintenanceWindowResult
    {
        public readonly string DayOfTheWeek;
        public readonly string Time;

        [OutputConstructor]
        private GetPgClusterMaintenanceWindowResult(
            string dayOfTheWeek,

            string time)
        {
            DayOfTheWeek = dayOfTheWeek;
            Time = time;
        }
    }
}
