// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dbaas.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class GetInmemorydbSnapshotPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetInmemorydbSnapshotPlainArgs Empty = new GetInmemorydbSnapshotPlainArgs();

    /**
     * The ID of the InMemoryDB Snapshot.
     * 
     */
    @Import(name="id", required=true)
    private String id;

    /**
     * @return The ID of the InMemoryDB Snapshot.
     * 
     */
    public String id() {
        return this.id;
    }

    /**
     * The location of the InMemoryDB Snapshot.
     * 
     */
    @Import(name="location", required=true)
    private String location;

    /**
     * @return The location of the InMemoryDB Snapshot.
     * 
     */
    public String location() {
        return this.location;
    }

    private GetInmemorydbSnapshotPlainArgs() {}

    private GetInmemorydbSnapshotPlainArgs(GetInmemorydbSnapshotPlainArgs $) {
        this.id = $.id;
        this.location = $.location;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetInmemorydbSnapshotPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetInmemorydbSnapshotPlainArgs $;

        public Builder() {
            $ = new GetInmemorydbSnapshotPlainArgs();
        }

        public Builder(GetInmemorydbSnapshotPlainArgs defaults) {
            $ = new GetInmemorydbSnapshotPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id The ID of the InMemoryDB Snapshot.
         * 
         * @return builder
         * 
         */
        public Builder id(String id) {
            $.id = id;
            return this;
        }

        /**
         * @param location The location of the InMemoryDB Snapshot.
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            $.location = location;
            return this;
        }

        public GetInmemorydbSnapshotPlainArgs build() {
            if ($.id == null) {
                throw new MissingRequiredPropertyException("GetInmemorydbSnapshotPlainArgs", "id");
            }
            if ($.location == null) {
                throw new MissingRequiredPropertyException("GetInmemorydbSnapshotPlainArgs", "location");
            }
            return $;
        }
    }

}
