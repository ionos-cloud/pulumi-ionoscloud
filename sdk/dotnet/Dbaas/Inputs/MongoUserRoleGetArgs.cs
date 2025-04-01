// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Dbaas.Inputs
{

    public sealed class MongoUserRoleGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [true] Database on which to apply the role.
        /// 
        /// **NOTE:** MongoDb users do not support update at the moment. Changing any attribute will result in the user being re-created.
        /// </summary>
        [Input("database")]
        public Input<string>? Database { get; set; }

        /// <summary>
        /// [true] Mongodb user role. Examples: read, readWrite, readAnyDatabase, readWriteAnyDatabase, dbAdmin, dbAdminAnyDatabase, clusterMonitor.
        /// </summary>
        [Input("role")]
        public Input<string>? Role { get; set; }

        public MongoUserRoleGetArgs()
        {
        }
        public static new MongoUserRoleGetArgs Empty => new MongoUserRoleGetArgs();
    }
}
