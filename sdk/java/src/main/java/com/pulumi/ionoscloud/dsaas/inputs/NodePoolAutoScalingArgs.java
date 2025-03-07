// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.dsaas.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.util.Objects;


public final class NodePoolAutoScalingArgs extends com.pulumi.resources.ResourceArgs {

    public static final NodePoolAutoScalingArgs Empty = new NodePoolAutoScalingArgs();

    /**
     * [int] The maximum number of worker nodes that the node pool can scale to. Should be greater than min_node_count
     * 
     */
    @Import(name="maxNodeCount", required=true)
    private Output<Integer> maxNodeCount;

    /**
     * @return [int] The maximum number of worker nodes that the node pool can scale to. Should be greater than min_node_count
     * 
     */
    public Output<Integer> maxNodeCount() {
        return this.maxNodeCount;
    }

    /**
     * [int] The minimum number of worker nodes the node pool can scale down to. Should be less than max_node_count
     * 
     */
    @Import(name="minNodeCount", required=true)
    private Output<Integer> minNodeCount;

    /**
     * @return [int] The minimum number of worker nodes the node pool can scale down to. Should be less than max_node_count
     * 
     */
    public Output<Integer> minNodeCount() {
        return this.minNodeCount;
    }

    private NodePoolAutoScalingArgs() {}

    private NodePoolAutoScalingArgs(NodePoolAutoScalingArgs $) {
        this.maxNodeCount = $.maxNodeCount;
        this.minNodeCount = $.minNodeCount;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(NodePoolAutoScalingArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private NodePoolAutoScalingArgs $;

        public Builder() {
            $ = new NodePoolAutoScalingArgs();
        }

        public Builder(NodePoolAutoScalingArgs defaults) {
            $ = new NodePoolAutoScalingArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param maxNodeCount [int] The maximum number of worker nodes that the node pool can scale to. Should be greater than min_node_count
         * 
         * @return builder
         * 
         */
        public Builder maxNodeCount(Output<Integer> maxNodeCount) {
            $.maxNodeCount = maxNodeCount;
            return this;
        }

        /**
         * @param maxNodeCount [int] The maximum number of worker nodes that the node pool can scale to. Should be greater than min_node_count
         * 
         * @return builder
         * 
         */
        public Builder maxNodeCount(Integer maxNodeCount) {
            return maxNodeCount(Output.of(maxNodeCount));
        }

        /**
         * @param minNodeCount [int] The minimum number of worker nodes the node pool can scale down to. Should be less than max_node_count
         * 
         * @return builder
         * 
         */
        public Builder minNodeCount(Output<Integer> minNodeCount) {
            $.minNodeCount = minNodeCount;
            return this;
        }

        /**
         * @param minNodeCount [int] The minimum number of worker nodes the node pool can scale down to. Should be less than max_node_count
         * 
         * @return builder
         * 
         */
        public Builder minNodeCount(Integer minNodeCount) {
            return minNodeCount(Output.of(minNodeCount));
        }

        public NodePoolAutoScalingArgs build() {
            if ($.maxNodeCount == null) {
                throw new MissingRequiredPropertyException("NodePoolAutoScalingArgs", "maxNodeCount");
            }
            if ($.minNodeCount == null) {
                throw new MissingRequiredPropertyException("NodePoolAutoScalingArgs", "minNodeCount");
            }
            return $;
        }
    }

}
