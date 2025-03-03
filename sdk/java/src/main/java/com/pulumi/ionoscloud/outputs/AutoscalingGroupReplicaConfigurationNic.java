// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.outputs.AutoscalingGroupReplicaConfigurationNicFirewallRule;
import com.pulumi.ionoscloud.outputs.AutoscalingGroupReplicaConfigurationNicFlowLog;
import com.pulumi.ionoscloud.outputs.AutoscalingGroupReplicaConfigurationNicTargetGroup;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class AutoscalingGroupReplicaConfigurationNic {
    /**
     * @return [bool] Dhcp flag for this replica Nic. This is an optional attribute with default value of `true` if not given in the request payload or given as null.
     * 
     */
    private @Nullable Boolean dhcp;
    /**
     * @return [bool] Firewall active flag.
     * 
     */
    private @Nullable Boolean firewallActive;
    /**
     * @return List of all firewall rules for the specified NIC.
     * 
     */
    private @Nullable List<AutoscalingGroupReplicaConfigurationNicFirewallRule> firewallRules;
    /**
     * @return [string] The type of firewall rules that will be allowed on the NIC. Valid values: INGRESS EGRESS BIDIRECTIONAL. If not specified, the default INGRESS value is used.
     * 
     */
    private @Nullable String firewallType;
    /**
     * @return [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
     * 
     */
    private @Nullable List<AutoscalingGroupReplicaConfigurationNicFlowLog> flowLogs;
    /**
     * @return [int] Lan ID for this replica Nic.
     * 
     */
    private Integer lan;
    /**
     * @return [string] Name for this replica volume.
     * 
     */
    private String name;
    /**
     * @return [list] In order to link VM to ALB, target group must be provided
     * 
     */
    private @Nullable AutoscalingGroupReplicaConfigurationNicTargetGroup targetGroup;

    private AutoscalingGroupReplicaConfigurationNic() {}
    /**
     * @return [bool] Dhcp flag for this replica Nic. This is an optional attribute with default value of `true` if not given in the request payload or given as null.
     * 
     */
    public Optional<Boolean> dhcp() {
        return Optional.ofNullable(this.dhcp);
    }
    /**
     * @return [bool] Firewall active flag.
     * 
     */
    public Optional<Boolean> firewallActive() {
        return Optional.ofNullable(this.firewallActive);
    }
    /**
     * @return List of all firewall rules for the specified NIC.
     * 
     */
    public List<AutoscalingGroupReplicaConfigurationNicFirewallRule> firewallRules() {
        return this.firewallRules == null ? List.of() : this.firewallRules;
    }
    /**
     * @return [string] The type of firewall rules that will be allowed on the NIC. Valid values: INGRESS EGRESS BIDIRECTIONAL. If not specified, the default INGRESS value is used.
     * 
     */
    public Optional<String> firewallType() {
        return Optional.ofNullable(this.firewallType);
    }
    /**
     * @return [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
     * 
     */
    public List<AutoscalingGroupReplicaConfigurationNicFlowLog> flowLogs() {
        return this.flowLogs == null ? List.of() : this.flowLogs;
    }
    /**
     * @return [int] Lan ID for this replica Nic.
     * 
     */
    public Integer lan() {
        return this.lan;
    }
    /**
     * @return [string] Name for this replica volume.
     * 
     */
    public String name() {
        return this.name;
    }
    /**
     * @return [list] In order to link VM to ALB, target group must be provided
     * 
     */
    public Optional<AutoscalingGroupReplicaConfigurationNicTargetGroup> targetGroup() {
        return Optional.ofNullable(this.targetGroup);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(AutoscalingGroupReplicaConfigurationNic defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable Boolean dhcp;
        private @Nullable Boolean firewallActive;
        private @Nullable List<AutoscalingGroupReplicaConfigurationNicFirewallRule> firewallRules;
        private @Nullable String firewallType;
        private @Nullable List<AutoscalingGroupReplicaConfigurationNicFlowLog> flowLogs;
        private Integer lan;
        private String name;
        private @Nullable AutoscalingGroupReplicaConfigurationNicTargetGroup targetGroup;
        public Builder() {}
        public Builder(AutoscalingGroupReplicaConfigurationNic defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.dhcp = defaults.dhcp;
    	      this.firewallActive = defaults.firewallActive;
    	      this.firewallRules = defaults.firewallRules;
    	      this.firewallType = defaults.firewallType;
    	      this.flowLogs = defaults.flowLogs;
    	      this.lan = defaults.lan;
    	      this.name = defaults.name;
    	      this.targetGroup = defaults.targetGroup;
        }

        @CustomType.Setter
        public Builder dhcp(@Nullable Boolean dhcp) {

            this.dhcp = dhcp;
            return this;
        }
        @CustomType.Setter
        public Builder firewallActive(@Nullable Boolean firewallActive) {

            this.firewallActive = firewallActive;
            return this;
        }
        @CustomType.Setter
        public Builder firewallRules(@Nullable List<AutoscalingGroupReplicaConfigurationNicFirewallRule> firewallRules) {

            this.firewallRules = firewallRules;
            return this;
        }
        public Builder firewallRules(AutoscalingGroupReplicaConfigurationNicFirewallRule... firewallRules) {
            return firewallRules(List.of(firewallRules));
        }
        @CustomType.Setter
        public Builder firewallType(@Nullable String firewallType) {

            this.firewallType = firewallType;
            return this;
        }
        @CustomType.Setter
        public Builder flowLogs(@Nullable List<AutoscalingGroupReplicaConfigurationNicFlowLog> flowLogs) {

            this.flowLogs = flowLogs;
            return this;
        }
        public Builder flowLogs(AutoscalingGroupReplicaConfigurationNicFlowLog... flowLogs) {
            return flowLogs(List.of(flowLogs));
        }
        @CustomType.Setter
        public Builder lan(Integer lan) {
            if (lan == null) {
              throw new MissingRequiredPropertyException("AutoscalingGroupReplicaConfigurationNic", "lan");
            }
            this.lan = lan;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("AutoscalingGroupReplicaConfigurationNic", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder targetGroup(@Nullable AutoscalingGroupReplicaConfigurationNicTargetGroup targetGroup) {

            this.targetGroup = targetGroup;
            return this;
        }
        public AutoscalingGroupReplicaConfigurationNic build() {
            final var _resultValue = new AutoscalingGroupReplicaConfigurationNic();
            _resultValue.dhcp = dhcp;
            _resultValue.firewallActive = firewallActive;
            _resultValue.firewallRules = firewallRules;
            _resultValue.firewallType = firewallType;
            _resultValue.flowLogs = flowLogs;
            _resultValue.lan = lan;
            _resultValue.name = name;
            _resultValue.targetGroup = targetGroup;
            return _resultValue;
        }
    }
}
