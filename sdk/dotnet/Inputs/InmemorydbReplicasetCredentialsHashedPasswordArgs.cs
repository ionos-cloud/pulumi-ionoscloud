// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class InmemorydbReplicasetCredentialsHashedPasswordArgs : global::Pulumi.ResourceArgs
    {
        [Input("algorithm", required: true)]
        public Input<string> Algorithm { get; set; } = null!;

        [Input("hash", required: true)]
        public Input<string> Hash { get; set; } = null!;

        public InmemorydbReplicasetCredentialsHashedPasswordArgs()
        {
        }
        public static new InmemorydbReplicasetCredentialsHashedPasswordArgs Empty => new InmemorydbReplicasetCredentialsHashedPasswordArgs();
    }
}
