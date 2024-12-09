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
    public sealed class AutoCertificateProviderExternalAccountBinding
    {
        /// <summary>
        /// The key ID of the external account binding
        /// </summary>
        public readonly string KeyId;
        /// <summary>
        /// The secret of the external account binding
        /// </summary>
        public readonly string KeySecret;

        [OutputConstructor]
        private AutoCertificateProviderExternalAccountBinding(
            string keyId,

            string keySecret)
        {
            KeyId = keyId;
            KeySecret = keySecret;
        }
    }
}
