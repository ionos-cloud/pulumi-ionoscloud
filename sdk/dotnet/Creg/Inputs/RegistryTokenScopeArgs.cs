// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Creg.Inputs
{

    public sealed class RegistryTokenScopeArgs : global::Pulumi.ResourceArgs
    {
        [Input("actions", required: true)]
        private InputList<string>? _actions;

        /// <summary>
        /// [string] Example: ["pull", "push", "delete"]
        /// </summary>
        public InputList<string> Actions
        {
            get => _actions ?? (_actions = new InputList<string>());
            set => _actions = value;
        }

        /// <summary>
        /// [string]
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// [string]
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public RegistryTokenScopeArgs()
        {
        }
        public static new RegistryTokenScopeArgs Empty => new RegistryTokenScopeArgs();
    }
}
