// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class DataplatformNodePoolMaintenanceWindowGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] Must be set with one the values `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` or `Sunday`.
        /// </summary>
        [Input("dayOfTheWeek", required: true)]
        public Input<string> DayOfTheWeek { get; set; } = null!;

        /// <summary>
        /// [string] Time at which the maintenance should start. Must conform to the 'HH:MM:SS' 24-hour format. This pattern matches the "HH:MM:SS 24-hour format with leading 0" format. For more information take a look at [this link](https://stackoverflow.com/questions/7536755/regular-expression-for-matching-hhmm-time-format).
        /// </summary>
        [Input("time", required: true)]
        public Input<string> Time { get; set; } = null!;

        public DataplatformNodePoolMaintenanceWindowGetArgs()
        {
        }
        public static new DataplatformNodePoolMaintenanceWindowGetArgs Empty => new DataplatformNodePoolMaintenanceWindowGetArgs();
    }
}
