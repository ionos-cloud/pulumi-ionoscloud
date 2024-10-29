// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Double;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetTemplateArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetTemplateArgs Empty = new GetTemplateArgs();

    /**
     * The CPU cores count.
     * 
     */
    @Import(name="cores")
    private @Nullable Output<Double> cores;

    /**
     * @return The CPU cores count.
     * 
     */
    public Optional<Output<Double>> cores() {
        return Optional.ofNullable(this.cores);
    }

    /**
     * A name of that resource.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return A name of that resource.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The RAM size in MB.
     * 
     */
    @Import(name="ram")
    private @Nullable Output<Double> ram;

    /**
     * @return The RAM size in MB.
     * 
     */
    public Optional<Output<Double>> ram() {
        return Optional.ofNullable(this.ram);
    }

    /**
     * The storage size in GB.
     * 
     * Any of the arguments ca be provided. If none, the datasource will return an error.
     * 
     */
    @Import(name="storageSize")
    private @Nullable Output<Double> storageSize;

    /**
     * @return The storage size in GB.
     * 
     * Any of the arguments ca be provided. If none, the datasource will return an error.
     * 
     */
    public Optional<Output<Double>> storageSize() {
        return Optional.ofNullable(this.storageSize);
    }

    private GetTemplateArgs() {}

    private GetTemplateArgs(GetTemplateArgs $) {
        this.cores = $.cores;
        this.name = $.name;
        this.ram = $.ram;
        this.storageSize = $.storageSize;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetTemplateArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetTemplateArgs $;

        public Builder() {
            $ = new GetTemplateArgs();
        }

        public Builder(GetTemplateArgs defaults) {
            $ = new GetTemplateArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param cores The CPU cores count.
         * 
         * @return builder
         * 
         */
        public Builder cores(@Nullable Output<Double> cores) {
            $.cores = cores;
            return this;
        }

        /**
         * @param cores The CPU cores count.
         * 
         * @return builder
         * 
         */
        public Builder cores(Double cores) {
            return cores(Output.of(cores));
        }

        /**
         * @param name A name of that resource.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name A name of that resource.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param ram The RAM size in MB.
         * 
         * @return builder
         * 
         */
        public Builder ram(@Nullable Output<Double> ram) {
            $.ram = ram;
            return this;
        }

        /**
         * @param ram The RAM size in MB.
         * 
         * @return builder
         * 
         */
        public Builder ram(Double ram) {
            return ram(Output.of(ram));
        }

        /**
         * @param storageSize The storage size in GB.
         * 
         * Any of the arguments ca be provided. If none, the datasource will return an error.
         * 
         * @return builder
         * 
         */
        public Builder storageSize(@Nullable Output<Double> storageSize) {
            $.storageSize = storageSize;
            return this;
        }

        /**
         * @param storageSize The storage size in GB.
         * 
         * Any of the arguments ca be provided. If none, the datasource will return an error.
         * 
         * @return builder
         * 
         */
        public Builder storageSize(Double storageSize) {
            return storageSize(Output.of(storageSize));
        }

        public GetTemplateArgs build() {
            return $;
        }
    }

}
