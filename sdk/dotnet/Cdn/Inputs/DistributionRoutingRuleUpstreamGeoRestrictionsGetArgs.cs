// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Cdn.Inputs
{

    public sealed class DistributionRoutingRuleUpstreamGeoRestrictionsGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("allowLists")]
        private InputList<string>? _allowLists;
        public InputList<string> AllowLists
        {
            get => _allowLists ?? (_allowLists = new InputList<string>());
            set => _allowLists = value;
        }

        [Input("blockLists")]
        private InputList<string>? _blockLists;
        public InputList<string> BlockLists
        {
            get => _blockLists ?? (_blockLists = new InputList<string>());
            set => _blockLists = value;
        }

        public DistributionRoutingRuleUpstreamGeoRestrictionsGetArgs()
        {
        }
        public static new DistributionRoutingRuleUpstreamGeoRestrictionsGetArgs Empty => new DistributionRoutingRuleUpstreamGeoRestrictionsGetArgs();
    }
}
