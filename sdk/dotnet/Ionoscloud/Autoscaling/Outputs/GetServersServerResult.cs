// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Autoscaling.Outputs
{

    [OutputType]
    public sealed class GetServersServerResult
    {
        /// <summary>
        /// The unique ID of the server.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetServersServerResult(string id)
        {
            Id = id;
        }
    }
}
