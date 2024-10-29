// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.outputs.GetAutoscalingGroupReplicaConfigurationNicFirewallRule;
import com.pulumi.ionoscloud.outputs.GetAutoscalingGroupReplicaConfigurationNicFlowLog;
import com.pulumi.ionoscloud.outputs.GetAutoscalingGroupReplicaConfigurationNicTargetGroup;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetAutoscalingGroupReplicaConfigurationNic {
    /**
     * @return Dhcp flag for this replica Nic. This is an optional attribute with default value of &#39;true&#39; if not given in the request payload or given as null.
     * 
     */
    private Boolean dhcp;
    /**
     * @return Activate or deactivate the firewall. By default, an active firewall without any defined rules will block all incoming network traffic except for the firewall rules that explicitly allows certain protocols, IP addresses and ports.
     * 
     */
    private Boolean firewallActive;
    /**
     * @return List of all firewall rules for the specified NIC.
     * 
     */
    private List<GetAutoscalingGroupReplicaConfigurationNicFirewallRule> firewallRules;
    /**
     * @return The type of firewall rules that will be allowed on the NIC. If not specified, the default INGRESS value is used.
     * 
     */
    private String firewallType;
    /**
     * @return Flow log configuration for the NIC. By default, the flow log is inactive. If you want to activate the flow log, you must specify the target resource and the type of traffic to log.
     * 
     */
    private List<GetAutoscalingGroupReplicaConfigurationNicFlowLog> flowLogs;
    /**
     * @return Lan ID for this replica Nic.
     * 
     */
    private Integer lan;
    /**
     * @return Name of an existing Autoscaling Group that you want to search for.
     * 
     * Either `name` or `id` must be provided. If none or both are provided, the datasource will return an error.
     * 
     */
    private String name;
    /**
     * @return In order to link VM to ALB, target group must be provided.
     * 
     */
    private List<GetAutoscalingGroupReplicaConfigurationNicTargetGroup> targetGroups;

    private GetAutoscalingGroupReplicaConfigurationNic() {}
    /**
     * @return Dhcp flag for this replica Nic. This is an optional attribute with default value of &#39;true&#39; if not given in the request payload or given as null.
     * 
     */
    public Boolean dhcp() {
        return this.dhcp;
    }
    /**
     * @return Activate or deactivate the firewall. By default, an active firewall without any defined rules will block all incoming network traffic except for the firewall rules that explicitly allows certain protocols, IP addresses and ports.
     * 
     */
    public Boolean firewallActive() {
        return this.firewallActive;
    }
    /**
     * @return List of all firewall rules for the specified NIC.
     * 
     */
    public List<GetAutoscalingGroupReplicaConfigurationNicFirewallRule> firewallRules() {
        return this.firewallRules;
    }
    /**
     * @return The type of firewall rules that will be allowed on the NIC. If not specified, the default INGRESS value is used.
     * 
     */
    public String firewallType() {
        return this.firewallType;
    }
    /**
     * @return Flow log configuration for the NIC. By default, the flow log is inactive. If you want to activate the flow log, you must specify the target resource and the type of traffic to log.
     * 
     */
    public List<GetAutoscalingGroupReplicaConfigurationNicFlowLog> flowLogs() {
        return this.flowLogs;
    }
    /**
     * @return Lan ID for this replica Nic.
     * 
     */
    public Integer lan() {
        return this.lan;
    }
    /**
     * @return Name of an existing Autoscaling Group that you want to search for.
     * 
     * Either `name` or `id` must be provided. If none or both are provided, the datasource will return an error.
     * 
     */
    public String name() {
        return this.name;
    }
    /**
     * @return In order to link VM to ALB, target group must be provided.
     * 
     */
    public List<GetAutoscalingGroupReplicaConfigurationNicTargetGroup> targetGroups() {
        return this.targetGroups;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetAutoscalingGroupReplicaConfigurationNic defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Boolean dhcp;
        private Boolean firewallActive;
        private List<GetAutoscalingGroupReplicaConfigurationNicFirewallRule> firewallRules;
        private String firewallType;
        private List<GetAutoscalingGroupReplicaConfigurationNicFlowLog> flowLogs;
        private Integer lan;
        private String name;
        private List<GetAutoscalingGroupReplicaConfigurationNicTargetGroup> targetGroups;
        public Builder() {}
        public Builder(GetAutoscalingGroupReplicaConfigurationNic defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.dhcp = defaults.dhcp;
    	      this.firewallActive = defaults.firewallActive;
    	      this.firewallRules = defaults.firewallRules;
    	      this.firewallType = defaults.firewallType;
    	      this.flowLogs = defaults.flowLogs;
    	      this.lan = defaults.lan;
    	      this.name = defaults.name;
    	      this.targetGroups = defaults.targetGroups;
        }

        @CustomType.Setter
        public Builder dhcp(Boolean dhcp) {
            if (dhcp == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupReplicaConfigurationNic", "dhcp");
            }
            this.dhcp = dhcp;
            return this;
        }
        @CustomType.Setter
        public Builder firewallActive(Boolean firewallActive) {
            if (firewallActive == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupReplicaConfigurationNic", "firewallActive");
            }
            this.firewallActive = firewallActive;
            return this;
        }
        @CustomType.Setter
        public Builder firewallRules(List<GetAutoscalingGroupReplicaConfigurationNicFirewallRule> firewallRules) {
            if (firewallRules == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupReplicaConfigurationNic", "firewallRules");
            }
            this.firewallRules = firewallRules;
            return this;
        }
        public Builder firewallRules(GetAutoscalingGroupReplicaConfigurationNicFirewallRule... firewallRules) {
            return firewallRules(List.of(firewallRules));
        }
        @CustomType.Setter
        public Builder firewallType(String firewallType) {
            if (firewallType == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupReplicaConfigurationNic", "firewallType");
            }
            this.firewallType = firewallType;
            return this;
        }
        @CustomType.Setter
        public Builder flowLogs(List<GetAutoscalingGroupReplicaConfigurationNicFlowLog> flowLogs) {
            if (flowLogs == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupReplicaConfigurationNic", "flowLogs");
            }
            this.flowLogs = flowLogs;
            return this;
        }
        public Builder flowLogs(GetAutoscalingGroupReplicaConfigurationNicFlowLog... flowLogs) {
            return flowLogs(List.of(flowLogs));
        }
        @CustomType.Setter
        public Builder lan(Integer lan) {
            if (lan == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupReplicaConfigurationNic", "lan");
            }
            this.lan = lan;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupReplicaConfigurationNic", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder targetGroups(List<GetAutoscalingGroupReplicaConfigurationNicTargetGroup> targetGroups) {
            if (targetGroups == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupReplicaConfigurationNic", "targetGroups");
            }
            this.targetGroups = targetGroups;
            return this;
        }
        public Builder targetGroups(GetAutoscalingGroupReplicaConfigurationNicTargetGroup... targetGroups) {
            return targetGroups(List.of(targetGroups));
        }
        public GetAutoscalingGroupReplicaConfigurationNic build() {
            final var _resultValue = new GetAutoscalingGroupReplicaConfigurationNic();
            _resultValue.dhcp = dhcp;
            _resultValue.firewallActive = firewallActive;
            _resultValue.firewallRules = firewallRules;
            _resultValue.firewallType = firewallType;
            _resultValue.flowLogs = flowLogs;
            _resultValue.lan = lan;
            _resultValue.name = name;
            _resultValue.targetGroups = targetGroups;
            return _resultValue;
        }
    }
}
