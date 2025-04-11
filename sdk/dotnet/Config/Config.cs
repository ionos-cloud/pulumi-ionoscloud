// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Immutable;

namespace Ionoscloud.Pulumi.Ionoscloud
{
    public static class Config
    {
        [global::System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "IDE1006", Justification = 
        "Double underscore prefix used to avoid conflicts with variable names.")]
        private sealed class __Value<T>
        {
            private readonly Func<T> _getter;
            private T _value = default!;
            private bool _set;

            public __Value(Func<T> getter)
            {
                _getter = getter;
            }

            public T Get() => _set ? _value : _getter();

            public void Set(T value)
            {
                _value = value;
                _set = true;
            }
        }

        private static readonly global::Pulumi.Config __config = new global::Pulumi.Config("ionoscloud");

        private static readonly __Value<string?> _contractNumber = new __Value<string?>(() => __config.Get("contractNumber"));
        public static string? ContractNumber
        {
            get => _contractNumber.Get();
            set => _contractNumber.Set(value);
        }

        private static readonly __Value<string?> _endpoint = new __Value<string?>(() => __config.Get("endpoint"));
        /// <summary>
        /// IonosCloud REST API URL. Usually not necessary to be set, SDKs know internally how to route requests to the API.
        /// </summary>
        public static string? Endpoint
        {
            get => _endpoint.Get();
            set => _endpoint.Set(value);
        }

        private static readonly __Value<bool?> _insecure = new __Value<bool?>(() => __config.GetBoolean("insecure"));
        /// <summary>
        /// This field is to be set only for testing purposes. It is not recommended to set this field in production environments.
        /// </summary>
        public static bool? Insecure
        {
            get => _insecure.Get();
            set => _insecure.Set(value);
        }

        private static readonly __Value<string?> _password = new __Value<string?>(() => __config.Get("password"));
        /// <summary>
        /// IonosCloud password for API operations. If token is provided, token is preferred
        /// </summary>
        public static string? Password
        {
            get => _password.Get();
            set => _password.Set(value);
        }

        private static readonly __Value<int?> _retries = new __Value<int?>(() => __config.GetInt32("retries"));
        public static int? Retries
        {
            get => _retries.Get();
            set => _retries.Set(value);
        }

        private static readonly __Value<string?> _s3AccessKey = new __Value<string?>(() => __config.Get("s3AccessKey"));
        /// <summary>
        /// Access key for IONOS Object Storage operations.
        /// </summary>
        public static string? S3AccessKey
        {
            get => _s3AccessKey.Get();
            set => _s3AccessKey.Set(value);
        }

        private static readonly __Value<string?> _s3Region = new __Value<string?>(() => __config.Get("s3Region"));
        /// <summary>
        /// Region for IONOS Object Storage operations.
        /// </summary>
        public static string? S3Region
        {
            get => _s3Region.Get();
            set => _s3Region.Set(value);
        }

        private static readonly __Value<string?> _s3SecretKey = new __Value<string?>(() => __config.Get("s3SecretKey"));
        /// <summary>
        /// Secret key for IONOS Object Storage operations.
        /// </summary>
        public static string? S3SecretKey
        {
            get => _s3SecretKey.Get();
            set => _s3SecretKey.Set(value);
        }

        private static readonly __Value<string?> _token = new __Value<string?>(() => __config.Get("token"));
        /// <summary>
        /// IonosCloud bearer token for API operations.
        /// </summary>
        public static string? Token
        {
            get => _token.Get();
            set => _token.Set(value);
        }

        private static readonly __Value<string?> _username = new __Value<string?>(() => __config.Get("username"));
        /// <summary>
        /// IonosCloud username for API operations. If token is provided, token is preferred
        /// </summary>
        public static string? Username
        {
            get => _username.Get();
            set => _username.Set(value);
        }

    }
}
