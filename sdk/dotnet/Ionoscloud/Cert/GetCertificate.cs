// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Cert
{
    public static class GetCertificate
    {
        /// <summary>
        /// The **Certificate data source** can be used to search for and return an existing certificate.
        /// You can provide a string for either id or name parameters which will be compared with provisioned certificates.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cert.GetCertificate.Invoke(new()
        ///     {
        ///         Id = "certificate_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cert.GetCertificate.Invoke(new()
        ///     {
        ///         Name = "Certificate Name Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetCertificateResult> InvokeAsync(GetCertificateArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetCertificateResult>("ionoscloud:cert/getCertificate:getCertificate", args ?? new GetCertificateArgs(), options.WithDefaults());

        /// <summary>
        /// The **Certificate data source** can be used to search for and return an existing certificate.
        /// You can provide a string for either id or name parameters which will be compared with provisioned certificates.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cert.GetCertificate.Invoke(new()
        ///     {
        ///         Id = "certificate_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cert.GetCertificate.Invoke(new()
        ///     {
        ///         Name = "Certificate Name Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetCertificateResult> Invoke(GetCertificateInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetCertificateResult>("ionoscloud:cert/getCertificate:getCertificate", args ?? new GetCertificateInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **Certificate data source** can be used to search for and return an existing certificate.
        /// You can provide a string for either id or name parameters which will be compared with provisioned certificates.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cert.GetCertificate.Invoke(new()
        ///     {
        ///         Id = "certificate_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Cert.GetCertificate.Invoke(new()
        ///     {
        ///         Name = "Certificate Name Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetCertificateResult> Invoke(GetCertificateInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetCertificateResult>("ionoscloud:cert/getCertificate:getCertificate", args ?? new GetCertificateInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCertificateArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Certificate body.
        /// </summary>
        [Input("certificate")]
        public string? Certificate { get; set; }

        /// <summary>
        /// Certificate chain.
        /// </summary>
        [Input("certificateChain")]
        public string? CertificateChain { get; set; }

        /// <summary>
        /// ID of the certificate you want to search for.
        /// 
        /// Either `name` or `id` must be provided, or both. If none are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of an existing certificate that you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetCertificateArgs()
        {
        }
        public static new GetCertificateArgs Empty => new GetCertificateArgs();
    }

    public sealed class GetCertificateInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Certificate body.
        /// </summary>
        [Input("certificate")]
        public Input<string>? Certificate { get; set; }

        /// <summary>
        /// Certificate chain.
        /// </summary>
        [Input("certificateChain")]
        public Input<string>? CertificateChain { get; set; }

        /// <summary>
        /// ID of the certificate you want to search for.
        /// 
        /// Either `name` or `id` must be provided, or both. If none are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of an existing certificate that you want to search for.
        /// </summary>
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
        /// <summary>
        /// Certificate body.
        /// </summary>
        public readonly string Certificate;
        /// <summary>
        /// Certificate chain.
        /// </summary>
        public readonly string CertificateChain;
        /// <summary>
        /// The id of the certificate.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name of the certificate.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private GetCertificateResult(
            string certificate,

            string certificateChain,

            string id,

            string name)
        {
            Certificate = certificate;
            CertificateChain = certificateChain;
            Id = id;
            Name = name;
        }
    }
}
