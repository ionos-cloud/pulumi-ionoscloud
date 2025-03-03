// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.ionoscloud.inputs.AutoscalingGroupPolicyArgs;
import com.pulumi.ionoscloud.inputs.AutoscalingGroupReplicaConfigurationArgs;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class AutoscalingGroupState extends com.pulumi.resources.ResourceArgs {

    public static final AutoscalingGroupState Empty = new AutoscalingGroupState();

    /**
     * [string] Unique identifier for the resource
     * 
     */
    @Import(name="datacenterId")
    private @Nullable Output<String> datacenterId;

    /**
     * @return [string] Unique identifier for the resource
     * 
     */
    public Optional<Output<String>> datacenterId() {
        return Optional.ofNullable(this.datacenterId);
    }

    /**
     * Location of the data center.
     * 
     */
    @Import(name="location")
    private @Nullable Output<String> location;

    /**
     * @return Location of the data center.
     * 
     */
    public Optional<Output<String>> location() {
        return Optional.ofNullable(this.location);
    }

    /**
     * [int] The maximum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;= 0 and &lt;= 200. Will be enforced for both automatic and manual changes.
     * 
     */
    @Import(name="maxReplicaCount")
    private @Nullable Output<Integer> maxReplicaCount;

    /**
     * @return [int] The maximum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;= 0 and &lt;= 200. Will be enforced for both automatic and manual changes.
     * 
     */
    public Optional<Output<Integer>> maxReplicaCount() {
        return Optional.ofNullable(this.maxReplicaCount);
    }

    /**
     * [int] The minimum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;= 0 and &lt;= 200. Will be enforced for both automatic and manual changes.
     * 
     */
    @Import(name="minReplicaCount")
    private @Nullable Output<Integer> minReplicaCount;

    /**
     * @return [int] The minimum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;= 0 and &lt;= 200. Will be enforced for both automatic and manual changes.
     * 
     */
    public Optional<Output<Integer>> minReplicaCount() {
        return Optional.ofNullable(this.minReplicaCount);
    }

    /**
     * [string] Name for this replica volume.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] Name for this replica volume.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [List] Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
     * 
     */
    @Import(name="policy")
    private @Nullable Output<AutoscalingGroupPolicyArgs> policy;

    /**
     * @return [List] Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
     * 
     */
    public Optional<Output<AutoscalingGroupPolicyArgs>> policy() {
        return Optional.ofNullable(this.policy);
    }

    /**
     * [List]
     * 
     */
    @Import(name="replicaConfiguration")
    private @Nullable Output<AutoscalingGroupReplicaConfigurationArgs> replicaConfiguration;

    /**
     * @return [List]
     * 
     */
    public Optional<Output<AutoscalingGroupReplicaConfigurationArgs>> replicaConfiguration() {
        return Optional.ofNullable(this.replicaConfiguration);
    }

    private AutoscalingGroupState() {}

    private AutoscalingGroupState(AutoscalingGroupState $) {
        this.datacenterId = $.datacenterId;
        this.location = $.location;
        this.maxReplicaCount = $.maxReplicaCount;
        this.minReplicaCount = $.minReplicaCount;
        this.name = $.name;
        this.policy = $.policy;
        this.replicaConfiguration = $.replicaConfiguration;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(AutoscalingGroupState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private AutoscalingGroupState $;

        public Builder() {
            $ = new AutoscalingGroupState();
        }

        public Builder(AutoscalingGroupState defaults) {
            $ = new AutoscalingGroupState(Objects.requireNonNull(defaults));
        }

        /**
         * @param datacenterId [string] Unique identifier for the resource
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(@Nullable Output<String> datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        /**
         * @param datacenterId [string] Unique identifier for the resource
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(String datacenterId) {
            return datacenterId(Output.of(datacenterId));
        }

        /**
         * @param location Location of the data center.
         * 
         * @return builder
         * 
         */
        public Builder location(@Nullable Output<String> location) {
            $.location = location;
            return this;
        }

        /**
         * @param location Location of the data center.
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            return location(Output.of(location));
        }

        /**
         * @param maxReplicaCount [int] The maximum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;= 0 and &lt;= 200. Will be enforced for both automatic and manual changes.
         * 
         * @return builder
         * 
         */
        public Builder maxReplicaCount(@Nullable Output<Integer> maxReplicaCount) {
            $.maxReplicaCount = maxReplicaCount;
            return this;
        }

        /**
         * @param maxReplicaCount [int] The maximum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;= 0 and &lt;= 200. Will be enforced for both automatic and manual changes.
         * 
         * @return builder
         * 
         */
        public Builder maxReplicaCount(Integer maxReplicaCount) {
            return maxReplicaCount(Output.of(maxReplicaCount));
        }

        /**
         * @param minReplicaCount [int] The minimum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;= 0 and &lt;= 200. Will be enforced for both automatic and manual changes.
         * 
         * @return builder
         * 
         */
        public Builder minReplicaCount(@Nullable Output<Integer> minReplicaCount) {
            $.minReplicaCount = minReplicaCount;
            return this;
        }

        /**
         * @param minReplicaCount [int] The minimum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;= 0 and &lt;= 200. Will be enforced for both automatic and manual changes.
         * 
         * @return builder
         * 
         */
        public Builder minReplicaCount(Integer minReplicaCount) {
            return minReplicaCount(Output.of(minReplicaCount));
        }

        /**
         * @param name [string] Name for this replica volume.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
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
         * @param policy [List] Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
         * 
         * @return builder
         * 
         */
        public Builder policy(@Nullable Output<AutoscalingGroupPolicyArgs> policy) {
            $.policy = policy;
            return this;
        }

        /**
         * @param policy [List] Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
         * 
         * @return builder
         * 
         */
        public Builder policy(AutoscalingGroupPolicyArgs policy) {
            return policy(Output.of(policy));
        }

        /**
         * @param replicaConfiguration [List]
         * 
         * @return builder
         * 
         */
        public Builder replicaConfiguration(@Nullable Output<AutoscalingGroupReplicaConfigurationArgs> replicaConfiguration) {
            $.replicaConfiguration = replicaConfiguration;
            return this;
        }

        /**
         * @param replicaConfiguration [List]
         * 
         * @return builder
         * 
         */
        public Builder replicaConfiguration(AutoscalingGroupReplicaConfigurationArgs replicaConfiguration) {
            return replicaConfiguration(Output.of(replicaConfiguration));
        }

        public AutoscalingGroupState build() {
            return $;
        }
    }

}
