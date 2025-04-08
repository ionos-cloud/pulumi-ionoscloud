// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute.Inputs
{

    public sealed class GroupUserArgs : global::Pulumi.ResourceArgs
    {
        [Input("administrator")]
        public Input<bool>? Administrator { get; set; }

        [Input("email")]
        public Input<string>? Email { get; set; }

        [Input("firstName")]
        public Input<string>? FirstName { get; set; }

        [Input("forceSecAuth")]
        public Input<bool>? ForceSecAuth { get; set; }

        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("lastName")]
        public Input<string>? LastName { get; set; }

        [Input("password")]
        public Input<string>? Password { get; set; }

        public GroupUserArgs()
        {
        }
        public static new GroupUserArgs Empty => new GroupUserArgs();
    }
}
