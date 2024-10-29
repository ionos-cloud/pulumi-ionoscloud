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
    public sealed class PgClusterConnectionPooler
    {
        public readonly bool Enabled;
        /// <summary>
        /// Represents different modes of connection pooling for the connection pooler
        /// </summary>
        public readonly string PoolMode;

        [OutputConstructor]
        private PgClusterConnectionPooler(
            bool enabled,

            string poolMode)
        {
            Enabled = enabled;
            PoolMode = poolMode;
        }
    }
}
