// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class MariadbClusterMaintenanceWindowGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the week day.
        /// </summary>
        [Input("dayOfTheWeek", required: true)]
        public Input<string> DayOfTheWeek { get; set; } = null!;

        /// <summary>
        /// Start of the maintenance window in UTC time.
        /// </summary>
        [Input("time", required: true)]
        public Input<string> Time { get; set; } = null!;

        public MariadbClusterMaintenanceWindowGetArgs()
        {
        }
        public static new MariadbClusterMaintenanceWindowGetArgs Empty => new MariadbClusterMaintenanceWindowGetArgs();
    }
}
