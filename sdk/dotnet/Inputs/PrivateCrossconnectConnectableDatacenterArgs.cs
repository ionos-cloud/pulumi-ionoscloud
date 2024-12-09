// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class PrivateCrossconnectConnectableDatacenterArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The UUID of the connectable datacenter
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The physical location of the connectable datacenter
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// [string] The name of the cross-connection.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public PrivateCrossconnectConnectableDatacenterArgs()
        {
        }
        public static new PrivateCrossconnectConnectableDatacenterArgs Empty => new PrivateCrossconnectConnectableDatacenterArgs();
    }
}
