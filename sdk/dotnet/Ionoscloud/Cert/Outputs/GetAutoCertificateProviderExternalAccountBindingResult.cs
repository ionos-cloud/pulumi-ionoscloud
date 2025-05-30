// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Cert.Outputs
{

    [OutputType]
    public sealed class GetAutoCertificateProviderExternalAccountBindingResult
    {
        /// <summary>
        /// [string] The key ID of the external account binding.
        /// </summary>
        public readonly string KeyId;

        [OutputConstructor]
        private GetAutoCertificateProviderExternalAccountBindingResult(string keyId)
        {
            KeyId = keyId;
        }
    }
}
