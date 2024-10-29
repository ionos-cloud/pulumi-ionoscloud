// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.inputs.AutoscalingGroupReplicaConfigurationNicFirewallRuleArgs;
import com.pulumi.ionoscloud.inputs.AutoscalingGroupReplicaConfigurationNicFlowLogArgs;
import com.pulumi.ionoscloud.inputs.AutoscalingGroupReplicaConfigurationNicTargetGroupArgs;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class AutoscalingGroupReplicaConfigurationNicArgs extends com.pulumi.resources.ResourceArgs {

    public static final AutoscalingGroupReplicaConfigurationNicArgs Empty = new AutoscalingGroupReplicaConfigurationNicArgs();

    /**
     * [bool] Dhcp flag for this replica Nic. This is an optional attribute with default value of `true` if not given in the request payload or given as null.
     * 
     */
    @Import(name="dhcp")
    private @Nullable Output<Boolean> dhcp;

    /**
     * @return [bool] Dhcp flag for this replica Nic. This is an optional attribute with default value of `true` if not given in the request payload or given as null.
     * 
     */
    public Optional<Output<Boolean>> dhcp() {
        return Optional.ofNullable(this.dhcp);
    }

    /**
     * [bool] Firewall active flag.
     * 
     */
    @Import(name="firewallActive")
    private @Nullable Output<Boolean> firewallActive;

    /**
     * @return [bool] Firewall active flag.
     * 
     */
    public Optional<Output<Boolean>> firewallActive() {
        return Optional.ofNullable(this.firewallActive);
    }

    /**
     * List of all firewall rules for the specified NIC.
     * 
     */
    @Import(name="firewallRules")
    private @Nullable Output<List<AutoscalingGroupReplicaConfigurationNicFirewallRuleArgs>> firewallRules;

    /**
     * @return List of all firewall rules for the specified NIC.
     * 
     */
    public Optional<Output<List<AutoscalingGroupReplicaConfigurationNicFirewallRuleArgs>>> firewallRules() {
        return Optional.ofNullable(this.firewallRules);
    }

    /**
     * [string] The type of firewall rules that will be allowed on the NIC. Valid values: INGRESS EGRESS BIDIRECTIONAL. If not specified, the default INGRESS value is used.
     * 
     */
    @Import(name="firewallType")
    private @Nullable Output<String> firewallType;

    /**
     * @return [string] The type of firewall rules that will be allowed on the NIC. Valid values: INGRESS EGRESS BIDIRECTIONAL. If not specified, the default INGRESS value is used.
     * 
     */
    public Optional<Output<String>> firewallType() {
        return Optional.ofNullable(this.firewallType);
    }

    /**
     * [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
     * 
     */
    @Import(name="flowLogs")
    private @Nullable Output<List<AutoscalingGroupReplicaConfigurationNicFlowLogArgs>> flowLogs;

    /**
     * @return [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
     * 
     */
    public Optional<Output<List<AutoscalingGroupReplicaConfigurationNicFlowLogArgs>>> flowLogs() {
        return Optional.ofNullable(this.flowLogs);
    }

    /**
     * [int] Lan ID for this replica Nic.
     * 
     */
    @Import(name="lan", required=true)
    private Output<Integer> lan;

    /**
     * @return [int] Lan ID for this replica Nic.
     * 
     */
    public Output<Integer> lan() {
        return this.lan;
    }

    /**
     * [string] Name for this replica volume.
     * 
     */
    @Import(name="name", required=true)
    private Output<String> name;

    /**
     * @return [string] Name for this replica volume.
     * 
     */
    public Output<String> name() {
        return this.name;
    }

    /**
     * [list] In order to link VM to ALB, target group must be provided
     * 
     */
    @Import(name="targetGroup")
    private @Nullable Output<AutoscalingGroupReplicaConfigurationNicTargetGroupArgs> targetGroup;

    /**
     * @return [list] In order to link VM to ALB, target group must be provided
     * 
     */
    public Optional<Output<AutoscalingGroupReplicaConfigurationNicTargetGroupArgs>> targetGroup() {
        return Optional.ofNullable(this.targetGroup);
    }

    private AutoscalingGroupReplicaConfigurationNicArgs() {}

    private AutoscalingGroupReplicaConfigurationNicArgs(AutoscalingGroupReplicaConfigurationNicArgs $) {
        this.dhcp = $.dhcp;
        this.firewallActive = $.firewallActive;
        this.firewallRules = $.firewallRules;
        this.firewallType = $.firewallType;
        this.flowLogs = $.flowLogs;
        this.lan = $.lan;
        this.name = $.name;
        this.targetGroup = $.targetGroup;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(AutoscalingGroupReplicaConfigurationNicArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private AutoscalingGroupReplicaConfigurationNicArgs $;

        public Builder() {
            $ = new AutoscalingGroupReplicaConfigurationNicArgs();
        }

        public Builder(AutoscalingGroupReplicaConfigurationNicArgs defaults) {
            $ = new AutoscalingGroupReplicaConfigurationNicArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param dhcp [bool] Dhcp flag for this replica Nic. This is an optional attribute with default value of `true` if not given in the request payload or given as null.
         * 
         * @return builder
         * 
         */
        public Builder dhcp(@Nullable Output<Boolean> dhcp) {
            $.dhcp = dhcp;
            return this;
        }

        /**
         * @param dhcp [bool] Dhcp flag for this replica Nic. This is an optional attribute with default value of `true` if not given in the request payload or given as null.
         * 
         * @return builder
         * 
         */
        public Builder dhcp(Boolean dhcp) {
            return dhcp(Output.of(dhcp));
        }

        /**
         * @param firewallActive [bool] Firewall active flag.
         * 
         * @return builder
         * 
         */
        public Builder firewallActive(@Nullable Output<Boolean> firewallActive) {
            $.firewallActive = firewallActive;
            return this;
        }

        /**
         * @param firewallActive [bool] Firewall active flag.
         * 
         * @return builder
         * 
         */
        public Builder firewallActive(Boolean firewallActive) {
            return firewallActive(Output.of(firewallActive));
        }

        /**
         * @param firewallRules List of all firewall rules for the specified NIC.
         * 
         * @return builder
         * 
         */
        public Builder firewallRules(@Nullable Output<List<AutoscalingGroupReplicaConfigurationNicFirewallRuleArgs>> firewallRules) {
            $.firewallRules = firewallRules;
            return this;
        }

        /**
         * @param firewallRules List of all firewall rules for the specified NIC.
         * 
         * @return builder
         * 
         */
        public Builder firewallRules(List<AutoscalingGroupReplicaConfigurationNicFirewallRuleArgs> firewallRules) {
            return firewallRules(Output.of(firewallRules));
        }

        /**
         * @param firewallRules List of all firewall rules for the specified NIC.
         * 
         * @return builder
         * 
         */
        public Builder firewallRules(AutoscalingGroupReplicaConfigurationNicFirewallRuleArgs... firewallRules) {
            return firewallRules(List.of(firewallRules));
        }

        /**
         * @param firewallType [string] The type of firewall rules that will be allowed on the NIC. Valid values: INGRESS EGRESS BIDIRECTIONAL. If not specified, the default INGRESS value is used.
         * 
         * @return builder
         * 
         */
        public Builder firewallType(@Nullable Output<String> firewallType) {
            $.firewallType = firewallType;
            return this;
        }

        /**
         * @param firewallType [string] The type of firewall rules that will be allowed on the NIC. Valid values: INGRESS EGRESS BIDIRECTIONAL. If not specified, the default INGRESS value is used.
         * 
         * @return builder
         * 
         */
        public Builder firewallType(String firewallType) {
            return firewallType(Output.of(firewallType));
        }

        /**
         * @param flowLogs [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
         * 
         * @return builder
         * 
         */
        public Builder flowLogs(@Nullable Output<List<AutoscalingGroupReplicaConfigurationNicFlowLogArgs>> flowLogs) {
            $.flowLogs = flowLogs;
            return this;
        }

        /**
         * @param flowLogs [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
         * 
         * @return builder
         * 
         */
        public Builder flowLogs(List<AutoscalingGroupReplicaConfigurationNicFlowLogArgs> flowLogs) {
            return flowLogs(Output.of(flowLogs));
        }

        /**
         * @param flowLogs [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
         * 
         * @return builder
         * 
         */
        public Builder flowLogs(AutoscalingGroupReplicaConfigurationNicFlowLogArgs... flowLogs) {
            return flowLogs(List.of(flowLogs));
        }

        /**
         * @param lan [int] Lan ID for this replica Nic.
         * 
         * @return builder
         * 
         */
        public Builder lan(Output<Integer> lan) {
            $.lan = lan;
            return this;
        }

        /**
         * @param lan [int] Lan ID for this replica Nic.
         * 
         * @return builder
         * 
         */
        public Builder lan(Integer lan) {
            return lan(Output.of(lan));
        }

        /**
         * @param name [string] Name for this replica volume.
         * 
         * @return builder
         * 
         */
        public Builder name(Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] Name for this replica volume.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param targetGroup [list] In order to link VM to ALB, target group must be provided
         * 
         * @return builder
         * 
         */
        public Builder targetGroup(@Nullable Output<AutoscalingGroupReplicaConfigurationNicTargetGroupArgs> targetGroup) {
            $.targetGroup = targetGroup;
            return this;
        }

        /**
         * @param targetGroup [list] In order to link VM to ALB, target group must be provided
         * 
         * @return builder
         * 
         */
        public Builder targetGroup(AutoscalingGroupReplicaConfigurationNicTargetGroupArgs targetGroup) {
            return targetGroup(Output.of(targetGroup));
        }

        public AutoscalingGroupReplicaConfigurationNicArgs build() {
            if ($.lan == null) {
                throw new MissingRequiredPropertyException("AutoscalingGroupReplicaConfigurationNicArgs", "lan");
            }
            if ($.name == null) {
                throw new MissingRequiredPropertyException("AutoscalingGroupReplicaConfigurationNicArgs", "name");
            }
            return $;
        }
    }

}
