// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Dbaas.Inputs
{

    public sealed class InMemoryDBReplicaSetMaintenanceWindowGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The name of the week day.
        /// </summary>
        [Input("dayOfTheWeek", required: true)]
        public Input<string> DayOfTheWeek { get; set; } = null!;

        /// <summary>
        /// [string] Start of the maintenance window in UTC time.
        /// </summary>
        [Input("time", required: true)]
        public Input<string> Time { get; set; } = null!;

        public InMemoryDBReplicaSetMaintenanceWindowGetArgs()
        {
        }
        public static new InMemoryDBReplicaSetMaintenanceWindowGetArgs Empty => new InMemoryDBReplicaSetMaintenanceWindowGetArgs();
    }
}
