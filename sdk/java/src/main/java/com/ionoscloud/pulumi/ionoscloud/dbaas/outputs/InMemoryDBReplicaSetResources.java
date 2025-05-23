// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dbaas.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class InMemoryDBReplicaSetResources {
    /**
     * @return [int] The number of CPU cores per instance.
     * 
     */
    private Integer cores;
    /**
     * @return [int] The amount of memory per instance in gigabytes (GB).
     * 
     */
    private Integer ram;
    /**
     * @return [int] The size of the storage in GB. The size is derived from the amount of RAM and the persistence mode and is not configurable.
     * 
     */
    private @Nullable Integer storage;

    private InMemoryDBReplicaSetResources() {}
    /**
     * @return [int] The number of CPU cores per instance.
     * 
     */
    public Integer cores() {
        return this.cores;
    }
    /**
     * @return [int] The amount of memory per instance in gigabytes (GB).
     * 
     */
    public Integer ram() {
        return this.ram;
    }
    /**
     * @return [int] The size of the storage in GB. The size is derived from the amount of RAM and the persistence mode and is not configurable.
     * 
     */
    public Optional<Integer> storage() {
        return Optional.ofNullable(this.storage);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(InMemoryDBReplicaSetResources defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Integer cores;
        private Integer ram;
        private @Nullable Integer storage;
        public Builder() {}
        public Builder(InMemoryDBReplicaSetResources defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.cores = defaults.cores;
    	      this.ram = defaults.ram;
    	      this.storage = defaults.storage;
        }

        @CustomType.Setter
        public Builder cores(Integer cores) {
            if (cores == null) {
              throw new MissingRequiredPropertyException("InMemoryDBReplicaSetResources", "cores");
            }
            this.cores = cores;
            return this;
        }
        @CustomType.Setter
        public Builder ram(Integer ram) {
            if (ram == null) {
              throw new MissingRequiredPropertyException("InMemoryDBReplicaSetResources", "ram");
            }
            this.ram = ram;
            return this;
        }
        @CustomType.Setter
        public Builder storage(@Nullable Integer storage) {

            this.storage = storage;
            return this;
        }
        public InMemoryDBReplicaSetResources build() {
            final var _resultValue = new InMemoryDBReplicaSetResources();
            _resultValue.cores = cores;
            _resultValue.ram = ram;
            _resultValue.storage = storage;
            return _resultValue;
        }
    }
}
