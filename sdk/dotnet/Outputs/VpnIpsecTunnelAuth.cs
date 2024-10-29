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
    public sealed class VpnIpsecTunnelAuth
    {
        /// <summary>
        /// [string] The authentication method to use for IPSec Authentication. Possible values: `PSK`.
        /// Default value: `PSK`.
        /// </summary>
        public readonly string? Method;
        /// <summary>
        /// [string] The pre-shared key to use for IPSec Authentication. **Note**: Required if method is
        /// PSK.
        /// </summary>
        public readonly string? PskKey;

        [OutputConstructor]
        private VpnIpsecTunnelAuth(
            string? method,

            string? pskKey)
        {
            Method = method;
            PskKey = pskKey;
        }
    }
}
