// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class AutoscalingGroupReplicaConfigurationNicTargetGroup {
    /**
     * @return [int] The port of the target group.
     * 
     */
    private Integer port;
    /**
     * @return [string] The ID of the target group.
     * 
     */
    private String targetGroupId;
    /**
     * @return [int] The weight of the target group.
     * 
     */
    private Integer weight;

    private AutoscalingGroupReplicaConfigurationNicTargetGroup() {}
    /**
     * @return [int] The port of the target group.
     * 
     */
    public Integer port() {
        return this.port;
    }
    /**
     * @return [string] The ID of the target group.
     * 
     */
    public String targetGroupId() {
        return this.targetGroupId;
    }
    /**
     * @return [int] The weight of the target group.
     * 
     */
    public Integer weight() {
        return this.weight;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(AutoscalingGroupReplicaConfigurationNicTargetGroup defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Integer port;
        private String targetGroupId;
        private Integer weight;
        public Builder() {}
        public Builder(AutoscalingGroupReplicaConfigurationNicTargetGroup defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.port = defaults.port;
    	      this.targetGroupId = defaults.targetGroupId;
    	      this.weight = defaults.weight;
        }

        @CustomType.Setter
        public Builder port(Integer port) {
            if (port == null) {
              throw new MissingRequiredPropertyException("AutoscalingGroupReplicaConfigurationNicTargetGroup", "port");
            }
            this.port = port;
            return this;
        }
        @CustomType.Setter
        public Builder targetGroupId(String targetGroupId) {
            if (targetGroupId == null) {
              throw new MissingRequiredPropertyException("AutoscalingGroupReplicaConfigurationNicTargetGroup", "targetGroupId");
            }
            this.targetGroupId = targetGroupId;
            return this;
        }
        @CustomType.Setter
        public Builder weight(Integer weight) {
            if (weight == null) {
              throw new MissingRequiredPropertyException("AutoscalingGroupReplicaConfigurationNicTargetGroup", "weight");
            }
            this.weight = weight;
            return this;
        }
        public AutoscalingGroupReplicaConfigurationNicTargetGroup build() {
            final var _resultValue = new AutoscalingGroupReplicaConfigurationNicTargetGroup();
            _resultValue.port = port;
            _resultValue.targetGroupId = targetGroupId;
            _resultValue.weight = weight;
            return _resultValue;
        }
    }
}
