// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Creg.Outputs
{

    [OutputType]
    public sealed class GetRegistryFeatureResult
    {
        public readonly bool VulnerabilityScanning;

        [OutputConstructor]
        private GetRegistryFeatureResult(bool vulnerabilityScanning)
        {
            VulnerabilityScanning = vulnerabilityScanning;
        }
    }
}
