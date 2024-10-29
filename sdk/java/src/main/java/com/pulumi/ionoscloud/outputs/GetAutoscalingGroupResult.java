// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.outputs.GetAutoscalingGroupPolicy;
import com.pulumi.ionoscloud.outputs.GetAutoscalingGroupReplicaConfiguration;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetAutoscalingGroupResult {
    private String datacenterId;
    /**
     * @return Unique identifier for the resource
     * 
     */
    private @Nullable String id;
    /**
     * @return Location of the datacenter. This location is the same as the one from the selected template.
     * 
     */
    private String location;
    /**
     * @return Maximum replica count value for `targetReplicaCount`. Will be enforced for both automatic and manual changes.
     * 
     */
    private Integer maxReplicaCount;
    /**
     * @return Minimum replica count value for `targetReplicaCount`. Will be enforced for both automatic and manual changes.
     * 
     */
    private Integer minReplicaCount;
    /**
     * @return The name of the Autoscaling Group.
     * 
     */
    private @Nullable String name;
    /**
     * @return Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
     * 
     */
    private List<GetAutoscalingGroupPolicy> policies;
    private List<GetAutoscalingGroupReplicaConfiguration> replicaConfigurations;
    private Integer targetReplicaCount;

    private GetAutoscalingGroupResult() {}
    public String datacenterId() {
        return this.datacenterId;
    }
    /**
     * @return Unique identifier for the resource
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    /**
     * @return Location of the datacenter. This location is the same as the one from the selected template.
     * 
     */
    public String location() {
        return this.location;
    }
    /**
     * @return Maximum replica count value for `targetReplicaCount`. Will be enforced for both automatic and manual changes.
     * 
     */
    public Integer maxReplicaCount() {
        return this.maxReplicaCount;
    }
    /**
     * @return Minimum replica count value for `targetReplicaCount`. Will be enforced for both automatic and manual changes.
     * 
     */
    public Integer minReplicaCount() {
        return this.minReplicaCount;
    }
    /**
     * @return The name of the Autoscaling Group.
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }
    /**
     * @return Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
     * 
     */
    public List<GetAutoscalingGroupPolicy> policies() {
        return this.policies;
    }
    public List<GetAutoscalingGroupReplicaConfiguration> replicaConfigurations() {
        return this.replicaConfigurations;
    }
    public Integer targetReplicaCount() {
        return this.targetReplicaCount;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetAutoscalingGroupResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String datacenterId;
        private @Nullable String id;
        private String location;
        private Integer maxReplicaCount;
        private Integer minReplicaCount;
        private @Nullable String name;
        private List<GetAutoscalingGroupPolicy> policies;
        private List<GetAutoscalingGroupReplicaConfiguration> replicaConfigurations;
        private Integer targetReplicaCount;
        public Builder() {}
        public Builder(GetAutoscalingGroupResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.datacenterId = defaults.datacenterId;
    	      this.id = defaults.id;
    	      this.location = defaults.location;
    	      this.maxReplicaCount = defaults.maxReplicaCount;
    	      this.minReplicaCount = defaults.minReplicaCount;
    	      this.name = defaults.name;
    	      this.policies = defaults.policies;
    	      this.replicaConfigurations = defaults.replicaConfigurations;
    	      this.targetReplicaCount = defaults.targetReplicaCount;
        }

        @CustomType.Setter
        public Builder datacenterId(String datacenterId) {
            if (datacenterId == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupResult", "datacenterId");
            }
            this.datacenterId = datacenterId;
            return this;
        }
        @CustomType.Setter
        public Builder id(@Nullable String id) {

            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder location(String location) {
            if (location == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupResult", "location");
            }
            this.location = location;
            return this;
        }
        @CustomType.Setter
        public Builder maxReplicaCount(Integer maxReplicaCount) {
            if (maxReplicaCount == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupResult", "maxReplicaCount");
            }
            this.maxReplicaCount = maxReplicaCount;
            return this;
        }
        @CustomType.Setter
        public Builder minReplicaCount(Integer minReplicaCount) {
            if (minReplicaCount == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupResult", "minReplicaCount");
            }
            this.minReplicaCount = minReplicaCount;
            return this;
        }
        @CustomType.Setter
        public Builder name(@Nullable String name) {

            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder policies(List<GetAutoscalingGroupPolicy> policies) {
            if (policies == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupResult", "policies");
            }
            this.policies = policies;
            return this;
        }
        public Builder policies(GetAutoscalingGroupPolicy... policies) {
            return policies(List.of(policies));
        }
        @CustomType.Setter
        public Builder replicaConfigurations(List<GetAutoscalingGroupReplicaConfiguration> replicaConfigurations) {
            if (replicaConfigurations == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupResult", "replicaConfigurations");
            }
            this.replicaConfigurations = replicaConfigurations;
            return this;
        }
        public Builder replicaConfigurations(GetAutoscalingGroupReplicaConfiguration... replicaConfigurations) {
            return replicaConfigurations(List.of(replicaConfigurations));
        }
        @CustomType.Setter
        public Builder targetReplicaCount(Integer targetReplicaCount) {
            if (targetReplicaCount == null) {
              throw new MissingRequiredPropertyException("GetAutoscalingGroupResult", "targetReplicaCount");
            }
            this.targetReplicaCount = targetReplicaCount;
            return this;
        }
        public GetAutoscalingGroupResult build() {
            final var _resultValue = new GetAutoscalingGroupResult();
            _resultValue.datacenterId = datacenterId;
            _resultValue.id = id;
            _resultValue.location = location;
            _resultValue.maxReplicaCount = maxReplicaCount;
            _resultValue.minReplicaCount = minReplicaCount;
            _resultValue.name = name;
            _resultValue.policies = policies;
            _resultValue.replicaConfigurations = replicaConfigurations;
            _resultValue.targetReplicaCount = targetReplicaCount;
            return _resultValue;
        }
    }
}
