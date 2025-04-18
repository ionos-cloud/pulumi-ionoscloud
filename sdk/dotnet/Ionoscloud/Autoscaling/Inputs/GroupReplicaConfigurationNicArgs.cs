// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Autoscaling.Inputs
{

    public sealed class GroupReplicaConfigurationNicArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Dhcp flag for this replica Nic. This is an optional attribute with default value of 'true' if not given in the request payload or given as null.
        /// </summary>
        [Input("dhcp")]
        public Input<bool>? Dhcp { get; set; }

        /// <summary>
        /// Activate or deactivate the firewall. By default, an active firewall without any defined rules will block all incoming network traffic except for the firewall rules that explicitly allows certain protocols, IP addresses and ports.
        /// </summary>
        [Input("firewallActive")]
        public Input<bool>? FirewallActive { get; set; }

        [Input("firewallRules")]
        private InputList<Inputs.GroupReplicaConfigurationNicFirewallRuleArgs>? _firewallRules;

        /// <summary>
        /// List of all firewall rules for the specified NIC.
        /// </summary>
        public InputList<Inputs.GroupReplicaConfigurationNicFirewallRuleArgs> FirewallRules
        {
            get => _firewallRules ?? (_firewallRules = new InputList<Inputs.GroupReplicaConfigurationNicFirewallRuleArgs>());
            set => _firewallRules = value;
        }

        /// <summary>
        /// The type of firewall rules that will be allowed on the NIC. If not specified, the default INGRESS value is used.
        /// </summary>
        [Input("firewallType")]
        public Input<string>? FirewallType { get; set; }

        [Input("flowLogs")]
        private InputList<Inputs.GroupReplicaConfigurationNicFlowLogArgs>? _flowLogs;

        /// <summary>
        /// List of all flow logs for the specified NIC.
        /// </summary>
        public InputList<Inputs.GroupReplicaConfigurationNicFlowLogArgs> FlowLogs
        {
            get => _flowLogs ?? (_flowLogs = new InputList<Inputs.GroupReplicaConfigurationNicFlowLogArgs>());
            set => _flowLogs = value;
        }

        /// <summary>
        /// Lan ID for this replica Nic.
        /// </summary>
        [Input("lan", required: true)]
        public Input<int> Lan { get; set; } = null!;

        /// <summary>
        /// [string] User-defined name for the Autoscaling Group.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// In order to link VM to ALB, target group must be provided.
        /// </summary>
        [Input("targetGroup")]
        public Input<Inputs.GroupReplicaConfigurationNicTargetGroupArgs>? TargetGroup { get; set; }

        public GroupReplicaConfigurationNicArgs()
        {
        }
        public static new GroupReplicaConfigurationNicArgs Empty => new GroupReplicaConfigurationNicArgs();
    }
}
