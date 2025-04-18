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
    public sealed class GetClustersClusterConfigUserResult
    {
        public readonly string Name;
        public readonly ImmutableDictionary<string, string> User;

        [OutputConstructor]
        private GetClustersClusterConfigUserResult(
            string name,

            ImmutableDictionary<string, string> user)
        {
            Name = name;
            User = user;
        }
    }
}
