// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Creg.Inputs
{

    public sealed class RegistryGarbageCollectionScheduleGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("days", required: true)]
        private InputList<string>? _days;
        public InputList<string> Days
        {
            get => _days ?? (_days = new InputList<string>());
            set => _days = value;
        }

        /// <summary>
        /// UTC time of day e.g. 01:00:00 - as defined by partial-time - RFC3339
        /// </summary>
        [Input("time", required: true)]
        public Input<string> Time { get; set; } = null!;

        public RegistryGarbageCollectionScheduleGetArgs()
        {
        }
        public static new RegistryGarbageCollectionScheduleGetArgs Empty => new RegistryGarbageCollectionScheduleGetArgs();
    }
}
