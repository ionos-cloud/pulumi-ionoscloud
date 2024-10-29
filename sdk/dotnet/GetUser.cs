// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetUser
    {
        /// <summary>
        /// The **User data source** can be used to search for and return existing users.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Email
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```typescript
        /// import * as pulumi from "@pulumi/pulumi";
        /// import * as ionoscloud from "@pulumi/ionoscloud";
        /// 
        /// const example = ionoscloud.getUser({
        ///     email: "example@email.com",
        /// });
        /// ```
        /// ```python
        /// import pulumi
        /// import pulumi_ionoscloud as ionoscloud
        /// 
        /// example = ionoscloud.get_user(email="example@email.com")
        /// ```
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.GetUser.Invoke(new()
        ///     {
        ///         Email = "example@email.com",
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
        /// 		_, err := ionoscloud.LookupUser(ctx, &amp;ionoscloud.LookupUserArgs{
        /// 			Email: pulumi.StringRef("example@email.com"),
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
        /// import com.pulumi.ionoscloud.inputs.GetUserArgs;
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
        ///         final var example = IonoscloudFunctions.getUser(GetUserArgs.builder()
        ///             .email("example@email.com")
        ///             .build());
        /// 
        ///     }
        /// }
        /// ```
        /// ```yaml
        /// variables:
        ///   example:
        ///     fn::invoke:
        ///       Function: ionoscloud:getUser
        ///       Arguments:
        ///         email: example@email.com
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// 
        /// ### By Email from Env Variables - Current User
        /// data "ionoscloud.User" "example" {
        /// }
        /// </summary>
        public static Task<GetUserResult> InvokeAsync(GetUserArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetUserResult>("ionoscloud:index/getUser:getUser", args ?? new GetUserArgs(), options.WithDefaults());

        /// <summary>
        /// The **User data source** can be used to search for and return existing users.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Email
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```typescript
        /// import * as pulumi from "@pulumi/pulumi";
        /// import * as ionoscloud from "@pulumi/ionoscloud";
        /// 
        /// const example = ionoscloud.getUser({
        ///     email: "example@email.com",
        /// });
        /// ```
        /// ```python
        /// import pulumi
        /// import pulumi_ionoscloud as ionoscloud
        /// 
        /// example = ionoscloud.get_user(email="example@email.com")
        /// ```
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.GetUser.Invoke(new()
        ///     {
        ///         Email = "example@email.com",
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
        /// 		_, err := ionoscloud.LookupUser(ctx, &amp;ionoscloud.LookupUserArgs{
        /// 			Email: pulumi.StringRef("example@email.com"),
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
        /// import com.pulumi.ionoscloud.inputs.GetUserArgs;
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
        ///         final var example = IonoscloudFunctions.getUser(GetUserArgs.builder()
        ///             .email("example@email.com")
        ///             .build());
        /// 
        ///     }
        /// }
        /// ```
        /// ```yaml
        /// variables:
        ///   example:
        ///     fn::invoke:
        ///       Function: ionoscloud:getUser
        ///       Arguments:
        ///         email: example@email.com
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// 
        /// ### By Email from Env Variables - Current User
        /// data "ionoscloud.User" "example" {
        /// }
        /// </summary>
        public static Output<GetUserResult> Invoke(GetUserInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetUserResult>("ionoscloud:index/getUser:getUser", args ?? new GetUserInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUserArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Email of an existing user that you want to search for.
        /// </summary>
        [Input("email")]
        public string? Email { get; set; }

        /// <summary>
        /// ID of the user you want to search for.
        /// 
        /// Either `email` or `id` can be provided. If no argument is set, the provider will search for the **email that was provided for the configuration**. If none is found, the provider will return an error.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        public GetUserArgs()
        {
        }
        public static new GetUserArgs Empty => new GetUserArgs();
    }

    public sealed class GetUserInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Email of an existing user that you want to search for.
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        /// <summary>
        /// ID of the user you want to search for.
        /// 
        /// Either `email` or `id` can be provided. If no argument is set, the provider will search for the **email that was provided for the configuration**. If none is found, the provider will return an error.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        public GetUserInvokeArgs()
        {
        }
        public static new GetUserInvokeArgs Empty => new GetUserInvokeArgs();
    }


    [OutputType]
    public sealed class GetUserResult
    {
        /// <summary>
        /// Indicates if the user is active
        /// </summary>
        public readonly bool Active;
        /// <summary>
        /// Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
        /// </summary>
        public readonly bool Administrator;
        /// <summary>
        /// The e-mail address for the user.
        /// </summary>
        public readonly string? Email;
        /// <summary>
        /// The first name for the user.
        /// </summary>
        public readonly string FirstName;
        /// <summary>
        /// Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
        /// </summary>
        public readonly bool ForceSecAuth;
        /// <summary>
        /// Shows the id and name of the groups that the user is a member of
        /// </summary>
        public readonly ImmutableArray<Outputs.GetUserGroupResult> Groups;
        /// <summary>
        /// The id of the user.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The last name for the user.
        /// </summary>
        public readonly string LastName;
        /// <summary>
        /// Canonical (S3) id of the user for a given identity
        /// </summary>
        public readonly string S3CanonicalUserId;
        /// <summary>
        /// Indicates if secure authentication is active for the user or not
        /// </summary>
        public readonly bool SecAuthActive;

        [OutputConstructor]
        private GetUserResult(
            bool active,

            bool administrator,

            string? email,

            string firstName,

            bool forceSecAuth,

            ImmutableArray<Outputs.GetUserGroupResult> groups,

            string? id,

            string lastName,

            string s3CanonicalUserId,

            bool secAuthActive)
        {
            Active = active;
            Administrator = administrator;
            Email = email;
            FirstName = firstName;
            ForceSecAuth = forceSecAuth;
            Groups = groups;
            Id = id;
            LastName = lastName;
            S3CanonicalUserId = s3CanonicalUserId;
            SecAuthActive = secAuthActive;
        }
    }
}
