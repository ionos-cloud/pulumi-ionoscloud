// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Vpn.Outputs
{

    [OutputType]
    public sealed class GetIpsecGatewayMaintenanceWindowResult
    {
        /// <summary>
        /// The name of the week day.
        /// </summary>
        public readonly string DayOfTheWeek;
        /// <summary>
        /// Start of the maintenance window in UTC time.
        /// </summary>
        public readonly string Time;

        [OutputConstructor]
        private GetIpsecGatewayMaintenanceWindowResult(
            string dayOfTheWeek,

            string time)
        {
            DayOfTheWeek = dayOfTheWeek;
            Time = time;
        }
    }
}
