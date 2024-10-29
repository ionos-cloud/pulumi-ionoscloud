// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class ApigatewayCustomDomainGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The certificate ID for the domain. Must be a valid certificate in UUID form.
        /// </summary>
        [Input("certificateId")]
        public Input<string>? CertificateId { get; set; }

        /// <summary>
        /// [string] The domain name. Externally reachable.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public ApigatewayCustomDomainGetArgs()
        {
        }
        public static new ApigatewayCustomDomainGetArgs Empty => new ApigatewayCustomDomainGetArgs();
    }
}
