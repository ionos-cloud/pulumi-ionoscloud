// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Dbaas.Outputs
{

    [OutputType]
    public sealed class InMemoryDBReplicaSetCredentialsHashedPassword
    {
        /// <summary>
        /// [string] The value can be only: "SHA-256".
        /// </summary>
        public readonly string Algorithm;
        /// <summary>
        /// [string] The hashed password.
        /// </summary>
        public readonly string Hash;

        [OutputConstructor]
        private InMemoryDBReplicaSetCredentialsHashedPassword(
            string algorithm,

            string hash)
        {
            Algorithm = algorithm;
            Hash = hash;
        }
    }
}
