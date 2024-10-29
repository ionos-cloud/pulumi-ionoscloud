// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetDatacenter
    {
        /// <summary>
        /// The **Datacenter data source** can be used to search for and return an existing Virtual Data Center.
        /// You can provide a string for the name and location parameters which will be compared with provisioned Virtual Data Centers.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Name &amp; Location
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```typescript
        /// import * as pulumi from "@pulumi/pulumi";
        /// import * as ionoscloud from "@pulumi/ionoscloud";
        /// 
        /// const example = ionoscloud.getDatacenter({
        ///     location: "us/las",
        ///     name: "Datacenter Example",
        /// });
        /// ```
        /// ```python
        /// import pulumi
        /// import pulumi_ionoscloud as ionoscloud
        /// 
        /// example = ionoscloud.get_datacenter(location="us/las",
        ///     name="Datacenter Example")
        /// ```
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.GetDatacenter.Invoke(new()
        ///     {
        ///         Location = "us/las",
        ///         Name = "Datacenter Example",
        ///     });
        /// 
        /// });
        /// ```
        /// ```go
        /// package main
        /// 
        /// import (
        /// 	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud"
        /// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
        /// )
        /// 
        /// func main() {
        /// 	pulumi.Run(func(ctx *pulumi.Context) error {
        /// 		_, err := ionoscloud.LookupDatacenter(ctx, &amp;ionoscloud.LookupDatacenterArgs{
        /// 			Location: pulumi.StringRef("us/las"),
        /// 			Name:     pulumi.StringRef("Datacenter Example"),
        /// 		}, nil)
        /// 		if err != nil {
        /// 			return err
        /// 		}
        /// 		return nil
        /// 	})
        /// }
        /// ```
        /// ```java
        /// package generated_program;
        /// 
        /// import com.pulumi.Context;
        /// import com.pulumi.Pulumi;
        /// import com.pulumi.core.Output;
        /// import com.pulumi.ionoscloud.IonoscloudFunctions;
        /// import com.pulumi.ionoscloud.inputs.GetDatacenterArgs;
        /// import java.util.List;
        /// import java.util.ArrayList;
        /// import java.util.Map;
        /// import java.io.File;
        /// import java.nio.file.Files;
        /// import java.nio.file.Paths;
        /// 
        /// public class App {
        ///     public static void main(String[] args) {
        ///         Pulumi.run(App::stack);
        ///     }
        /// 
        ///     public static void stack(Context ctx) {
        ///         final var example = IonoscloudFunctions.getDatacenter(GetDatacenterArgs.builder()
        ///             .location("us/las")
        ///             .name("Datacenter Example")
        ///             .build());
        /// 
        ///     }
        /// }
        /// ```
        /// ```yaml
        /// variables:
        ///   example:
        ///     fn::invoke:
        ///       Function: ionoscloud:getDatacenter
        ///       Arguments:
        ///         location: us/las
        ///         name: Datacenter Example
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Task<GetDatacenterResult> InvokeAsync(GetDatacenterArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDatacenterResult>("ionoscloud:index/getDatacenter:getDatacenter", args ?? new GetDatacenterArgs(), options.WithDefaults());

        /// <summary>
        /// The **Datacenter data source** can be used to search for and return an existing Virtual Data Center.
        /// You can provide a string for the name and location parameters which will be compared with provisioned Virtual Data Centers.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Name &amp; Location
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```typescript
        /// import * as pulumi from "@pulumi/pulumi";
        /// import * as ionoscloud from "@pulumi/ionoscloud";
        /// 
        /// const example = ionoscloud.getDatacenter({
        ///     location: "us/las",
        ///     name: "Datacenter Example",
        /// });
        /// ```
        /// ```python
        /// import pulumi
        /// import pulumi_ionoscloud as ionoscloud
        /// 
        /// example = ionoscloud.get_datacenter(location="us/las",
        ///     name="Datacenter Example")
        /// ```
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.GetDatacenter.Invoke(new()
        ///     {
        ///         Location = "us/las",
        ///         Name = "Datacenter Example",
        ///     });
        /// 
        /// });
        /// ```
        /// ```go
        /// package main
        /// 
        /// import (
        /// 	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud"
        /// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
        /// )
        /// 
        /// func main() {
        /// 	pulumi.Run(func(ctx *pulumi.Context) error {
        /// 		_, err := ionoscloud.LookupDatacenter(ctx, &amp;ionoscloud.LookupDatacenterArgs{
        /// 			Location: pulumi.StringRef("us/las"),
        /// 			Name:     pulumi.StringRef("Datacenter Example"),
        /// 		}, nil)
        /// 		if err != nil {
        /// 			return err
        /// 		}
        /// 		return nil
        /// 	})
        /// }
        /// ```
        /// ```java
        /// package generated_program;
        /// 
        /// import com.pulumi.Context;
        /// import com.pulumi.Pulumi;
        /// import com.pulumi.core.Output;
        /// import com.pulumi.ionoscloud.IonoscloudFunctions;
        /// import com.pulumi.ionoscloud.inputs.GetDatacenterArgs;
        /// import java.util.List;
        /// import java.util.ArrayList;
        /// import java.util.Map;
        /// import java.io.File;
        /// import java.nio.file.Files;
        /// import java.nio.file.Paths;
        /// 
        /// public class App {
        ///     public static void main(String[] args) {
        ///         Pulumi.run(App::stack);
        ///     }
        /// 
        ///     public static void stack(Context ctx) {
        ///         final var example = IonoscloudFunctions.getDatacenter(GetDatacenterArgs.builder()
        ///             .location("us/las")
        ///             .name("Datacenter Example")
        ///             .build());
        /// 
        ///     }
        /// }
        /// ```
        /// ```yaml
        /// variables:
        ///   example:
        ///     fn::invoke:
        ///       Function: ionoscloud:getDatacenter
        ///       Arguments:
        ///         location: us/las
        ///         name: Datacenter Example
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Output<GetDatacenterResult> Invoke(GetDatacenterInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDatacenterResult>("ionoscloud:index/getDatacenter:getDatacenter", args ?? new GetDatacenterInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDatacenterArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Id of an existing Virtual Data Center that you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Id of the existing Virtual Data Center's location.
        /// 
        /// Either `name`, `location` or `id` must be provided. If none, the datasource will return an error.
        /// </summary>
        [Input("location")]
        public string? Location { get; set; }

        /// <summary>
        /// Name of an existing Virtual Data Center that you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetDatacenterArgs()
        {
        }
        public static new GetDatacenterArgs Empty => new GetDatacenterArgs();
    }

    public sealed class GetDatacenterInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Id of an existing Virtual Data Center that you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Id of the existing Virtual Data Center's location.
        /// 
        /// Either `name`, `location` or `id` must be provided. If none, the datasource will return an error.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Name of an existing Virtual Data Center that you want to search for.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetDatacenterInvokeArgs()
        {
        }
        public static new GetDatacenterInvokeArgs Empty => new GetDatacenterInvokeArgs();
    }


    [OutputType]
    public sealed class GetDatacenterResult
    {
        /// <summary>
        /// Array of features and CPU families available in a location
        /// </summary>
        public readonly ImmutableArray<Outputs.GetDatacenterCpuArchitectureResult> CpuArchitectures;
        /// <summary>
        /// Description for the Virtual Data Center
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// List of features supported by the location this data center is part of
        /// </summary>
        public readonly ImmutableArray<string> Features;
        /// <summary>
        /// UUID of the Virtual Data Center
        /// </summary>
        public readonly string? Id;
        public readonly string Ipv6CidrBlock;
        /// <summary>
        /// The regional location where the Virtual Data Center will be created
        /// </summary>
        public readonly string? Location;
        /// <summary>
        /// The name of the Virtual Data Center
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// Boolean value representing if the data center requires extra protection e.g. two factor protection
        /// </summary>
        public readonly bool SecAuthProtection;
        /// <summary>
        /// The version of that Data Center. Gets incremented with every change
        /// </summary>
        public readonly int Version;

        [OutputConstructor]
        private GetDatacenterResult(
            ImmutableArray<Outputs.GetDatacenterCpuArchitectureResult> cpuArchitectures,

            string description,

            ImmutableArray<string> features,

            string? id,

            string ipv6CidrBlock,

            string? location,

            string? name,

            bool secAuthProtection,

            int version)
        {
            CpuArchitectures = cpuArchitectures;
            Description = description;
            Features = features;
            Id = id;
            Ipv6CidrBlock = ipv6CidrBlock;
            Location = location;
            Name = name;
            SecAuthProtection = secAuthProtection;
            Version = version;
        }
    }
}
