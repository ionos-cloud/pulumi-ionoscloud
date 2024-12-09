// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Outputs
{

    [OutputType]
    public sealed class GetNfsShareClientGroupNfResult
    {
        /// <summary>
        /// The squash mode for the export. The squash mode can be: none - No squash mode. no mapping, root-anonymous - Map root user to anonymous uid, all-anonymous - Map all users to anonymous uid.
        /// </summary>
        public readonly string Squash;

        [OutputConstructor]
        private GetNfsShareClientGroupNfResult(string squash)
        {
            Squash = squash;
        }
    }
}
