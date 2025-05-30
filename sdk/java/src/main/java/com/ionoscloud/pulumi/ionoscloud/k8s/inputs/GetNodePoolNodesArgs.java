// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.k8s.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class GetNodePoolNodesArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetNodePoolNodesArgs Empty = new GetNodePoolNodesArgs();

    /**
     * K8s Cluster&#39; UUID
     * 
     */
    @Import(name="k8sClusterId", required=true)
    private Output<String> k8sClusterId;

    /**
     * @return K8s Cluster&#39; UUID
     * 
     */
    public Output<String> k8sClusterId() {
        return this.k8sClusterId;
    }

    @Import(name="nodePoolId", required=true)
    private Output<String> nodePoolId;

    public Output<String> nodePoolId() {
        return this.nodePoolId;
    }

    private GetNodePoolNodesArgs() {}

    private GetNodePoolNodesArgs(GetNodePoolNodesArgs $) {
        this.k8sClusterId = $.k8sClusterId;
        this.nodePoolId = $.nodePoolId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetNodePoolNodesArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetNodePoolNodesArgs $;

        public Builder() {
            $ = new GetNodePoolNodesArgs();
        }

        public Builder(GetNodePoolNodesArgs defaults) {
            $ = new GetNodePoolNodesArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param k8sClusterId K8s Cluster&#39; UUID
         * 
         * @return builder
         * 
         */
        public Builder k8sClusterId(Output<String> k8sClusterId) {
            $.k8sClusterId = k8sClusterId;
            return this;
        }

        /**
         * @param k8sClusterId K8s Cluster&#39; UUID
         * 
         * @return builder
         * 
         */
        public Builder k8sClusterId(String k8sClusterId) {
            return k8sClusterId(Output.of(k8sClusterId));
        }

        public Builder nodePoolId(Output<String> nodePoolId) {
            $.nodePoolId = nodePoolId;
            return this;
        }

        public Builder nodePoolId(String nodePoolId) {
            return nodePoolId(Output.of(nodePoolId));
        }

        public GetNodePoolNodesArgs build() {
            if ($.k8sClusterId == null) {
                throw new MissingRequiredPropertyException("GetNodePoolNodesArgs", "k8sClusterId");
            }
            if ($.nodePoolId == null) {
                throw new MissingRequiredPropertyException("GetNodePoolNodesArgs", "nodePoolId");
            }
            return $;
        }
    }

}
