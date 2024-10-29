// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class TargetGroupHttpHealthCheckArgs extends com.pulumi.resources.ResourceArgs {

    public static final TargetGroupHttpHealthCheckArgs Empty = new TargetGroupHttpHealthCheckArgs();

    /**
     * [string]
     * 
     */
    @Import(name="matchType", required=true)
    private Output<String> matchType;

    /**
     * @return [string]
     * 
     */
    public Output<String> matchType() {
        return this.matchType;
    }

    /**
     * [string] The method for the HTTP health check.
     * 
     */
    @Import(name="method")
    private @Nullable Output<String> method;

    /**
     * @return [string] The method for the HTTP health check.
     * 
     */
    public Optional<Output<String>> method() {
        return Optional.ofNullable(this.method);
    }

    /**
     * [bool]
     * 
     */
    @Import(name="negate")
    private @Nullable Output<Boolean> negate;

    /**
     * @return [bool]
     * 
     */
    public Optional<Output<Boolean>> negate() {
        return Optional.ofNullable(this.negate);
    }

    /**
     * [string] The path (destination URL) for the HTTP health check request; the default is /.
     * 
     */
    @Import(name="path")
    private @Nullable Output<String> path;

    /**
     * @return [string] The path (destination URL) for the HTTP health check request; the default is /.
     * 
     */
    public Optional<Output<String>> path() {
        return Optional.ofNullable(this.path);
    }

    /**
     * [bool]
     * 
     */
    @Import(name="regex")
    private @Nullable Output<Boolean> regex;

    /**
     * @return [bool]
     * 
     */
    public Optional<Output<Boolean>> regex() {
        return Optional.ofNullable(this.regex);
    }

    /**
     * [string] The response returned by the request, depending on the match type.
     * 
     */
    @Import(name="response", required=true)
    private Output<String> response;

    /**
     * @return [string] The response returned by the request, depending on the match type.
     * 
     */
    public Output<String> response() {
        return this.response;
    }

    private TargetGroupHttpHealthCheckArgs() {}

    private TargetGroupHttpHealthCheckArgs(TargetGroupHttpHealthCheckArgs $) {
        this.matchType = $.matchType;
        this.method = $.method;
        this.negate = $.negate;
        this.path = $.path;
        this.regex = $.regex;
        this.response = $.response;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(TargetGroupHttpHealthCheckArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private TargetGroupHttpHealthCheckArgs $;

        public Builder() {
            $ = new TargetGroupHttpHealthCheckArgs();
        }

        public Builder(TargetGroupHttpHealthCheckArgs defaults) {
            $ = new TargetGroupHttpHealthCheckArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param matchType [string]
         * 
         * @return builder
         * 
         */
        public Builder matchType(Output<String> matchType) {
            $.matchType = matchType;
            return this;
        }

        /**
         * @param matchType [string]
         * 
         * @return builder
         * 
         */
        public Builder matchType(String matchType) {
            return matchType(Output.of(matchType));
        }

        /**
         * @param method [string] The method for the HTTP health check.
         * 
         * @return builder
         * 
         */
        public Builder method(@Nullable Output<String> method) {
            $.method = method;
            return this;
        }

        /**
         * @param method [string] The method for the HTTP health check.
         * 
         * @return builder
         * 
         */
        public Builder method(String method) {
            return method(Output.of(method));
        }

        /**
         * @param negate [bool]
         * 
         * @return builder
         * 
         */
        public Builder negate(@Nullable Output<Boolean> negate) {
            $.negate = negate;
            return this;
        }

        /**
         * @param negate [bool]
         * 
         * @return builder
         * 
         */
        public Builder negate(Boolean negate) {
            return negate(Output.of(negate));
        }

        /**
         * @param path [string] The path (destination URL) for the HTTP health check request; the default is /.
         * 
         * @return builder
         * 
         */
        public Builder path(@Nullable Output<String> path) {
            $.path = path;
            return this;
        }

        /**
         * @param path [string] The path (destination URL) for the HTTP health check request; the default is /.
         * 
         * @return builder
         * 
         */
        public Builder path(String path) {
            return path(Output.of(path));
        }

        /**
         * @param regex [bool]
         * 
         * @return builder
         * 
         */
        public Builder regex(@Nullable Output<Boolean> regex) {
            $.regex = regex;
            return this;
        }

        /**
         * @param regex [bool]
         * 
         * @return builder
         * 
         */
        public Builder regex(Boolean regex) {
            return regex(Output.of(regex));
        }

        /**
         * @param response [string] The response returned by the request, depending on the match type.
         * 
         * @return builder
         * 
         */
        public Builder response(Output<String> response) {
            $.response = response;
            return this;
        }

        /**
         * @param response [string] The response returned by the request, depending on the match type.
         * 
         * @return builder
         * 
         */
        public Builder response(String response) {
            return response(Output.of(response));
        }

        public TargetGroupHttpHealthCheckArgs build() {
            if ($.matchType == null) {
                throw new MissingRequiredPropertyException("TargetGroupHttpHealthCheckArgs", "matchType");
            }
            if ($.response == null) {
                throw new MissingRequiredPropertyException("TargetGroupHttpHealthCheckArgs", "response");
            }
            return $;
        }
    }

}
