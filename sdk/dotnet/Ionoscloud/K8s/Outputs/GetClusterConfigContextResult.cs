// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.K8s.Outputs
{

    [OutputType]
    public sealed class GetClusterConfigContextResult
    {
        public readonly ImmutableDictionary<string, string> Context;
        /// <summary>
        /// Name of an existing cluster that you want to search for.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private GetClusterConfigContextResult(
            ImmutableDictionary<string, string> context,

            string name)
        {
            Context = context;
            Name = name;
        }
    }
}
