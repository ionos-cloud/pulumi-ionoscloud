// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Outputs
{

    [OutputType]
    public sealed class GetGroupUserResult
    {
        public readonly bool Administrator;
        public readonly string Email;
        public readonly string FirstName;
        public readonly bool ForceSecAuth;
        /// <summary>
        /// ID of the group you want to search for.
        /// 
        /// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        public readonly string Id;
        public readonly string LastName;

        [OutputConstructor]
        private GetGroupUserResult(
            bool administrator,

            string email,

            string firstName,

            bool forceSecAuth,

            string id,

            string lastName)
        {
            Administrator = administrator;
            Email = email;
            FirstName = firstName;
            ForceSecAuth = forceSecAuth;
            Id = id;
            LastName = lastName;
        }
    }
}
