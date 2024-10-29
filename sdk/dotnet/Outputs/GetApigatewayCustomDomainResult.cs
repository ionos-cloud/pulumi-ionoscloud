// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Outputs
{

    [OutputType]
    public sealed class GetApigatewayCustomDomainResult
    {
        /// <summary>
        /// The ID of the certificate to use for the distribution.
        /// </summary>
        public readonly string CertificateId;
        /// <summary>
        /// Name of an existing API Gateway that you want to search for.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private GetApigatewayCustomDomainResult(
            string certificateId,

            string name)
        {
            CertificateId = certificateId;
            Name = name;
        }
    }
}
