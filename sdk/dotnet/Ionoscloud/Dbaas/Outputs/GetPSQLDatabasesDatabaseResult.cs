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
    public sealed class GetPSQLDatabasesDatabaseResult
    {
        /// <summary>
        /// [string] The ID of the database.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// [string] The name of the database.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// [string] Filter using a specific owner.
        /// </summary>
        public readonly string Owner;

        [OutputConstructor]
        private GetPSQLDatabasesDatabaseResult(
            string id,

            string name,

            string owner)
        {
            Id = id;
            Name = name;
            Owner = owner;
        }
    }
}
