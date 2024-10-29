// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class AutoCertificateProviderExternalAccountBindingArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The key ID of the external account binding
        /// </summary>
        [Input("keyId", required: true)]
        public Input<string> KeyId { get; set; } = null!;

        [Input("keySecret", required: true)]
        private Input<string>? _keySecret;

        /// <summary>
        /// The secret of the external account binding
        /// </summary>
        public Input<string>? KeySecret
        {
            get => _keySecret;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _keySecret = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public AutoCertificateProviderExternalAccountBindingArgs()
        {
        }
        public static new AutoCertificateProviderExternalAccountBindingArgs Empty => new AutoCertificateProviderExternalAccountBindingArgs();
    }
}
