// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;


public final class AutoscalingGroupReplicaConfigurationNicTargetGroupArgs extends com.pulumi.resources.ResourceArgs {

    public static final AutoscalingGroupReplicaConfigurationNicTargetGroupArgs Empty = new AutoscalingGroupReplicaConfigurationNicTargetGroupArgs();

    /**
     * [int] The port of the target group.
     * 
     */
    @Import(name="port", required=true)
    private Output<Integer> port;

    /**
     * @return [int] The port of the target group.
     * 
     */
    public Output<Integer> port() {
        return this.port;
    }

    /**
     * [string] The ID of the target group.
     * 
     */
    @Import(name="targetGroupId", required=true)
    private Output<String> targetGroupId;

    /**
     * @return [string] The ID of the target group.
     * 
     */
    public Output<String> targetGroupId() {
        return this.targetGroupId;
    }

    /**
     * [int] The weight of the target group.
     * 
     */
    @Import(name="weight", required=true)
    private Output<Integer> weight;

    /**
     * @return [int] The weight of the target group.
     * 
     */
    public Output<Integer> weight() {
        return this.weight;
    }

    private AutoscalingGroupReplicaConfigurationNicTargetGroupArgs() {}

    private AutoscalingGroupReplicaConfigurationNicTargetGroupArgs(AutoscalingGroupReplicaConfigurationNicTargetGroupArgs $) {
        this.port = $.port;
        this.targetGroupId = $.targetGroupId;
        this.weight = $.weight;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(AutoscalingGroupReplicaConfigurationNicTargetGroupArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private AutoscalingGroupReplicaConfigurationNicTargetGroupArgs $;

        public Builder() {
            $ = new AutoscalingGroupReplicaConfigurationNicTargetGroupArgs();
        }

        public Builder(AutoscalingGroupReplicaConfigurationNicTargetGroupArgs defaults) {
            $ = new AutoscalingGroupReplicaConfigurationNicTargetGroupArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param port [int] The port of the target group.
         * 
         * @return builder
         * 
         */
        public Builder port(Output<Integer> port) {
            $.port = port;
            return this;
        }

        /**
         * @param port [int] The port of the target group.
         * 
         * @return builder
         * 
         */
        public Builder port(Integer port) {
            return port(Output.of(port));
        }

        /**
         * @param targetGroupId [string] The ID of the target group.
         * 
         * @return builder
         * 
         */
        public Builder targetGroupId(Output<String> targetGroupId) {
            $.targetGroupId = targetGroupId;
            return this;
        }

        /**
         * @param targetGroupId [string] The ID of the target group.
         * 
         * @return builder
         * 
         */
        public Builder targetGroupId(String targetGroupId) {
            return targetGroupId(Output.of(targetGroupId));
        }

        /**
         * @param weight [int] The weight of the target group.
         * 
         * @return builder
         * 
         */
        public Builder weight(Output<Integer> weight) {
            $.weight = weight;
            return this;
        }

        /**
         * @param weight [int] The weight of the target group.
         * 
         * @return builder
         * 
         */
        public Builder weight(Integer weight) {
            return weight(Output.of(weight));
        }

        public AutoscalingGroupReplicaConfigurationNicTargetGroupArgs build() {
            if ($.port == null) {
                throw new MissingRequiredPropertyException("AutoscalingGroupReplicaConfigurationNicTargetGroupArgs", "port");
            }
            if ($.targetGroupId == null) {
                throw new MissingRequiredPropertyException("AutoscalingGroupReplicaConfigurationNicTargetGroupArgs", "targetGroupId");
            }
            if ($.weight == null) {
                throw new MissingRequiredPropertyException("AutoscalingGroupReplicaConfigurationNicTargetGroupArgs", "weight");
            }
            return $;
        }
    }

}
