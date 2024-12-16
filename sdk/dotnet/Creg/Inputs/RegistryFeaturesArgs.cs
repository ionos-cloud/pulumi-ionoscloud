// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Creg.Inputs
{

    public sealed class RegistryFeaturesArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Enables vulnerability scanning for images in the container registry. Note: this feature can incur additional charges
        /// </summary>
        [Input("vulnerabilityScanning")]
        public Input<bool>? VulnerabilityScanning { get; set; }

        public RegistryFeaturesArgs()
        {
        }
        public static new RegistryFeaturesArgs Empty => new RegistryFeaturesArgs();
    }
}
