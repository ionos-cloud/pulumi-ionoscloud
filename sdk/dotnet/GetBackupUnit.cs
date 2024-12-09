// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetBackupUnit
    {
        /// <summary>
        /// The **Backup Unit data source** can be used to search for and return an existing Backup Unit.
        /// You can provide a string for either id or name parameters which will be compared with provisioned Backup Units. 
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned. 
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Name
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.GetBackupUnit.Invoke(new()
        ///     {
        ///         Name = "Backup Unit Example",
        ///     });
        /// 
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Task<GetBackupUnitResult> InvokeAsync(GetBackupUnitArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetBackupUnitResult>("ionoscloud:index/getBackupUnit:getBackupUnit", args ?? new GetBackupUnitArgs(), options.WithDefaults());

        /// <summary>
        /// The **Backup Unit data source** can be used to search for and return an existing Backup Unit.
        /// You can provide a string for either id or name parameters which will be compared with provisioned Backup Units. 
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned. 
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Name
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.GetBackupUnit.Invoke(new()
        ///     {
        ///         Name = "Backup Unit Example",
        ///     });
        /// 
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Output<GetBackupUnitResult> Invoke(GetBackupUnitInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetBackupUnitResult>("ionoscloud:index/getBackupUnit:getBackupUnit", args ?? new GetBackupUnitInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetBackupUnitArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the backup unit you want to search for.
        /// 
        /// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of an existing backup unit that you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetBackupUnitArgs()
        {
        }
        public static new GetBackupUnitArgs Empty => new GetBackupUnitArgs();
    }

    public sealed class GetBackupUnitInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the backup unit you want to search for.
        /// 
        /// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of an existing backup unit that you want to search for.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetBackupUnitInvokeArgs()
        {
        }
        public static new GetBackupUnitInvokeArgs Empty => new GetBackupUnitInvokeArgs();
    }


    [OutputType]
    public sealed class GetBackupUnitResult
    {
        /// <summary>
        /// The e-mail address you want assigned to the backup unit.
        /// </summary>
        public readonly string Email;
        /// <summary>
        /// The id of the Backup Unit.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The login associated with the backup unit. Derived from the contract number.
        /// </summary>
        public readonly string Login;
        /// <summary>
        /// The name of the Backup Unit.
        /// </summary>
        public readonly string? Name;

        [OutputConstructor]
        private GetBackupUnitResult(
            string email,

            string? id,

            string login,

            string? name)
        {
            Email = email;
            Id = id;
            Login = login;
            Name = name;
        }
    }
}
