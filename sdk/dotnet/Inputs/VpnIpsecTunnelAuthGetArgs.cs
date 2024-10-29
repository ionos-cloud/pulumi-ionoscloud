// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class VpnIpsecTunnelAuthGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The authentication method to use for IPSec Authentication. Possible values: `PSK`.
        /// Default value: `PSK`.
        /// </summary>
        [Input("method")]
        public Input<string>? Method { get; set; }

        [Input("pskKey")]
        private Input<string>? _pskKey;

        /// <summary>
        /// [string] The pre-shared key to use for IPSec Authentication. **Note**: Required if method is
        /// PSK.
        /// </summary>
        public Input<string>? PskKey
        {
            get => _pskKey;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _pskKey = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public VpnIpsecTunnelAuthGetArgs()
        {
        }
        public static new VpnIpsecTunnelAuthGetArgs Empty => new VpnIpsecTunnelAuthGetArgs();
    }
}
