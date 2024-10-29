// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.inputs.K8sNodePoolAutoScalingArgs;
import com.pulumi.ionoscloud.inputs.K8sNodePoolLanArgs;
import com.pulumi.ionoscloud.inputs.K8sNodePoolMaintenanceWindowArgs;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class K8sNodePoolArgs extends com.pulumi.resources.ResourceArgs {

    public static final K8sNodePoolArgs Empty = new K8sNodePoolArgs();

    /**
     * When set to true, allows the update of immutable fields by destroying and re-creating the node pool
     * 
     */
    @Import(name="allowReplace")
    private @Nullable Output<Boolean> allowReplace;

    /**
     * @return When set to true, allows the update of immutable fields by destroying and re-creating the node pool
     * 
     */
    public Optional<Output<Boolean>> allowReplace() {
        return Optional.ofNullable(this.allowReplace);
    }

    /**
     * [map] A key/value map of annotations
     * 
     */
    @Import(name="annotations")
    private @Nullable Output<Map<String,String>> annotations;

    /**
     * @return [map] A key/value map of annotations
     * 
     */
    public Optional<Output<Map<String,String>>> annotations() {
        return Optional.ofNullable(this.annotations);
    }

    /**
     * [string] Wether the Node Pool should autoscale. For more details, please check the API documentation
     * 
     */
    @Import(name="autoScaling")
    private @Nullable Output<K8sNodePoolAutoScalingArgs> autoScaling;

    /**
     * @return [string] Wether the Node Pool should autoscale. For more details, please check the API documentation
     * 
     */
    public Optional<Output<K8sNodePoolAutoScalingArgs>> autoScaling() {
        return Optional.ofNullable(this.autoScaling);
    }

    /**
     * [string] - The desired Compute availability zone - See the API documentation for more information. *This attribute is immutable*.
     * 
     */
    @Import(name="availabilityZone", required=true)
    private Output<String> availabilityZone;

    /**
     * @return [string] - The desired Compute availability zone - See the API documentation for more information. *This attribute is immutable*.
     * 
     */
    public Output<String> availabilityZone() {
        return this.availabilityZone;
    }

    /**
     * [int] - The CPU cores count for each node of the node pool. *This attribute is immutable*.
     * 
     */
    @Import(name="coresCount", required=true)
    private Output<Integer> coresCount;

    /**
     * @return [int] - The CPU cores count for each node of the node pool. *This attribute is immutable*.
     * 
     */
    public Output<Integer> coresCount() {
        return this.coresCount;
    }

    /**
     * [string] The desired CPU Family - See the API documentation for more information. *This attribute is immutable*.
     * 
     */
    @Import(name="cpuFamily", required=true)
    private Output<String> cpuFamily;

    /**
     * @return [string] The desired CPU Family - See the API documentation for more information. *This attribute is immutable*.
     * 
     */
    public Output<String> cpuFamily() {
        return this.cpuFamily;
    }

    /**
     * [string] A Datacenter&#39;s UUID
     * 
     */
    @Import(name="datacenterId", required=true)
    private Output<String> datacenterId;

    /**
     * @return [string] A Datacenter&#39;s UUID
     * 
     */
    public Output<String> datacenterId() {
        return this.datacenterId;
    }

    /**
     * [string] A k8s cluster&#39;s UUID
     * 
     */
    @Import(name="k8sClusterId", required=true)
    private Output<String> k8sClusterId;

    /**
     * @return [string] A k8s cluster&#39;s UUID
     * 
     */
    public Output<String> k8sClusterId() {
        return this.k8sClusterId;
    }

    /**
     * [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
     * 
     */
    @Import(name="k8sVersion", required=true)
    private Output<String> k8sVersion;

    /**
     * @return [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
     * 
     */
    public Output<String> k8sVersion() {
        return this.k8sVersion;
    }

    /**
     * [map] A key/value map of labels
     * 
     */
    @Import(name="labels")
    private @Nullable Output<Map<String,String>> labels;

    /**
     * @return [map] A key/value map of labels
     * 
     */
    public Optional<Output<Map<String,String>>> labels() {
        return Optional.ofNullable(this.labels);
    }

    /**
     * [list] A list of numeric LAN id&#39;s you want this node pool to be part of. For more details, please check the API documentation, as well as the example above
     * 
     */
    @Import(name="lans")
    private @Nullable Output<List<K8sNodePoolLanArgs>> lans;

    /**
     * @return [list] A list of numeric LAN id&#39;s you want this node pool to be part of. For more details, please check the API documentation, as well as the example above
     * 
     */
    public Optional<Output<List<K8sNodePoolLanArgs>>> lans() {
        return Optional.ofNullable(this.lans);
    }

    /**
     * See the **maintenance_window** section in the example above
     * 
     */
    @Import(name="maintenanceWindow")
    private @Nullable Output<K8sNodePoolMaintenanceWindowArgs> maintenanceWindow;

    /**
     * @return See the **maintenance_window** section in the example above
     * 
     */
    public Optional<Output<K8sNodePoolMaintenanceWindowArgs>> maintenanceWindow() {
        return Optional.ofNullable(this.maintenanceWindow);
    }

    /**
     * [string] The name of the Kubernetes Cluster. *This attribute is immutable*.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] The name of the Kubernetes Cluster. *This attribute is immutable*.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [int] - The desired number of nodes in the node pool
     * 
     */
    @Import(name="nodeCount", required=true)
    private Output<Integer> nodeCount;

    /**
     * @return [int] - The desired number of nodes in the node pool
     * 
     */
    public Output<Integer> nodeCount() {
        return this.nodeCount;
    }

    /**
     * [list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements
     * 
     */
    @Import(name="publicIps")
    private @Nullable Output<List<String>> publicIps;

    /**
     * @return [list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements
     * 
     */
    public Optional<Output<List<String>>> publicIps() {
        return Optional.ofNullable(this.publicIps);
    }

    /**
     * [int] - The desired amount of RAM, in MB. *This attribute is immutable*.
     * 
     */
    @Import(name="ramSize", required=true)
    private Output<Integer> ramSize;

    /**
     * @return [int] - The desired amount of RAM, in MB. *This attribute is immutable*.
     * 
     */
    public Output<Integer> ramSize() {
        return this.ramSize;
    }

    /**
     * [int] - The size of the volume in GB. The size should be greater than 10GB. *This attribute is immutable*.
     * 
     */
    @Import(name="storageSize", required=true)
    private Output<Integer> storageSize;

    /**
     * @return [int] - The size of the volume in GB. The size should be greater than 10GB. *This attribute is immutable*.
     * 
     */
    public Output<Integer> storageSize() {
        return this.storageSize;
    }

    /**
     * [string] - The desired storage type - SSD/HDD. *This attribute is immutable*.
     * 
     */
    @Import(name="storageType", required=true)
    private Output<String> storageType;

    /**
     * @return [string] - The desired storage type - SSD/HDD. *This attribute is immutable*.
     * 
     */
    public Output<String> storageType() {
        return this.storageType;
    }

    private K8sNodePoolArgs() {}

    private K8sNodePoolArgs(K8sNodePoolArgs $) {
        this.allowReplace = $.allowReplace;
        this.annotations = $.annotations;
        this.autoScaling = $.autoScaling;
        this.availabilityZone = $.availabilityZone;
        this.coresCount = $.coresCount;
        this.cpuFamily = $.cpuFamily;
        this.datacenterId = $.datacenterId;
        this.k8sClusterId = $.k8sClusterId;
        this.k8sVersion = $.k8sVersion;
        this.labels = $.labels;
        this.lans = $.lans;
        this.maintenanceWindow = $.maintenanceWindow;
        this.name = $.name;
        this.nodeCount = $.nodeCount;
        this.publicIps = $.publicIps;
        this.ramSize = $.ramSize;
        this.storageSize = $.storageSize;
        this.storageType = $.storageType;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(K8sNodePoolArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private K8sNodePoolArgs $;

        public Builder() {
            $ = new K8sNodePoolArgs();
        }

        public Builder(K8sNodePoolArgs defaults) {
            $ = new K8sNodePoolArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param allowReplace When set to true, allows the update of immutable fields by destroying and re-creating the node pool
         * 
         * @return builder
         * 
         */
        public Builder allowReplace(@Nullable Output<Boolean> allowReplace) {
            $.allowReplace = allowReplace;
            return this;
        }

        /**
         * @param allowReplace When set to true, allows the update of immutable fields by destroying and re-creating the node pool
         * 
         * @return builder
         * 
         */
        public Builder allowReplace(Boolean allowReplace) {
            return allowReplace(Output.of(allowReplace));
        }

        /**
         * @param annotations [map] A key/value map of annotations
         * 
         * @return builder
         * 
         */
        public Builder annotations(@Nullable Output<Map<String,String>> annotations) {
            $.annotations = annotations;
            return this;
        }

        /**
         * @param annotations [map] A key/value map of annotations
         * 
         * @return builder
         * 
         */
        public Builder annotations(Map<String,String> annotations) {
            return annotations(Output.of(annotations));
        }

        /**
         * @param autoScaling [string] Wether the Node Pool should autoscale. For more details, please check the API documentation
         * 
         * @return builder
         * 
         */
        public Builder autoScaling(@Nullable Output<K8sNodePoolAutoScalingArgs> autoScaling) {
            $.autoScaling = autoScaling;
            return this;
        }

        /**
         * @param autoScaling [string] Wether the Node Pool should autoscale. For more details, please check the API documentation
         * 
         * @return builder
         * 
         */
        public Builder autoScaling(K8sNodePoolAutoScalingArgs autoScaling) {
            return autoScaling(Output.of(autoScaling));
        }

        /**
         * @param availabilityZone [string] - The desired Compute availability zone - See the API documentation for more information. *This attribute is immutable*.
         * 
         * @return builder
         * 
         */
        public Builder availabilityZone(Output<String> availabilityZone) {
            $.availabilityZone = availabilityZone;
            return this;
        }

        /**
         * @param availabilityZone [string] - The desired Compute availability zone - See the API documentation for more information. *This attribute is immutable*.
         * 
         * @return builder
         * 
         */
        public Builder availabilityZone(String availabilityZone) {
            return availabilityZone(Output.of(availabilityZone));
        }

        /**
         * @param coresCount [int] - The CPU cores count for each node of the node pool. *This attribute is immutable*.
         * 
         * @return builder
         * 
         */
        public Builder coresCount(Output<Integer> coresCount) {
            $.coresCount = coresCount;
            return this;
        }

        /**
         * @param coresCount [int] - The CPU cores count for each node of the node pool. *This attribute is immutable*.
         * 
         * @return builder
         * 
         */
        public Builder coresCount(Integer coresCount) {
            return coresCount(Output.of(coresCount));
        }

        /**
         * @param cpuFamily [string] The desired CPU Family - See the API documentation for more information. *This attribute is immutable*.
         * 
         * @return builder
         * 
         */
        public Builder cpuFamily(Output<String> cpuFamily) {
            $.cpuFamily = cpuFamily;
            return this;
        }

        /**
         * @param cpuFamily [string] The desired CPU Family - See the API documentation for more information. *This attribute is immutable*.
         * 
         * @return builder
         * 
         */
        public Builder cpuFamily(String cpuFamily) {
            return cpuFamily(Output.of(cpuFamily));
        }

        /**
         * @param datacenterId [string] A Datacenter&#39;s UUID
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(Output<String> datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        /**
         * @param datacenterId [string] A Datacenter&#39;s UUID
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(String datacenterId) {
            return datacenterId(Output.of(datacenterId));
        }

        /**
         * @param k8sClusterId [string] A k8s cluster&#39;s UUID
         * 
         * @return builder
         * 
         */
        public Builder k8sClusterId(Output<String> k8sClusterId) {
            $.k8sClusterId = k8sClusterId;
            return this;
        }

        /**
         * @param k8sClusterId [string] A k8s cluster&#39;s UUID
         * 
         * @return builder
         * 
         */
        public Builder k8sClusterId(String k8sClusterId) {
            return k8sClusterId(Output.of(k8sClusterId));
        }

        /**
         * @param k8sVersion [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
         * 
         * @return builder
         * 
         */
        public Builder k8sVersion(Output<String> k8sVersion) {
            $.k8sVersion = k8sVersion;
            return this;
        }

        /**
         * @param k8sVersion [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
         * 
         * @return builder
         * 
         */
        public Builder k8sVersion(String k8sVersion) {
            return k8sVersion(Output.of(k8sVersion));
        }

        /**
         * @param labels [map] A key/value map of labels
         * 
         * @return builder
         * 
         */
        public Builder labels(@Nullable Output<Map<String,String>> labels) {
            $.labels = labels;
            return this;
        }

        /**
         * @param labels [map] A key/value map of labels
         * 
         * @return builder
         * 
         */
        public Builder labels(Map<String,String> labels) {
            return labels(Output.of(labels));
        }

        /**
         * @param lans [list] A list of numeric LAN id&#39;s you want this node pool to be part of. For more details, please check the API documentation, as well as the example above
         * 
         * @return builder
         * 
         */
        public Builder lans(@Nullable Output<List<K8sNodePoolLanArgs>> lans) {
            $.lans = lans;
            return this;
        }

        /**
         * @param lans [list] A list of numeric LAN id&#39;s you want this node pool to be part of. For more details, please check the API documentation, as well as the example above
         * 
         * @return builder
         * 
         */
        public Builder lans(List<K8sNodePoolLanArgs> lans) {
            return lans(Output.of(lans));
        }

        /**
         * @param lans [list] A list of numeric LAN id&#39;s you want this node pool to be part of. For more details, please check the API documentation, as well as the example above
         * 
         * @return builder
         * 
         */
        public Builder lans(K8sNodePoolLanArgs... lans) {
            return lans(List.of(lans));
        }

        /**
         * @param maintenanceWindow See the **maintenance_window** section in the example above
         * 
         * @return builder
         * 
         */
        public Builder maintenanceWindow(@Nullable Output<K8sNodePoolMaintenanceWindowArgs> maintenanceWindow) {
            $.maintenanceWindow = maintenanceWindow;
            return this;
        }

        /**
         * @param maintenanceWindow See the **maintenance_window** section in the example above
         * 
         * @return builder
         * 
         */
        public Builder maintenanceWindow(K8sNodePoolMaintenanceWindowArgs maintenanceWindow) {
            return maintenanceWindow(Output.of(maintenanceWindow));
        }

        /**
         * @param name [string] The name of the Kubernetes Cluster. *This attribute is immutable*.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] The name of the Kubernetes Cluster. *This attribute is immutable*.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param nodeCount [int] - The desired number of nodes in the node pool
         * 
         * @return builder
         * 
         */
        public Builder nodeCount(Output<Integer> nodeCount) {
            $.nodeCount = nodeCount;
            return this;
        }

        /**
         * @param nodeCount [int] - The desired number of nodes in the node pool
         * 
         * @return builder
         * 
         */
        public Builder nodeCount(Integer nodeCount) {
            return nodeCount(Output.of(nodeCount));
        }

        /**
         * @param publicIps [list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements
         * 
         * @return builder
         * 
         */
        public Builder publicIps(@Nullable Output<List<String>> publicIps) {
            $.publicIps = publicIps;
            return this;
        }

        /**
         * @param publicIps [list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements
         * 
         * @return builder
         * 
         */
        public Builder publicIps(List<String> publicIps) {
            return publicIps(Output.of(publicIps));
        }

        /**
         * @param publicIps [list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements
         * 
         * @return builder
         * 
         */
        public Builder publicIps(String... publicIps) {
            return publicIps(List.of(publicIps));
        }

        /**
         * @param ramSize [int] - The desired amount of RAM, in MB. *This attribute is immutable*.
         * 
         * @return builder
         * 
         */
        public Builder ramSize(Output<Integer> ramSize) {
            $.ramSize = ramSize;
            return this;
        }

        /**
         * @param ramSize [int] - The desired amount of RAM, in MB. *This attribute is immutable*.
         * 
         * @return builder
         * 
         */
        public Builder ramSize(Integer ramSize) {
            return ramSize(Output.of(ramSize));
        }

        /**
         * @param storageSize [int] - The size of the volume in GB. The size should be greater than 10GB. *This attribute is immutable*.
         * 
         * @return builder
         * 
         */
        public Builder storageSize(Output<Integer> storageSize) {
            $.storageSize = storageSize;
            return this;
        }

        /**
         * @param storageSize [int] - The size of the volume in GB. The size should be greater than 10GB. *This attribute is immutable*.
         * 
         * @return builder
         * 
         */
        public Builder storageSize(Integer storageSize) {
            return storageSize(Output.of(storageSize));
        }

        /**
         * @param storageType [string] - The desired storage type - SSD/HDD. *This attribute is immutable*.
         * 
         * @return builder
         * 
         */
        public Builder storageType(Output<String> storageType) {
            $.storageType = storageType;
            return this;
        }

        /**
         * @param storageType [string] - The desired storage type - SSD/HDD. *This attribute is immutable*.
         * 
         * @return builder
         * 
         */
        public Builder storageType(String storageType) {
            return storageType(Output.of(storageType));
        }

        public K8sNodePoolArgs build() {
            if ($.availabilityZone == null) {
                throw new MissingRequiredPropertyException("K8sNodePoolArgs", "availabilityZone");
            }
            if ($.coresCount == null) {
                throw new MissingRequiredPropertyException("K8sNodePoolArgs", "coresCount");
            }
            if ($.cpuFamily == null) {
                throw new MissingRequiredPropertyException("K8sNodePoolArgs", "cpuFamily");
            }
            if ($.datacenterId == null) {
                throw new MissingRequiredPropertyException("K8sNodePoolArgs", "datacenterId");
            }
            if ($.k8sClusterId == null) {
                throw new MissingRequiredPropertyException("K8sNodePoolArgs", "k8sClusterId");
            }
            if ($.k8sVersion == null) {
                throw new MissingRequiredPropertyException("K8sNodePoolArgs", "k8sVersion");
            }
            if ($.nodeCount == null) {
                throw new MissingRequiredPropertyException("K8sNodePoolArgs", "nodeCount");
            }
            if ($.ramSize == null) {
                throw new MissingRequiredPropertyException("K8sNodePoolArgs", "ramSize");
            }
            if ($.storageSize == null) {
                throw new MissingRequiredPropertyException("K8sNodePoolArgs", "storageSize");
            }
            if ($.storageType == null) {
                throw new MissingRequiredPropertyException("K8sNodePoolArgs", "storageType");
            }
            return $;
        }
    }

}
