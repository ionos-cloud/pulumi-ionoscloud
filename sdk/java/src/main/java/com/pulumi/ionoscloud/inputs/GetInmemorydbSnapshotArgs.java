// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class GetInmemorydbSnapshotArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetInmemorydbSnapshotArgs Empty = new GetInmemorydbSnapshotArgs();

    @Import(name="id", required=true)
    private Output<String> id;

    public Output<String> id() {
        return this.id;
    }

    @Import(name="location", required=true)
    private Output<String> location;

    public Output<String> location() {
        return this.location;
    }

    private GetInmemorydbSnapshotArgs() {}

    private GetInmemorydbSnapshotArgs(GetInmemorydbSnapshotArgs $) {
        this.id = $.id;
        this.location = $.location;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetInmemorydbSnapshotArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetInmemorydbSnapshotArgs $;

        public Builder() {
            $ = new GetInmemorydbSnapshotArgs();
        }

        public Builder(GetInmemorydbSnapshotArgs defaults) {
            $ = new GetInmemorydbSnapshotArgs(Objects.requireNonNull(defaults));
        }

        public Builder id(Output<String> id) {
            $.id = id;
            return this;
        }

        public Builder id(String id) {
            return id(Output.of(id));
        }

        public Builder location(Output<String> location) {
            $.location = location;
            return this;
        }

        public Builder location(String location) {
            return location(Output.of(location));
        }

        public GetInmemorydbSnapshotArgs build() {
            if ($.id == null) {
                throw new MissingRequiredPropertyException("GetInmemorydbSnapshotArgs", "id");
            }
            if ($.location == null) {
                throw new MissingRequiredPropertyException("GetInmemorydbSnapshotArgs", "location");
            }
            return $;
        }
    }

}
