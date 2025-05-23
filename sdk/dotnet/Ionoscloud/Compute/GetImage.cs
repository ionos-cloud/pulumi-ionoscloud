// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Compute
{
    public static class GetImage
    {
        /// <summary>
        /// The **Image data source** can be used to search for and return an existing image which can then be used to provision a server.  
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned. 
        /// When this happens, please refine your search string so that it is specific enough to return only one result. In case multiple matches are found, enable debug(`TF_LOG=debug`) to show the name and location of the images.
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var cdrom = Ionoscloud.Compute.GetImage.Invoke(new()
        ///     {
        ///         ImageAlias = "ubuntu:latest_iso",
        ///         Type = "CDROM",
        ///         Location = "de/txl",
        ///         CloudInit = "NONE",
        ///     });
        /// 
        /// });
        /// ```
        /// Finds an image with alias `ubuntu:latest_iso`, in location `de/txl`, that does not support `cloud_init` and is of type `CDROM`.
        /// 
        /// ### Additional Examples
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetImage.Invoke(new()
        ///     {
        ///         ImageAlias = "ubuntu:latest",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// Finds an image with alias `ubuntu:latest` in location `de/txl`. Uses exact matching on both fields.
        /// 
        /// ### Additional Examples
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetImage.Invoke(new()
        ///     {
        ///         Type = "HDD",
        ///         CloudInit = "V1",
        ///         ImageAlias = "ubuntu:latest",
        ///         Location = "us/ewr",
        ///     });
        /// 
        /// });
        /// ```
        /// Finds an image named `ubuntu-20.04.6` in location `de/txl`. Uses exact matching.
        /// </summary>
        public static Task<GetImageResult> InvokeAsync(GetImageArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetImageResult>("ionoscloud:compute/getImage:getImage", args ?? new GetImageArgs(), options.WithDefaults());

        /// <summary>
        /// The **Image data source** can be used to search for and return an existing image which can then be used to provision a server.  
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned. 
        /// When this happens, please refine your search string so that it is specific enough to return only one result. In case multiple matches are found, enable debug(`TF_LOG=debug`) to show the name and location of the images.
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var cdrom = Ionoscloud.Compute.GetImage.Invoke(new()
        ///     {
        ///         ImageAlias = "ubuntu:latest_iso",
        ///         Type = "CDROM",
        ///         Location = "de/txl",
        ///         CloudInit = "NONE",
        ///     });
        /// 
        /// });
        /// ```
        /// Finds an image with alias `ubuntu:latest_iso`, in location `de/txl`, that does not support `cloud_init` and is of type `CDROM`.
        /// 
        /// ### Additional Examples
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetImage.Invoke(new()
        ///     {
        ///         ImageAlias = "ubuntu:latest",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// Finds an image with alias `ubuntu:latest` in location `de/txl`. Uses exact matching on both fields.
        /// 
        /// ### Additional Examples
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetImage.Invoke(new()
        ///     {
        ///         Type = "HDD",
        ///         CloudInit = "V1",
        ///         ImageAlias = "ubuntu:latest",
        ///         Location = "us/ewr",
        ///     });
        /// 
        /// });
        /// ```
        /// Finds an image named `ubuntu-20.04.6` in location `de/txl`. Uses exact matching.
        /// </summary>
        public static Output<GetImageResult> Invoke(GetImageInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetImageResult>("ionoscloud:compute/getImage:getImage", args ?? new GetImageInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **Image data source** can be used to search for and return an existing image which can then be used to provision a server.  
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned. 
        /// When this happens, please refine your search string so that it is specific enough to return only one result. In case multiple matches are found, enable debug(`TF_LOG=debug`) to show the name and location of the images.
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var cdrom = Ionoscloud.Compute.GetImage.Invoke(new()
        ///     {
        ///         ImageAlias = "ubuntu:latest_iso",
        ///         Type = "CDROM",
        ///         Location = "de/txl",
        ///         CloudInit = "NONE",
        ///     });
        /// 
        /// });
        /// ```
        /// Finds an image with alias `ubuntu:latest_iso`, in location `de/txl`, that does not support `cloud_init` and is of type `CDROM`.
        /// 
        /// ### Additional Examples
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetImage.Invoke(new()
        ///     {
        ///         ImageAlias = "ubuntu:latest",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// Finds an image with alias `ubuntu:latest` in location `de/txl`. Uses exact matching on both fields.
        /// 
        /// ### Additional Examples
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetImage.Invoke(new()
        ///     {
        ///         Type = "HDD",
        ///         CloudInit = "V1",
        ///         ImageAlias = "ubuntu:latest",
        ///         Location = "us/ewr",
        ///     });
        /// 
        /// });
        /// ```
        /// Finds an image named `ubuntu-20.04.6` in location `de/txl`. Uses exact matching.
        /// </summary>
        public static Output<GetImageResult> Invoke(GetImageInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetImageResult>("ionoscloud:compute/getImage:getImage", args ?? new GetImageInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetImageArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Cloud init compatibility ("NONE" or "V1"). Exact match.
        /// </summary>
        [Input("cloudInit")]
        public string? CloudInit { get; set; }

        /// <summary>
        /// description of the image
        /// </summary>
        [Input("description")]
        public string? Description { get; set; }

        /// <summary>
        /// Image alias of the image you are searching for. Exact match. E.g. =`centos:latest`, `ubuntu:latest`
        /// </summary>
        [Input("imageAlias")]
        public string? ImageAlias { get; set; }

        /// <summary>
        /// Id of the existing image's location. Exact match. Possible values: `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `us/ewr`, `us/las`
        /// </summary>
        [Input("location")]
        public string? Location { get; set; }

        /// <summary>
        /// Name of an existing image that you want to search for. It will return an exact match if one exists, otherwise it will retrieve partial matches.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The image type, HDD or CD-ROM. Exact match.
        /// </summary>
        [Input("type")]
        public string? Type { get; set; }

        /// <summary>
        /// The version of the image that you want to search for.
        /// 
        /// If both "name" and "version" are provided the plugin will concatenate the two strings in this format [name]-[version].
        /// The resulting string will be used to search for an exact match. An error will be thrown if one is not found.
        /// </summary>
        [Input("version")]
        public string? Version { get; set; }

        public GetImageArgs()
        {
        }
        public static new GetImageArgs Empty => new GetImageArgs();
    }

    public sealed class GetImageInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Cloud init compatibility ("NONE" or "V1"). Exact match.
        /// </summary>
        [Input("cloudInit")]
        public Input<string>? CloudInit { get; set; }

        /// <summary>
        /// description of the image
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Image alias of the image you are searching for. Exact match. E.g. =`centos:latest`, `ubuntu:latest`
        /// </summary>
        [Input("imageAlias")]
        public Input<string>? ImageAlias { get; set; }

        /// <summary>
        /// Id of the existing image's location. Exact match. Possible values: `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `us/ewr`, `us/las`
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Name of an existing image that you want to search for. It will return an exact match if one exists, otherwise it will retrieve partial matches.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The image type, HDD or CD-ROM. Exact match.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        /// <summary>
        /// The version of the image that you want to search for.
        /// 
        /// If both "name" and "version" are provided the plugin will concatenate the two strings in this format [name]-[version].
        /// The resulting string will be used to search for an exact match. An error will be thrown if one is not found.
        /// </summary>
        [Input("version")]
        public Input<string>? Version { get; set; }

        public GetImageInvokeArgs()
        {
        }
        public static new GetImageInvokeArgs Empty => new GetImageInvokeArgs();
    }


    [OutputType]
    public sealed class GetImageResult
    {
        /// <summary>
        /// Cloud init compatibility
        /// </summary>
        public readonly string CloudInit;
        /// <summary>
        /// Is capable of CPU hot plug (no reboot required)
        /// </summary>
        public readonly bool CpuHotPlug;
        /// <summary>
        /// Is capable of CPU hot unplug (no reboot required)
        /// </summary>
        public readonly bool CpuHotUnplug;
        /// <summary>
        /// description of the image
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// Is capable of SCSI drive hot plug (no reboot required)
        /// </summary>
        public readonly bool DiscScsiHotPlug;
        /// <summary>
        /// Is capable of SCSI drive hot unplug (no reboot required)
        /// </summary>
        public readonly bool DiscScsiHotUnplug;
        /// <summary>
        /// Is capable of Virt-IO drive hot plug (no reboot required)
        /// </summary>
        public readonly bool DiscVirtioHotPlug;
        /// <summary>
        /// Is capable of Virt-IO drive hot unplug (no reboot required)
        /// </summary>
        public readonly bool DiscVirtioHotUnplug;
        /// <summary>
        /// Indicates if the serial ID of the disk attached to the server will be exposed or not.
        /// </summary>
        public readonly bool ExposeSerial;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string ImageAlias;
        /// <summary>
        /// List of image aliases mapped for this Image
        /// </summary>
        public readonly ImmutableArray<string> ImageAliases;
        /// <summary>
        /// OS type of this Image
        /// </summary>
        public readonly string LicenceType;
        /// <summary>
        /// Location of that image/snapshot.
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// name of the image
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Is capable of nic hot plug (no reboot required)
        /// </summary>
        public readonly bool NicHotPlug;
        /// <summary>
        /// Is capable of nic hot unplug (no reboot required)
        /// </summary>
        public readonly bool NicHotUnplug;
        /// <summary>
        /// Indicates if the image is part of the public repository or not
        /// </summary>
        public readonly bool Public;
        /// <summary>
        /// Is capable of memory hot plug (no reboot required)
        /// </summary>
        public readonly bool RamHotPlug;
        /// <summary>
        /// Is capable of memory hot unplug (no reboot required)
        /// </summary>
        public readonly bool RamHotUnplug;
        /// <summary>
        /// The size of the image in GB
        /// </summary>
        public readonly double Size;
        /// <summary>
        /// This indicates the type of image
        /// </summary>
        public readonly string Type;
        public readonly string Version;

        [OutputConstructor]
        private GetImageResult(
            string cloudInit,

            bool cpuHotPlug,

            bool cpuHotUnplug,

            string description,

            bool discScsiHotPlug,

            bool discScsiHotUnplug,

            bool discVirtioHotPlug,

            bool discVirtioHotUnplug,

            bool exposeSerial,

            string id,

            string imageAlias,

            ImmutableArray<string> imageAliases,

            string licenceType,

            string location,

            string name,

            bool nicHotPlug,

            bool nicHotUnplug,

            bool @public,

            bool ramHotPlug,

            bool ramHotUnplug,

            double size,

            string type,

            string version)
        {
            CloudInit = cloudInit;
            CpuHotPlug = cpuHotPlug;
            CpuHotUnplug = cpuHotUnplug;
            Description = description;
            DiscScsiHotPlug = discScsiHotPlug;
            DiscScsiHotUnplug = discScsiHotUnplug;
            DiscVirtioHotPlug = discVirtioHotPlug;
            DiscVirtioHotUnplug = discVirtioHotUnplug;
            ExposeSerial = exposeSerial;
            Id = id;
            ImageAlias = imageAlias;
            ImageAliases = imageAliases;
            LicenceType = licenceType;
            Location = location;
            Name = name;
            NicHotPlug = nicHotPlug;
            NicHotUnplug = nicHotUnplug;
            Public = @public;
            RamHotPlug = ramHotPlug;
            RamHotUnplug = ramHotUnplug;
            Size = size;
            Type = type;
            Version = version;
        }
    }
}
