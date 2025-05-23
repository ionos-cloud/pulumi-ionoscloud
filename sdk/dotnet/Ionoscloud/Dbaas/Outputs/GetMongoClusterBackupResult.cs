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
    public sealed class GetMongoClusterBackupResult
    {
        /// <summary>
        /// The location where the cluster backups will be stored. If not set, the backup is stored in the nearest location of the cluster. Possible values are de, eu-south-2, or eu-central-2.
        /// </summary>
        public readonly string Location;

        [OutputConstructor]
        private GetMongoClusterBackupResult(string location)
        {
            Location = location;
        }
    }
}
