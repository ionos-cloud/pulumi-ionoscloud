// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Outputs
{

    [OutputType]
    public sealed class GetK8sClustersClusterConfigUserResult
    {
        public readonly string Name;
        public readonly ImmutableDictionary<string, string> User;

        [OutputConstructor]
        private GetK8sClustersClusterConfigUserResult(
            string name,

            ImmutableDictionary<string, string> user)
        {
            Name = name;
            User = user;
        }
    }
}
