// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetCertificate
    {
        public static Task<GetCertificateResult> InvokeAsync(GetCertificateArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetCertificateResult>("ionoscloud:index/getCertificate:getCertificate", args ?? new GetCertificateArgs(), options.WithDefaults());

        public static Output<GetCertificateResult> Invoke(GetCertificateInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetCertificateResult>("ionoscloud:index/getCertificate:getCertificate", args ?? new GetCertificateInvokeArgs(), options.WithDefaults());

        public static Output<GetCertificateResult> Invoke(GetCertificateInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetCertificateResult>("ionoscloud:index/getCertificate:getCertificate", args ?? new GetCertificateInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCertificateArgs : global::Pulumi.InvokeArgs
    {
        [Input("certificate")]
        public string? Certificate { get; set; }

        [Input("certificateChain")]
        public string? CertificateChain { get; set; }

        [Input("id")]
        public string? Id { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        public GetCertificateArgs()
        {
        }
        public static new GetCertificateArgs Empty => new GetCertificateArgs();
    }

    public sealed class GetCertificateInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("certificate")]
        public Input<string>? Certificate { get; set; }

        [Input("certificateChain")]
        public Input<string>? CertificateChain { get; set; }

        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetCertificateInvokeArgs()
        {
        }
        public static new GetCertificateInvokeArgs Empty => new GetCertificateInvokeArgs();
    }


    [OutputType]
    public sealed class GetCertificateResult
    {
        public readonly string Certificate;
        public readonly string CertificateChain;
        public readonly string? Id;
        public readonly string? Name;

        [OutputConstructor]
        private GetCertificateResult(
            string certificate,

            string certificateChain,

            string? id,

            string? name)
        {
            Certificate = certificate;
            CertificateChain = certificateChain;
            Id = id;
            Name = name;
        }
    }
}
