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
    public sealed class GetMongoUserRoleResult
    {
        /// <summary>
        /// [true] Database on which to apply the role.
        /// 
        /// **NOTE:** MongoDb users do not support update at the moment. Changing any attribute will result in the user being re-created.
        /// </summary>
        public readonly string Database;
        /// <summary>
        /// [true] Mongodb user role. Examples: read, readWrite, readAnyDatabase, readWriteAnyDatabase, dbAdmin, dbAdminAnyDatabase, clusterMonitor and enableSharding.
        /// </summary>
        public readonly string Role;

        [OutputConstructor]
        private GetMongoUserRoleResult(
            string database,

            string role)
        {
            Database = database;
            Role = role;
        }
    }
}
